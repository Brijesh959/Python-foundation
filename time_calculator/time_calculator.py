#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add_time(m,n,t=0):
    a=m
    b=n
    r=t
    if r==0:
        k=[a,b] 
    else:
        k=[a,b,r]
    c=a.split()[0]
    d1=int(c.split(':')[0])
    e1=int(c.split(':')[1])
    f=a.split()[1]
    s=b.split(':')
    d2=int(s[0])
    e2=int(s[1])
    if d1+d2<12 and e1+e2<60:
        a=d1+d2
        z=e1+e2   
        return('{}:{} {}'.format(a,z,f))
    else:
        a=d1+(d2%24)
        z=e1+e2
        if z>=60:
            a=a+1
            z=z-60
            z=str(z)
            if len(z)==1:
                z=str(0)+z
            else:
                z=z
            if a>=24:
                if a-12==0:
                    a=12
                else:
                    a=a-12
                if f=='PM':
                    f=f
                else:
                    f='AM'
            else:
                if a-12==0:
                    a=12
                else:
                    a=a-12
                if f=='PM':
                    f='AM'
                else:
                    f='PM'
        else:
            a=a
            z=z
            if a>=24:
                if a-12==0:
                    a=12
                else:
                    a=a-12
                if f=='PM':
                    f=f
                else:
                    f='AM'
            else:
                if a-12==0:
                    a=12
                else:
                    a=a-12
                if f=='PM':
                    f='AM'
                else:
                    f='PM'   
        x=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        y=0
        if r in x:
            q=x.index(r)
            y=y+q
        a1=d1+d2
        z1=e1+e2
        if z1>=60:
            a1=a1+1
            z1=z1-60
        else:
            a1=a1
            z1=z1
        v=a1//24
        h=v+1
        if v==0:
            l=r
        else :
            l=x[y+(h%7)]
        if (r in k): 
            if (v>=1):          
                return('{}:{} {}, {} ({} days later)'.format(a,z,f,l,h))  
            else:
                return('{}:{} {}, {}'.format(a,z,f,l,h))
        elif v==0:
            if f=='AM' :
                return('{}:{} {} (next day)'.format(a,z,f,h))
            elif f=='PM':
                return('{}:{} {}'.format(a,z,f,h)) 
        else:
            return('{}:{} {} ({} days later)'.format(a,z,f,h))
 

print(add_time('3:00 PM','3:10'))
print(add_time('11:30 AM','2:32','Monday'))
print(add_time('11:43 AM','00:20'))
print(add_time('10:10 PM','3:30'))
print(add_time('11:43 PM','24:20','Tuesday'))
print(add_time('6:30 PM','205:12'))


# In[ ]:




