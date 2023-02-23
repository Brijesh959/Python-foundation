#!/usr/bin/env python
# coding: utf-8

# In[187]:


import pandas as pd


# In[188]:


a=pd.read_csv('C:/Users/LENOVO/Desktop/adult.csv')
a.head()


# In[189]:


b=a.info()
b


# In[190]:


k=a
k.head()


# 1)How many people of each race are represented in this dataset?

# In[191]:


v=k.groupby(['race']).count()
j=v.iloc[:,0]
j


# 2)What is the average age of men?

# In[192]:



k.head()


# In[193]:


s=k.groupby('sex').mean()
v=round(s.iloc[1,0],2)
v


# 3)What is the percentage of people who have a Bachelor's degree?

# In[194]:



k.head()


# In[195]:


s=k['education'].count()
n=s
n


# In[196]:


s=k.groupby('education').count()
p=s.iloc[9,0]
p


# In[197]:


percentage=round((p*100)/n,2)
percentage


# 4)What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

# In[198]:



k.head()


# In[199]:


z=k.loc[(k['education']=='Bachelors') |(k['education']=='Masters')|(k['education']=='Doctorate')]
z.head()


# In[200]:


c=z.loc[z['salary']=='>50K']
c.head()


# In[201]:


c.shape


# In[202]:


h=c.shape[0]
h


# In[203]:


n


# In[204]:


percentage=round(h*100/n,2)
percentage


# 5)What percentage of people without advanced education make more than 50K?

# In[205]:


k=a
k.head()


# In[206]:


z=k.loc[(k['education']!='Bachelors') |(k['education']!='Masters')|(k['education']!='Doctorate')]
z.head()


# In[207]:


c=z.loc[z['salary']=='>50K']
c.head()


# In[208]:


h=c.shape[0]
h


# In[209]:


s=k['education'].count()
n=s
n


# In[210]:


percentage=round(h*100/n,2)
percentage


# 6)What is the minimum number of hours a person works per week?

# In[211]:


k=a
k.head()


# In[212]:


b=k['hours-per-week'].min()
b


# 7)What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

# In[213]:


k=a
k.head()


# In[214]:


F=k.loc[(k['hours-per-week']==k['hours-per-week'].min()) & (k['salary']=='>50K')]
F


# In[215]:


g=F['age'].count()
h=g
h


# In[216]:


s=k['education'].count()
n=s
p1=n
n


# In[217]:


percentage=round(h*100/n,2)
percentage


# 8)What country has the highest percentage of people that earn >50K and what is that percentage?

# In[218]:


k=a
k.head()


# In[219]:


x=k.loc[k['salary']=='>50K']
x.head()


# In[220]:


g=x.groupby('native-country').count()
g.head()


# In[221]:


f=g.loc[g['salary']==g['salary'].max()]
f


# In[222]:


country=f.index[0]
country


# In[223]:


w=f.iloc[0,0]
y=w
y


# In[ ]:





# In[224]:


percentage=round(y*100/p1,2)
percentage


# 9)Identify the most popular occupation for those who earn >50K in India?

# In[225]:


k=a
k.head()


# In[226]:


d=k.loc[(k['native-country']=='India') & (k['salary']=='>50K')]
d.head()


# In[227]:


j=d.groupby('occupation').count()
j


# In[228]:


p1= j[j['age']==j['age'].max()].index
print(p1[0])


# In[ ]:





# In[ ]:





# In[ ]:




