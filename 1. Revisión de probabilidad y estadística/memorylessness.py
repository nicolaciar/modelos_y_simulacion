#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.stats import expon


# In[2]:


media = 0
for _ in range(10000):
    media += expon.rvs(0,3)
print(media/10000)


# In[5]:


prob_t = 0
prob_condicional = 0
condicion = 0
s = 1
t = 1.5
for _ in range(10000):
    EXP = expon.rvs(0,2)    
    if EXP > t:
        prob_t += 1
    if EXP > s:
        condicion += 1
        if EXP > s + t:
            prob_condicional += 1
prob_condicional /= condicion
prob_t /= 10000
print(prob_t, prob_condicional)


# In[ ]:




