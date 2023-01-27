#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


a=pd.read_csv('C:/Users/LENOVO/Desktop/game.txt',delimiter=',')


# In[4]:


a


# In[6]:


c=a.info()


# In[8]:


a.head()


# 1)Total number of goals in all games from winning teams?

# In[10]:


b=a['winner_goals'].sum()
b


# 2)Total number of goals in all games from both teams combined?

# In[11]:


b=a['winner_goals'].sum()+a['opponent_goals'].sum()
b


# 3)Average number of goals in all games from the winning teams?

# In[12]:


b=a['winner_goals'].mean()
b


# 4)Average number of goals in all games from the winning teams rounded to two decimal places?

# In[13]:


b=round(a['winner_goals'].mean(),2)
b


# 5)Average number of goals in all games from both teams?

# In[15]:


a['total_goal']=a['winner_goals']+a['opponent_goals']
a.head()


# In[16]:


b=a['total_goal'].mean()
b


# 6)Most goals scored in a single game by one team?

# In[23]:


b=a.loc[a['total_goal']==a['total_goal'].max()]
b


# In[24]:


c=b.iloc[0,4]
print(c)


# 7)Number of games where the winning team scored more than two goals?

# In[25]:


a.head()


# In[29]:


b=a.loc[a['winner_goals']>2]
b


# In[31]:


b.count()[0]


# 8)Winner of the 2018 tournament team name?

# In[33]:


a.head()


# In[36]:


b=a.loc[(a['year']==2018) & (a['round']=='Final')]
b


# In[38]:


b['winner'][0]


# 9)List of teams who played in the 2014 'Eighth-Final' round?

# In[44]:


a.head()


# In[43]:


b=a.loc[ (a['year']==2014) & (a['round']=='Eighth-Final') ]
b


# In[59]:


s=list(b['winner'])
d=list(b['opponent'])
s+d


# 10)List of unique winning team names in the whole data set?

# In[60]:


a.head()


# In[64]:


b=a.groupby('winner').count()
b.head()


# In[67]:


b=list(b.index)
b


# 11)Year and team name of all the champions?
# 

# In[68]:


a.head()


# In[69]:


b=a.loc[a['round']=='Final']
b.head()


# In[77]:


s=b.iloc[:,0:3:2]
s.reset_index(drop=True)


# 12)List of teams that start with 'Co'?

# In[73]:


a.head()


# In[85]:


import re
b=a.loc[a['winner'].str.contains('^Co[a-z]*',flags=re.I,regex=True)]
c=a.loc[a['opponent'].str.contains('^Co[a-z]*',flags=re.I,regex=True)]
b


# In[86]:


c


# In[93]:


s=list(b.iloc[:,2])
s


# In[ ]:




