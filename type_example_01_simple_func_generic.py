from random import choice
from typing import Sequence

# from typing import TypeVar
#
# T = TypeVar("T")
#


def get_random_elem[T](items: Sequence[T]) -> T:
    return choice(items)


def main() -> None:
    num = get_random_elem([1, 3, 5])
    print(num)
    name = get_random_elem(["John", "Sam", "Nick"])
    print(name)


if __name__ == "__main__":
    main()
