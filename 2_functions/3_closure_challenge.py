from typing import Callable, Union


def make_division_by(n: Union[int, float]) -> Callable:
    assert n != 0, "You cannot divide by zero."

    def division(x: Union[int, float]) -> Union[int, float]:
        return x / n

    return division


def main():
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)

    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))


if __name__ == "__main__":
    main()
