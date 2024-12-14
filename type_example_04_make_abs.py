from typing import MutableSequence


def make_abs[T: MutableSequence[int]](numbers: T) -> T:
    for idx, num in enumerate(numbers):
        numbers[idx] = abs(num)

    return numbers


def main() -> None:
    nn_numbers = make_abs([1, 2, -3, -4])
    print(nn_numbers)
    numbers = [1, 2, -3]
    print(numbers)
    make_abs(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
