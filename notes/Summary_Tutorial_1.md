# 如何形式化描述机器学习问题？

已知$m$个样本，其中第$i$个样本记为$\{\mathbf{x}^i, y^i\}$  
待建立的模型记为$Model(\mathbf{x}, \theta)$（为了下面公式表达方便，也可记为$F(\mathbf{x}, \theta)$）  
建立损失函数$L(F(\mathbf{x}, \theta), y)$，（损失函数的具体定义，请参考[机器学习中的损失函数](./Summary_Tutorial_2.md)）  
待求解参数
$$\theta = argmin_{\theta}L(F(\mathbf{x}, \theta), y)$$
