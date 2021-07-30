from typing import List

def is_palindrome(string: str) -> bool:
  string = string.replace(" ", "").lower()
  return string == string[::-1]

def run():
  words: List[str]  = ["Oso", "Hannah", "Sebastian", 1000]
  for word in words:
    print(f"Is {word} a palindrome? {is_palindrome(word)}")
  is_palindrome(1000000)

if __name__ == "__main__":
  # mypy 1_static_typing/palindrome.py --check-untyped-defs
  run()