class Pair[K, V]:
    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value

    def get_key(self) -> K:
        return self.key

    def get_value(self) -> V:
        return self.value


def main() -> None:
    pair_one = Pair[str, int]("one", 1)
    key_one = pair_one.get_key()
    value_one = pair_one.get_value()
    print(key_one, ":", value_one)

    pair_two = Pair(2, "two")
    key_two = pair_two.get_key()
    value_two = pair_two.get_value()
    print(key_two, ":", value_two)

    pair_three = Pair("foo", "bar")
    key_three = pair_three.get_key()
    value_three = pair_three.get_value()
    print(key_three, ":", value_three)


if __name__ == "__main__":
    main()
