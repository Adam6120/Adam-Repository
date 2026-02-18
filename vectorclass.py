"""
   Vector Class containing some standard vector operations
"""

class Vector:
    
    
    def __init__(self, x, y, z):      #init creates a new vector
        self.x = x                    #x,y,z are vector parameters
        self.y = y                    #self.x=x stores x value, self is the object name like comm.world
        self.z = z
        
    def __str__(self):
        """
        Assumes floating point when printing
        """
        return f"Vector: ({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    
    
                                      #self is v1, other is v2
                                      #returns a new vector post summation
    def __add__(self, other):         #add is for v1 + v2
        """                           
        Add two vectors
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    
    def __sub__(self, other):
        """
        Subtract two vectors
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def magnitude(self):
        """
        Calculate the magnitude of the vector
        """
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def dot(self, other):
        """
        Calculate the dot product with another vector
        """
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    
    def cross(self, other):
        """
        Calculate the cross product with another vector
        """
        crossx = (self.y * other.z - self.z * other.y)
        crossy = (self.z * other.x - self.x * other.z)
        crossz = (self.x * other.y - self.y * other.x)
        return Vector(crossx, crossy, crossz)
       
class ComplexVector(Vector): # Child class inheritance from Vector class
    """
    ComplexVector class inheriting from Vector class which handles
    complex-valued vectors required for EM field calculations
    """
    #Redefining operations with complex number i
    def __str__(self): #
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    
    #:4f where 4 is the number of decimal places
    
    def __add__(self, other):
        return ComplexVector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return ComplexVector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def magnitude(self):
        """
        New magnitude for complex numbers, using complex conjugate
        |z|^2 = z* x z
        """
        return (self.x.conjugate() * self.x + self.y.conjugate() * self.y + self.z.conjugate() * self.z)
         
    def dot(self, other):
        """
        New dot product for complex numbers, using a* dot b
        """
        return (self.x.conjugate() * other.x + self.y.conjugate() * other.y + self.z.conjugate() * other.z)
    
    def cross(self, other):
        """
        Calculate the cross product with complex vectors, unchanged formula
        """
        crossx = (self.y * other.z - self.z * other.y)
        crossy = (self.z * other.x - self.x * other.z)
        crossz = (self.x * other.y - self.y * other.x)
        return ComplexVector(crossx, crossy, crossz)
    
    def __mul__(self, scalar):
        """
        Defining multiplication and division due to issues with unsupported
        operand types with complex vectors
        """
        #Python will pass any integer and define it as scalar.
        return ComplexVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar):
        """
        Division in python 3 is _truediv_
        """
        return ComplexVector(self.x / scalar, self.y / scalar, self.z / scalar)
