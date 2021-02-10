import random
from random import shuffle
from random import shuffle as my_shuffle

fruits = ["apples", "pears", "bananas"]
print(fruits)
random.shuffle(fruits)
print(fruits)
print(random.choice(fruits))

# using from random import shuffle - using only the function
shuffle(fruits)
print(fruits)

# using shuffle as renamed function
my_shuffle(fruits)
print(fruits)