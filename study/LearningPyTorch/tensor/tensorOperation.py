#https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
#https://tutorials.pytorch.kr/beginner/introyt/tensors_deeper_tutorial.html#:~:text=(%E2%80%9CCUDA%E2%80%9D%20stands%20for%20Compute,Nvidia%27s%20platform%20for%20parallel%20computing.)
#Operations on Tensor
import numpy as np
import torch

print(torch.__version__)

tensor = torch.ones(4,4)
print(f"Frist row: {tensor[0]}")
print(f"Device tensor is stored on: {tensor.device}") #prints CPU

# Move out tensor to the GPU if it's available (cuz typically GPU has higher speeds than CPU)
if torch.cuda.is_available(): # check whether GPU is available
    print("We have a GPU!")
    tensor = tensor.to("cuda")
    print(f"Device tensor is stored on: {tensor.device}") # if it's available, move out it to the GPU
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
print(f"First column: {tensor[:, 0]}")
print(f"last column: {tensor[:, -1]}")

tensor[:,2] = 0

print(tensor)

#Joining tensors
''' 
use torch.cat to concatenate a sequence of tensors along a given dimension
[list of Concatenating Tensors], dim = 'dimension to along'
'''
t1 = torch.cat([tensor, tensor, tensor], dim =1)
print(t1)

t0 = torch.cat([tensor, tensor, tensor], dim =0)
print(t0)

#Arithmetic Operation
#This computes the matrix multiplication between two tensors. y1, y2, y3 will have the same value
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out = y3)

#This computes the element-wise product. z1, z2, z3 will have the same value
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)


#Single-element tensors : 
agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

#in-place operation 
print(f"{tensor} \n")
tensor.add_(5)
print(tensor)




# Bridge with Numpy

 #Tensor to NumPy array
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n:{n}")

 #NumPy array to Tensor
n = np.ones(5)
t = torch.from_numpy(n)

 #Changes in the NumPy array reflects in the tensor
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")