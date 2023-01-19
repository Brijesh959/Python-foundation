#!/usr/bin/env python
# coding: utf-8

# In[4]:


def arithmetic_arranger(D1):
        import sys
        a1=D1
        a=[]
        for i in a1:
            i=i.replace(" ",'')
            a.append(i)
        ##############################################################################################
        if len(a)>5:
            print('Error:Too many problems.')
            sys.exit()

        ##############################################################################################
        #partition conversion according to operand
        k=[]
        l=[]
        for i in a:
            if '+' in i:
                p=i.partition('+')
                k.append(p)
            elif '/' in i:
                p=i.partition('/')
                k.append(p)
            elif '*' in i:
                p=i.partition('*')
                k.append(p)
            else:
                p=i.partition('-')
                k.append(p)
        for i in k:
            i=list(i)
            l.append(i)
        #############################################################################################

        m=[]

        for i in range(len(l)):
            for j in range(0,len(l[i]),2):
                m.append(l[i][j])
        for i in range(len(m)):
            if len(m[i])>4:
                print('Error:Numbers cannot be more than four digits.')
                sys.exit()
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j].isdigit():
                    pass
                else:
                    print('Error:Numbers must only contain digits.')
                    sys.exit()

        ###########################################################################################
        #length and maximum length  calculation after partition
        s=[]
        f=[]
        for i in range(len(l)):
            a=[]
            for j in range(len(l[i])):
                d=len(l[i][j])
                a.append(d)
            f.append(max(a))
            s.append(a)
        #number of space calculation for first row
        g=[]
        for i in range(len(f)):
            for j in range(len(s[i])):
                if j!=0:
                    continue
                elif i==0 and j==0:
                    n=f[i]-s[i][j]+2
                    g.append(n)
                else:
                    n=f[i]-s[i][j]+6
                    g.append(n)
        #ADDITION CALCULATION
        v=[]
        d=[] # addition list
        for i in range(len(l)):
                for j in range(len(l[i])):
                    if l[i][1]=='+':
                        c=int(l[i][0])+int(l[i][2])
                        v.append(c)
                    elif l[i][1]=='-' :
                        c=int(l[i][0])-int(l[i][2])
                        v.append(c)
                    else:
                        print("Error:Operator must be '+' or '-'.")
                        sys.exit()
        for i in v:
            if i not in d:
                d.append(i)
        #str conversion
        x=[]
        for i in d:
            x.append(str(i))
        #length calcultion
        b=[]
        for i in x:
            b.append(len(i))       
        # number of dash calculation
        c=[] #NUMBER OF DASH
        for i in range(len(f)):
            if i==0:
                for j in range(f[i]+2):
                    print(end='')
                c.append(j+1)
            else:
                print("    ",end='')
                for j in range(f[i]+2):
                    print(end='')
                c.append(j+1)
        print()
        #len differece calculation
        o=[]
        for i,j in zip(c,b):
            o.append(i-j)
        h=[] # space after operator
        for i in range(len(f)):
            k=f[i]-s[i][2]+1
            h.append(k)
        #######################################################################################
        #first row printing
        for i in range(len(g)):
            for j in range(g[i]):
                print(' ',end='')
            print(l[i][0],end='')
        print()
        ########################################################################################
        #SECOND ROW PRINTING
        for i in range(len(f)):
            if i==0:
                print(l[i][1],end='')
                for j in range(h[i]):
                    print(' ',end='')
                print(l[i][2],end='')
            else:
                print('    ',end='')
                print(l[i][1],end='')
                for j in range(h[i]):
                    print(' ',end='')
                print(l[i][2],end='')
        print()
        ######################################################################################
        #dash printing
        c=[] #NUMBER OF DASH
        for i in range(len(f)):
            if i==0:
                for j in range(f[i]+2):
                    print('-',end='')
                c.append(j+1)
            else:
                print("    ",end='')
                for j in range(f[i]+2):
                    print('-',end='')
                c.append(j+1)
        print()
        #########################################################################################
        #value printing
        for i in range(len(o)):
            if i==0:
                for j in range(o[i]):
                    print(' ',end='')
                print(d[i],end='')
            else:
                print('    ',end='')
                for j in range(o[i]):
                    print(' ',end='')
                print(d[i],end='')
        print()
        ###########################################################################################
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])


# In[ ]:




