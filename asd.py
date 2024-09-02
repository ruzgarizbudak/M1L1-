kisaltmalar={
    "LOL":"komik bir şeye verilen cevap",
    "SHESSH":"onaylamamak",
    "AGGRO":"agresifleşmek/sinirlenmek",
    "AFK":"sabit duran bişey yapmayan",
    "CRINGE":"garip ya da utandırıcı bir şey",
}

kelime=input("Bilmediğiniz kelimeyi giriniz.").upper()


if kelime in kisaltmalar.keys():
    print(kisaltmalar[kelime])
else:
    print("Kelimeyi bulamadım")
