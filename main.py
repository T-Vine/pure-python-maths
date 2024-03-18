def pi() -> float:
    res: list[float] = []
    for i in range(0,10000000):
        new_res = (-1)**i
        new_res /= (2*i + 1)
        res.append(new_res)
    return sum(res)*4
PI: float = pi()
def sine(theta: float) -> float:
    results: list[float] = []
    r: float = 0.0
    for i in range(0, 50):
        r = (-1)**i
        r /= factorial((2*i)+1)
        r *= theta**((2*i)+1)
        results.append(r)
    return sum(results)


def cosine(theta: float) -> float:
    if theta < 90:
        return sine(to_radians(90)-theta) # Graphs are the same but skewed.
    return sine(theta-to_radians(90))

def tangent(theta: float) -> float:
    return sine(theta)/cosine(theta)

def arcsine(x: float) -> float:
    if abs(x) > 1:
        return None
    return arctan(x/root(1-(x**2)))

def arctan(x: float) -> int:
    results: list[float] = []
    r: float = 0.0
    if abs(x) > 1:
        return None
    for i in range(0,50):
        r = (-1)**i
        r /= ((2*i)+1)
        r *= x**((2*i)+1)
        results.append(r)
    return sum(results)
    
def arccos(x: float) -> int:
    if abs(x) > 1:
        return None
    if arcsine(x) < 90:
        return 90-arcsine(x)
    return arcsine(x)-90

def root(x: float) -> float:
    rand = 50 # A random starting point.
    res: float = 0
    for i in range(10):
        res = 0.5*(rand+(x/rand))
        rand = res
    return res
    
def factorial(x: int) -> int:
    f_res: int = x
    while x > 1:
        x -= 1
        f_res *= x
    return f_res

def to_radians(degrees: float) -> float:
    return degrees*PI/180

def to_degrees(radians: float) -> float:
    return radians*(180/PI)

if __name__ == "__main__":
    print(root(11301))
    print(sine(to_radians(17))) # Accepts radians.
    print(cosine(to_radians(0)))
    print(tangent(to_radians(45)))

