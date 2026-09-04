import numpy as np 
import random
'''no_1 = 0
no_2 = 0
no_3 = 0 
no_4 = 0
no_5 = 0
no_6 = 0'''
prob = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
def uniform(n, m):
  return np.random.randint(1, n+1, size = m)
print(uniform(2, 1))
print(uniform(2, 10))
print(uniform(2,100))


for i in range(1000000):
    guess = random.randint(1,6)
    if guess == 1:
        prob[1] += 1
    elif guess == 2:
        prob[2] += 1
    elif guess == 3:
        prob[3] += 1
    elif guess == 4:
        prob[4] += 1
    elif guess == 5:
        prob[5] += 1
    else:
        prob[6] += 1
print(prob)

   


