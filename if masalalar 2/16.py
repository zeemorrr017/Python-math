yosh = int(input("Yoshingizni kriting: "))
jins = input("Jinsingizni kriting: ")

if jins == "ayol":
    if (yosh >= 18):
        print("Ro'mol")
    else:
        print("Qo'g'rchoq")
elif jins == "erkak":
    if (yosh >= 18):
        print("moshina")
    else:
        print("robit oynchoq")