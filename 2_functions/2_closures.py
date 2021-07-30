from typing import Callable, Union


def make_multiplier(x: Union[float, int]) -> Callable:

    def multiplier(n: Union[float, int]) -> Union[float, int]:
        return x * n

    return multiplier


def make_repeater_of(n: int) -> Callable:
    def repeater(string: str) -> str:
        assert type(string) == str, "Only strings"
        return string * n
    return repeater

def run():
    t_10 = make_multiplier(10)
    t_4 = make_multiplier(4)

    print(t_10(3))
    print(t_10(5))
    print(t_10(t_4(2)))
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))

if __name__ == "__main__":
    run()