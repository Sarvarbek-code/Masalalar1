# # ======================================
# # 1-MASALA. Kofe do'konidagi arifmetika
# # ======================================
# kun = input("Hafta kunini kiriting: ").lower()
# stakan_soni = int(input("Sotilgan stakanlar sonini kiriting: "))
# narx = int(input("Bir stakan narxini kiriting (so'mda): "))
# if kun == "shanba" or kun == "yakshanba":
#     stakan_soni = stakan_soni * 1.5
#     print("Daromad:", stakan_soni * narx, "so'm")
# elif kun in ["dushanba", "seshanba", "chorshanba", "payshanba", "juma"]:
#     print("Daromad:", stakan_soni * narx, "so'm")
# else:
#     print("Bunday kun mavjud emas!")
#
#
# # ============================
# # 2-MASALA. Qadam o'lchagich
# # ============================
# qadam = int(input("Necha qadam yurdingiz: "))
# uzunlik = float(input("Bir qadam uzunligi (metrda): "))
# if qadam < 0 or uzunlik <= 0:
#     print("Xato kiritildi!")
# else:
#     masofa = qadam * uzunlik / 1000
#     print("Bugun yurilgan masofa:", masofa, "km")
#
#
# # ==========================
# # 3-MASALA. Elektr chiroqlari
# # ==========================
# chiroq_soni = int(input("Chiroqlar sonini kiriting: "))
# quvvat = float(input("Har bir chiroq quvvati (Vt): "))
# soat = float(input("Yoqilgan soat: "))
# if chiroq_soni <= 0 or quvvat <= 0 or soat <= 0:
#     print("Xato kiritildi!")
# else:
#     energiya = chiroq_soni * quvvat * soat / 1000
#     print("Kunlik energiya sarfi:", energiya, "kVt·soat")
#
#
# # ====================
# # 4-MASALA. Tort pishirish
# # ====================
# tort_soni = int(input("Nechta tort pishirmoqchisiz: "))
# if tort_soni <= 0:
#     print("Xato kiritildi!")
# else:
#     print("Un:", 450 * tort_soni, "g")
#     print("Tuxum:", 5 * tort_soni, "dona")
#     print("Shakar:", 250 * tort_soni, "g")
#
#
# # ===========================
# # 5-MASALA. BMI indeksi
# # ===========================
# boy = float(input("Bo'yingiz (metrda): "))
# vazn = float(input("Vazningiz (kg): "))
# if boy <= 0 or vazn <= 0:
#     print("Xato kiritildi!")
# else:
#     bmi = vazn / (boy * boy)
#     if bmi < 18.5:
#         print("Ozg'in (BMI:", bmi, ")")
#     elif bmi < 25:
#         print("Normal (BMI:", bmi, ")")
#     elif bmi < 30:
#         print("Ortiqcha vazn (BMI:", bmi, ")")
#     else:
#         print("Semizlik (BMI:", bmi, ")")
#
#
# # ===================================
# # 6-MASALA. Quyoshli kunlarda suv bug‘lanishi
# # ===================================
# suv = float(input("Boshlang‘ich suv miqdori (litr): "))
# kun = int(input("Kunlar soni: "))
# if suv <= 0 or kun <= 0:
#     print("Xato kiritildi!")
# else:
#     i = 0
#     while i < kun:
#         suv = suv - suv * 1.2 / 100
#         i = i + 1
#     print(kun, "kundan keyin suv miqdori:", suv, "litr")
#
#
# # =============================
# # 7-MASALA. Kitob o'qish tezligi
# # =============================
# foiz = int(input("Kuniga kitobning necha foizini o'qisiz (%): "))
# if foiz <= 0 or foiz > 100:
#     print("Xato kiritildi!")
# else:
#     kun_soni = 100 / foiz
#     if 100 % foiz != 0:
#         kun_soni = int(kun_soni) + 1
#     print("Kitobni tugatish uchun:", kun_soni, "kun kerak")
#
#
# # =========================
# # 8-MASALA. Kompas burchagi
# # =========================
# b1 = int(input("Birinchi burilish (gradusda): "))
# b2 = int(input("Ikkinchi burilish (gradusda): "))
# b3 = int(input("Uchinchi burilish (gradusda): "))
# natija = (b1 + b2 + b3) % 360
# print("Yakuniy burchak:", natija, "gradus")
#
#
# # ======================
# # 9-MASALA. Pitsa bo'lish
# # ======================
# r = float(input("Pitsa radiusini kiriting (sm): "))
# n = int(input("Necha kishiga bo‘linadi: "))
# if r <= 0 or n <= 0:
#     print("Xato kiritildi!")
# else:
#     pi = 3.14159
#     s = pi * r * r / n
#     print("Har bir kishiga to'g'ri keladigan yuza:", s, "sm²")
#
#
# # ===============================
# # 10-MASALA. Mahsulotlar chegirmasi
# # ===============================
# a = int(input("1-mahsulot narxi: "))
# b = int(input("2-mahsulot narxi: "))
# c = int(input("3-mahsulot narxi: "))
# jami = a + b + c
# if jami > 40000:
#     natija = jami * 0.9
#     print("Chegirma qo'llandi. Yakuniy to'lov:", natija)
# else:
#     print("Chegirma yo'q. To'lov:", jami)
#
#
# # =======================
# # 11-MASALA. Muz bo'lagi hajmi
# # =======================
# a = float(input("Kub tomoni (sm): "))
# if a <= 0:
#     print("Xato kiritildi!")
# else:
#     hajm = a * a * a * (1 + 0.008)
#     print("Yangi hajm:", hajm, "sm³")
#
#
# # ======================
# # 12-MASALA. Ish soatlari
# # ======================
# kunlik = float(input("Har kuni necha soat ishlaysiz: "))
# hafta = int(input("Haftada necha kun ishlaysiz: "))
# if kunlik <= 0 or hafta <= 0:
#     print("Xato kiritildi!")
# else:
#     ish_kunlari = kunlik * hafta
#     print("Haftalik ish soati:", ish_kunlari)
#
#
# # ============================
# # 13-MASALA. Taksi tarifi
# # ============================
# masofa = float(input("Masofani kiriting (km): "))
# if masofa <= 0:
#     print("Xato kiritildi!")
# elif masofa <= 2:
#     print("To'lov: 10000 so'm")
# else:
#     print("To'lov:", 10000 + (masofa - 2) * 4000, "so'm")
#
#
# # ==============================
# # 14-MASALA. Oltin taqinchoq qiymati
# # ==============================
# gramm = float(input("Uzuk og‘irligi (gramm): "))
# narx = float(input("1 gramm oltin narxi (so‘m): "))
# if gramm <= 0 or narx <= 0:
#     print("Xato kiritildi!")
# else:
#     summa = gramm * narx
#     yakuniy = summa * 1.02
#     print("Uzuk narxi:", yakuniy, "so'm")
#
#
# # ==============================
# # 15-MASALA. Astronomik kuzatuv
# # ==============================
# R = float(input("Yer radiusi (km): "))
# h = float(input("Sun’iy yo‘ldosh balandligi (km): "))
# if R <= 0 or h < 0:
#     print("Xato kiritildi!")
# else:
#     d = (2 * R * h + h * h) ** 0.5
#     print("Ko‘rinish radiusi:", d, "km")
#
#
# # ======================================
# # 16-MASALA. Quyosh panelining samaradorligi
# # ======================================
# quyosh = float(input("Quyosh nuri (Vt/m²): "))
# yuzasi = float(input("Panel yuzasi (m²): "))
# soat = float(input("Necha soat davomida quyosh tushadi: "))
# if quyosh <= 0 or yuzasi <= 0 or soat <= 0:
#     print("Xato kiritildi!")
# else:
#     quvvat = quyosh * yuzasi * 0.18
#     energiya = quvvat * soat / 1000
#     print("Ishlab chiqarilgan energiya:", energiya, "kVt·soat")
#
#
# # ==========================
# # 17-MASALA. Kvadrat ildizli masofa
# # ==========================
# a = float(input("a: "))
# b = float(input("b: "))
# if a == 0 and b == 0:
#     print("Masofa 0")
# else:
#     masofa = (a * a + b * b) ** 0.5
#     print("Masofa:", masofa)
#
#
# # =============================
# # 18-MASALA. Kredit murakkab foiz
# # =============================
# P = float(input("Kredit summasi: "))
# r = float(input("Oylik foiz (0.02 shaklida): "))
# n = int(input("Necha oy davomida: "))
# if P <= 0 or r <= 0 or n <= 0:
#     print("Xato kiritildi!")
# else:
#     S = P * (1 + r) ** n
#     print(n, "oy oxirida to‘lanadigan summa:", S, "so'm")
#
#
# # =======================
# # 19-MASALA. Raketa tezlanishi
# # =======================
# v = float(input("Oxirgi tezlik (m/s): "))
# t = float(input("Vaqt (s): "))
# if v <= 0 or t <= 0:
#     print("Xato kiritildi!")
# else:
#     a = v / t
#     yo_l = 0.5 * a * t * t
#     print("Tezlanish:", a, "m/s²")
#     print("Bosib o'tgan yo'l:", yo_l, "m")
#
#
# # =============================
# # 20-MASALA. Valyuta konvertatsiyasi
# # =============================
# dollar = float(input("Jahongir yuborgan dollar miqdori: "))
# kurs = float(input("1 dollar kursi (so‘m): "))
# if dollar <= 0 or kurs <= 0:
#     print("Xato kiritildi!")
# else:
#     so_m = dollar * kurs
#     so_m = so_m * 0.96
#     so_m = so_m * 0.88
#     print("Jahongirga tushgan sof summa:", so_m, "so'm")

# ustoz "chat gpt" lekin kod lari ko'rib chiqdim 👍