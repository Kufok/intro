import sys
import random

def generate_numbers(dices):
    throw = []
    for _ in range(dices):
        throw.append(random.randint(1,6))

    return throw


def count_result(throw):
    pass

def main():
    origin_throw = generate_numbers(6)
    print("Hodil jsi:", origin_throw)

if __name__ == "__main__":
    sys.exit(main())
