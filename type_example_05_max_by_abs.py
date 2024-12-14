from typing import SupportsAbs


def find_max_by_abs[T: SupportsAbs[float]](*values: T) -> T:
    return max(values, key=abs)


def main() -> None:
    max_num = find_max_by_abs(-5, 1, 2, 3, -4)
    print(max_num)


if __name__ == "__main__":
    main()
