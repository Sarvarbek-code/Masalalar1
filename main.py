# xavf_darajasi = int(input("Xavf darajasni kiriting: (0-100)"))
# harakat_sensori = input("uyda harakat aniqlanganmi (ha/yoq): ")
# eshik_sensori =  input("eshik ochilganmi (ha/yoq): ")
# vaqt = float(input("Vaqtni kirgizing (0-23)"))
# energiya_darajasi = float(input("Energiya darajasini kiriting (0-100) tizimning batareya zaryadi : "))
# internet_aloqasi = input("Internet aloqasi ulanganmi: (ha/yoq)")
# foydalanuvchi_rejimi = input("Foydalanuvchi rejimini kiriting: (rejim, matn: uyda, tashqarida, ta’til)")
#
#
# # if not xavf_darajasi > 0  <=100:
# #     print("Xato xavf darajasi")
# # if not vaqt >=23:
# #     print("Noto‘g‘ri vaqt")
# # if not energiya_darajasi >= 100:
# #     print("Xato energiya darajasi")
# # if not foydalanuvchi_rejimi in {"uyda , tashqarida , ta'til"}:
# #     print("Noto‘g‘ri rejim")


# === Kirishlar ===  
xavf = int(input("Xavf darajasini kiriting (0-100): "))
harakat = input("Harakat sensori (ha/yo'q): ").lower() == "ha"
eshik = input("Eshik sensori (ha/yo'q): ").lower() == "ha"
soat = int(input("Vaqt soatini kiriting (0-23): "))
energiya = float(input("Energiya darajasini kiriting (%, 0-100): "))
internet = input("Internet aloqasi (ha/yo'q): ").lower() == "ha"
rejim = input("Rejimni kiriting (uyda, tashqarida, ta'til): ").lower()

# === Xatoliklar ===
if not (0 <= xavf <= 100):
    print("Xato xavf darajasi")
elif not (0 <= soat <= 23):
    print("Noto‘g‘ri vaqt")
elif not (0 <= energiya <= 100):
    print("Xato energiya darajasi")
elif rejim not in ["uyda", "tashqarida", "ta'til"]:
    print("Noto‘g‘ri rejim")
elif energiya == 0:
    print("Tizim o‘chirilgan")
else:
    tun = soat >= 22 or soat < 6
    kunduz_chegirma = 0.9 if 6 <= soat < 22 else 1.0
    tun_koeff = 1.2 if tun else 1.0
    harakat_turi = "Hech narsa"
    xarajat = 0
    energiya_sarf = 0

    if energiya < 5:
        harakat_turi = "Monitoring"
        energiya_sarf = 2
        if rejim == "uyda" and xavf < 30:
            xarajat = 0
        else:
            xarajat = 500 * kunduz_chegirma
    elif energiya < 10:
        harakat_turi = "Ogohlantirish"
        energiya_sarf = 5
        xarajat = 5000 if internet else 1000
        if 12 <= soat <= 15 and xavf < 50:
            xarajat *= 0.9
        xarajat *= tun_koeff
    else:
        if rejim == "uyda":
            if xavf > 90:
                harakat_turi = "Signalizatsiya"
            elif 30 <= xavf <= 90 or (harakat and not eshik):
                harakat_turi = "Ogohlantirish"
            else:
                harakat_turi = "Monitoring"
        elif rejim == "tashqarida":
            if xavf > 70 or (harakat and eshik):
                harakat_turi = "Signalizatsiya"
            elif 40 <= xavf <= 70 or (harakat and not eshik):
                harakat_turi = "Ogohlantirish"
            else:
                harakat_turi = "Monitoring"
        elif rejim == "ta'til":
            if xavf > 60 or (harakat or eshik):
                harakat_turi = "Signalizatsiya"
            elif 30 <= xavf <= 60:
                harakat_turi = "Ogohlantirish"
            else:
                harakat_turi = "Monitoring"

        if harakat_turi == "Signalizatsiya":
            energiya_sarf = 10
            xarajat = 50000 if internet else 10000
            if rejim == "ta'til" and internet:
                xarajat *= 0.85
            xarajat *= tun_koeff
        elif harakat_turi == "Ogohlantirish":
            energiya_sarf = 5
            xarajat = 5000 if internet else 1000
            if 12 <= soat <= 15 and xavf < 50:
                xarajat *= 0.9
            xarajat *= tun_koeff
        elif harakat_turi == "Monitoring":
            energiya_sarf = 2
            if rejim == "uyda" and xavf < 30:
                xarajat = 0
            else:
                xarajat = 500 * kunduz_chegirma


    print("Umumiy xarajat:", f"{int(round(xarajat))} so'm")




