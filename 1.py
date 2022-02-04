# random seed
import random

# random.seed(10)
# print(random.random())

# random.seed(10)
# print(random.random())

# random getstate
# print(random.getstate())

# random setstate
# print(random.random())

# a = random.getstate()
# print(random.random())

# random.setstate(a)
# print(random.random())

# getrandbits
# print(random.getrandbits(8))

# randrange
print(random.randrange(3, 9))

# randint
print(random.randint(3, 9))

# random choice
print(random.choice(["apple", "banana", "cherry"]))
print(random.choice("WELCOME"))

# random choices
print(random.choices(
    ["apple", "banana", "cherry"],
    weights=[10, 1, 1],
    k = 14
))