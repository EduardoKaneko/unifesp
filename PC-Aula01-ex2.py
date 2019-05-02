# Soma de todas as frações 1/2 + 2/3
S = 0
i = 2
for n in range(1, 1000001):
    S += (n/i)
    i += 1
print(S)
