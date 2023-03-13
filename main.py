def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for x in range(113_000_000, 114_000_000 + 1):
    p = (x / 2) ** 0.5
    if int(p) == p and is_prime(p):
        print(x, int(2 * p))
