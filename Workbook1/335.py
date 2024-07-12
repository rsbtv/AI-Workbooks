arr = [i for i in range(0, 10)]
arr[::2] = arr[::2][::-1]
print(arr)
