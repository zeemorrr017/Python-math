col = int(input('Balandlik: '))
row = int(input('Uzunlik: '))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if (j + i) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()