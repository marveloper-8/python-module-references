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
a = ["apple", "banana", "cherry"]
print(random.choice(a))
print(random.choice("WELCOME"))

# random choices
print(random.choices(
    a,
    weights=[10, 1, 1],
    k = 14
))

# random shuffle
# random.shuffle(a)
print(a)

# def b():
#     return 0.1

# random.shuffle(a, b)
# print(a)

# random sample
print(random.sample(a, k=2))

# random random
print(random.random())

# random uniform
print(random.uniform(20, 60))

# random triangular
print(random.triangular(20, 60, 30))

