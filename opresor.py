from ortools.linear_solver import pywraplp
from data import dersler, ogretmenler, derslikler

# Çizelgeleme Fonksiyonu
def ders_cizelgele():
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
    saatler = list(range(9, 17))  # 9:00 - 16:00 (8 saatlik dilim)
    
    # Solver tanımı
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("SCIP çözücüsü yüklenemedi!")
        return None


    # Karar değişkenleri: x[i, j, k, l, m]
    x = {}
    for i, ders in enumerate(dersler):
        for j, ogretmen in enumerate(ogretmenler):
            if ders["kod"] in ogretmen["verdigi_dersler"]:  # Uygun öğretmen kontrolü
                for k, derslik in enumerate(derslikler):
                     if ders["online"] == 0 or derslik["kod"] == "ZOOM": #online dersler sadece zoom dersliğine gider
                        for l, gun in enumerate(gunler):
                            if gun in ogretmen["calisma_gunleri"]:  # Çalışma günü kontrolü
                                for m in range(len(saatler) - ders["saat"] + 1):
                                    x[i, j, k, l, m] = solver.BoolVar(f'x_{i}_{j}_{k}_{l}_{m}')


    # Kısıtlar
    # 1. Her ders yalnızca bir kez atanmalı
    for i, ders in enumerate(dersler):
        solver.Add(sum(x[i, j, k, l, m] 
                       for j in range(len(ogretmenler))
                       for k in range(len(derslikler))
                       for l in range(len(gunler))
                       for m in range(len(saatler) - ders["saat"] + 1)
                       if (i, j, k, l, m) in x) == 1)


    # 2. Her öğretmen aynı anda yalnızca bir ders almalı
    for j, ogretmen in enumerate(ogretmenler):
        for l, gun in enumerate(gunler):
            for m in range(len(saatler)):
                solver.Add(sum(x[i, j, k, l, m]
                               for i in range(len(dersler))
                               for k in range(len(derslikler))
                               if (i, j, k, l, m) in x) <= 1)


    # 3. Her derslik aynı anda yalnızca bir ders almalı
    for k, derslik in enumerate(derslikler):
        for l, gun in enumerate(gunler):
            for m in range(len(saatler)):
                solver.Add(sum(x[i, j, k, l, m]
                               for i in range(len(dersler))
                               for j in range(len(ogretmenler))
                               if (i, j, k, l, m) in x) <= 1)


    # 4. Aynı sınıfın dersleri aynı anda çakışmamalı
    for sinif in range(1, 5):  # 1'den 4. sınıfa kadar
        for l, gun in enumerate(gunler):
            for m in range(len(saatler)):
                solver.Add(sum(x[i, j, k, l, m]
                               for i, ders in enumerate(dersler)
                               for j in range(len(ogretmenler))
                               for k in range(len(derslikler))
                               if (i, j, k, l, m) in x and ders["sinif"] == sinif) <= 1)


# 5. Dersin süresi boyunca başka ders atanamaz
    for k, derslik in enumerate(derslikler):
      for l, gun in enumerate(gunler):
          for m in range(len(saatler)):
            solver.Add(sum(
                x[i, j, k, l, t]
                for i, ders in enumerate(dersler)
                for j in range(len(ogretmenler))
                for t in range(max(0, m - ders["saat"] + 1), min(len(saatler) ,m +1 ))
                if (i, j, k, l, t) in x
            ) <= 1)


    # Amaç fonksiyonu: Tüm atamaları maksimize et
    objective = solver.Objective()
    for key, var in x.items():
        objective.SetCoefficient(var, 1)
    objective.SetMaximization()


    # Çözümü çalıştır
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Çözüm bulundu!")
        cizelge = []
        for key, var in x.items():
            if var.solution_value() == 1:
                i, j, k, l, m = key
                cizelge.append({
                    "ders_kodu": dersler[i]["kod"],
                    "ogretmen": ogretmenler[j]["isim"],
                    "derslik": derslikler[k]["kod"],
                    "gun": gunler[l],
                    "saat": saatler[m],
                    "sinif": dersler[i]["sinif"],
                })
        return cizelge
    else:
        print("Çözüm bulunamadı.")
        return None


# Çalıştırma 
cizelge = ders_cizelgele()
if cizelge:
    for ders in cizelge:
        print(f"{ders}")