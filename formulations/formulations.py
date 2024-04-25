import math

class Basic:
    def Exponent(Base, Exponent):
        return Base**Exponent
    def Round(num):
        if (num - int(num) >= 0.5):
            return int(num) + 1
        else:
            return int(num)
    def Is_Whole(num):
        if num >= 0 and int(num) == num:
            return True
        else:
            return False
    def Is_Integer(num):
        if int(num) == num:
            return True
        else:
            return False
    def Is_Float(num):
        if not int(num) == num:
            return True
        else:
            return False

class Science:
    def MC2(Mass):
        return Mass * 299792458 ** 2

class Algebra:
    def abs(num):
        return math.sqrt(num**2)
    def Growth(Initial, Rate, Time):
        return Initial * (1 + Rate)**Time
    def Slope(y1, y2, x1, x2):
        return (y1-y2)/(x1-x2)
    def Slope_Intercept_Form(m, x, b):
        return m*x+b
    def PeiceWise(TrueReturn, If, FalseReturn = None):
        if If:
            return TrueReturn
        else:
            return FalseReturn
    def Floor(Num):
        return int(Num)
    def Ceiling (Num):
        if int(Num) == Num:
            return Num
        return int(Num + 1)

class Geometry:
    def Square(Length):
        return Length**2
    def Rectangle(Length, Width):
        return Length * Width
    def Parallelogram(Length, Width):
        return Geometry.Rectangle(Length, Width)
    def Triangle(Length, Height):
        return (Length * Height) / 2 
    def Trapezoid(BaseA, BaseB, Height):
        return ((BaseA + BaseB) / 2) * Height
    def Distance2D(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    def Distance3D (x1, y1, z1, x2, y2, z2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    def Pathatgeryon(ASide, BSide):
        return math.sqrt(ASide**2 + BSide**2)
    def Cube(Length):
        return Length**3
    def RectangularPrism(Length, Width, Height):
        return Length * Width * Height
    def Circle(Radius):
        return math.pi * Radius**2
    def Circumference(Radius):
        return 2 * math.pi * Radius
    def Ellipse(A, B):  
        return math.pi * A * B
    def Cylinder(Radius, Height):
        return (math.pi * Radius**2)*Height
    def Sphere(Radius):
        return (4/3) * math.pi * Radius**3
    def Pyramid(Length, Width, Height):
        return (Length * Width * Height) / 3
    def Cone(Radius, Height):
        return math.pi * Radius * (Radius + math.sqrt(Height**2 + Radius**2))
    def Rhombus(Length, Height):
        return Geometry.Triangle(Length, Height)
    def TriangularPrism(BaseA, BaseB, BaseC, Height):
        if((BaseA + BaseB) > BaseC) & ((BaseA + BaseC) > BaseB) & ((BaseB + BaseC) > BaseA):
            return 0.25 * Height * math.sqrt(-BaseA**4 + 2 * (BaseA * BaseB)**2 + 2 * (BaseA * BaseC)**2 - BaseB**4 + 2 * (BaseB * BaseC)**2 - BaseC**4)
        else:
            if not((BaseA + BaseB) > BaseC):
                raise Exception("Make Sure (BaseA + BaseB) > BaseC")
            elif not((BaseA + BaseC) > BaseB):
                raise Exception("Make Sure (BaseA + BaseC) > BaseB")
            elif not((BaseB + BaseC) > BaseA):
                raise Exception("Make Sure (BaseB + BaseC) > BaseA")
            else:
                raise Exception("Unknow Error Occured")
    def TriangularPrismSimple(Length, Width, Height):
        return Geometry.Triangle(Length, Width) * Height