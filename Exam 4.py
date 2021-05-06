#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[41]:


def observed_kmers(k, seq):
    f_list = []
    u_list = []
    count = 0
    string = len(seq)
    for i in range(1,string+1):
        putk = seq[(i-1):(i-1+k)]
        if len(putk) == k:
            f_list.append(putk)
    for item in f_list:
        if item not in u_list:
            count +=1
            u_list.append(item)
    return(count)
    


# In[43]:


observed_kmers(5, "ATTTGGATT")


# In[33]:


def possible_kmers(k, seq):
    string=len(seq)
    a = string - k + 1
    b = 4**k
    if a < b:
        return a
    else:
        return b
    
    


# In[29]:


pkmers(6, "GAATTAA")


# In[53]:


def k_table_df(seq):
    
    data = [] 
    string = len(seq)  
    for i in range(1, string+1): 
        k = i 
        data.append([observed_kmers(k, seq), possible_kmers(k, seq)]) 
    Table = pd.DataFrame(data, index = range(1,string+1), columns = ['Observed kmers', 'Possible kmers']) 
    Table.loc['Total']= Table.sum()  
    return(Table)


# In[54]:


k_table_df("ATTTGGATT")


# In[36]:





# In[38]:





# In[ ]:




