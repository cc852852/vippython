from sympy import *
x = symbols('x')
x0 = 0.5
x_list = [x0]
i = 0

def f(x):
    f = x**3-x-1
    return f

while True:   
    if diff(f(x),x).subs(x,x0) == 0:
        print('极值点：',x0)
        break
    else:
        x0 = x0 - f(x0)/diff(f(x),x).subs(x,x0)
        x_list.append(x0)
    if len(x_list) > 1:
        i += 1
        error = abs((x_list[-1] - x_list[-2]) / x_list[-1])
        if error < 10 ** (-5):
            print(f'迭代第{i}次后，误差小于10^(-5)，误差为{error}')
            break
    else:
        pass
print(f'所求方程式的根为{x_list[-1]}')
