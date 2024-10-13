# Virtual environment

## Use existing virtual environment

- Load Anaconda3
```shell
module load Anaconda3
```
- List the existing environments
```shell
conda env list
```
- Output in Simlab
```shell
# conda environments:
#
GPUIA                    /home/imad.kissami/.conda/envs/GPUIA
                         /srv/data/imad.kissami/.local/easybuild/software/Anaconda3/2023.09-0
base                  *  /srv/software/easybuild/software/Anaconda3/2020.11
```
- Source the Anaconda environment In Toubkal
```shell
source /srv/software/easybuild/software/Anaconda3/2020.11/etc/profile.d/conda.sh
```
- Activate the tensorflow (using gpu) environment:
```shell
conda activate GPUIA
```
***You can now run tensorflow using gpus.***

## Create a new virtual environment 
**Be careful when installing new packages. The max. storage = 100GB**

- Check the current home storage
```shell
du -sh /home/<login>
```
- Check the files/directories' size
```shell
du -h --max-depth=1
```
- Display the files/directories' with size > 100MB
```shell
du -h --max-depth=1 /home/<login> | awk '$1 ~ /M$/ && $1+0 > 100 {print $1, $2}'
```
- Load Anaconda3
```shell
module load Anaconda3
```

- Create a new virtual environment
```shell
conda create --name venv_name
```
- Source the Anaconda environment In Toubkal
```shell
source /srv/software/easybuild/software/Anaconda3/2020.11/etc/profile.d/conda.sh
```
- Activate the `venv_name` environment:
```shell
conda activate venv_name
```
- Installing a new package (eg. numpy)
```shell
conda install numpy
