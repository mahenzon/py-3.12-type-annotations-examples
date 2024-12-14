def repeat[T](val: T, times: int) -> list[T]:
    return [val] * times


def main() -> None:
    nums = repeat(5, 4)
    print(nums)
    words = repeat("word", 3)
    print(words)
    pairs = repeat((4, 2), 2)
    print(pairs)
    pairs2 = repeat((4, "fours"), 2)
    print(pairs2)


if __name__ == "__main__":
    main()
