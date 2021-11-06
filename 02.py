# Exercises from Chapter 2 - Python Refresher
# Collection of things I haven't used and interesting observations of those things I haven't used.

# Use Default Dictionary to create a dictionary that will insert default values using a function
from collections import defaultdict 
# Function equivalent to d= defaultdict(lambda: "Not Present") 
def def_value():
    return("No Value Present")

d = defaultdict(def_value) # First Argument must be callable function [no params] or value None
d["a"] = 1
d["b"] = 2
# Prints results
print("==============================================")
print("Exercises for Default Dictionary Starts here")
print("==============================================")
print(d["a"]) # Prints 1
print(d["b"]) # Prints 2
print(d["c"]) # Prints No Value Present

# Random has some neat functions I haven't used
import random
random_shuffle = list(range(10)) # Create a list of 1 to 10 to be shuffled
random.shuffle(random_shuffle) # Shuffles the original list, so no need to assign a variable
random_range   = random.randrange(3,6) # Pick a Random Number from the following Range
random_choice  = random.choice(["Alice","Bob","Charlie"]) # Picks a value from the list
random_seed    = random.seed(10) # Ensure randomness is seeded for predictable results


# print(f"Random Seed: {random_seed}") # value will be None cause it's meant to setup the range not return a value!
print("==============================================")
print("Exercise in Randomness starts here")
print("==============================================")
print(f"Random Range: {random_range}")
print(f"Random Shuffle: {random_shuffle}")
print(f"Random Choice: {random_choice}")

# Exercises in Enumeration : Enumeration returns the current iteration and value at that iteration
print("==============================================")
print("Exercise in Enumeration starts here")
print("==============================================")
Names= ["Alex","Yeral","Matt","Glo"] #Enumeration is based on iteration : [(0, 'Alex'), (1, 'Yeral'), (2, 'Matt'), (3, 'Glo')]
print(list(enumerate(Names, start=1))) # Enumerations can be started on something other than 0
for _ , j in enumerate(Names):# Use underscore to throw away unnesecary values [i.e. get Alex instead of (0,'Alex') ]
    print(j)
print(next(enumerate(Names))) # Enumerate is an iterable and it can be moved with Next() and stop by yield()

# Exercises in Enumeration : Enumeration returns the current iteration and value at that iteration
print("==============================================")
print("Exercise in Zip starts here")
print("==============================================")
first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]
zipped = list(zip(first,second,third)) # [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]
a,b,c = zipped
print(f"First: {first}\n Second: {second}\n Third: {third}")
print(f"Zipped content:{zipped}")
print(f"Unpacked Values:\n{a}\n{b}\n{c}")
# * - Unpacking for lists
# ** - Unpacking for dictionaries
print("Unpacking the zip using star")
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs) # This unpacks a list.
print(f"Thing to unpack: {pairs}")
print(f"Numbers: {numbers}")
print(f"Letters: {letters}")






