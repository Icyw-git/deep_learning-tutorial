"""基础功能测试"""
import torch
import numpy as np
import pytest


def test_tensor_creation():
    """测试张量创建和基本操作"""
    # 创建张量
    x = torch.tensor([1, 2, 3])
    assert x.shape == (3,)
    assert x.dtype == torch.int64
    
    # 测试张量运算
    y = torch.tensor([4, 5, 6])
    z = x + y
    assert torch.allclose(z, torch.tensor([5, 7, 9]))
    
    # 测试张量转numpy
    x_np = x.numpy()
    assert isinstance(x_np, np.ndarray)
    assert np.array_equal(x_np, np.array([1, 2, 3]))


def test_autograd():
    """测试自动求导功能"""
    x = torch.tensor(2.0, requires_grad=True)
    y = x ** 2
    
    # 计算梯度
    y.backward()
    
    # 验证梯度
    assert x.grad.item() == 4.0


def test_model_basic():
    """测试基本模型结构"""
    import torch.nn as nn
    
    # 创建简单的神经网络
    model = nn.Sequential(
        nn.Linear(10, 20),
        nn.ReLU(),
        nn.Linear(20, 5)
    )
    
    # 创建输入
    x = torch.randn(32, 10)
    
    # 前向传播
    output = model(x)
    
    # 验证输出形状
    assert output.shape == (32, 5)


def test_data_loader():
    """测试数据加载器"""
    from torch.utils.data import TensorDataset, DataLoader
    
    # 创建数据集
    X = torch.randn(100, 10)
    y = torch.randint(0, 5, (100,))
    
    dataset = TensorDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    
    # 测试数据加载
    batch_X, batch_y = next(iter(dataloader))
    assert batch_X.shape[0] == 32
    assert batch_y.shape[0] == 32


if __name__ == "__main__":
    pytest.main([__file__])