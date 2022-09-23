print((4 + 31 + 1) % 33)
print((4 - 33 + 1) % 33)
print((4 + 33 ** 1) % 33)
for i in range(-30, 3000):
    for j in range(1, 3000):
        if ((i + j + 1) % j) != ((i % j + 1) % j):
            print(i, j)
