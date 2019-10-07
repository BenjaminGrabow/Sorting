# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
  if arr != None:
    for i in range(len(arr)):
        smallest_num_index = i
        for j in range(i+1, len(arr)):
            if arr[smallest_num_index] > arr[j]:
                smallest_num_index = j
        arr[i], arr[smallest_num_index] = arr[smallest_num_index], arr[i]
    return arr

# TO-DO:  implement the Bubble Sort function below

# SOLUTION WITH WHILE LOOP
def bubble_sort(arr):
  if arr != None:
    check = True
    while check:
      check = False
      for index in range(0, len(arr) - 1):
          if arr[index] > arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
            check = True
  return arr

# SOLUTION WITH DOUBLE LOOP
def bubble_sort(arr):
  if arr != None:
    for i in arr:
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

# DIFFERENT SOLUTION WITH DOUBLE LOOP
def bubble_sort(arr):
  if arr != None:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
  return arr

# RECURSIVE SOLUTION BUBBLE SORT
def bubble_sort(arr):
  if arr != None:
    for i in range(len(arr)):
        try:
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                bubble_sort(arr)
        except IndexError:
            pass
  return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
