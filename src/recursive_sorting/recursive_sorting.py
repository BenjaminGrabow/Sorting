def merge( arrA, arrB ):
    result = []# final output array

    arrA_index = arrB_index = 0 # start index 0 for booth parts

    while arrA_index < len(arrA) and arrB_index < len(arrB):# if booth indices doesn't reached the end => loop
      if arrA[arrA_index] < arrB[arrB_index]:#if a's num (num comes from current index) is smaller than the num from b's side
        result.append(arrA[arrA_index]) # add the smaller number to result
        arrA_index += 1 # and go to the next num in the side
      else: # same for the other site
        result.append(arrB[arrB_index])
        arrB_index += 1
    
    if arrA_index == len(arrA):# after the while loop there can be
    # elements left on one of the sides (a or b) left
    # to  check we compare the index with the length
      result.extend(arrB[arrB_index:]) # after check we extend the last elements 
    else: # same for other side
      result.extend(arrA[arrA_index:])

    return result


def merge_sort( arr ):
    if len(arr) <= 1: # a list if zero or one elements is sorted, by definition
      return arr
    # create midpoint for splicing
    midpoint = int(len(arr) / 2)
    #split the list in half and call merge sort recursively on each half
    leftArray, rightArray = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])
    #merge the now sorted sublists
    return merge(leftArray, rightArray)




#Single method solution 
def mergeSort(arr): 
    if len(arr) >1: 
        midpoint = int(len(arr)/2) 
        leftList = arr[:midpoint]   
        rightList = arr[midpoint:] 
  
        mergeSort(leftList)
        mergeSort(rightList)
  
        leftIndex = rightIndex = resultIndex = 0
          
        while leftIndex < len(leftList) and rightIndex < len(rightList): 
            if leftList[leftIndex] < rightList[rightIndex]: 
                arr[resultIndex] = leftList[leftIndex] 
                leftIndex+=1
            else: 
                arr[resultIndex] = rightList[rightIndex] 
                rightIndex+=1
            resultIndex+=1
          
        while leftIndex < len(leftList): 
            arr[resultIndex] = leftList[leftIndex] 
            leftIndex+=1
            resultIndex+=1
          
        while rightIndex < len(rightList): 
            arr[resultIndex] = rightList[rightIndex] 
            rightIndex+=1
            resultIndex+=1

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
