# Testing recursion 
def countdown(i):
    if i <= 0: # Base case
        return i
    else: # Recursive Base
        countdown(i-1)



def fact(x):
    if x == 1:
        return 1
    else: 
        return 2 + fact(x - 1)

    
print(fact(3))
