# 深度学习学习项目

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python版本">
    <img src="https://img.shields.io/badge/PyTorch-1.8+-red.svg" alt="PyTorch版本">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

## 项目简介

这是一个基于 PyTorch 的深度学习学习项目，包含了从基础张量操作到高级模型应用的完整学习路径。项目旨在帮助初学者理解深度学习的核心概念和实践应用，所有教程和注释均为中文，适合中文用户学习。

## 目录结构

```
deep_learning/
├── notebooks/                    # Jupyter notebooks
│   ├── 基础知识/                 # 基础概念教程
│   │   ├── 张量.ipynb           # 张量操作基础
│   │   ├── 神经网络.ipynb        # 神经网络基础
│   │   ├── 梯度下降优化.ipynb     # 优化算法实现
│   │   ├── 正则化.ipynb          # 正则化技术
│   │   └── 深度学习模型简介.md      # 模型理论介绍
│   ├── cnn/                    # 卷积神经网络
│   │   └── CNN卷积模型.ipynb      # CNN实现与应用
│   ├── rnn/                    # 循环神经网络
│   │   └── RNN卷积模型.ipynb      # RNN实现与应用
│   └── 综合案例/                # 实战案例
│       ├── 图像识别案例.ipynb      # MNIST手写数字识别
│       ├── 手机价格分类案例.ipynb    # 手机价格预测
│       └── 歌词生成器案例.ipynb     # 基于RNN的歌词生成
├── tests/                      # 单元测试
│   ├── test_basic.py           # 基础功能测试
│   ├── test_models.py          # 模型测试
│   └── test_simple.py          # 简单测试
├── .github/workflows/          # GitHub Actions工作流
│   └── python-ci.yml          # CI/CD配置
├── pyproject.toml             # 项目配置文件
├── requirements.txt           # Python依赖包
├── .gitignore                # Git忽略文件
├── LICENSE                   # MIT许可证
└── README.md                 # 项目说明文档
```

## 快速开始

### 如何运行

### 1. 环境配置

```bash
# 安装依赖包
pip install -r requirements.txt

# 或使用conda
conda create -n deep_learning python=3.8
conda activate deep_learning
pip install -r requirements.txt
```

### 2. 运行教程

```bash
# 启动Jupyter Notebook
jupyter notebook

# 或使用Jupyter Lab
jupyter lab
```

然后按照学习路径顺序打开notebooks学习。

### 3. 使用代码格式化工具

```bash
# 使用black格式化代码
black .

# 使用isort整理导入语句
isort .

# 组合使用
isort . && black .

# 检查格式（不修改文件）
black --check .
isort --check .
```

## 项目配置文件

项目使用 `pyproject.toml` 进行统一配置：

- **项目信息**：项目名称、版本、描述等
- **代码格式化**：black和isort的配置
- **测试配置**：pytest的配置
- **代码检查**：flake8的配置

确保所有开发者使用相同的工具配置，保持代码风格一致。

## 学习路径

### 第一阶段：基础入门
1. **张量.ipynb** - 掌握PyTorch张量操作的基础
2. **神经网络.ipynb** - 理解神经网络的基本结构和原理
3. **梯度下降优化.ipynb** - 学习各种优化算法的实现
4. **正则化.ipynb** - 了解防止过拟合的技术

### 第二阶段：模型学习
1. **深度学习模型简介.md** - 学习各种深度学习模型的理论
2. **CNN卷积模型.ipynb** - 掌握卷积神经网络的实现
3. **RNN卷积模型.ipynb** - 掌握循环神经网络的实现

### 第三阶段：实战应用
1. **图像识别案例.ipynb** - MNIST手写数字识别实战
2. **手机价格分类案例.ipynb** - 机器学习分类任务实战
3. **歌词生成器案例.ipynb** - 基于RNN的文本生成实战

## 主要功能

### 基础操作
- ✅ 张量创建与操作
- ✅ 自动求导机制
- ✅ 神经网络构建
- ✅ 模型训练流程

### 模型实现
- ✅ 全连接神经网络
- ✅ 卷积神经网络(CNN)
- ✅ 循环神经网络(RNN)

### 实战案例
- ✅ MNIST图像分类
- ✅ 手机价格预测
- ✅ 中文歌词生成

## 技术栈

| 技术/库 | 版本 | 用途 |
|---------|------|------|
| Python | 3.7+ | 编程语言 |
| PyTorch | 1.8+ | 深度学习框架 |
| torchvision | - | 计算机视觉工具 |
| numpy | 1.19+ | 数值计算 |
| matplotlib | 3.3+ | 数据可视化 |
| seaborn | 0.10+ | 统计图表绘制 |
| jieba | 0.42+ | 中文分词 |
| torchsummary | 1.5+ | 模型结构可视化 |
| pytest | 6.0+ | 单元测试框架 |
| pytest-cov | 2.10+ | 测试覆盖率工具 |
| black | 22.0+ | 代码格式化工具 |
| isort | 5.0+ | 导入语句整理工具 |
| flake8 | 4.0+ | 代码质量检查工具 |
| GitHub Actions | - | CI/CD自动化 |
| pyproject.toml | - | 项目配置文件 |

## CI/CD配置

本项目使用GitHub Actions进行持续集成和持续部署：

- **自动测试**：每次push或pull request时自动运行单元测试
- **多版本测试**：在Python 3.7、3.8、3.9环境下测试
- **代码质量检查**：使用flake8、black、isort进行代码风格检查
- **测试覆盖率**：使用pytest-cov生成测试覆盖率报告
- **自动构建**：通过后自动构建Python包

## 项目特点

✨ **循序渐进** - 从基础到高级，适合不同水平的学习者  
📚 **理论结合实践** - 既有详细的理论解释，又有完整的代码实现  
🇨🇳 **中文友好** - 所有注释和说明均为中文  
💻 **代码清晰** - 代码结构清晰，注释详细  
🎯 **实战导向** - 通过真实案例加深理解  

## 如何贡献

欢迎提交Issue和Pull Request！如果你发现了bug或者有新的想法，请随时联系我们。

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

**注意**：本项目仅供学习和教学使用