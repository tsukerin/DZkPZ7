import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

a = [1,4,-2,3,5,-16,7,2,1,-3,-2,-8,2,-1,2,-3,5,-7,4,9]
sum_ = a[0]
klerk = 0
ValueREP = []
for i in range(1,len(a)):
    if (sum_ < 0):
        for c in range(klerk):
            ValueREP.append(zuz)
        ValueREP.append(0)
        klerk = 1
        sum_ = a[i]
        zuz = -2
    else:
        klerk += 1
        zuz = sum_
        sum_ += a[i]

с = list(map(str, a))
plt.bar(с, ValueREP)
plt.xlabel('Числа по очереди')
plt.ylabel('Сумма последовательности')
plt.show()