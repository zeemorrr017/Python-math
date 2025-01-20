daromad = int(input("Daromadizni kriting: "))
qarzi = int(input("Qarzizni kriting: "))

if daromad > qarzi:
    print("Kredit olishingiz mumkun")
elif daromad < qarzi:
    print("Siz kredit ololmaysz")
else:
    print("Daromad yoki qarzingizni kriting")