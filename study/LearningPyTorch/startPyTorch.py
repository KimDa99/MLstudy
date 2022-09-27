import torch
import numpy as np

#Initializing Tensor

# 1) Directly from Data
data = [[1,3],[2,4]]
x_data = torch.tensor(data)

# 2) From a Numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# 3) From another Tensor
x_ones = torch.ones_like(x_data)
print(f"One Tensor: \n{x_ones}\n")

x_rand = torch.rand_like(x_data, dtype = torch.float)
print(f"Random Tensor: \n {x_rand} \n")

print("\n\n")
## + With random or constant values
shape = (2,4,2) #(num of row, num of col, num of matirx)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n{rand_tensor}\n")
print(f"Ones Tensor: \n{ones_tensor}\n")
print(f"Zeros Tensor: \n{zeros_tensor}\n")