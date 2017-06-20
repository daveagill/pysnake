import math
import random

class Vector2(object):
    EQUALITY_THRESHOLD = 0.0001 # currently chosen arbitrarily
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, val):
        return Vector2(self.x * val, self.y * val)
    
    def __div__(self, val):
        return self.__mul__(1/val)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
    
    def __imul__(self, val):
        self.x *= val
        self.y *= val
    
    def __idiv__(self, val):
        return self.__imul__(1/val)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __eq__(self, other):
        return abs(self.x - other.x) <= Vector2.EQUALITY_THRESHOLD and \
               abs(self.y - other.y) <= Vector2.EQUALITY_THRESHOLD

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __getitem__(self, key):    
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        raise IndexError("Vector2 index out of range")
    
    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        if key == 1:
            self.y = value
        raise IndexError("Vector2 index out of range")
    
    def __str__(self):
        return "[%.1f, %.1f]" % (self.x, self.y)

def isVector2(vec):
    return hasattr(vec, '__class__') and vec.__class__ is Vector2

def zero():
    return Vector2(0, 0)

def randomRange(startX, endX, startY, endY):
    return Vector2(random.randrange(startX, endX), random.randrange(startY, endY))
    
def dot(a, b):
    return (a.x * b.x) + (a.y * b.y)

def lengthSquared(vec):
    return dot(vec, vec)

def length(vec):
    return sqrt(lengthSquared(vec))

def normalise(vec):
    vec /= length(vec)
    return vec

def normalised(vec):
    return normalise(Vector2(vec.x, vec.y))