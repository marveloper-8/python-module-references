# random seed
import random

# random.seed(10)
# print(random.random())

# random.seed(10)
# print(random.random())

# random getstate
# print(random.getstate())

# random setstate
print(random.random())

a = random.getstate()
print(random.random())

random.setstate(a)
print(random.random())