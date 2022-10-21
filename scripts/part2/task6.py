def make_valley(arr: list):
    arr.sort(reverse=True)
    bottom = arr[-1:]
    left = arr[:-1:][::2]
    right = arr[:-1:][1::2]
    return left + bottom + right[::-1]