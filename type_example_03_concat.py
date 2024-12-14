# from typing import TypeVar
#
# T = TypeVar('T', str, bytes)

def concatenate[T: (str, bytes)](left: T, right: T) -> T:
    return left + right


def main() -> None:
    foobar = concatenate("foo", "bar")
    print(foobar)
    spam_eggs = concatenate(b"spam", b"eggs")
    print(spam_eggs)


if __name__ == "__main__":
    main()
