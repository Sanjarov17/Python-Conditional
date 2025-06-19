narx = 100
yosh = int(input("Yoshingizni kiriting: "))
yakuniy_narx = narx

if yosh < 7:
    yakuniy_narx = narx * 0.5
    print(f"Yakuniy narx: {int(yakuniy_narx)} so'm (50% chegirma qo'llanildi)")

if yosh >= 7 and yosh <= 17:
    yakuniy_narx = narx * 0.8
    print(f"Yakuniy narx: {int(yakuniy_narx)} so'm (20% chegirma qo'llanildi)")

if yosh > 60:
    yakuniy_narx = narx * 0.7
    print(f"Yakuniy narx: {int(yakuniy_narx)} so'm (30% chegirma qo'llanildi)")

if yosh >= 18 and yosh <= 60:
    print(f"Yakuniy narx: {int(yakuniy_narx)} so'm (chegirma qo'llanilmadi)")

