# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below

# while loop 
def bubble_sort(arr):
  check = True
  while check:
    check = False
    for index in range(0, len(arr) - 1):
      if arr[index] > arr[index + 1]:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
        check = True
  return arr

# try with double loop:

# try with recursive solution:

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr