from numpy import zeros

arr = zeros((8, 8))
for i in range(0, 8, 2):
    arr[i][::2] = 1
    for j in range(1, 8, 2):
        for k in range(1, 8, 2):
            arr[j][k] = 1
print(arr)
