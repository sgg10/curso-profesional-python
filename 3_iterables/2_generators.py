from time import time, sleep

def even_numbers(max_numbers=None):
    x = 0
    count = 1
    while True:
        if not max_numbers or count <= max_numbers:
            yield x
            x += 2
            count += 1
        else:
            break

my_generator = (x**2 for x in [0,1,4,7,9,10])

if __name__ == "__main__":
    for i in my_generator:
        print(i)

    for i in even_numbers():
        print(i)
        sleep(0.5)