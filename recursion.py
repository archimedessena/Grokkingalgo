# While loop 
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
        if item.is_a_box():
            pile.append(item)
        elif item.is_a_key():
        print “found the key!”

# The recursion form of that code, every recursive function has two part the base case and the recursive case
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) # Recursion
        elif item.is_a_key():
            print "found the key!"



# infinite recursive function but it a countdown
def countdown(i):
    print i
countdown(i-1)

# the correct form of the code above
def countdown(i):
    print i
    if i <= 0: # Base case
        return i
    else: # Recursive Base
        countdown(i-1)
countdown(i-1)

