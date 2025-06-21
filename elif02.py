son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input ("Ikkinchi sonni kiriting: "))
amal = input ("Amalni kiriting (+, -, /): ")

if amal== "+":
    print("Natija:", son1 + son2)
elif amal == "-":
    print("Natija:", son1-son2)
elif amal == "/":
    print("Natija:", son1 / son2)
else:
    print("xatolik noto'g'ri amal kiritildi. Faqat +, -, / ruxsat etiladi.")
