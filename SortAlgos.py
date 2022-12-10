


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


def insertion_sort(list):
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


def selection_sort(list):
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

def mergesort(list):
  # if the length of the list is 0 or 1, the list is already sorted
  if len(list) <= 1:
    return list
  
  # divide the list in half
  center = len(list) // 2
  L = list[:center]
  R = list[center:]
  
  # sort the L and R halves of the list using the mergesort function
  L = mergesort(L)
  R = mergesort(R)
  
  # initialize empty lists for storing the merged list
  sorted_list = []
  L_index = 0
  R_index = 0
  
  # iterate through the L and R halves of the list, and merge the
  # elements in sorted order into the sorted_list list
  while L_index < len(L) and R_index < len(R):
    if L[L_index] < R[R_index]:
      sorted_list.append(L[L_index])
      L_index += 1
    else:
      sorted_list.append(R[R_index])
      R_index += 1
      
  # add any remaining elements from the L or R


list = [5, 1, 3, 2, 4]
sorted_list = bubblesort(list)
print(sorted_list) 

list2 = [67, 90 , 23, 12 , 13 , 13, 2, 3,1, 3]
sorted_list2 = quicksort(list2)
print(sorted_list2) 

