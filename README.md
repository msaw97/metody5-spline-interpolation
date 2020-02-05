# metody5-spline-interpolation
Interpolation of a spline function. Examples are subject to change in the code.

### Following example where:
- t = [0, 1, 2, 3]
- y =  [1, 1, 0, 10]

### Resulting equations are:
- S0(x) = 0.0(1 - x)^3 + -1.0(x - 0)^3 + 2.0(x - 0) + 1.0(1 - x)
- S1(x) = -1.0(2 - x)^3 + 3.0(x - 1)^3 + -3.0(x - 1) + 2.0(2 - x)
- S2(x) = 3.0(3 - x)^3 + 0.0(x - 2)^3 + 10.0(x - 2) + -3.0(3 - x)

### Graph of a example spline function:
![](/images/Figure_1.png)
