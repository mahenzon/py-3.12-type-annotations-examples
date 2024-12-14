from typing import reveal_type


class Storage[T]:
    def __init__(self, value: T) -> None:
        self.value = value


class SuperStorage[T](Storage[T]):
    def multiply_data(self, times: int) -> list[T]:
        return [self.value] * times


def main() -> None:
    foo_storage = Storage[str]("foo")
    reveal_type(foo_storage)

    spam_super_storage = SuperStorage[str]("spam")
    reveal_type(spam_super_storage)
    spams = spam_super_storage.multiply_data(2)
    print(spams)

    nums_super_storage = SuperStorage(7)
    reveal_type(nums_super_storage)
    nums = nums_super_storage.multiply_data(3)
    print(nums)


if __name__ == "__main__":
    main()
