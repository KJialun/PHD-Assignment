from math import sqrt,sin,cos,acos

"""
This class represent a point in 2D space.
Common vector operations are provided.
- Can you explain how it works?
- How would you improve the design?
- Can you implement a method to rotate the vector towards another one?
- Does this class adhere to the SOLID principles?
    - If not, how would you improve upon it? 
"""

class Vector2D:


    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __add__(self,v):
        """
        Explain how this method work
        """
        if type(v) is Vector2D:
            ret = Vector2D(self.x+v.x,self.y+v.y)
        else:
            ret = Vector2D(self.x+v,self.y+v)
        return ret

    def __sub__(self,v):
        if type(v) is Vector2D:
            ret = Vector2D(self.x-v.x,self.y-v.y)
        else:
            ret = Vector2D(self.x-v,self.y-v)
        return ret

    def __mul__(self,v) -> float:
        if type(v) is Vector2D:
            ret = self.x*v.x+self.y*v.y
        else:
            ret = Vector2D(self.x*v,self.y*v)
        return ret

    def mod(self):
        return sqrt(self.x**2 + self.y**2)
    
    def distance(self, v2):
        
        return sqrt((self.x-v2.x)**2 + (self.y-v2.y)**2)

    def norm(self):
        module = self.mod()
        
        return Vector2D(self.x/module, self.y/module)

    def rotate(self, angle):
        #Can you explain this function and why it is implemented this way?
        s = sin(angle)
        c = cos(angle)
        vn = self.norm()
        x = vn.x*c - vn.y*s
        y = vn.x*s + vn.y*c
        
        ret = Vector2D(x,y).norm()*self.mod()
        
        return ret

    def __repr__(self):
        return "(x=%.3f,y=%.3f)" % (self.x, self.y)

