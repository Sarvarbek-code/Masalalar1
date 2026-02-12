#11-masala  Mehmonlar ro‘yxatini boshqarish
invited = {'Ali', 'Vali', 'Salim'}
arrived = {'Vali', 'Sami'}

#1-vazifa Yangi mehmon 'Aziza'ni invited ga qo‘shing!
invited.add("Aziza")
print(f"1-vazifa natijasi: {invited}")

#2-vazifa Faqat kelganlar ro‘yxatini alohida setga ajrating → intersection()
arrived.intersection(invited)
print(f"2-vazifa natijasi: {arrived}")

#3-vazifa Kelmagan mehmonlarni ajrating → difference()
invited.difference(arrived)
print(f"3-vazifa natijasi: {invited}")

#4-vazifa Ikkala ro‘yxatni birlashtiring → union()
a = invited.union(arrived)
print(f"4-vazifa natijasi: {a}")

#5-vazifa Avvaldan taklif qilinganlar ro‘yxatini tozalang → clear()
invited.clear()
print(f"5-vazifa natijasi: {invited}")

#6-vazifa Kelganlar ro‘yxatidan 'Sami'ni olib tashlang → discard()
arrived.discard("Sami")
print(f"6-vazifa natijasi: {arrived}")

#7-vazifa Yangi kelgan mehmon 'Sardor'ni qo‘shing
arrived.add("Sardor")
print(f"7-vazifa natijasi: {arrived}")

#8-vazifa Taklif qilinmagan, lekin kelgan mehmonlarni toping
arrived.difference(invited)
print(f"8-vazifa natijasi: {arrived}")

#9-vazifa arrived setining uzunligini aniqlang
b = len(arrived)
print(f"9-vazifa natijasi: {b}")

#10-vazifa
print(f"10-vazifa natijasi: {arrived} {invited}")

#12-masala  Online kursga yozilganlar
udemy = {'Alisher', 'Dilshod', 'Malika'}
coursera = {'Malika', 'Zafar'}

#1-vazifa udemy ga 'Shahnoza' ni qo‘shing
udemy.add("Shahnoza")
print(f"1-vazifa natijasi: {udemy}")

#2-vazifa Faqat ikkalasida ham yozilganlarni toping
y = udemy.intersection(coursera)
print(f"2-vazifa natijasi: {y}")

#3-vazifa Faqat coursera da yozilganlarni ajrating
coursera.intersection(udemy)
print(f"3-vazifa natijasi: {coursera}")

#4-vazifa  Umumiy yozilganlar ro‘yxatini yarating
udemy.union(coursera)
print(f"4-vazifa natijasi: {udemy}")

#5-vazifa  udemy dagilarni nusxalang → copy()
coppied = udemy.copy()
print(f"5-vazifa natijasi: {coppied}")

#6-vazifa Nusxadan 'Dilshod' ni olib tashlang
coppied.remove("Dilshod")
print(f"6-vazifa natijasi: {coppied}")

#7-vazifa Faqat bir kursda qatnashayotganlarni aniqlang
faqat_bir_kursda = udemy ^ coursera
print(f"7-vazifa natijasi: {faqat_bir_kursda}")

#8-vazifa Alifbo tartibida ro‘yxat chiqaring
sorted(udemy)
print(f"8-vazifa natijasi: {udemy}")

#9-vazifa Har bir set uzunligini ko‘rsating
u = len(udemy)
c = len(coursera)
print(f"9-vazifa natijasi:(udemy) {u} , (Coursera) {c}")

#10-vazifa Yakuniy natijalarni chop eting
print(f"10-vazifa natijasi: {udemy} , {coursera}")




#13-masala  Bo‘sh ish o‘rinlariga ariza topshirganlar

it_vacancy = {'Azamat', 'Javlon', 'Sarvar'}
design_vacancy = {'Javlon', 'Sabrina'}

#1-vazifa 'Kamila' ni it_vacancy ga qo‘shing
it_vacancy.add("Kamila")
print(f"1-vaifa natijasi: {it_vacancy}")


#2-vazifa Faqat IT ga topshirganlarni ko‘rsating
it_vacancy.difference(design_vacancy)
print(f"2-vazifa natijasi: {it_vacancy}")

#3-vazifa Har ikkala bo‘sh ish o‘rniga topshirganlarni aniqlang
t = it_vacancy.intersection(design_vacancy)
print(f"3-vazifa natijasi: {t}")

#4-vazifa Faqat dizayn bo‘sh ish o‘rniga topshirganlarni ko‘rsating
design_vacancy.difference(it_vacancy)
print(f"4-vazifa natijasi: {design_vacancy}")

#5-vazifa Barcha arizachilar ro‘yxatini yarating
j = it_vacancy.union(design_vacancy)
print(f"5-vazifa natijasi: {j}")

#6-vazifa Har ikkala ro‘yxatni birlashtirib nusxa oling
s = j.copy()
print(f"6-vazifa natijasi :{s}")

#7-vazifa 'Sarvar' ni olib tashlang
s.remove("Sarvar")
print(f"7-vazifa natijasi:{s}")

#8-vazifa Farqli arizachilarni aniqlang
it_vacancy.symmetric_difference_update(design_vacancy)
print(f"8-vazifa natijasi : {it_vacancy}")

#9-vazifa Har bir ro‘yxat uzunligini toping
l = len(it_vacancy)
k = len(design_vacancy)
print(f"9-vazifa:  it_vacancy uzunligi  {l} ,design_vacancy uzunligi {k}")

#10-vazifa Natijalarni alifbo bo‘yicha tartiblang
o =  sorted(it_vacancy)
p = sorted(design_vacancy)
print(f"10-vazifa: {o} , {p}")



#14-Masala: Tibbiy tekshiruvdan o‘tganlar
students = {'Ali', 'Soliha', 'Bobur'}
checked = {'Bobur', 'Ali'}

#1-vazifa 'Gulbahor' ni checked ga qo‘shing
checked.add("Gulbahor")
print(f"1-vazifa natijasi: {checked}")

#2-vazifa Tibbiy tekshiruvdan o‘tmaganlarni aniqlang
students.difference(checked)
print(f"2-vazifa natijasi : {students}")


#3-vazifa Tibbiy tekshiruvdan o‘tganlar ro‘yxatini tartiblang
checked.difference(students)
print(f"3-vazifa natijasi : {checked}")

# 4-vazifa Ikkala ro‘yxatni birlashtiring
students.union(checked)
print(f"4-vazifa natijasi: {students}")

#5-vazifa Tibbiy tekshiruvdan o‘tganlar sonini aniqlang
l = len(checked)
print(f"5-vazifa natijasi: Tibbiy tekshiruvdan o‘tganlar soni  {l}")

#6-vazifa Nusxa olib 'Ali' ni o‘chirib tashlang
coppied = students.copy()
print(f"{coppied}")
coppied.remove("Ali")
print(f"6-vazifa natijasi: {coppied}")

#7-vazifa Simmetrik farqni toping

students.symmetric_difference(checked)
print(f"7-vazifa natijasi: {students}")

#8-vazifa To‘plamlar bo‘sh emasligini tekshiring
q =  bool(students)
p =  bool(checked)
print(f"8-vazifa natijasi: {q} , {p}")

#9-vazifa Har ikkala ro‘yxat orasidagi umumiylarni ko‘rsating

n = students.intersection(checked)
print(f"9-vazifa natijasi: {n}")

#10-vazifa Yakuniy ma’lumotni ekranga chiqaring
print(f"10-vazifa natijasi: {students} , {checked}")





# 15-masala: Sayohat qilgan o‘quvchilar

toshkent_trip = {'Olim', 'Rustam', 'Ziyoda'}
samarkand_trip = {'Ziyoda', 'Kamola'}


#1-vazifa 'Nodira' ni toshkent_trip ga qo‘shing
toshkent_trip.add("Nodira")
print(f"1-vazifa natijasi: {toshkent_trip}")

#2-vazifa Har ikki shaharni ziyorat qilgan o‘quvchilarni toping
a = toshkent_trip.intersection(samarkand_trip)
print(f"2-vazifa natijasi: {a}")

#3-vazifa Faqat Toshkentga borganlarni ko‘rsating
toshkent_trip.difference(samarkand_trip)
print(f"3-vazifa natijasi: {toshkent_trip}")

# 4-vazifa Umumiy sayohatchilar ro‘yxatini yarating

b = toshkent_trip.union(samarkand_trip)
print(f"4-vazifa natijasi: {b}")

#5-vazifa Simmetrik farqni aniqlang
toshkent_trip.symmetric_difference(samarkand_trip)
print(f"5-vazifa natijasi: {toshkent_trip}")

# 6-vazifa 'Ziyoda'ni olib tashlang
b.remove("Ziyoda")
print(f"6-vazifa natijasi: {b}")

# 7-vazifa Nusxa oling va uni bo‘shating → clear()
b.copy().clear()
print(f"7-vazifa natijasi: {b}")

# 8-vazifa Har ikkala set uzunligini toping
m = len(toshkent_trip)
h = len(samarkand_trip)
print(f"8-vazifa natijasi: toshkent_trip uzunligi {m} , samarkand_trip uzunligi {h}")


# 9-vazifa Alifbo bo‘yicha tartiblash
sorted(b)
print(f"9-vazifa natijasi: {b}")

# 10-vazifa Har bir bosqichdan keyin natijani chop eting
print(f"10-vazifa natijasi: {toshkent_trip} , {samarkand_trip} {b}")







