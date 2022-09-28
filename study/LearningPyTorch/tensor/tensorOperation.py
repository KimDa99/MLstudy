#https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
#https://tutorials.pytorch.kr/beginner/introyt/tensors_deeper_tutorial.html#:~:text=(%E2%80%9CCUDA%E2%80%9D%20stands%20for%20Compute,Nvidia%27s%20platform%20for%20parallel%20computing.)
#Operations on Tensor
import torch

tensor = torch.rand(3,4)
# Move out tensor to the GPU if it's available (cuz typically GPU has higher speeds than CPU)
if torch.cuda.is_available(): # check whether GPU is available
    print("We have a GPU!")
    tensor = tensor.to("cuda") # if it's available, move out it to the GPU
else:
    print("We do not have a GPU :(") # Shows it is not available

"""
- what is cuda? 
CUDA stands for Compute Unified Device Architecture,
which is Nvidia's platform for parallel computing
You need to install it before
If you do not have a CUDA-compatible GPU and CUDA drivers installed, the executable cells in this section will not execute any GPU-related code.
"""
