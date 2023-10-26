import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


def maxSubArray(nums):
    arrayOfSums = [nums[0]]
    maxSum = nums[0]
    maxPosition = 0

    for i in range(1, len(nums)):
        if arrayOfSums[i - 1] > 0:
            arrayOfSums.append(arrayOfSums[i - 1] + nums[i])
        else:
            arrayOfSums.append(nums[i])

        if arrayOfSums[i] > maxSum:
            maxSum = arrayOfSums[i]
            maxPosition = i

    if maxSum < 0:
        return nums[maxPosition]

    endOfMaxSubarray = maxPosition
    startOfMaxSubarray = endOfMaxSubarray

    while startOfMaxSubarray >= 0 and arrayOfSums[startOfMaxSubarray] >= 0:
        startOfMaxSubarray -= 1

    return nums[startOfMaxSubarray + 1:endOfMaxSubarray + 1]


sourceArray = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]
a = sourceArray
sum_ = a[0]
klerk = 0
ValueREP = []
max_ = -100000000
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
        max_ = max(max_, zuz)

plt.bar(str(maxSubArray(sourceArray)), max_)
plt.xlabel('Наименование')
plt.ylabel('Значение')
plt.title('Гистограмма')
plt.show()