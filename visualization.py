#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[16]:


result = pd.read_table('form_results.txt', sep = ' ', index_col = 0)


# In[18]:


result.head()


# In[61]:


#create the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
sns.countplot(x="Grade", data=result, ax = ax1)
sns.countplot(x="Curve_Grade", data=result, ax = ax2)
#save the graphs
plt.savefig('letter_grades.png')


# In[62]:


#create the distributions
sns.histplot(x = 'Percent', bins = 10, color = 'skyblue', data = result).set(title = 'Distribution of Percentages')
sns.histplot(x = 'Curved', bins = 10, color = 'orange', kde = False, data = result) 
plt.savefig("grade_dists.png")


# In[ ]:




