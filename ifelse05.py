email = input("Email manzilingizni kiriting: ")

if "@" in email:
    if email.endswith(".com") or email.endswith(".uz") or email.endswith(".net") or email.endswith(".org"):
        print("Email qabul qilindi.")

if "@" not in email or not (email.endswith(".com") or email.endswith(".uz") or email.endswith(".net") or email.endswith(".org")):
    print("Email noto'g'ri formatda.")

