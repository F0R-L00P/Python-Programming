import numpy as np
from scipy.optimize import least_squares

#y = mx + b

b = 1
m = 0

x = [1, 2, 3]

y = [1, 1, 1]


#sum[y - (mx +b)]^2


# define a function

def least_square(x, y, y_intercept, slope):
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(x)):
        list1.append(x[i] * m)
    for j in range(len(list1)):
        list2.append(list1[i] + b)
    for i in range(len(list2)):
        list3.append((y[i] - list2[i])**2)

    return sum(list3)


least_square(x, y, y_intercept =b, slope=m )


from functools import partial

def eq_line(x, y_inter, slope):
    return (slope*x) + y_inter

eq_line()
x0 = np.array(x)

least_squares(partial(eq_line, y_inter = 1, slope = 0), x0 = x0)






