def my_is_sort(arr):
    if len(arr) == 0:
        return True
    if arr == sorted(arr,reverse=False):
        return True
    elif arr == sorted(arr,reverse=True):
        return True
    else:
        return False

# my_is_sort([10, 4, 5, 8, 10])
# my_is_sort([1, 2, 3])
# my_is_sort([2, 1, -1])
# my_is_sort([4, 7, 0, 3])
# my_is_sort([])
    