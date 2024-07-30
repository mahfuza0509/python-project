# 1. "Umid market” da X kg konfet F so’m turadi, 1 kg konfetning narxini aniqlang.
f = 10000  # kg konfetning narxi
x = 1  # 1 kg konfet
print(f"\"Umid market\" da {x} kg konfet {f * x} so'm turadi.")

print("  ")

# 2. Ahmad aka uyini xavfsizlik uchun uyini devor bilan o’ramoqchi. Uyining uzunligi 15 metr, eniga 25 metr. Uyni to’liq o’rab olish uchun qancha m2 devor kerak.
height = 15  # Uyining uzunligi
width = 25  # Uyining eni
print(f"Uyni to'liq o'rab olish uchun {height * width} m2 devor kerak.")
print("  ")

# 3. Angliya va O’zbekiston futbo’l o’yinida terma jamoamiz har 15 minutdan go’l ursa hisob qancha bo’ladi. Eslatma hakam har 1 taym uchun kamida 5 minut qo’shimcha vaqt beradi.
taym_vaqti = 45  #taym
qoshimcha_vaqt = 5  #bitta gol=qoshimcha VAXT
jami_taymlar = 2  

jami_vaqt = (taym_vaqti + qoshimcha_vaqt) * jami_taymlar 

print(f"Terma jamoamiz har 15 minutdan go'l ursa hisob {jami_vaqt // 15} bo'ladi.")
print("  ")
# 4. 
print(f"Dilnura {502.4 * 4} kkal(kilo kaloriya) snikers istemol qiladi.")
print("  ")
# 5. 
print(f"Ahmad jami {0.27 * 1000} energiya sarf qiladi.")
print("  ")
# 6. 
yiliga_daromad = 10  
oyiga_daromad = yiliga_daromad * (1 + 35.8 / 100) / 12 
print(f"Yil boshidagi statistikaga qaraganda. Uning daromadi oyiga 35.8% oshsa, shu oy u {oyiga_daromad:.3} daromad qiladi.")
print("  ")
# 7. 
jami_vaqt = 90  

print(f"Terma jamoamiz har 15 minutdan go'l ursa hisob {jami_vaqt // 15} bo'ladi.")
print("  ")
# 8.
uy_perimetri = 2 * (15 + 25)

devor_yuzasi = uy_perimetri * 1.5

gisht_yuzasi = 0.24 * 0.05

kerakli_gishtlar_soni = devor_yuzasi / gisht_yuzasi

print(f"Shu talablarni muvaffaqiyatli bajarish uchun, {kerakli_gishtlar_soni} g'isht kerak bo'ladi.")
print("  ")
# 9.
snickers_kaloriya = 502.4
yegan_snickers_soni = 2
bir_qadam_kaloriya = 0.27

print(f"Bu energiyani chiqarib yuborish uchun Firdavsbekjon {int(yegan_snickers_soni * snickers_kaloriya / bir_qadam_kaloriya)} qadam bosishi kerak")