import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True

def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate


def main():
    num_bits = 100
    p = generate_prime(num_bits)
    q = generate_prime(num_bits)
    while p == q:
        q = generate_prime(num_bits)
    fo = open('prime.txt','w')
    fo.write(str(p)+'\n')
    fo.write(str(q))

main()