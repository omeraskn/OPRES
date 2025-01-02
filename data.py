# Dersler
dersler = [
    {"kod": "MAT1071", "ders": "Matematik 1", "online": 0, "sinif": 1, "saat": 3},
    {"kod": "FIZ1001", "ders": "Fizik 1", "online": 1, "sinif": 1, "saat": 2},
    {"kod": "ATA1031", "ders": "Atatürk İlkeleri İnk. Tar", "online": 1, "sinif": 1, "saat": 1},
    {"kod": "BLM1011", "ders": "Bilgisayar Bilimlerine Gir.", "online": 0, "sinif": 1, "saat": 2},
    {"kod": "MAT1320", "ders": "Lineer Cebir", "online": 0, "sinif": 1, "saat": 2},
    {"kod": "TDB1031", "ders": "Türkçe 1", "online": 1, "sinif": 1, "saat": 1},
    {"kod": "BLM2011", "ders": "İst. ve Olasılık Hes.", "online": 0, "sinif": 2, "saat": 2},
    {"kod": "BLM2012", "ders": "Nesneye Yönelik Prog.", "online": 0, "sinif": 2, "saat": 3},
    {"kod": "BLM2642", "ders": "Bilg. Müh. İçin Diff. Denk.", "online": 0, "sinif": 2, "saat": 3},
    {"kod": "BLM2521", "ders": "Ayrık Matematik", "online": 0, "sinif": 2, "saat": 2},
    {"kod": "BLM2611", "ders": "Lojik Devreler", "online": 0, "sinif": 2, "saat": 3},
    {"kod": "BLM3021", "ders": "Algoritma Analizi", "online": 0, "sinif": 3, "saat": 3},
    {"kod": "BLM3042", "ders": "Seminer ve Meslek Etiği", "online": 0, "sinif": 3, "saat": 2},
    {"kod": "BLM3061", "ders": "Mikroişl. Sist. ve Assmb", "online": 0, "sinif": 3, "saat": 3},
    {"kod": "BLM3730", "ders": "Blokzincir Temelleri", "online": 0, "sinif": 4, "saat": 2},
    {"kod": "BLM4011", "ders": "Bilişim Sis. Güvenliği", "online": 0, "sinif": 4, "saat": 3},
    {"kod": "BLM4710", "ders": "Yönetim Bilgi Sis.", "online": 0, "sinif": 4, "saat": 3},
    {"kod": "BLM4770", "ders": "Yaz.Kal.Test.Sür.", "online": 0, "sinif": 4, "saat": 3},
    {"kod": "BLM4021", "ders": "Gömülü Sistemler", "online": 0, "sinif": 4, "saat": 3},
    {"kod": "BLM3780", "ders": "Ver. Tab. Sis. Gerç.", "online": 0, "sinif": 4, "saat": 3},
    {"kod": "BLM3041", "ders": "Veritabanı Yönetimi ", "online": 0, "sinif": 3, "saat": 2},
    #{"kod": "BLM2031", "ders": "Yapısal Programlama", "online": 0, "sinif": 2, "saat": 3}, II. DONEM
    #{"kod": "BLM2041", "ders": "Bilgisayar Mühendisleri için Sinyaller ve Sistemler", "online": 1, "sinif": 2, "saat": 2},
]

# Öğretmenler
ogretmenler = [
    {"isim": "Pınar Albayrak", "verdigi_dersler": ["MAT1071", "MAT1320"], "calisma_gunleri": ["Pazartesi", "Çarşamba"]},
    {"isim": "Çiğdem ORUÇ", "verdigi_dersler": ["FIZ1001"], "calisma_gunleri": ["Salı", "Perşembe"]},
    {"isim": "Zafer Doğan", "verdigi_dersler": ["ATA1031"], "calisma_gunleri": ["Pazartesi", "Cuma"]},
    {"isim": "Sevgi Kocaoba", "verdigi_dersler": ["ITB3330"], "calisma_gunleri": ["Çarşamba", "Cuma"]},
    {"isim": "Göksel Biricik", "verdigi_dersler": ["BLM1011", "BLM3042"], "calisma_gunleri": ["Salı", "Cuma"]},
    {"isim": "Oğuz Altun", "verdigi_dersler": ["BLM2011", "BLM3730"], "calisma_gunleri": ["Pazartesi", "Salı"]},
    {"isim": "M.Amaç Güvensan", "verdigi_dersler": ["BLM2031", "BLM3021", "BLM1011"], "calisma_gunleri": ["Salı", "Çarşamba"]},
    {"isim": "Alican Karaca", "verdigi_dersler": ["BLM2041", "BLM4021"], "calisma_gunleri": ["Perşembe", "Cuma"]},
    {"isim": "Ahmet Elbir", "verdigi_dersler": ["BLM2521"], "calisma_gunleri": ["Çarşamba", "Cuma"]},
    {"isim": "Gökhan Bilgin", "verdigi_dersler": ["BLM2611"], "calisma_gunleri": ["Salı", "Pazartesi"]},
    {"isim": "Hülya Polat", "verdigi_dersler": ["MDB2001"], "calisma_gunleri": ["Salı", "Perşembe"]},
    {"isim": "Utku Kalaycı", "verdigi_dersler": ["BLM3041", "BLM3780"], "calisma_gunleri": ["Pazartesi", "Çarşamba"]},
    {"isim": "Furkan Çakmak", "verdigi_dersler": ["BLM3061", "BLM2012"], "calisma_gunleri": ["Salı", "Çarşamba"]},
    {"isim": "Hilal Tufan", "verdigi_dersler": ["TDB1031"], "calisma_gunleri": ["Pazartesi", "Cuma"]},
    {"isim": "A.Gökhan Yavuz", "verdigi_dersler": ["BLM4011"], "calisma_gunleri": ["Pazartesi", "Salı", "Cuma"]},
    {"isim": "Oya Kalıpsız", "verdigi_dersler": ["BLM4770", "BLM4710"], "calisma_gunleri": ["Pazartesi", "Salı", "Cuma"]},
    {"isim": "M.Fatih Amasyalı", "verdigi_dersler": ["BLM2642"], "calisma_gunleri": ["Cuma"]},
]

# Derslikler
derslikler = [
    {"kod": "D109", "kapasite": 50},
    {"kod": "D110", "kapasite": 50},
    {"kod": "D012", "kapasite": 70},
    {"kod": "D111", "kapasite": 70},
    {"kod": "D108", "kapasite": 50},
    {"kod": "D107", "kapasite": 50},
    {"kod": "D106", "kapasite": 50},
    {"kod": "DB11", "kapasite": 70},
    {"kod": "EEF Konferans Salonu", "kapasite": 100},
    {"kod": "ZOOM", "kapasite": 1000},
]