secund = int(input("Secund kriting: "))

soat = (secund // 60) // 60
minut = secund // 60 % 60
secund2 = secund % 60

print(f"{soat} soat _ {minut} minut _ {secund2} secund")