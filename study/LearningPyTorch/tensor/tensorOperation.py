#https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
#https://tutorials.pytorch.kr/beginner/introyt/tensors_deeper_tutorial.html#:~:text=(%E2%80%9CCUDA%E2%80%9D%20stands%20for%20Compute,Nvidia%27s%20platform%20for%20parallel%20computing.)
#Operations on Tensor
from numpy import dtype
import torch
from zmq import device

print(torch.__version__)

tensor = torch.ones(4,4)
print(f"Frist row: {tensor[0]}")
print(f"Device tensor is stored on: {tensor.device}")

# Move out tensor to the GPU if it's available (cuz typically GPU has higher speeds than CPU)
if torch.cuda.is_available(): # check whether GPU is available
    print("We have a GPU!")
    tensor = tensor.to("cuda")
    print(f"Device tensor is stored on: {tensor.device}")
    #tensor = torch.tensor.to(device, dtype = torch.float32) # if it's available, move out it to the GPU
else:
    print("We can use CPU only :(") # Shows it is not available

"""
- what is cuda? 
CUDA stands for Compute Unified Device Architecture,
which is Nvidia's platform for parallel computing
You need to install it before using
If you do not have a CUDA-compatible GPU and CUDA drivers installed, the executable cells in this section will not execute any GPU-related code.
"""

#Standard numpy-like indexing and slicing:
print(f"Frist row: {tensor[0]}")
tensor = torch.ones(2,2)
print(f"Device tensor is stored on: {tensor.device}")
