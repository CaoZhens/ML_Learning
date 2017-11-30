# 指数分布族

指数分布族（The Exponential Family)，是指**可表示为指数形式的概率分布**。  
指数分布的形式为：
$$P(y;\eta) = b(y)\exp(\eta^TT(y)-a(\eta))$$
当参数a、b、T固定时，即定义了一个以$\eta$为参数的函数族。  
下面分别将正态分布和伯努利分布表示成指数分布族的形式。

# 正态分布的指数分布形式
$$p(y) = \frac{1}{\sqrt{2\pi}\sigma} \rm{exp}({-\frac{(y-\mu_y)^2}{2\sigma^2}}) = \frac{1}{\sqrt{2\pi}} \rm{exp}(-\frac{y^2}{2}) \rm{exp}(\mu_yy-\frac{\mu_y^2}{2})$$

将上式与指数族分布形式对比：
$$b(y) = \frac{1}{\sqrt{2\pi}} \rm{exp}(-\frac{y^2}{2})$$
$$\eta = \mu$$
$$a(\eta) = a(\mu) = -\frac{\mu_y^2}{2}$$


# 伯努利分布的指数分布形式
$$p(y;\phi)=\phi^y(1-\phi)^{1-y} = \exp(y\log\phi+(1-y)\log(1-\phi)) = \exp(y\log\frac{\phi}{1-\phi}+\log(1-\phi))$$

将上式与指数组分布形式对比：
$$b(y) = 1$$
$$\eta = \log\frac{\phi}{1-\phi}$$
$$a(\eta) = -\log(1-\phi)$$

# 其它分布
除正态分布和伯努利分布之外，其它很多概率分布都可以表示成指数分布族的形式，比如：
* 多项式分布
* 高斯分布
* 泊松分布
* gamma分布
* 指数分布