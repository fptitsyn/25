from fnmatch import *
odd = "13579"
even = "02468"
k = 206
for i in range(k, 10**8, k):
    for o in odd:
        for e in even:
            if fnmatch(str(i), f"123*{o}{e}56"):
                print(i, i // k)
