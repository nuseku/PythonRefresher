
import random

def bubblesort(list):
  for i in range(len(list)):
    # compare i and i+1
    for j in range(i+1, len(list)):
      # if the current element is greater than the next element, swap 
      if list[i] > list[j]:
        list[i], list[j] = list[j], list[i]
  return list


def quicksort(list):
  # base case
  if len(list) <= 1:
    return list
  # choose an element from the list to sort around
  point = list[0]
  # two lists to store less than and greater than point
  Lpoint = []
  Gpoint = []
  
  # iterate through list, and add each value to the correct list
  for i in range(1, len(list)):
    if list[i] > pivot:
      Gpoint.append(list[i])
    else:
      Lpoint.append(list[i])
      
  # sort the lists
  Gpoint = quicksort(Gpoint)
  Lpoint = quicksort(Lpoint)
  

  return Lpoint + [point] + Lpoint


def insertionsort(list):
  # iterate through the list
  for i in range(1, len(list)):
    # store the current element
    current = list[i]
    
    # iterate through the sorted sublist
    for j in range(i):
      # if the current element is less than the element at j,
      # move the element at j to the R, and set the current
      # element to the element at j
      if current < list[j]:
        list[j+1] = list[j]
        list[j] = current
  # return the sorted list
  return list


def selectionsort(list):
  # iterate through the list
  for i in range(len(list)):
    # store the current element
    current = list[i]
    # store the index of the minimum element
    min_index = i
    # iterate through the rest of the list
    for j in range(i+1, len(list)):
      # if the current element is greater than the element at j,
      # set the index of the minimum element to j
      if current > list[j]:
        min_index = j
    # swap the current element with the minimum element
    list[i], list[min_index] = list[min_index], list[i]
  # return the sorted list
  return list

def mergesort(arr):
  if len(arr) <= 1:
    return arr
  
  # divide the list into two halves
  middle = len(arr) // 2
  left = arr[:middle]
  right = arr[middle:]
  
  # sort each half recursively
  left = merge_sort(left)
  right = merge_sort(right)
  
  # merge the sorted halves back together
  return merge(left, right)

def merge(left, right):
  result = []
  
  # keep track of the current position in each list
  left_index = 0
  right_index = 0
  
  # compare the elements at the current position in each list
  # and append the smaller element to the result
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
  
  # append any remaining elements in the left list
  result.extend(left[left_index:])
  
  # append any remaining elements in the right list
  result.extend(right[right_index:])
  
  return result



nuray = [random.randint(0, 99) for _ in range(100)]
mergesort(biglist)
print(biglist)
todd = [16, 11, 6, 19, 4, 18, 14, 10, 7, 9, 15, 5, 2, 20, 3, 12, 1, 17, 13, 8]
bubblesort(todd)
print(todd)
abuziddin= [3, 8, 17, 7, 19, 10, 11, 12, 5, 1, 2, 20, 16, 15, 4, 9, 14, 13, 18, 6]
insertionsort(abuziddin)
print(abuziddin)
fehmi= [6, 19, 8, 16, 7, 4, 15, 5, 13, 1, 11, 18, 17, 20, 3, 2, 9, 10, 12, 14]
quicksort(fehmi)
print(fehmi)
alan= [17, 5, 7, 16, 15, 2, 6, 3, 1, 18, 19, 11, 8, 20, 9, 4, 13, 10, 14, 12]
selectionsort(alan)
print(alan)





