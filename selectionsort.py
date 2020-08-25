# selection sort algorithm
def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value
    smallest_index = 0 #Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#Now you can use this function to write selection sort:
def selectionSort(arr): #Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # Finds the smallest element in the array, and adds it to the new array
        newArr.append(arr.pop(smallest))
    return newArr



print(selectionSort([5, 3, 6, 2, 10, 23, 78, 89, 12, 4, 6, 89, 2, 57, 84, 35, 67, 78, 23, 56, 7889]))




