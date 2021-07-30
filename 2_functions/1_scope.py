# Local Scope

# def my_func() -> None:
#     y: int = 5
#     print(y)


# Global Scope

# y: int = 5


# def my_function() -> None:
#     print(y)


# def my_another_functions() -> None:
#     print(y)


# my_function()
# my_another_functions()

y: int = 5


def my_function() -> None:
    y: int = 3

    def my_another_functions() -> None:
        y: int = 2
        print(y)

    my_another_functions()

    print(y)


my_function()

print(y)
