from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        time_elapsed = datetime.now() - initial_time
        print(f"{time_elapsed.total_seconds()}s")

    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def sub(a: int, b: int) -> int:
    return a - b


random_func()
sub(5, 4)
