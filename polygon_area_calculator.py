#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return(self.width*self.height)
    def get_perimeter(self):
        return((2*self.width)+(2*self.height))
    def shape_calculator(self):
        if self.width !=self.height:
            return(f"Rectangle(width={self.width},height={self.height})")
        else:
            return(f"Square(side={self.width})")        
    def get_diagonal(self):
        return(((self.width**2)+(self.height**2))**0.5)
    def get_picture(self):
        if self.width>50:
             print('Too big for picture.')
        else:
            for i in range(1,self.height+1):
                for j in range(1,self.width+1):
                    print("*",end="")
                print()
    def get_amount_inside(self):
        return(int((self.width*self.height*0.5)**0.5))
rect=Rectangle(10,5)
print(rect.get_area())
rect.height=3
print(rect.get_perimeter())
print(rect.shape_calculator())
rect.get_picture()

class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)
        self.side=side
sq=Square(9)
print(sq.get_area())
sq=Square(4)
print(sq.get_diagonal())
print(sq.shape_calculator())
sq.get_picture()


rect.height=8
rect.width=16
print(rect.get_amount_inside())

