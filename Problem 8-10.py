#!/usr/bin/env python
# coding: utf-8

# ## problem 8
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
# 
# 

# In[1]:


N = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


# In[2]:


N 


# In[3]:


import numpy as np
import pandas as pd
import math


# In[4]:


numb_list = list(map(int,list(str(N))))
all_comb = [numb_list[idx:idx+13] for idx in range(len(numb_list)) if 0 not in numb_list[idx:idx+13]]
data = [[comb,math.prod(comb)] for comb in all_comb]
df = pd.DataFrame(data)


# In[5]:


df.sort_values(by=[1],ascending=False).head()


# In[6]:


math.prod([9, 4, 7, 8, 8, 5, 1, 8, 4, 3, 8, 5, 8])


# In[7]:


np.prod(all_comb)


# In[8]:


numb_list[idx:idx+13]


# In[ ]:


numb_list[12]


# ## Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# In[ ]:


for a in range(1,1000):
    for b in range(a,1000-a):
        c = 1000-a-b
        if((a**2)+(b**2)==c**2):
            print("I found it! Yeay")
            print(a,b,c)
            break
        else:
             b+=1
    a+=1
    


# In[ ]:


200*375*425


# ## prob 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

# In[ ]:


not 10%2 or 10%3


# In[ ]:


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True


# In[ ]:


N = 2*10**6


# In[ ]:


sum([numb for numb in range(1,N+1) if is_prime(numb)])


