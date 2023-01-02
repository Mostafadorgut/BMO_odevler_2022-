sinav_sonuc = {'isimler': ['ayse K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
               'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'], 'vize': [60, 40, 97, 45, 56, 95],
               'final': [70, 30, 23, 80, 78, 46]}#tabloyu sinav_sonuc isimli bir sözlük oluşturduk


for l in range(6):
    notortalamasi =yeni_vize[l]*0.3+yeni_final[l]*0.7# her öğrenci için geçme notunu, %30 vize ve %70 final
    if(notortalamasi>=60):#not ortalamasi 59 dan daha fazla 
        print(yeni_isim[l],"gecti")#ogrenci isim ve gecti ekrana yazacak
    else:
        print(yeni_isim[l],"gecmedi")#ogrenci isim ve gecmedi ekrana yazacak
    print(notortalamasi)#notortalamasi ekrana yazacak
def yeni_kayit(): #yeni fonk olusturduk
    yeni_ismi = []# yeni dizi olusturduk yeni isim  icin
    yeni_cinsiyet = []# yeni dizi olusturduk yeni cinsiyet icin
    yeni_vize_not = []# yeni dizi olusturduk yeni vize  icin
    yeni_final_not = []# yeni dizi olusturduk yeni final  icin
    for i in range(2):
        isim = input("isim giriniz :")
        cinsiyet = input("cinsiyet giriniz :")
        vize_notu = input("vize notu giriniz:")
        final_notu = input("final notu giriniz :")
        yeni_ismi.append(isim)# yeni isim eklemek icin
        yeni_cinsiyet.append(cinsiyet)# yeni cinsiyet eklemek icin
        yeni_vize_not.append(vize_notu)# yeni vize notu eklemek icin
        yeni_final_not.append(final_notu)# yeni final notu eklemek icin
        print(yeni_ismi)
        print(yeni_cinsiyet)
        print(yeni_vize_not)
        print(yeni_final_not)
    for k in range(2):
        sinav_sonuc['isimler'].append(yeni_ismi[k])#eski tablo isimler anahtari icinde yeni isimler eklemek icin
        sinav_sonuc['cinsiyet'].append(yeni_cinsiyet[k])
        sinav_sonuc['vize'].append(yeni_vize_not[k])
        sinav_sonuc['final'].append(yeni_final_not[k])

        print(sinav_sonuc["isimler"], '\n')
        print(sinav_sonuc["cinsiyet"], '\n')
        print(sinav_sonuc["vize"], '\n')
        print(sinav_sonuc["final"])


yeni_kayit()
