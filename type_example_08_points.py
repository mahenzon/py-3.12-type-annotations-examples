class Point[T]:
    def __init__(self, x: T, y: T) -> None:
        self.x = x
        self.y = y

    def equals(self, other: "Point[T]") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x!r}, {self.y!r})"


def main() -> None:
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    print(point1)
    print(point2)
    point_foobar = Point("foo", "bar")
    print(point_foobar)
    point3 = Point(1, 4)
    print(point3)
    print("point1.equals(point3):", point1.equals(point3))
    point3.y = 2
    print(point3)
    print("point1.equals(point3):", point1.equals(point3))
    # print(point3.equals(point_foobar))


if __name__ == "__main__":
    main()
