
# ## Problem 16
# ### What is the sum of the digits of the number 2 power 1000?
# 
# 

# In[46]:


num = 2**1000


# In[47]:


numb_list = list(map(int,list(str(num))))


# In[48]:


sum(numb_list)


# ## Problem 17
# Number letter counts
# 
# https://en.wikipedia.org/wiki/English_numerals

# In[46]:


import inflect
p = inflect.engine()


# In[44]:


l=[ len((p.number_to_words(x).replace(" ","")).replace("-","").replace(",","")) for x in range (1,1000+1)]


# In[45]:


sum(l)


# ## Problem 18
# triangle path max sum
# Using multi-stage dynamic programming

# In[47]:


numbs = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


# In[196]:


mst = [list(map(int,x.split(" "))) for x in numbs.split("\n") if x!=""] 


# In[197]:


[mst[baris] for baris in range(len(mst))]


# In[214]:


data=[]
for baris in range(len(mst)-1):
    data_baris=[]
    for kolom in range(len(mst[baris])):
        add = [mst[baris+1]]
        data_baris+= add
    data+=[data_baris]


# In[215]:


for baris in range(len(data)):
    for kolom in range(len(data[baris])): 
        for idx in range(len(data[baris][kolom])):
            if (idx not in [kolom,kolom+1]):
                data[baris][kolom][idx]=0
                

