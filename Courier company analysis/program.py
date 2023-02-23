#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


k1=pd.read_csv('C:/Users/LENOVO/Desktop/Company X - Order Report.csv')
k1.head()


# In[3]:


k2=pd.read_csv('C:/Users/LENOVO/Desktop/Company X - SKU Master.csv')
k2.head()


# In[4]:


l1=k1.sort_values('SKU')
l1.head()


# In[5]:


l2=k2.sort_values('SKU')
l2.head()


# In[6]:


a1=l1[l1['ExternOrderNo']==2001806232]
a1


# In[7]:


g1=pd.merge(l1, l2, on='SKU', how='inner')
g1.head()


# In[8]:


s1=g1.sort_values('ExternOrderNo')
s1


# In[9]:


s1['Total weight as per X (G)']=s1['Order Qty']*s1['Weight (g)']
s1.head()


# In[10]:


s2=s1
s2.head()


# In[11]:


s2['Total weight as per X (KG)']=round(s2['Total weight as per X (G)']/1000,2)
s2.head()


# In[12]:


s4=s2[['ExternOrderNo','Total weight as per X (KG)']]
s4


# In[13]:


s5=s4.groupby('ExternOrderNo').sum()
s5.head()


# In[14]:


s5.info()


# In[15]:


#final weight according to X COMPANY
s6=s5.reset_index()
s6


# In[16]:


z1=s6
z1.head()


# In[17]:


z2=z1
z2.shape
p1=z2.shape[0]
p2=z2.shape[1]


# In[18]:


k1=z2['Total weight as per X (KG)'].max()
k1


# In[ ]:





# In[19]:


z2.loc[z2['Total weight as per X (KG)']<=0.5,'Weight slab as per X (KG)']=0.5
z2.loc[(z2['Total weight as per X (KG)']>0.5) & (z2['Total weight as per X (KG)']<=1.00) ,'Weight slab as per X (KG)']=1
z2.loc[(z2['Total weight as per X (KG)']>1.0) & (z2['Total weight as per X (KG)']<=1.5) ,'Weight slab as per X (KG)']=1.5
z2.loc[(z2['Total weight as per X (KG)']>1.5) & (z2['Total weight as per X (KG)']<=2.00) ,'Weight slab as per X (KG)']=2
z2.loc[(z2['Total weight as per X (KG)']>2.0) & (z2['Total weight as per X (KG)']<=2.5) ,'Weight slab as per X (KG)']=2.5
z2.loc[(z2['Total weight as per X (KG)']>2.5) & (z2['Total weight as per X (KG)']<=3.00) ,'Weight slab as per X (KG)']=3.0
z2.loc[(z2['Total weight as per X (KG)']>3.0) & (z2['Total weight as per X (KG)']<=3.5) ,'Weight slab as per X (KG)']=3.5
z2


# In[20]:


#final weight slab
z3=z2
z3.head()


# In[21]:


d1=z3[(z3['ExternOrderNo']==2001806232) | (z3['ExternOrderNo']==2001806210)]
d1


# In[22]:


k4=pd.read_csv('C:/Users/LENOVO/Desktop/Courier Company - Invoice.csv')
k4.head()


# In[23]:


x1=k4[['Order ID','Charged Weight']]
x1.head()


# In[24]:


###final updated order id column name
z3.rename(columns = {'ExternOrderNo':'Order ID'}, inplace = True)
z3


# In[25]:


c=pd.merge(z3,x1,on='Order ID', how='inner')
c.head()


# In[26]:


c1=c
c1.head()


# In[27]:


c1.info()


# In[28]:


c1.loc[c1['Charged Weight']<=0.5,'Weight slab charged by Courier Company (KG)']=0.5
c1.loc[(c1['Charged Weight']>0.5) & (c1['Charged Weight']<=1.00) ,'Weight slab charged by Courier Company (KG)']=1
c1.loc[(c1['Charged Weight']>1.0) & (c1['Charged Weight']<=1.5) ,'Weight slab charged by Courier Company (KG)']=1.5
c1.loc[(c1['Charged Weight']>1.5) & (c1['Charged Weight']<=2.00) ,'Weight slab charged by Courier Company (KG)']=2
c1.loc[(c1['Charged Weight']>2.0) & (c1['Charged Weight']<=2.5) ,'Weight slab charged by Courier Company (KG)']=2.5
c1.loc[(c1['Charged Weight']>2.5) & (c1['Charged Weight']<=3.00) ,'Weight slab charged by Courier Company (KG)']=3.0
c1.loc[(c1['Charged Weight']>3.0) & (c1['Charged Weight']<=3.5) ,'Weight slab charged by Courier Company (KG)']=3.5
c1.head()


# In[29]:


c1.info()


# In[30]:


v1=pd.read_csv('C:/Users/LENOVO/Desktop/Company X - Pincode Zones.csv')
v1.head()


# In[31]:


v1.rename(columns = {'Zone':'Delivery Zone as per X'}, inplace = True)
v1.head()


# In[32]:


v2=k4[['Order ID','Warehouse Pincode','Customer Pincode','Zone']]
v2.head()


# In[33]:


v2.rename(columns = {'Zone':'Delivery Zone charged by Courier Company'}, inplace = True)
v2.head()


# In[34]:


k4.head()


# In[35]:


f2=pd.concat([k4.iloc[:,1],k4.iloc[:,4],v1.iloc[:,-1],v2.iloc[:,-1]],axis=1)
f2.head()


# In[36]:


f3=pd.merge(c1,f2,on='Order ID',how='inner')
f3.head()


# In[37]:


f3.rename(columns = {'Zone':'Delivery Zone charged by Courier Company'}, inplace = True)
f3.head()


# In[38]:


f3[(f3['Order ID']==2001806232) |(f3['Order ID']==2001806210) ]


# In[39]:


c1.loc[c1['Charged Weight']<=0.5,'Weight slab charged by Courier Company (KG)']=0.5
c1.loc[(c1['Charged Weight']>0.5) & (c1['Charged Weight']<=1.00) ,'Weight slab charged by Courier Company (KG)']=1
c1.loc[(c1['Charged Weight']>1.0) & (c1['Charged Weight']<=1.5) ,'Weight slab charged by Courier Company (KG)']=1.5
c1.loc[(c1['Charged Weight']>1.5) & (c1['Charged Weight']<=2.00) ,'Weight slab charged by Courier Company (KG)']=2
c1.loc[(c1['Charged Weight']>2.0) & (c1['Charged Weight']<=2.5) ,'Weight slab charged by Courier Company (KG)']=2.5
c1.loc[(c1['Charged Weight']>2.5) & (c1['Charged Weight']<=3.00) ,'Weight slab charged by Courier Company (KG)']=3.0
c1.loc[(c1['Charged Weight']>3.0) & (c1['Charged Weight']<=3.5) ,'Weight slab charged by Courier Company (KG)']=3.5
c1.loc[(c1['Charged Weight']>3.5) & (c1['Charged Weight']<=4.00) ,'Weight slab charged by Courier Company (KG)']=4.0
c1.loc[(c1['Charged Weight']>4.0) & (c1['Charged Weight']<=4.5) ,'Weight slab charged by Courier Company (KG)']=4.5
c1


# In[40]:


j1=pd.read_csv('C:/Users/LENOVO/Desktop/Courier Company - Rates.csv')
j1.head()


# In[41]:


d5=f3.iloc[:,0:8:2]
d5


# In[42]:


d6=k4.iloc[:,-2]
d6.head()


# In[43]:


j2=pd.concat([d5,d6],axis=1)
j2


# In[44]:


j2.loc[j2['Type of Shipment']=='Forward charges','Type of Shipment']=1 
j2.loc[j2['Type of Shipment']=='Forward and RTO charges','Type of Shipment']=2
j2.head()


# In[45]:


j1.head()


# In[46]:


j5=j1.rename(columns = {'fwd_a_fixed':'af1','fwd_a_additional':'af2','fwd_b_fixed':'bf1','fwd_b_additional':'bf2'})
j5.head()


# In[47]:


j5.rename(columns = {'fwd_c_fixed':'cf1','fwd_c_additional':'cf2','fwd_d_fixed':'df1','fwd_d_additional':'df2'},inplace=True)
j5.head()


# In[48]:


j5.rename(columns = {'fwd_e_fixed':'ef1','fwd_e_additional':'ef2'},inplace=True)
j5.head()


# In[49]:


j5.rename(columns = {'rto_a_fixed':'ar1','rto_a_additional':'ar2','rto_b_fixed':'br1','rto_b_additional':'br2'},inplace=True)
j5.head()


# In[50]:


j5.rename(columns = {'rto_c_fixed':'cr1','rto_c_additional':'cr2','rto_d_fixed':'dr1','rto_d_additional':'dr2'},inplace=True)
j5.head()


# In[51]:


j5.rename(columns = {'rto_e_fixed':'er1','rto_e_additional':'er2'},inplace=True)
j5.head()


# In[52]:


k6=j5.T
k6.head()


# In[53]:


k6.rename(columns = {0:'cost'}, inplace = True)


# In[54]:


k6.head()


# In[55]:


k7=k6.reset_index()
k7.head()


# In[56]:


k7.rename(columns = {'index':'tos'}, inplace = True)


# In[57]:


###final
k8=k7
k8.head()


# In[58]:


j2.head()


# In[59]:


j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='a') ,'cx']=k8.iloc[0,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='b') ,'cx']=k8.iloc[2,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='c') ,'cx']=k8.iloc[4,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='d') ,'cx']=k8.iloc[6,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='e') ,'cx']=k8.iloc[8,1]
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='a') ,'cx']=(k8.iloc[0,1])+(k8.iloc[10,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='b') ,'cx']=(k8.iloc[2,1])+(k8.iloc[12,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='c') ,'cx']=(k8.iloc[4,1])+(k8.iloc[14,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='d') ,'cx']=(k8.iloc[6,1])+(k8.iloc[16,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']==0.5) & (j2['Delivery Zone as per X']=='e') ,'cx']=(k8.iloc[8,1])+(k8.iloc[18,1])
j2.head()


# In[60]:


j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='a') ,'cx']=(k8.iloc[0,1]+k8.iloc[1,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='b') ,'cx']=(k8.iloc[2,1]+k8.iloc[3,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='c') ,'cx']=(k8.iloc[4,1]+k8.iloc[5,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='d') ,'cx']=(k8.iloc[6,1]+k8.iloc[7,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='e') ,'cx']=(k8.iloc[8,1]+k8.iloc[9,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='a') ,'cx']=(k8.iloc[0,1]+k8.iloc[10,1]+k8.iloc[1,1]+k8.iloc[11,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='b') ,'cx']=(k8.iloc[2,1]+k8.iloc[12,1]+k8.iloc[3,1]+k8.iloc[13,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='c') ,'cx']=(k8.iloc[4,1]+k8.iloc[14,1]+k8.iloc[5,1]+k8.iloc[15,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='d') ,'cx']=(k8.iloc[6,1]+k8.iloc[16,1]+k8.iloc[7,1]+k8.iloc[17,1])*(j2['Weight slab as per X (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab as per X (KG)']>0.5) & (j2['Delivery Zone as per X']=='e') ,'cx']=(k8.iloc[8,1]+k8.iloc[18,1]+k8.iloc[9,1]+k8.iloc[19,1])*(j2['Weight slab as per X (KG)'])
j2.head()


# In[61]:


n1=j2[(j2['Order ID']==2001806232) | (j2['Order ID']==2001806210)]
n1


# In[62]:


k8


# In[63]:


j2.info()


# In[64]:


pd.set_option('display.max_rows', None)


# In[65]:


j2.head()


# In[66]:


j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='a') ,'cc']=k8.iloc[0,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='b') ,'cc']=k8.iloc[2,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='c') ,'cc']=k8.iloc[4,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='d') ,'cc']=k8.iloc[6,1]
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='e') ,'cc']=k8.iloc[8,1]
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='a') ,'cc']=(k8.iloc[0,1])+(k8.iloc[10,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='b') ,'cc']=(k8.iloc[2,1])+(k8.iloc[12,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='c') ,'cc']=(k8.iloc[4,1])+(k8.iloc[14,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='d') ,'cc']=(k8.iloc[6,1])+(k8.iloc[16,1])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']==0.5) & (j2['Delivery Zone as per X']=='e') ,'cc']=(k8.iloc[8,1])+(k8.iloc[18,1])
j2.head()


# In[67]:


j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='a') ,'cc']=(k8.iloc[0,1]+k8.iloc[1,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='b') ,'cc']=(k8.iloc[2,1]+k8.iloc[3,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='c') ,'cc']=(k8.iloc[4,1]+k8.iloc[5,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='d') ,'cc']=(k8.iloc[6,1]+k8.iloc[7,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==1) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='e') ,'cc']=(k8.iloc[8,1]+k8.iloc[9,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='a') ,'cc']=(k8.iloc[0,1]+k8.iloc[10,1]+k8.iloc[1,1]+k8.iloc[11,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='b') ,'cc']=(k8.iloc[2,1]+k8.iloc[12,1]+k8.iloc[3,1]+k8.iloc[13,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='c') ,'cc']=(k8.iloc[4,1]+k8.iloc[14,1]+k8.iloc[5,1]+k8.iloc[15,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='d') ,'cc']=(k8.iloc[6,1]+k8.iloc[16,1]+k8.iloc[7,1]+k8.iloc[17,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.loc[(j2['Type of Shipment']==2) & (j2['Weight slab charged by Courier Company (KG)']>0.5) & (j2['Delivery Zone as per X']=='e') ,'cc']=(k8.iloc[8,1]+k8.iloc[18,1]+k8.iloc[9,1]+k8.iloc[19,1])*(j2['Weight slab charged by Courier Company (KG)'])
j2.head()


# In[68]:


j2.info()


# In[69]:


jf=j2
jf.info()


# In[70]:


jf['Difference in amount']=jf['cx']-jf['cc']
jf.head()


# In[71]:


jf.info()


# In[72]:


jf.head()


# In[73]:


k5=k4.iloc[:,0]
k5.head()
k5.info()


# In[74]:


v25=k4.iloc[:,0:2]
v25.head()


# In[75]:


v25[v25["AWB Code"]==1091117221940]


# In[76]:


v50=pd.merge(v25,jf,on='Order ID',how='inner')
v50


# In[77]:


v50[(v50["AWB Code"]==1091117221940) |(v50["AWB Code"]==1091117222124)]


# In[78]:


c1.head()


# In[79]:


h25=pd.concat([c1.iloc[:,0:2],c1.iloc[:,3]],axis=1)
h25.head()


# In[80]:


b25=pd.merge(v50,h25,on='Order ID',how='inner')
b25.head()


# In[81]:


b25.info()


# In[82]:


a12=pd.concat([f3.iloc[:,0],f3.iloc[:,-1]],axis=1)
a12.head()


# In[83]:


a25=pd.merge(b25,a12,on='Order ID',how='inner')
a25.head()


# In[84]:


a25.info()


# In[85]:


a25.drop(['Type of Shipment'], axis=1)


# In[86]:


p=a25.columns.values # array conversion
p=list(a25)          # list conversion
p


# In[87]:


a25=a25[[p[1]] +[p[0]]+[p[-3]]+[p[2]]+[p[-2]]+[p[3]]+[p[4]]+[p[-1]]+p[6:9] ] 
a25.head()


# In[88]:


a25.info()


# In[89]:


a25[(a25['Order ID']==2001806232) |(a25['Order ID']==2001806210)]


# In[90]:


ff=a25
ff.info()


# In[91]:


ff.rename(columns = {'index':'tos'}, inplace = True)


# In[92]:


p=ff.columns.values # array conversion
p=list(ff)          # list conversion
p


# In[93]:


f50=ff.rename(columns = {'AWB Code':'AWB Number','Charged Weight':'Total weight as per Courier Company(KG)','cx':'Expected Charge as per X(Rs.)','cc':'Charged Billed by Courier Company(Rs.)','Difference in amount':'Difference Between Expected Charges and Billed Charges(Rs.)'})
f50.head()


# In[94]:


f50.to_excel('order level calculation.xlsx',index=False)


# In[95]:


f51=f50
f51.head()


# In[96]:


f51.loc[f51['Difference Between Expected Charges and Billed Charges(Rs.)']==0,'conclusion']='Correctly Charged'
f51.loc[f51['Difference Between Expected Charges and Billed Charges(Rs.)']<0,'conclusion']='Over Charged'
f51.loc[f51['Difference Between Expected Charges and Billed Charges(Rs.)']>0,'conclusion']='Under Charged'


# In[97]:


f51.head()


# In[98]:


f52=f51
f52.head()


# In[99]:


f53=f52.groupby('conclusion').sum()
f53


# In[100]:


f53.reset_index()


# In[101]:


f53.loc[f53['Difference Between Expected Charges and Billed Charges(Rs.)']==0,'Difference Between Expected Charges and Billed Charges(Rs.)']=f53.iloc[0,-2]


# In[102]:


f53


# In[103]:


Amount=(f53.iloc[:,-1])
Amount


# In[104]:


f54=f52.groupby('conclusion').count()
f54


# In[105]:


count=f54.iloc[:,0]
count


# In[106]:


summery=pd.merge(count,Amount,on='conclusion',how='inner')
summery


# In[107]:


k100=summery.rename(columns ={'Order ID':'count','Difference Between Expected Charges and Billed Charges(Rs.)':'Amount'})
k100


# In[108]:


k100.to_excel('Summery table.xlsx')


# In[ ]:




