===================================BUG REPORT===================================
================================================================================
The following directories listed in your path were found to be non-existent: {WindowsPath('vs/workbench/api/node/extensionHostProcess')}
The following directories listed in your path were found to be non-existent: {WindowsPath('//matplotlib_inline.backend_inline'), WindowsPath('module')}
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching in backup paths...
The following directories listed in your path were found to be non-existent: {WindowsPath('/usr/local/cuda/lib64')}
DEBUG: Possible options found for libcudart.so: set()
CUDA SETUP: PyTorch settings found: CUDA_VERSION=118, Highest Compute Capability: 8.9.
CUDA SETUP: To manually override the PyTorch CUDA version please see:https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
CUDA SETUP: Loading binary d:\code\venv_LBS\venv_llm3\Lib\site-packages\bitsandbytes\libbitsandbytes_cuda118.so...
[WinError 193] %1은(는) 올바른 Win32 응용 프로그램이 아닙니다
CUDA SETUP: Problem: The main issue seems to be that the main CUDA runtime library was not detected.
CUDA SETUP: Solution 1: To solve the issue the libcudart.so location needs to be added to the LD_LIBRARY_PATH variable
CUDA SETUP: Solution 1a): Find the cuda runtime library via: find / -name libcudart.so 2>/dev/null
CUDA SETUP: Solution 1b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_1a
CUDA SETUP: Solution 1c): For a permanent solution add the export from 1b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Solution 2: If no library was found in step 1a) you need to install CUDA.
CUDA SETUP: Solution 2a): Download CUDA install script: wget https://raw.githubusercontent.com/TimDettmers/bitsandbytes/main/cuda_install.sh
CUDA SETUP: Solution 2b): Install desired CUDA version to desired location. The syntax is bash cuda_install.sh CUDA_VERSION PATH_TO_INSTALL_INTO.
CUDA SETUP: Solution 2b): For example, "bash cuda_install.sh 113 ~/local/" will download CUDA 11.3 and install into the folder ~/local
d:\code\venv_LBS\venv_llm3\Lib\site-packages\bitsandbytes\cuda_setup\main.py:167: UserWarning: Welcome to bitsandbytes. For bug reports, please run

python -m bitsandbytes
