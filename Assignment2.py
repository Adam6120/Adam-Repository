import math
import cmath #Module that handles complex numbers
from vectorclass import Vector, ComplexVector


# Area of a Triangle: 1/2 * b * H

# Triangle 1
A = Vector(0,0,0)
B = Vector(1,0,0)
C = Vector(0,1,0)

# Triangle 2
D = Vector(-1,-1,-1)
E = Vector(0,-1,-1)
F = Vector(-1,0,-1)

#Triangle 3
G = Vector(1,0,0)
H = Vector(0,0,1)
I = Vector(0,0,0)

#Triangle 4
J = Vector(0,0,0)
K = Vector(1,-1,0)
L = Vector(0,0,1)

#Function for calculating the area of the triangle, using parallelogram method
#Steps: Find 2 sides, AB and AC (defined by variable edge)
#       1/2 * |AB x AC|
def triangle_area(vertix1, vertix2, vertix3):
    side1 = vertix2 - vertix1
    side2 = vertix3 - vertix1
    cross = side1.cross(side2)
    return 0.5 * cross.magnitude()

#Using the area function for all triangles
area1 = triangle_area(A, B, C)
area2 = triangle_area(D, E, F)
area3 = triangle_area(G, H, I)
area4 = triangle_area(J, K, L)


#Function for finding angles at each of the three vertices of each triangle
#vertix 1 = A
#vertix 2 = B
#vertix 3 = C
def triangle_angles(vertix1, vertix2, vertix3):
    
    #Calculating magnitudes of triangle sides
    edge1a = vertix2 - vertix1
    edge1b = vertix3 - vertix1
    
    edge2a = vertix1 - vertix2
    edge2b = vertix3 - vertix2
    
    edge3a = vertix1 - vertix3
    edge3b = vertix2 - vertix3
    
    #Angle at vertix 1 = A
    #Using math.degrees to force from radians to degrees
    angle1 = math.degrees(math.acos(edge1a.dot(edge1b) / (edge1a.magnitude() * edge1b.magnitude())))
    angle2 = math.degrees(math.acos(edge2a.dot(edge2b) / (edge2a.magnitude() * edge2b.magnitude())))
    angle3 = math.degrees(math.acos(edge3a.dot(edge3b) / (edge3a.magnitude() * edge3b.magnitude())))
    
    return angle1, angle2, angle3

#Calling angles for each triangle, [0,1,2] calls angle1, 2 and 3 respectively
anglesABC = triangle_angles(A, B, C)
anglesDEF = triangle_angles(D, E, F)
anglesGHI = triangle_angles(G, H, I)
anglesJKL = triangle_angles(J, K, L)

#Placing all task 2 values in a table for easier viewing
print("===========================================================")
print("TRIANGLE RESULTS")
print("===========================================================")
print(f"{'Triangle':<12} {'Area':<10} {'Angle 1':<10} {'Angle 2':<10} {'Angle 3':<10} {'Sum':<10}")
print("===========================================================")

# Triangle 1
print(f"{'Triangle 1':<12} {area1:<10.4f} {anglesABC[0]:<10.2f} {anglesABC[1]:<10.2f} {anglesABC[2]:<10.2f} {sum(anglesABC):<10.2f}")

# Triangle 2
print(f"{'Triangle 2':<12} {area2:<10.4f} {anglesDEF[0]:<10.2f} {anglesDEF[1]:<10.2f} {anglesDEF[2]:<10.2f} {sum(anglesDEF):<10.2f}")

# Triangle 3
print(f"{'Triangle 3':<12} {area3:<10.4f} {anglesGHI[0]:<10.2f} {anglesGHI[1]:<10.2f} {anglesGHI[2]:<10.2f} {sum(anglesGHI):<10.2f}")

# Triangle 4
print(f"{'Triangle 4':<12} {area4:<10.4f} {anglesJKL[0]:<10.2f} {anglesJKL[1]:<10.2f} {anglesJKL[2]:<10.2f} {sum(anglesJKL):<10.2f}")

print("===========================================================")

k = ComplexVector(0,0, math.pi)
kmag = k.magnitude()
#print("k:",k)
#print("|k|:",kmag)

#Defining Hansen Vectors
def m_function(x,y,z):
    """
    Hansen Vector M = [1,0,0] * exp(i*k dot x)
    """
    position_x = ComplexVector(x, y, z)
    kdotx = k.dot(position_x)
    exponential = cmath.exp(1j * kdotx)
    return ComplexVector(exponential, 0, 0)

def n_function(x,y,z):
    """
    Hansen Vector N = [0,1,0] * exp(i*k dot x)
    """
    position_x = ComplexVector(x, y, z)
    kdotx = k.dot(position_x)
    exponential = cmath.exp(1j * kdotx)
    return ComplexVector(0, exponential, 0)


#Defining Partial Derivatives for Divergence and Curl
#Finite difference requires us to define an increment H to compare the function by
#0.1 as a placeholder, not sure which increment to pick
H = 0.001

def partialx(v, x, y, z):
    """
    Partial derivative functions for differentating a vector v with respect to x, y and z respectively
    """
    return (v(x+H, y, z) - v(x-H, y, z)) * (1/(2*H))    #Need to call y and z to keep them fixed because we're in 3D.
            
def partialy(v, x, y, z):
    return (v(x, y+H, z) - v(x, y-H, z)) * (1/(2*H))

def partialz(v, x, y, z):
    return (v(x, y, z+H) - v(x, y, z-H)) * (1/(2*H)) 

#Divergence (del dot v)
def divergence(v, x, y, z):
    del_v_dx = partialx(v, x, y, z)
    del_v_dy = partialy(v, x, y, z)
    del_v_dz = partialz(v, x ,y, z)
    return del_v_dx.x + del_v_dy.y + del_v_dz.z

#Curl (del cross v)
def curl(v, x, y, z):
    del_v_dx = partialx(v, x, y, z)
    del_v_dy = partialy(v, x, y, z)
    del_v_dz = partialz(v, x ,y, z)
    
    curl_x = del_v_dy.z - del_v_dz.y
    curl_y = del_v_dz.x - del_v_dx.z
    curl_z = del_v_dx.y - del_v_dy.x
    
    return ComplexVector(curl_x, curl_y, curl_z)

print("Testing Hansen Vector Properties:")
points = [(0, 0, 0), (1, 0, 0), (10,10,10), (29, 56, 450)] #List of points for sweeping through equations


for point in points: #Function for testing Hansen Vectors
    x, y, z = point
    print(f"Point: ({x}, {y}, {z})")
    M = m_function(x, y, z)
    N = n_function(x, y, z)
    
    divM = divergence(m_function, x, y, z)
    print(f"∇·M = {divM.real:}", "Expected: 0.0") #.real gets rid of the imaginary part to look cleaner
    
    divN = divergence(n_function, x, y, z)
    print(f"∇·N = {divN.real:}","Expected: 0.0") #.real gets rid of the imaginary part to look cleaner
    
    curlM = curl(m_function, x, y, z)
    expectationM = N / kmag
    print(f"∇×M = {curlM}", f"Expected: {expectationM}")
    
    curlN = curl(n_function, x, y, z)
    expectationN = M / kmag
    print(f"∇×N = {curlN}", f"Expected: {expectationN}")
    
    print("===========================================================")
    print(f"Beginning Final Verification Steps For Each Point: ({x}, {y}, {z})")
    #Checking if properties are satisfied
    #Using the 'math.isclose() tool to compare answers.
    #Why not simply equate our answers? All values are floating point and won't be exactly equal
    #parameter abs_tol must be defined for values close to zero
    
    #Divergence Satisfaction
    if divM.real == 0:
        print("∇·M = 0 ✔")
    else:
        print("∇·M ≠ 0 𝐗")
        
    if divN.real == 0:
        print("∇·N = 0 ✔")
    else:
        print("∇·N ≠ 0 𝐗")
        
    #Curl Satisfcation
    if curlM == expectationM:
        print("∇×M = N/|k| ✔")
    else:
        print("∇×M ≠ N/|k| 𝐗")

    if curlN == expectationN:
        print("∇×N = M/|k| ✔")
    else:
        print("∇×N ≠ M/|k| 𝐗")

print("Verification Complete.")
