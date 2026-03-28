"""模型测试"""

import pytest
import torch
import torch.nn as nn


class SimpleCNN(nn.Module):
    """简单的CNN模型"""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(6 * 14 * 14, 10)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = x.view(-1, 6 * 14 * 14)
        x = self.fc1(x)
        return x


class SimpleRNN(nn.Module):
    """简单的RNN模型"""

    def __init__(self, vocab_size, embedding_dim, hidden_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        output, hidden = self.rnn(x, hidden)
        output = self.fc(output)
        return output, hidden


def test_cnn_model():
    """测试CNN模型"""
    model = SimpleCNN()

    # 创建输入数据（模拟MNIST）
    x = torch.randn(32, 1, 28, 28)

    # 前向传播
    output = model(x)

    # 验证输出形状
    assert output.shape == (32, 10)


def test_rnn_model():
    """测试RNN模型"""
    vocab_size = 1000
    embedding_dim = 128
    hidden_size = 256

    model = SimpleRNN(vocab_size, embedding_dim, hidden_size)

    # 创建输入数据
    x = torch.randint(0, vocab_size, (32, 10))

    # 前向传播
    output, hidden = model(x)

    # 验证输出形状
    assert output.shape == (32, 10, vocab_size)
    assert hidden.shape == (1, 32, hidden_size)


def test_model_training():
    """测试模型训练流程"""
    model = SimpleCNN()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # 创建训练数据
    x = torch.randn(32, 1, 28, 28)
    y = torch.randint(0, 10, (32,))

    # 训练步骤
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

    # 验证损失是一个标量
    assert isinstance(loss.item(), float)


def test_model_save_load():
    """测试模型保存和加载"""
    model = SimpleCNN()

    # 保存模型
    torch.save(model.state_dict(), "test_model.pth")

    # 加载模型
    model2 = SimpleCNN()
    model2.load_state_dict(torch.load("test_model.pth"))

    # 验证参数相同
    for (name1, param1), (name2, param2) in zip(
        model.named_parameters(), model2.named_parameters()
    ):
        assert name1 == name2
        assert torch.allclose(param1.data, param2.data)

    # 清理测试文件
    import os

    if os.path.exists("test_model.pth"):
        os.remove("test_model.pth")


if __name__ == "__main__":
    pytest.main([__file__])
