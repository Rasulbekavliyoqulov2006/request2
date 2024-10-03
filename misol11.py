fayl = input("fayl nomini kiriting: ")

try:
    with open(fayl, "r") as fayl:
        matn = fayl.read()
        print(matn)
except FileNotFoundError:
    print("fayl topilmadi")