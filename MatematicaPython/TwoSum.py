def twoSum(list, target):

    sum = 0
    for i, v1 in enumerate(list):
        for j, v2 in enumerate(list):
            sum = v1+v2
            if sum == target:
                return i, j


v = [2, 7, 11, 15]
print(twoSum(v, 9))
