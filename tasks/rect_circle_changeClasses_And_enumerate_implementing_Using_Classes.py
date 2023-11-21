"""class rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.area=None
    def recta(self):
        return self.width*self.height

class circle:
    def __init__(self,rad):
        self.PI = 3.14
        self.radius = rad
        self.area = None
    def circle(self):
        return self.PI * self.radius**2

class Editor:
    def __init__(self):
        self.rectangle=None
        self.circ=None
    def create_rect(self,width,height):
        self.rectangle = rect(width,height)
    def create_circle(self,radius):
        self.circ = circle(radius)
    def change(self,factor):
        width , height = factor
        self.rectangle.width = self.rectangle.width + width
        self.rectangle.height = self.rectangle.height + height

editor=Editor()
editor.create_rect(3,5)
editor.create_circle(5)
print(editor.rectangle.recta() , editor.circ.circle())
editor.change((2,2))
print(editor.rectangle.recta() , editor.circ.circle())
"""

class Myrange:
    def __init__(self,start,end,step):
        self.temp=start
        self.start=start
        self.end=end
        self.step=step
        self.count=0

    def has_next(self):
        if(self.count < (self.end-self.start)/self.step):
            return True
        else:
            return False

    def get_next(self):
        #count=0
        if(self.count < (self.end-self.start)/self.step):
            self.count += 1
            self.temp += self.step
            return (self.count - 1, self.temp - self.step)
        '''or
        for i in range(self.start,self.end,self.step):
            count += 1
            if(count == self.count):
                return (count-1 , i)
        '''
test=Myrange(10,5,-2)
print(test.get_next())
print(test.has_next())
print(test.get_next())
print(test.has_next())
print(test.get_next())
print(test.has_next())
print(test.get_next())
print(test.has_next())
print(test.get_next())
print(test.has_next())
print(test.get_next())
print(test.has_next())