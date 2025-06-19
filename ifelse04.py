balans = 5000
summa = int(input("Yechmoqchi bo'lgan summani kiriting: "))

if summa < 0:
    print("Manfiy summa kiritib bo'lmaydi.")

if summa <= balans and summa >= 0:
    qolgan = balans - summa
    print(f"Pul yechildi. Qolgan balans: {qolgan} so'm")

if summa > balans:
    print(f"Mablag' yetarli emas. Sizning balansingiz: {balans} so'm")

