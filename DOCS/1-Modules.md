
<h1 align="center">Module commands</h1>

### Display the installed GCC versions:

```shell
module spider GCC
```
```shell
------------------------------------------------------------------------------------------------------------------------------------------------------------------
  GCC:
------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
      The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
      libgcj,...).

     Versions:
        GCC/7.3.0-2.30
        GCC/8.2.0-2.31.1
        GCC/8.3.0
        GCC/9.3.0
        GCC/10.2.0
        GCC/10.3.0
        GCC/11.2.0
        GCC/11.3.0
        GCC/12.3.0
     Autres candidats possibles :
        GCCcore  gcccuda

```

- Or


```shell
module --terse avail 2>&1 | grep -i '^\(gcc\)'
```
```shell
GCC/
GCC/7.3.0-2.30
GCC/8.2.0-2.31.1
GCC/8.3.0
GCC/9.3.0
GCC/10.2.0
GCC/10.3.0
GCC/11.2.0
GCC/11.3.0
GCCcore/
GCCcore/7.3.0
GCCcore/8.2.0
GCCcore/8.3.0
GCCcore/9.3.0
GCCcore/10.2.0
GCCcore/10.3.0
GCCcore/11.2.0
GCCcore/11.3.0
GCCcore/12.2.0
gcccuda/
gcccuda/2018b
gcccuda/2020b
```
### Load a module (default one)

```shell
module load GCC
```
### List the loaded modules

```shell
module list
```
- Output:
```shell
Currently Loaded Modules:
  1) GCCcore/12.3.0   2) zlib/1.2.13-GCCcore-12.3.0   3) binutils/2.40-GCCcore-12.3.0   4) GCC/12.3.0  
```
### Unload module
```shell
module unload binutils/2.40-GCCcore-12.3.0
```
- Output (after module list):
```shell
Currently Loaded Modulefiles:  
  1) GCCcore/12.3.0   2) zlib/1.2.13-GCCcore-12.3.0   3) GCC/12.3.0
```
### Unload all modules
```shell
module purge
```
- Output (after module list):
```shell
No Modulefiles Currently Loaded
```
### Modules conflict handling
- Load the default GCC
```shell
module load GCC
```
```shell
module list
```
- Output:
```shell
Currently Loaded Modules:
  1) GCCcore/12.3.0   2) zlib/1.2.13-GCCcore-12.3.0   3) binutils/2.40-GCCcore-12.3.0   4) GCC/12.3.0  
```

- Load GCC/9.3.0 
```shell
module load GCC/9.3.0 
```

```shell
Les modules suivants ont été rechargés avec un changement de version :
  1) GCC/12.3.0 => GCC/9.3.0             3) binutils/2.40-GCCcore-12.3.0 => binutils/2.34-GCCcore-9.3.0
  2) GCCcore/12.3.0 => GCCcore/9.3.0     4) zlib/1.2.13-GCCcore-12.3.0 => zlib/1.2.11-GCCcore-9.3.0
```
***The dependent modules will be reloaded automatically with the new GCC version.***

### Add modules to `~/.bashrc` file

- Open `~/.bashrc` file, and add the modules that you load most of the time

```shell
module load Python/3.8.2-GCCcore-9.3.0 
```
```shell
source ~/.bashrc
```
**You no longer need to load Python/3.8.2-GCCcore-9.3.0 after each connection.**
