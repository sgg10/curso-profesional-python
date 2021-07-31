from time import sleep

def fibo_gen(max_iteration: int = None):
    a, b = 0, 1
    counter = 0
    while not max_iteration or counter <= max_iteration:
        yield a
        a, b = b, a+b
        counter += 1

if __name__ == "__main__":
    for i in fibo_gen():
        print(i)
        sleep(0.5)