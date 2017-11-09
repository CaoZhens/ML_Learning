# 机器学习的数学基础（2）Gamma函数

## 由两个基本积分式到Gamma函数

### 基本积分式1：$x^n$积分

$$\int_0^{+\infty} x^n \,{\rm d}x = \left. \frac{1}{n+1}x^{n+1} \right|_0^{+ \infty}$$

### 基本积分式2：$e^{-x}$积分

$$\int_0^{+\infty} e^{-x}\,{\rm d}x = \left. {-e^{-x}} \right|_0^{+\infty} = -e^{-\infty} - (-e^{-0}) = 1$$

### 提问：如果对$x^ne^{-x}$积分呢？

记：
$$\int_0^{+\infty} x^ne^{-x}\,{\rm d}x$$是关于n的函数。

稍微变换一下表现形式：
$$\int_0^{+\infty} t^{x-1}e^{-t}\,{\rm d}t = \Gamma(x)$$
即Gamma函数$\Gamma(x)$。

下面我们来推导$\Gamma(x)$的求解并阐述其代数意义。

## Gamma函数的求解与代数意义

首先，当$x=1$时，Gamma函数退化为基本积分式2:
$$\Gamma(1) = \int_0^{+\infty} t^{0}e^{-t}\,{\rm d}t = \int_0^{+\infty} e^{-t}\,{\rm d}t = 1$$

下面，根据分步积分原理推导$\Gamma(x)$:
$$\Gamma(x) = \int_0^{+\infty} t^{x-1}e^{-t}\,{\rm d}t = -\int_0^{+\infty} t^{x-1}\,{\rm d}(e^{-t}) = \left. -t^{x-1}e^{-t}\right|_0^{+\infty} + \int_0^{+\infty} e^{-t}\,{\rm d}(t^{x-1}) = 0 + (x-1) \int_0^{+\infty} t^{x-2}e^{-t}\,{\rm d}t = (x-1)\Gamma(x-1)$$

根据上述推导得：
$$\Gamma(x) = (x-1)!$$

即：**Gamma函数的代数意义是：阶乘在实数域上的推广！**