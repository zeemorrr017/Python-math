son = int(input("Son kriting: "))

brinchi = son // 100
ikkinchi = (son // 10) % 10
uchinchi = son % 10

opshiy = brinchi + ikkinchi + uchinchi

print(f"{brinchi} + {ikkinchi} + {uchinchi} = {opshiy}")