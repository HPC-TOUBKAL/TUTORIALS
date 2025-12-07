

<h1 align="center">Reservation commands</h1>

## Some definition

- A node is one computer unit of an HPC cluster each containing memory and one or more CPUs. There are generally two classifications of nodes; login and compute. 
	- login node: this is where users first login to stage their job scripts and do file and directory manipulations with text file editors and Unix commands.
	- compute node; A cluster can contain a few compute nodes or thousands of compute nodes. These are often referred to as just nodes since jobs are only scheduled on the compute nodes.

- Core
	- Slurm refers to cores as CPUs.
	- there are 56/112/128 cores in Toubkal 
	- up to 192GB memory per node compute nodes & up to 1.5TB for some nodes

- Task
	- a task can be considered a command such as blast, bwa, script.py
 	- default: 1 cpu per task

## I. Reserve resources


### 1. `srun` command
- Obtain a terminal on a CPU or GPU compute node within which you can execute your code,
- Directly execute your code on the CPUs or GPUs.

**Example 1: Connecting to a compute node**

```shell
srun --ntasks=1 --pty bash
```
- Running this command will redirect you directly to a compute node
- An interactive terminal is obtained with the --pty option.
- This command will allocate one task in the default partition (defq).

***run `python3 script.py`***

**Example 2: Running Python script**

- Run the Python file `script.py`
```python
import socket

def get_host_info():
    # Get the hostname
    hostname = socket.gethostname()
    return hostname

if __name__ == "__main__":
    host = get_host_info()
    print(f"Hostname: {host}")
```
- Load Python module if it's not loaded, then run this command
```shell
srun --ntasks=1 python3 script.py
```
- This command will allocate one task in the default partition (compute).
- The resources will be deallocated once the task is finished

- Output:
```shell
Hostname: slurm-compute-h23c5-u3-svn2
```

### 2. `salloc` command
- This command will allow you to reserve CPU or GPU resources to run multiple executions.
```shell
salloc --ntasks=1
```
- Ouput
```shell
salloc: Granted job allocation 2705972
salloc: Nodes slurm-compute-h23c5-u3-svn2 are ready for job
```
- Display the submitted jobs
```shell
squeue -u $USER
```

- Output:
```shell
     JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   2705972   compute interact imad.kis  R       0:11      1 slurm-compute-h23c5-u3-svn2
```
- You can either run a command in the current terminal or access to the requested resources from another terminal (In this example slurm-compute-h23c5-u3-svn2)
```shell
ssh slurm-compute-h23c5-u3-svn2
```

### 3. `sbatch` command

- This command run jobs in the backend (recommended).
- Create file `job.slurm`
```shell
#!/bin/bash

#SBATCH --ntasks=1

# unload any modules to start with a clean environment
module purge

# load software modules
module load Python/3.8.2-GCCcore-9.3.0

# run commands
python3 script.py
```
- Run the job file
```shell
sbatch job.slurm
```
- Output:
```shell
Submitted batch job 2705977
```
- Display the information of the job 2705977
```shell
squeue -j 2705977
```
***This command can display nothing if the job is very fast.***
***But you can check the job output, by running this command:***
```shell
cat slurm-2705977.out
```
***The file slurm-jobid.out is generated automatically.***

## II. Check the available resources using `sinfo` and `squeue` commands
- It's recommended to check the available resources before submitting a job to be sure that your job won't be waiting/pending.

### 1. `sinfo` command
- Display all partitions information
```shell
sinfo
```
- Output:
```shell
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute*     up   infinite    653  down$ slurm-compute-h21a5-u23-svn[2,4],slurm-compute-h21a5-u24-svn[1,3],slurm-compute-h21a5-u25-svn[2,4],slurm-compute-h21a5-u26-svn[1,3],slurm-compute-h21a5-u27-svn[2,4],slurm-compute-h21a5-u28-svn[1,3],slurm-compute-h21a5-u29-svn[2,4],slurm-compute-h21a5-u30-svn[1,3],slurm-compute-h21a5-u31-svn[2,4],slurm-compute-h21a5-u32-svn[1,3],slurm-compute-h21a5-u33-svn[2,4],slurm-compute-h21a5-u34-svn[1,3],slurm-compute-h21a5-u35-svn[2,4],slurm-compute-h21a5-u36-svn[1,3],slurm-compute-h21a8-u1-svn[2,4],slurm-compute-h21a8-u2-svn[1,3],slurm-compute-h21a8-u23-svn[2,4],
[...]
himem        up   infinite      1  maint slurm-himem-h22a8-u5-sv
himem        up   infinite      1    mix slurm-himem-h22a8-u9-sv
himem        up   infinite      2  alloc slurm-himem-h22a8-u1-sv,slurm-himem-h22a8-u3-sv
himem        up   infinite      1   idle slurm-himem-h22a8-u7-sv
gpu          up   infinite      1  maint slurm-a100-gpu-h22a2-u14-sv
gpu          up   infinite      2    mix slurm-a100-gpu-h22a2-u10-sv,slurm-a100-gpu-h22a2-u18-sv
gpu          up   infinite      2   idle slurm-a100-gpu-h22a2-u22-sv,slurm-a100-gpu-h22a2-u26-sv
```
<table>
  <tr>
    <th>Partition</th>
    <th>Nodes available for the partition</th>
  </tr>
  <tr>
    <td>compute</td>
    <td>1219</td>
  </tr>
  <tr>
    <td>himem</td>
    <td>5</td>
  </tr>
  <tr>
    <td>gpu</td>
    <td>5</td>
  </tr>
</table>

- Display the state for each node 
```shell
sinfo -o "%n %G %C %t"
```
- Output:
```shell
[...]
slurm-himem-h22a8-u9-sv (null) 112/0/0/112 alloc
slurm-himem-h22a8-u1-sv (null) 112/0/0/112 alloc
slurm-himem-h22a8-u3-sv (null) 0/112/0/112 idle
slurm-himem-h22a8-u5-sv (null) 0/112/0/112 idle
slurm-himem-h22a8-u7-sv (null) 0/112/0/112 idle
slurm-a100-gpu-h22a2-u10-sv gpu:4 120/8/0/128 mix
slurm-a100-gpu-h22a2-u14-sv gpu:4 95/33/0/128 mix
slurm-a100-gpu-h22a2-u18-sv gpu:4 0/128/0/128 idle
slurm-a100-gpu-h22a2-u22-sv gpu:4 0/128/0/128 idle
slurm-a100-gpu-h22a2-u26-sv gpu:4 0/128/0/128 idle
```
- Display the available CPUs per partition:
```shell
sinfo -o "%n %G %C %t %P" --noheader | grep -v -e "resv" -e "drain" -e "maint" | awk '{split($3,cpus,"/"); partition[$5]+=cpus[2]} END {for (p in partition) print p, partition[p]}'
```
- Output:

```shell
gpu       511
himem     114
compute*  20682
```
- Or add this command to `~/.bashrc` file, then tap `source ~/.bashrc`
```shell
alias cpusinfo='sinfo -o "%n %G %C %t %P" --noheader | grep -v -e "resv" -e "drain" -e "maint" | awk '\''{split($3,cpus,"/"); partition[$5]+=cpus[2]} END {for (p in partition) print p, partition[p]}'\'' | colum -t'
```
***You can run `cpusinfo` command to get the same output***

- Display the gpu node information:
```shell
sinfo -p gpu
```

- Output:
```shell
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
gpu          up   infinite      2    mix slurm-a100-gpu-h22a2-u10-sv,slurm-a100-gpu-h22a2-u14-sv
gpu          up   infinite      3   idle slurm-a100-gpu-h22a2-u18-sv,slurm-a100-gpu-h22a2-u22-sv,slurm-a100-gpu-h22a2-u26-sv
```

### 2. `squeue` command

- Display information for all jobs
```shell
squeue
```

- Display only your jobs information
```shell
squeue -u $USER
```
- Output
```shell
 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
       2713658   compute power_ef imad.kis PD       0:00      1 (Priority)
	   2706559   compute power_ef imad.kis  R       0:00      2 slurm-compute-h21a5-u6-svn[1,3]
	   2706560   compute power_ef imad.kis  R       0:00      5 slurm-compute-h21a5-u3-svn[2,4],slurm-compute-h21a5-u4-svn[1,3],slurm-compute-h21a5-u5-sv
```

- Display a specific job information
```shell
squeue -j 2706656
```
- Ouput:
```shell
 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
     2706559   compute     bash imad.kis  R       0:03      2 slurm-compute-h21a5-u6-svn[1,3]
```
- Display the pending jobs
```shell
squeue -u $USER -t pending
```
- Output:
```shell
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    2706736   compute power_ef imad.kis PD       0:00      2 (Resources)
[...]
```

- Display gpu jobs
```shell
sinfo -p gpu
```

### 3. `scancel` command

- Delete a job

```shell
scancel jobid
```

- Delete all jobs
```shell
scancel -u $USER
```


## III.  Slurm Parameters: nodes, partitions, tasks, memory, time

### 1. `--nodes`
  - *number of nodes to use where a node is one computer unit of many in an HPC cluster (optional)*
    - `--nodes=1` \# request 1 node (optional since default=1)
    - *used for multi-node jobs*
      - `--nodes=2`
    - *if the number of cpus per node is not specified then defaults to 1 cpu*
    - ***defaults=1 node*** if `--nodes` not used 

```shell
srun --nodes=2 --pty bash
```
***This command will allocate two nodes => two cpus (one cpu per node).***

### 2. `--partition`
  - *specify a partition (queue)*

1. Partition
<table>
  <tr>
    <th>Partition</th>
    <th>Nodes available for the partition</th>
  </tr>
  <tr>
    <td>compute</td>
    <td>1219</td>
  </tr>
  <tr>
    <td>himem</td>
    <td>5</td>
  </tr>
  <tr>
    <td>gpu</td>
    <td>5</td>
  </tr>
</table>

2. Qos
```shell
sacctmgr show qos
```

| QOS              | Time Limit     | Max. allowed usage of resources per user for all jobs     | Max. Minutes for all jobs |
|-------------------|---------------|---------------|-----------|
| intr              | 01:00:00      | gres/gpu=1, node=3       | |
| default-cpu       | 1-12:00:00    | cpu=3584,node=64      | |
| himem-cpu         | 1-12:00:00    | cpu=112       | |
| low-cpu           | 12:00:00      | node=16       |  cpu=4129440 |
| default-gpu       | 1-00:00:00    | cpu=64,gres/gpu=2,node=1   | |
| low-gpu           | 12:00:00      | node=4        |gres/gpu=1200|
| long-cpu          | 28-00:00:00   | cpu=1792,node=32      | |
| large-cpu         | 1-12:00:00    | cpu=7168,node=128      | |
| low-default-cpu  | 1-12:00:00    | cpu=7168      | |
| long-himem        | 7-00:00:00    | cpu=112       | |
| benchmark-cpu     | 1-12:00:00    | cpu=14336     | |
| long-gpu          | 7-00:00:00    | cpu=256,gres/gpu=8,node=2    | |

- Check the qos allowed for you (by defaut you are allowed to low-cpu and default-cpu).
```shell
sacctmgr show assoc where user=$USER format=qos%30,account%50,partition
```
***Send an email to support-hpc@um6p.ma to get access to other qos***
- Output:
```shell
                          QOS                                            Account  Partition 
------------------------------ -------------------------------------------------- ---------- 
[...]
```
**Example 1**

- Allocate resources in the gpu partition:
```shell
srun --nodes=1 --partition=gpu --account=<GPU-ACCOUNT> --gres=gpu:2 --pty bash
```
```shell
squeue -u $SUSER
```
```shell
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    2716772       gpu     bash imad.kis  R       0:03      1 slurm-a100-gpu-h22a2-u14-sv
```
- Display job information
```shell
scontrol show job 2716772
```
- Output:
```shell
JobId=2716772 JobName=bash
   UserId=imad.kissami(1853008732) GroupId=utilisateurs du domaine(1853000513) MCS_label=N/A
   Priority=9403 Nice=0 Account=...
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=0 Reboot=0 ExitCode=0:0
   RunTime=00:00:25 TimeLimit=1-00:00:00 TimeMin=N/A
   SubmitTime=2024-10-13T15:54:55 EligibleTime=2024-10-13T15:54:55
   AccrueTime=Unknown
   StartTime=2024-10-13T15:54:55 EndTime=2024-10-14T15:54:55 Deadline=N/A
   PreemptEligibleTime=2024-10-13T15:54:55 PreemptTime=None
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2024-10-13T15:54:55 Scheduler=Main
   Partition=gpu AllocNode:Sid=slurm-login-h23d5-u38-svn1:1061684
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=slurm-a100-gpu-h22a2-u14-sv
   BatchHost=slurm-a100-gpu-h22a2-u14-sv
   NumNodes=1 NumCPUs=1 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   ReqTRES=cpu=1,mem=8050M,node=1,billing=1,gres/gpu=2
   AllocTRES=cpu=1,mem=8050M,node=1,billing=1,gres/gpu=2
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=1 MinMemoryCPU=8050M MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=bash
   WorkDir=/home/imad.kissami
   Power=
   TresPerNode=gres/gpu:2
   ```
  **Example 2**
- Allocate resources in the himem partition (run cpusinfo to check if there are available cpus):
```shell
srun --nodes=1 --ntasks=1 --partition=himem --qos=himem-cpu --account=<CPU-ACCOUNT> --pty bash
```
   
### 3. `--ntasks`
  - *a task can be considered a command such as blastn, .exe, script.py, etc.*
    - `--ntasks=1` \# total tasks across all nodes per job

**Example:** Multi tasks using OpenMPI
- Display available version:
```sh
$ module spider OpenMPI
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  OpenMPI:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
      The Open MPI Project is an open source MPI-3 implementation.

     Versions:
        OpenMPI/3.1.1-GCC-7.3.0-2.30
        OpenMPI/3.1.3-GCC-8.2.0-2.31.1
        OpenMPI/3.1.4-GCC-8.3.0
        OpenMPI/4.0.3-GCC-9.3.0
        OpenMPI/4.0.5-GCC-10.2.0
        OpenMPI/4.0.5-gcccuda-2020b
        OpenMPI/4.1.1-GCC-10.3.0
        OpenMPI/4.1.1-GCC-11.2.0
        OpenMPI/4.1.4-GCC-11.3.0

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Pour de l'information détaillée à propos d'un module "OpenMPI" spécifique (incluant comment charger ce module), utilisez le nom complet.
  Par exemple :

     $ module spider OpenMPI/4.1.4-GCC-11.3.0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
- Load OpenMPI (version 4.0.3 compiled with GCC 9.3.0):
```sh
$ module load OpenMPI/4.0.3-GCC-9.3.0
```
- Install mpi4py using pip
	- First load both OpenMPI and Python
 ```sh
module load  OpenMPI/4.0.3-GCC-9.3.0 Python/3.8.2-GCCcore-9.3.0 
```
```sh
pip3 install mpi4py
```
  - Create file `mpiscript.py`
```python
from mpi4py import MPI
COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

if RANK==0: print("the number of cpus is:", SIZE)
```
- Run the script using 44 cores in one node (load python/3.8.2-GCCcore-9.3.0 and OpenMPI/4.0.3-GCC-9.3.0)
```shell
srun --partition=compute --nodes=1 --ntasks=44 --pty bash
```
***This command will allocate one node with 44 tasks***
- Then run
```shell
 mpirun python3 mpiscript.py
```
***If there is no node with 44 tasks available the job will be pending***

- You can ask for 44 tasks without specifying the number of nodes. 
	- This command can reserve more than one node if it's needed
```shell
srun --partition=compute --ntasks=44 --pty bash
```
***You can specify the number of tasks per node using the option `--ntasks-per-node` unstead of `ntasks`.***

### 4. `--time`
  - *max runtime for job (required); format: days-hours:minutes:seconds (days- is optional)*
    - `--time=24:00:00`   *# max runtime 24 hours (same as `--time=1-00:00:00`)*
    - `--time=7-00:00:00` *# max runtime 7 days*
    - In Toubkal, the time limite depends on the qos
   
- Display the time limite for all jobs
```shell
squeue -l
```
- Output:
```shell
Sat Dec  9 15:06:00 2023
JOBID PARTITION     NAME     USER    STATE       TIME TIME_LIMI  NODES NODELIST(REASON)
  2708747   compute power_ef imad.kis  RUNNING       0:01 1-12:00:00      4 slurm-compute-h21a5-u3-svn[2,4],slurm-compute-h21a5-u4-svn[1,3]
  2708748   compute power_ef imad.kis  RUNNING       0:01 1-12:00:00      1 slurm-compute-h21a5-u6-svn1
  2716773   compute     bash imad.kis  RUNNING       1:30 1-12:00:00      1 slurm-compute-h22b5-u36-svn3

```
**Example:**
- If you have access to `default-gpu` qos in Toubkal, the jobs are limite to 24 hours:

| QOS              | Time Limit     | Max. allowed usage of resources per user     |
|-------------------|---------------|---------------|-----------|
| default-gpu           | 1:00:00:00      | cpu=64,gres/gpu=2,node=1| 
- Runing multiple batch files asking for 1 gpu 

```shell
#!/bin/bash

#SBATCH --partition=gpu # partition name
#SBATCH --account=<GPU-ACCOUNT>
#SBATCH --nodes=1  # number of nodes to reserve
#SBATCH --gres=gpu:1 # use 1 gpus (On toubkal each node has 4 gpus)
#SABTCH --time=00:10:00

sleep 100 
```

### 5. `--mem`
  - *total memory for each node (required)*
    - `--mem=40G` *# request 40GB total memory per node*. If `--nodes=2`, means that the memory allocated will be 40G in each node.
**Example**:
```shell
srun --partition=compute  --nodes=2 --mem=40G --pty bash
```
***This command will allocate two nodes with 40GB in each node in the partition `gpu`.***
- Check that using `scontrol`
```shell
squeue -u $USER
```
```shell
 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    2716802   compute     bash imad.kis  R       1:55      2 slurm-compute-h24d8-u3-svn[2,4]
```
```shell
scontrol show job 2716802
```
```shell
 UserId=imad.kissami(1853008732) GroupId=utilisateurs du domaine(1853000513) MCS_label=N/A
   Priority=3789 Nice=0 Account=... QOS=default-cpu
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=0 Reboot=0 ExitCode=0:0
   RunTime=00:00:53 TimeLimit=1-12:00:00 TimeMin=N/A
   SubmitTime=2024-10-13T16:08:37 EligibleTime=2024-10-13T16:08:37
   AccrueTime=2024-10-13T16:08:37
   StartTime=2024-10-13T16:09:09 EndTime=2024-10-15T04:09:09 Deadline=N/A
   PreemptEligibleTime=2024-10-13T16:09:09 PreemptTime=None
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2024-10-13T16:09:09 Scheduler=Main
   Partition=compute AllocNode:Sid=slurm-login-h23d5-u38-svn1:1070311
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=slurm-compute-h24d8-u3-svn[2,4]
   BatchHost=slurm-compute-h24d8-u3-svn2
   NumNodes=2 NumCPUs=26 NumTasks=2 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   ReqTRES=cpu=2,mem=80G,node=2,billing=2
   AllocTRES=cpu=26,mem=80G,node=2,billing=26
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=13 MinMemoryNode=40G MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=bash
   WorkDir=/home/imad.kissami

```
  ### - In Toubkal

| Partition | MEMORY     | MEMORY PER CPU
|------------|------------|------------|
| compute     | 186 GB  |3.3GB|
| himem     | 1.5 TB  | 13.5GB |
| gpu     | 1 TB  | 8GB|

***By default, the allocated CPU memory is proportional to the number of reserved cores. For example, if you request 1/4 of the cores of a node, you will have access to 1/4 of its memory.***

**Example 1** 
- Allocate 2 cpus with 4GB
```shell
 srun --partition=compute  --ntasks 2 --mem=4GB --pty bash
```
```shell
squeue -u $USER 
```
```shell
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   2716820   compute     bash imad.kis  R       0:03      1 slurm-compute-h21c5-u8-svn1
```
```shell
scontrol show jobid 2716820
```
```shell
JobId=2716820 JobName=bash
   UserId=imad.kissami(1853008732) GroupId=utilisateurs du domaine(1853000513) MCS_label=N/A
   Priority=3789 Nice=0 Account=... QOS=default-cpu
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=0 Reboot=0 ExitCode=0:0
   RunTime=00:00:20 TimeLimit=1-12:00:00 TimeMin=N/A
   SubmitTime=2024-10-13T16:13:05 EligibleTime=2024-10-13T16:13:05
   AccrueTime=Unknown
   StartTime=2024-10-13T16:13:05 EndTime=2024-10-15T04:13:05 Deadline=N/A
   PreemptEligibleTime=2024-10-13T16:13:05 PreemptTime=None
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2024-10-13T16:13:05 Scheduler=Main
   Partition=compute AllocNode:Sid=slurm-login-h23d5-u38-svn1:1070311
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=slurm-compute-h21c5-u8-svn1
   BatchHost=slurm-compute-h21c5-u8-svn1
   NumNodes=1 NumCPUs=2 NumTasks=2 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   ReqTRES=cpu=2,mem=4G,node=1,billing=2
   AllocTRES=cpu=2,mem=4G,node=1,billing=2
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=2 MinMemoryNode=4G MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=bash
   WorkDir=/home/imad.kissami
   Power=
```
**Example 2** 

- Allocate 1 cpus with 20GB
```shell
 srun --partition=compute  --ntasks 1 --mem=20GB --pty bash
```
```shell
squeue -u $USER 
```
```shell
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
  2716821   compute     bash imad.kis  R       0:05      1 slurm-compute-h22b5-u36-svn3
```
```shell
scontrol show jobid 2716821
```
```shell
JobId=2716821 JobName=bash
   UserId=imad.kissami(1853008732) GroupId=utilisateurs du domaine(1853000513) MCS_label=N/A
   Priority=3789 Nice=0 Account=... QOS=default-cpu
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=0 Reboot=0 ExitCode=0:0
   RunTime=00:00:25 TimeLimit=1-12:00:00 TimeMin=N/A
   SubmitTime=2024-10-13T16:13:55 EligibleTime=2024-10-13T16:13:55
   AccrueTime=Unknown
   StartTime=2024-10-13T16:13:55 EndTime=2024-10-15T04:13:55 Deadline=N/A
   PreemptEligibleTime=2024-10-13T16:13:55 PreemptTime=None
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2024-10-13T16:13:55 Scheduler=Main
   Partition=compute AllocNode:Sid=slurm-login-h23d5-u38-svn1:1070311
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=slurm-compute-h22b5-u36-svn3
   BatchHost=slurm-compute-h22b5-u36-svn3
   NumNodes=1 NumCPUs=7 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   ReqTRES=cpu=1,mem=20G,node=1,billing=1
   AllocTRES=cpu=7,mem=20G,node=1,billing=7
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=7 MinMemoryNode=20G MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=bash
   WorkDir=/home/imad.kissami
   Power=
```
***The number of allocated cpus is equal to 7, even if you asked only one. This is because to satisfy 20GB you need at least 7 cpus (7x3.3=23,1GB).***
***So the rule is when you want to allocate a specific memory, check first if there are enough cpus***
***In Toubkal the memory depends on the partition (see the table above).***

### 6. `--job-name`
 - *set the job name, keep it short and concise without spaces (optional but highly recommended)*
   - `--job-name=myjob`
```shell
srun --partition=compute --job-name=myjob --pty bash
```
```shell
ssqueue 
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   2716829   compute    myjob imad.kis  R       0:05      1 slurm-compute-h21c5-u8-svn1
```

### 7. `--output` and `--error`
- When you run a job using `sbatch`, a default file will be generated called `slurm-jobid.out`. This file will contain both the output of your execution and errors if there are any.
- So to change the name of this default file, you can:
    - *use just `--output` to save stdout and stderr to the same output file:* `--output=output.%j.log`
	- *save all stdout to a specified file (optional but highly recommended for debugging)*
	    - `--output=stdout.%x.%j` *# saves stdout to a file named stdout.jobname.JobID*
	- *save all stderr to a specified file (optional but highly recommended for debugging)*
	    - `--error=stderr.%x.%j` *# saves stderr to a file named stderr.jobname.JobID*

**Example 1**
- Create `job3.slurm`
```shell
#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --output=output.%j.log
sleep 30
echo "this is test file"
```
- Run the job
```shell
sbatch job3.slurm
```
- Run `squeue -u $SUSER`
```shell
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
 2716829   compute    myjob imad.kis  R       1:02      1 slurm-compute-h21c5-u8-svn1
```
- Display the content of the file
```shell
cat output.2716829.log
```
- Output:
```shell
this is test file
```

**Example 2:**

- Create `job4.slurm`
```shell
#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --output=stdout.%x.%j
#SBATCH --error=stderr.%x.%j
sleep 30
echo "this is test file"
module load bizzare
```
- Run the job
```shell
sbatch job4.slurm
```
- Run `squeue -u $SUSER`
```shell
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    2716845      compute    myjob imad.kis  R       1:02      1 slurm-compute-h21c5-u8-svn1
```
- Display the content of the output file
```shell
cat stdout.job4.slurm.2716845
```
- Output:
```shell
this is test file
```
- Display the content of the error file
```shell
cat stderr.job4.slurm.2716845
```
- Output:
```shell
ERROR: Unable to locate a modulefile for 'bizzare'
```

### 8. `--array`

- Array jobs are good to use when you have multiple samples each of which can utilize an entire compute node running software that
supports multiple threads but does not support MPI
	- `--array=0-23` # job array indexes 0-23
	- `--array=1-24` # job array indexes 1-24
	- `--array=1,3,5,7` # job array indexes 1,3,5,7
	- `--array=1-7:2` # job array indexes 1 to 7 with a step size of 2 do not use `--nodes` with `--array`
 
- Use the index value to select which commands to run either from a text file of commands or as part of the input file name or parameter value
	- `$SLURM_ARRAY_TASK_ID` is the array index value

- stdout and stderr files can be saved per index value
	- `--output=stdout.%x.%A_%a`
	- `--error=stderr.%x.%A_%a`
- maximum array size is 1000 and max total pending and running jobs per user is 1000
	- Limit the number of simultaneously running tasks
	- can help prevent reaching file and disk quotas due to many intermediate and temporary files
	- as one job completes another array index is run on an available node
	- `--array=1-40%5` # job array with indexes 1-40; max of 5 running array jobs

**Example:**

```shell
#!/bin/bash
#SBATCH --jobname=pi_estimation 
#SBATCH --partition=compute 
#SBATCH -n 6
#SBATCH --array=1-6

# Load python module                                                                                                                                                                                       module load Python/3.8.2-GCCcore-9.3.0

# Define the array of num_samples                                                                                                                                                                           
num_samples_array=(1000 10000 100000 1000000 10000000 100000000)

# Get the num_samples for this task
num_samples=${num_samples_array[$SLURM_ARRAY_TASK_ID-1]}

# Run the python script
python -c "
import random                                                                                                                                                                                              def estimate_pi(num_samples):                                                                                                                                                                                  num_inside_circle = 0
    for _ in range(num_samples): 
        x = random.uniform(-1, 1) 
        y = random.uniform(-1, 1) 
        distance = x**2 + y**2
                                                                                                                                                                                                            
        if distance <= 1: 
            num_inside_circle += 1
            
    return 4 * num_inside_circle / num_samples 
print(estimate_pi($num_samples))
"
```

### 8. Reservations 

- Check the reservations
```shell
scontrol show reservation 
```

```shell
 ReservationName=power_efficiency_testing StartTime=2024-04-02T12:16:10 EndTime=2099-04-02T12:16:10 Duration=27392-23:00:00
   Nodes=slurm-compute-h21a5-u3-svn[2,4],slurm-compute-h21a5-u4-svn[1,3],slurm-compute-h21a5-u5-svn[2,4],slurm-compute-h21a5-u6-svn[1,3] NodeCnt=8 CoreCnt=448 Features=(null) PartitionName=(null) Flags=OVERLAP,IGNORE_JOBS,SPEC_NODES
   TRES=cpu=448
   Users=imad.kissami,pfb29 Groups=(null) Accounts=(null) Licenses=(null) State=ACTIVE BurstBuffer=(null) Watts=n/a
   MaxStartDelay=(null)
```

- Or
```shell
scontrol show reservation | tr ' ' '\n' | egrep "ReservationName=|StartTime=|EndTime=|Nodes=" | paste - - - -
```

```shell
srun -N 1 -n 56 --reservation=power_efficiency_testing --partition=compute --pty bash
```
