import timeit
import time
import pandas as pd
import matplotlib.pyplot as plt
b = []
c = []
code_to_test = """
tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [10]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)
b.append((elapsed_time))

code_to_test = """
tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [15]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)
b.append((elapsed_time))

code_to_test = """
tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [20]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)
b.append((elapsed_time))

code_to_test = """
tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [25]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)
b.append((elapsed_time))

code_to_test = """
tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [30]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)
b.append((elapsed_time))

tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [10, 15, 20, 25, 30]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])
print(tribonacciNumbersValue)

def F(n):
    if (n == 1 or n == 2):
        return 0
    elif (n == 3):
        return 1
    return F(n - 1) + F(n - 2) + F(n - 3)

start = int(round(time.time() * 1000)) ## точка отсчета времени
print(F(10))
end = int(round(time.time() * 1000)) - start ## собственно время работы программы
c.append((end)*10**(-3))

start = int(round(time.time() * 1000)) ## точка отсчета времени
print(F(15))
end = int(round(time.time() * 1000)) - start ## собственно время работы программы
c.append((end)*10**(-3))

start = int(round(time.time() * 1000)) ## точка отсчета времени
print(F(20))
end = int(round(time.time() * 1000)) - start ## собственно время работы программы
c.append((end)*10**(-3))

start = int(round(time.time() * 1000)) ## точка отсчета времени
print(F(25))
end = int(round(time.time() * 1000)) - start ## собственно время работы программы
c.append((end)*10**(-3))

start = int(round(time.time() * 1000)) ## точка отсчета времени
print(F(30))
end = int(round(time.time() * 1000)) - start ## собственно время работы программы
c.append((end)*10**(-3))
a = [10, 15, 20, 25, 30]
print(a)
print(b)
print(c)

plt.plot(a, b, marker='o', linestyle='-', color='lightskyblue', markersize=8, linewidth=2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xlabel('Численные параметры', fontsize=12)
plt.ylabel('Затраченное время в секундах', fontsize=12)
plt.title('Соотношение введенных параметров и затраченного времени для первого варианта', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
plt.plot(a, c, marker='o', linestyle='-', color='lightskyblue', markersize=8, linewidth=2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xlabel('Численные параметры', fontsize=12)
plt.ylabel('Затраченное время в секундах', fontsize=12)
plt.title('Соотношение введенных параметров и затраченного времени для второго варианта', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()