def merge( arrA, arrB ):
    result = []

    arrA_index = arrB_index = 0

    while arrA_index < len(arrA) and arrB_index < len(arrB):
      if arrA[arrA_index] < arrB[arrB_index]:
        result.append(arrA[arrA_index])
        arrA_index += 1
      else:
        result.append(arrB[arrB_index])
        arrB_index += 1
    
    if arrA_index == len(arrA):
      result.extend(arrB[arrB_index:])
    else:
      result.extend(arrA[arrA_index:])

    return result


def merge_sort( arr ):
    if len(arr) <= 1:
      return arr
    
    midpoint = int(len(arr) / 2)

    leftArray, rightArray = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(leftArray, rightArray)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
