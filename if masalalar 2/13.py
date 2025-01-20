baho1 = int(input("Baho kriting: "))
baho2 = int(input("Baho kriting: "))
baho3 = int(input("Baho kriting: "))

umumiy =  ((baho1 + baho2 + baho3) /3)

if umumiy >= 5:
    print("Yaxshi", umumiy)
elif umumiy >= 4:
    print("Ortacha", umumiy)
elif umumiy >= 3:
    print("Yomon", umumiy)
else:
    print("Faqat 3,4,5 kriting")
