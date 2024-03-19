def pi() -> float:
    """Returns approximations of Pi. 
    Increased iterations increases accuracy."""
    res: list[float] = []
    for i in range(0,10000000):
        new_res = (-1)**i
        new_res /= (2*i + 1)
        res.append(new_res)
    return sum(res)*4

PI: float = pi()

def sine(theta: float) -> float:
    """Returns approximations of sine.

    Keyword arguments:
    theta -- the angle
    """
    results: list[float] = []
    r: float = 0.0
    for i in range(0, 50):
        r = (-1)**i
        r /= factorial((2*i)+1)
        r *= theta**((2*i)+1)
        results.append(r)
    return sum(results)

def cosine(theta: float) -> float:
    """Returns approximations of cosine.
    
    Keyword arguments:
    theta -- the angle
    """
    if theta < 90:
        return sine(to_radians(90)-theta)
    return sine(theta-to_radians(90))

def tangent(theta: float) -> float:
    """Returns approximations of tangent.
    
    Keyword arguments:
    theta -- the angle
    """
    return sine(theta)/cosine(theta)

def arcsine(x: float) -> float:
    """Returns approximations of arcsine, in radians.
    
    Keyword arguments:
    x -- input 'y-value' between -1 and 1.
    """
    if abs(x) > 1:
        return None
    if 1-(x**2) == 0:
        return to_radians(90)
    return arctan(x/root(1-(x**2)))

def arctan(x: float) -> int:
    """Returns approximations of arctan, in radians.
    
    Keyword arguments:
    x -- input 'y-value' between -1 and 1.
    """
    results: list[float] = []
    r: float = 0.0
    if abs(x) > 1:
        return (PI/2 - arctan(1/x))
    for i in range(0,50):
        r = (-1)**i
        r /= ((2*i)+1)
        r *= x**((2*i)+1)
        results.append(r)
    return sum(results)
    
def arccos(x: float) -> int:
    """Returns approximations of arccosine, in radians.
    
    Keyword arguments:
    x -- input 'y-value' between -1 and 1.
    """
    if abs(x) > 1:
        return None
    if arcsine(x) < 90:
        return 90-arcsine(x)
    return arcsine(x)-90

def root(x: float) -> float:
    """Returns an approximated square root.
    
    Keyword arguments:
    x -- input value to be square-rooted.
    """
    rand = 50
    res: float = 0
    for i in range(10):
        res = 0.5*(rand+(x/rand))
        rand = res
    return res
    
def factorial(x: int) -> int:
    """Returns the factorial of a value."""
    f_res: int = x
    while x > 1:
        x -= 1
        f_res *= x
    return f_res

def to_radians(degrees: float) -> float:
    """Returns the radians of a degree value."""
    return degrees*PI/180

def to_degrees(radians: float) -> float:
    """Returns degrees of a radian value."""
    return radians*(180/PI)

if __name__ == "__main__":
    # Testing. To be moved to a proper file later.
    print(sine(to_radians(30)))
    print(sine(to_radians(0)))
    print(sine(to_radians(90)))

    print(cosine(to_radians(60)))
    print(cosine(to_radians(0)))
    print(cosine(to_radians(90)))

    print(tangent(to_radians(45)))

    print(to_degrees(arcsine(0.5))) # 30
    print(to_degrees(arcsine(1))) # 90
    
    #print(to_degrees(arccos(0.5))) # 60
    #print(to_degrees(arccos(0))) # 90
    