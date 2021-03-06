from time import sleep

class FiboIter:

    def __init__(self, max_iter = None):
        self.max_iter = max_iter

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max_iter or self.counter <= self.max_iter:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                aux = self. n1 + self.n2
                self.n1, self.n2 = self.n2, aux
                self.counter += 1
                return aux
        else:
            raise StopIteration

if __name__ == "__main__":
    fibonacci = FiboIter(15)
    for element in fibonacci:
        print(element)
        sleep(0.5)