parol = input("Parol kiriting: ")

uzunlik_togri = False
harf_bor = False
raqam_bor = False

if len(parol) >= 8:
    uzunlik_togri = True

for belgi in parol:
    if ('A' <= belgi <= 'Z') or ('a' <= belgi <= 'z'):
        harf_bor = True
    if '0' <= belgi <= '9':
        raqam_bor = True

if uzunlik_togri and harf_bor and raqam_bor:
    print("Parol qabul qilindi.")
if not (uzunlik_togri and harf_bor and raqam_bor):
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")


