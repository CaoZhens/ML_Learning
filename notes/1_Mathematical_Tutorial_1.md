# 机器学习的数学基础（1）自然底数e

##  对数函数$y=\log_{a}(x)$的图像

讨论对数函数$y=\log_{a}(x)$，当$a>1$时，在点$(1,0)$处的切线斜率：随$a$增大，斜率增大
**提问：当对数函数$y=\log_{a}(x)$在点$(1,0)$处的切线斜率恰好为1时，底数$a$等于多少？**

## 问题分析
> 根据导数的定义与几何意义，如果函数$y=f(x)$在点$P(x_0, f(x_0))$处可导，则点$P$处的切线斜率即为函数在该点处的导数值$f^\prime(x_0)$

令对数函数$y=log_{a}(x)$，根据导数的定义有$$y^\prime(x) = \lim_{\Delta{x} \to 0} \frac{f(x+\Delta{x})-f(x)}{\Delta{x}} = \lim_{\Delta{x} \to 0} \log_{a}(\frac{x+\Delta{x}}{x})^{\frac{1}{\Delta{x}}}$$

代入已知条件，得$$\lim_{\Delta{x} \to 0} \log_{a}(1+\Delta{x})^{\frac{1}{\Delta{x}}} = 1$$
即$$a = \lim_{\Delta{x} \to 0} (1+\Delta{x}^{\frac{1}{\Delta{x}}})$$
**也可以表示为$$a = \lim_{x \to \infty} (1+\frac{1}{x})^{x}$$**

**将求底数$a$转化为求函数极限$ \lim_{x \to \infty} (1+\frac{1}{x})^{x}$问题**
## 证明该函数极限的存在性

### 数列的极限

构造数列$\{a_n\} = \left( 1 + \frac1n \right) ^{n}$

**首先，证明数列$\{a_n\}$单调递增**

$\{a_n\} = (1+\frac{1}{n})^{n} = 1\cdot \underbrace{(1+\frac{1}{n})\cdots(1+\frac{1}{n})}_{n}$
根据算术-几何平均不等式：
> 算术-几何平均不等式（Arithmetic–Geometric Mean Inequality, AGM Inequality）
$$\frac{a_1+a_2+\ldots+a_n}{n} \geq \sqrt[n]{a_1a_2\ldots a_n}$$
其中，$a_i$非负

$$ \{a_n\} = 1\cdot \underbrace{(1+\frac{1}{n})\cdots(1+\frac{1}{n})}_{n} $$

$$ \{a_n\} \leq \left[ \frac{1+\underbrace{(1+\frac{1}{n})+\cdots+(1+\frac{1}{n})}_{n}}{n+1}\right]^{n+1} $$

$$ \{a_n\} \leq \left[ \frac{\underbrace{1+\cdots+1}_{n+1} + \underbrace{\frac1n+\cdots+\frac1n}_{n}}{n+1}\right]^{n+1}$$

$$ \{a_n\} \leq \left( 1+\frac{1}{n+1}\right)^{n+1} = \{a_{n+1}\}$$

**其次，证明数列$\{a_n\}$有上界**

将其展开得
$$ \{a_n\} = C_{n}^{0}\left(\frac{1}{n}\right)^{0}+C_{n}^{1}\left(\frac{1}{n}\right)^{1}+\ldots+C_{n}^{n}\left(\frac{1}{n}\right)^{n} $$

即
$$\{a_n\} < 3$$

> 极限存在准则：单调递增有上界的数列一定收敛

**根据极限存在准则，数列$\{a_n\}$ 的极限$\lim_{n \to \infty} (1+\frac{1}{n})^{n}$存在，记为$e$**

### 函数的极限

**首先考虑$ x \to +\infty $**

总存在正整数$n$，使$n \leq x \leq n+1$
则 $$ 1+ \frac{1}{n+1} \leq 1+\frac1x\leq 1+ \frac1n $$

$$ \left( 1+ \frac{1}{n+1} \right)^n \leq \left(1+\frac1x \right)^x \leq \left( 1+ \frac1n \right)^{n+1} $$

不等式左右两端的极限均为$e$
根据两边夹定理
$$ \lim_{x \to +\infty} \left( 1+\frac{1}{x} \right)^{x} = e $$

**其次考虑$ x \to -\infty $**

令 $t = -x-1$
$$ \lim_{x \to -\infty} \left( 1+\frac{1}{x} \right)^{x} 
= \lim_{t \to +\infty} \left( 1-\frac{1}{t+1} \right)^{-(t+1)} 
= \lim_{t \to +\infty} \left( 1+\frac{1}{t} \right)^{t}\cdot \left( 1+\frac{1}{t} \right) = e
$$

**综合上述两步推导：**

$$ \lim_{x \to \infty} \left( 1+\frac{1}{x} \right)^{x} = e
$$