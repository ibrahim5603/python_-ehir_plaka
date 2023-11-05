sehirler_ve_plakalar = [
    {"şehir": "Adana", "plaka": 1, "yemek": "Kebap", "en_bilindik_yer": "Seyhan Barajı"},
    {"şehir": "Adıyaman", "plaka": 2, "yemek": "Köfte", "en_bilindik_yer": "Nemrut Dağı"},
    {"şehir": "Afyonkarahisar", "plaka": 3, "yemek": "Sucuk", "en_bilindik_yer": "Afyonkarahisar Kalesi"},
    {"şehir": "Ağrı", "plaka": 4, "yemek": "Kelle", "en_bilindik_yer": "İshak Paşa Sarayı"},
    {"şehir": "Amasya", "plaka": 5, "yemek": "Çorba", "en_bilindik_yer": "Amasya Kalesi"},
    {"şehir": "Ankara", "plaka": 6, "yemek": "Kokoreç", "en_bilindik_yer": "Anıtkabir"},
    # diğer şehirler buraya eklenebilir
]

print("İşlem seçiniz:")
print("1. Şehir ismi ile plaka bulmak")
print("2. Plaka ismi ile şehir bulmak")
print("3. Şehir ismi ile yemek bulmak")
print("4. En bilindik yeri bulmak")

calistir = input("İşlem seçiniz: ")

def sehir_bulma():
    sehir = input("Şehiri giriniz: ")
    sehir_varmi = False
    for i in sehirler_ve_plakalar:
        if sehir.capitalize() == i["şehir"]:
            print("Şehir bu plakaya ait:", i["plaka"])
            sehir_varmi = True
            break
    if not sehir_varmi:
        print("Bu şehir bulunamadı")

def plaka_bulma():
    plaka = input("Plakayı giriniz: ")
    plaka_varmi = False
    for i in sehirler_ve_plakalar:
        if int(plaka) == i["plaka"]:
            print("Plaka bu şehire ait:", i["şehir"])
            plaka_varmi = True
            break
    if not plaka_varmi:
        print("Maalesef bulunamadı")

def yemek_bulma():
    sehir_plaka = input("Şehiri veya plakayı giriniz: ")
    sehir_plaka = sehir_plaka.capitalize()
    yemek_varmi = False
    for i in sehirler_ve_plakalar:
        if sehir_plaka == i["şehir"] or sehir_plaka == str(i["plaka"]):
            print("Bu şehrin bilinen yemeği:", i["yemek"])
            yemek_varmi = True
            break
    if not yemek_varmi:
        print("Bu şehir veya plaka bulunamadı")
def en_bilindik_yer_bulma():
    sehir_plaka = input("Şehiri veya plakayı giriniz: ")
    sehir_plaka = sehir_plaka.capitalize()
    yer_varmi = False
    for i in sehirler_ve_plakalar:
        if sehir_plaka == i["şehir"] or sehir_plaka == str(i["plaka"]):
            print("Bu şehrin en bilindik yeri:", i["en_bilindik_yer"])
            yer_varmi = True
            break
    if not yer_varmi:
        print("Bu şehir veya plaka bulunamadı")



if calistir == '1':
    sehir_bulma()
elif calistir == '2':
    plaka_bulma()
elif calistir == '3':
    yemek_bulma()
elif calistir == '4':
    en_bilindik_yer_bulma()
else:
    print("Geçersiz işlem seçimi. Lütfen 1, 2, 3 veya 4 giriniz.")
