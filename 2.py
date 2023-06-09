# Пусть N(k) = 750 000 + k, где k – натуральное число. Найдите пять наименьших значений k,
# при которых N(k) имеет нечётное количество различных чётных делителей. В ответе запишите найденные значения k в порядке возрастания,
# справа от каждого значения запишите число чётных делителей N(k).
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


c = 0
for k in range(1, 10000000):
    x = 750_000 + k
    for n in range(2, 151, 2):
        p = (x / 2) ** (1 / n)
        if int(p) == p and is_prime(p):
            c += 1
            print(k, n + 1)
    if c == 5:
        break
