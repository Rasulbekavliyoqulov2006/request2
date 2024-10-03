import json

malumot = {
    "ism": input("ismingizni kiriting: "),
    "familiya": input("familiyangizni kiriting: "),
    "yosh": int(input("yoshingizni kiriting: ")),
    "tug'ilgan_yil":input("tugilgan yilingizni kiriting(Yil:oy:kun): "),
    "telefon raqam": int(input("telefon raqamingizni kiriting: " ))
    }

with open("misol7.json", "w") as fayl:
    json.dump(malumot, fayl, indent=4) 