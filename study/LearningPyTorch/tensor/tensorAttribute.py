import torch

tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}")
print(f"DataType of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")