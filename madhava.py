PI = 22/7

def sine(theta):
    results = []
    r = 0.0
    for i in range(0, 50):
        r = (-1)**i
        r /= factorial((2*i)+1)
        r *= theta**((2*i)+1)
        results.append(r)
    return sum(results)


def cosine(theta):
    if theta < 90:
        return sine(theta+toRadians(90)) # Graphs are the same but skewed.
    return sine(theta-toRadians(90))

def tangent(theta):
    return sine(theta)/cosine(theta)

def arcsine(x):
    if not 0<abs(x)<1:
        return None
    if x < 0:
        return arctan(x/math.sqrt(1-(x**2)))
    return arctan(x/root(1-(x**2)))

def arctan(x):
    results = []
    r = 0.0
    if abs(x) > 1:
        return None
    for i in range(0,50):
        r = (-1)**i
        r /= ((2*i)+1)
        r *= x**((2*i)+1)
        results.append(r)
    return sum(results)

def root(x):
    rand = 50 # A random starting point.
    res = 0
    for i in range(10):
        res = 0.5*(rand+(x/rand))
        rand = res
    return res
    
def factorial(x):
    fRes = x
    while x > 1:
        x -= 1
        fRes *= x
    return fRes

def toRadians(degrees):
    return degrees*PI/180

def toDegrees(radians):
    return radians*(180/PI)

x = 0.524
#print(root(11301))
print(sine(toRadians(17))) # Accepts radians.
#print(cosine(toRadians(0)))
#print(tangent(toRadians(45)))
