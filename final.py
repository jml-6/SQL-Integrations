#!/usr/bin/env python
# coding: utf-8

# In[41]:


from sqlalchemy import create_engine
import sys
import pandas as pd


# In[64]:


#create the connection
eng = create_engine('mysql+pymysql://stat226:cougars19@statdb.byu.edu/Stat226')


# In[111]:


quer1 = 'describe Domain'
quer2 = 'describe Students'
print(pd.read_sql(quer1, eng))
print(pd.read_sql(quer2, eng))


# In[112]:


#get the tables
df1 = pd.read_sql('select * from Students', con=eng)
df2 = pd.read_sql('select * from Domain', con=eng)
df = pd.merge(df1, df2, on=['Form','Qnum'])
form = sys.argv[1]

#just with SQL
#query = f'select StudentID, Score, Form, Domain_num from Students inner join Domain on Student.Form = Domain.Form and Students.Qnum = Domain.Qnum where Form = "{Form}"'
#results = eng.execute(query)


# In[113]:


#form = 'B'
df = df[df['Form'] == form]


# In[114]:


#domain with lowest mean score

#means = df.groupby('Domain_num', as_index = False)['Score'].mean()
#means.sort_values(by = 'Score')['Domain_num'].iloc[0]
int(df.groupby('Domain_num', as_index = False)['Score'].mean().sort_values(by = 'Score').iloc[0][0])


# In[118]:


Scores = df.groupby('StudentID').sum().reset_index()


# In[123]:


# Scores.head()


# In[120]:


#create new column
Scores['Percent'] = Scores.Score / 150


# In[137]:


#define function for grading
def auto_grade(perc):
# calculate the percentage of correct answers

  # assign a letter grade based on the percentage
  if perc >= 0.9:
    return 'A'
  elif perc >= 0.8:
    return 'B'
  elif perc >= 0.7:
    return 'C'
  elif perc >= 0.6:
    return 'D'
  else:
    return 'F'


# In[144]:


#apply the function to the grades
Scores['Grade'] = Scores['Percent'].apply(auto_grade)


# In[145]:


#curved percentages
Scores['Curved'] = Scores['Score'] / Scores['Score'].max()


# In[146]:


#curved grades
Scores['Curve_Grade'] = Scores['Curved'].apply(auto_grade)


# In[166]:


# Scores


# In[164]:


#new connector to new database
eng1 = create_engine('mysql+pymysql://stats:stats@localhost/stats255_final')
conn = eng1.connect()


# In[165]:


#send to sql
Scores.to_sql('Final_Results', conn)


# In[167]:


#output file
Scores.to_csv('form_results.txt', sep = ' ')

