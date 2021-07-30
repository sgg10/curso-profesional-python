from typing import List

def is_prime(n: int) -> bool:
  return False if n < 2 else len([i for i in range(2, n) if n % i == 0]) == 0

def run():
  n_list: List[int] = [i for i in range(10)]
  for n in n_list:
    print(f"Is {n} a prime number? {is_prime(n)}")
  is_prime("Pepe")

if __name__ == '__main__':
  # mypy 1_static_typing/prime.py --check-untyped-defs
  run()