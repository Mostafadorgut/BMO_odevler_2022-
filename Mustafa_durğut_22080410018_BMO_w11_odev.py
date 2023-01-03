# ana liste
sinav_sonuc = {'isimler':['ayse K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],'cinsiyet':['K','E','E','E','K','K'],'matematik':[60,40,97,45,56,95],'turkce':[70,30,23,90,78,46]}
print(sinav_sonuc['isimler'])
print(sinav_sonuc['cinsiyet'])
print(sinav_sonuc['matematik'])
print(sinav_sonuc['turkce'])
# bu iki bos liste kadin ve erkek turkce notlari ayri ayri ayirlasin
kadinlarin_turkce_notlari = []
erkeklerin_turkce_notlari = []
count_k = 0
count_e = 0
k_mat = 0
k_turk = 0
e_mat = 0
e_turk = 0
for i in range(len(sinav_sonuc['cinsiyet'])):
    # egir kadin sayaci + 1
    if sinav_sonuc['cinsiyet'][i] == 'K':
        count_k +=1
        k_mat = k_mat + sinav_sonuc['matematik'][i]
        k_turk = k_turk + sinav_sonuc['turkce'][i]
        #burda kadinler turkce notu aliyor
        kadinlarin_turkce_notlari.append(sinav_sonuc['turkce'][i])
        #degilse erkik sayaci + 1
    else :
        count_e += 1
        e_mat = e_mat + sinav_sonuc['matematik'][i]
        e_turk = e_turk + sinav_sonuc['turkce'][i]
        #burda erkikler turkce notu aliyor
        erkeklerin_turkce_notlari.append(sinav_sonuc['turkce'][i])
        #suslu barantes icinde islem yapiyor
print(f"Erkek Matatematik Ortalamasi: {e_mat/count_e}\n\
Kadinlarin Matematik Ortalamasi: {k_mat/count_k}\n\
Turkce Dersinin Ortalamasi : {(k_turk + e_turk)/(count_e + count_k)}")
print("Kadinlarin En Yuksek Turkce Notu : ", max(kadinlarin_turkce_notlari))
print("Erkeklerin En Yuksek Turkce Notu : ", max(erkeklerin_turkce_notlari))