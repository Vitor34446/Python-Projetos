import numpy as np


rng = np.random.default_rng()
# print(rng.integers(1,34,(3,5)))
# np.random.seed(1)

# print(np.random.uniform(2,5,(2,3)) * 100)
# array = np.array([1,2,3,4,5,6])
# rng.shuffle(array)
# print(array)

frutas = ['banana','maçã','melancia','mamão']
frutas = rng.choice(frutas, 3)
print(frutas)