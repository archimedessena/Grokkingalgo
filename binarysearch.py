# Binary search algorithm in python 
def binary_search(list, item):
    low = 0 # low position
    high = len(list) - 1 # highest number and position

    while low <= high:  # While you haven`t narrowed it down to one element
        mid = (low + high)  # check middle element
        guess = list[mid]
        if guess == item: # found item
            return mid
        if guess > item: # guess was too high
            high = mid - 1
        else: # guess was too high
            low = mid + 1
    return None # item does not exist 


my_list = [100, 99, 98, 97, 96, 95]

print(binary_search(my_list, 95))






#Binary search algorithm
def binary_searchone(arr, items):
    small = 0
    largest = len(arr) - 1
    while small <= largest:
        midd = (small + largest)
        guss = arr[midd]
        if guss == items:
            return midd
        if guss > items:
            largest = midd - 1
        else:
            low + 1
    return None

my_list = [100, 99, 98, 97, 96, 95]

print(binary_searchone(my_list, 95))        

