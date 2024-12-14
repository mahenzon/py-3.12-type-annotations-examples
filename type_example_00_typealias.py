from typing import Sequence
from typing import reveal_type
from typing import TypeAlias


# host, port
Connection: TypeAlias = tuple[str, int]

# list of hosts+ports
Connections: TypeAlias = list[Connection]


LinesAlias: TypeAlias = Sequence[str]
type Lines = Sequence[str]
reveal_type(LinesAlias)
reveal_type(Lines)

print("LinesAlias:", LinesAlias)
print("Lines:", Lines)

print("LinesAlias == Sequence[str]:", LinesAlias == Sequence[str])
print("Lines == Sequence[str]:", Lines == Sequence[str])
print("Lines == LinesAlias:", Lines == LinesAlias)

print()
print()
number: TypeAlias = float | int
print(number)
reveal_type(number)

print("isinstance(42, number):", isinstance(42, number))
print("isinstance(3.1415, number):", isinstance(3.1415, number))
print("isinstance(False, number):", isinstance(False, number))
print('isinstance("Suren", number):', isinstance("Suren", number))


def make_titles(strings: Lines) -> Lines:
    return [s.title() for s in strings]


def main() -> None:
    names = [
        "john",
        "SAM",
        "nIcK",
    ]
    for name in make_titles(names):
        print(name)


if __name__ == "__main__":
    main()
