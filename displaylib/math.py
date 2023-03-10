from __future__ import annotations

from math import sqrt


__all__ = ["Vec2"]


class Vec2:
    """Vector2 data structure

    Components: `x`, `y`

    Usefull for storing position or direction
    """
    def __init__(self, x: int | float = 0, y: int | float = 0) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vec2({self.x}, {self.y})"
    
    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vec2 | int | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vec2(self.x * other, self.y * other)
    
    def __floordiv__(self, other: Vec2 | int | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        elif isinstance(other, (int, float)):
            return Vec2(self.x // other, self.y // other)
    
    def __truediv__(self, other: Vec2 | int | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return Vec2(self.x / other, self.y / other)
    
    def __mod__(self, other: int | float) -> Vec2:
        return Vec2(self.x % other, self.y % other)
    
    def __eq__(self, other: Vec2) -> bool:
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self, other: Vec2) -> bool:
        return (self.x != other.x) or (self.y != other.y)
    
    def __gt__(self, other: Vec2) -> bool:
        return self.x > other.x and self.y > other.y
    
    def __lt__(self, other: Vec2) -> bool:
        return self.x < other.x and self.y < other.y
    
    def __ge__(self, other: Vec2) -> bool:
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other: Vec2) -> bool:
        return self.x <= other.x and self.y <= other.y

    def length(self) -> float:
        if self.x == 0 and self.y == 0:
            return 0.0
        return sqrt(self.x*self.x + self.y*self.y)
    
    def normalized(self) -> Vec2:
        length = self.length()
        if length == 0:
            return Vec2(0, 0)
        return self / self.length()
