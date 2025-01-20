son = int(input("Son kriting: "))

brinchi = son // 100
ikkinchi = (son % 100) // 10
uchinchi = son % 10 

son2 = uchinchi * 100 + ikkinchi * 10 + brinchi

print(son2)
