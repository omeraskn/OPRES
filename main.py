import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QComboBox
)
from PyQt5.QtCore import QAbstractTableModel, Qt
from opresor import ders_cizelgele
import pandas as pd

class DersProgramiUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ders Programı Oluşturma Aracı")
        self.layout = QVBoxLayout()

        # Ders Giriş Alanı
        self.ders_form = QFormLayout()
        self.ders_adi_edit = QLineEdit()
        self.ders_suresi_edit = QLineEdit()
        self.ders_sinif_combo = QComboBox()
        self.ders_sinif_combo.addItems(["1", "2", "3", "4"])

        self.ders_form.addRow("Ders Adı:", self.ders_adi_edit)
        self.ders_form.addRow("Ders Süresi:", self.ders_suresi_edit)
        self.ders_form.addRow("Ders Sınıfı:", self.ders_sinif_combo)
        self.ders_ekle_button = QPushButton("Ders Ekle")
        self.ders_form.addRow(self.ders_ekle_button)

        self.layout.addLayout(self.ders_form)
        self.dersler_text_area = QLineEdit()
        self.layout.addWidget(self.dersler_text_area)

        # Butonlar
        self.cizelge_olustur_button = QPushButton("Çizelge Oluştur")
        self.excel_olustur_button = QPushButton("Excel Tablosu Kaydet")
        self.layout.addWidget(self.cizelge_olustur_button)
        self.layout.addWidget(self.excel_olustur_button)

        self.setLayout(self.layout)

        # Bağlantılar
        self.ders_ekle_button.clicked.connect(self.ders_ekle)
        self.cizelge_olustur_button.clicked.connect(self.cizelge_olustur)
        self.excel_olustur_button.clicked.connect(self.excel_kaydet)

        self.dersler = []
        self.cizelge = []

    def ders_ekle(self):
        ders_adi = self.ders_adi_edit.text()
        ders_suresi = self.ders_suresi_edit.text()
        ders_sinifi = self.ders_sinif_combo.currentText()
        self.dersler.append({"kod": ders_adi, "online": 0, "sinif": int(ders_sinifi), "saat": int(ders_suresi)})
        self.dersler_text_area.setText(f"Dersler: {', '.join([d['kod'] for d in self.dersler])}")
        self.ders_adi_edit.clear()
        self.ders_suresi_edit.clear()

    def cizelge_olustur(self):
        # Çizelgeyi oluştur
        self.cizelge = ders_cizelgele()
        if self.cizelge:
            QMessageBox.information(self, "Başarılı", "Çizelge başarıyla oluşturuldu!")
        else:
            QMessageBox.warning(self, "Başarısız", "Çizelge oluşturulamadı!")

    def excel_kaydet(self):
        if not self.cizelge:
            QMessageBox.warning(self, "Uyarı", "Çizelge oluşturulmadı! Önce çizelgeyi oluşturun.")
            return

        dosya_adi = "data/curriculum.xlsx"
        self.cizelgeyi_excele_yaz(self.cizelge, dosya_adi)
        QMessageBox.information(self, "Başarılı", f"Çizelge {dosya_adi} dosyasına kaydedildi.")

    def cizelgeyi_excele_yaz(self, cizelge, dosya_adi=r"C:\Users\omera\Desktop\OPRES\data\curriculum.xlsx"):
        df = pd.DataFrame(cizelge)
        df["Saat"] = df["saat"].apply(lambda x: f"{x}:00-{x + 1}:00")

        # Pazartesi-Cuma ve 09:00-20:00 saat aralığını oluştur
        saat_araligi = [f"{h}:00-{h + 1}:00" for h in range(9, 21)]
        gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
        df_pivot = pd.DataFrame(index=saat_araligi, columns=gunler).fillna("Boş")

        for _, row in df.iterrows():
            gun = row.get("gun", "Boş")
            saat = row["Saat"]
            ders_kodu = row["ders_kodu"]
            if gun in df_pivot.columns and saat in df_pivot.index:
                df_pivot.loc[saat, gun] = ders_kodu

        df_pivot.to_excel(dosya_adi)
        print(f"{dosya_adi} dosyasına yazıldı.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = DersProgramiUI()
    ui.show()
    sys.exit(app.exec_())
