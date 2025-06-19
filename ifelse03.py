import os

fayl = input("Fayl nomini kiriting: ")

if os.path.exists(fayl):
    print(f"Fayl '{fayl}' mavjud.")

if not os.path.exists(fayl):
    print(f"Fayl '{fayl}' topilmadi.")

