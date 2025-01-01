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
        writer = pd.ExcelWriter(dosya_adi, engine='xlsxwriter')
        workbook = writer.book

        saat_araligi = [f"{h}:00-{h + 1}:00" for h in range(9, 17)]  # Saat aralığı
        gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]  # Günler

        for sinif in range(1, 5):
            # Her sınıf için ayrı filtreleme
            sinif_cizelgesi = [row for row in cizelge if row["sinif"] == sinif]

            # Eğer bu sınıf için çizelge yoksa sayfayı boş bırak
            if not sinif_cizelgesi:
                continue

            # Boş bir pivot tablo oluştur
            df_pivot = pd.DataFrame(index=saat_araligi, columns=gunler).fillna("")

            for row in sinif_cizelgesi:
                saat_index = f"{row['saat']}:00-{row['saat'] + 1}:00"
                ders_bilgisi = (
                    f"{row['ders_kodu']}\n"
                    f"{row['derslik']}\n"
                    f"{row['ogretmen']}"
                )
                if row["gun"] in df_pivot.columns and saat_index in df_pivot.index:
                    df_pivot.loc[saat_index, row["gun"]] = ders_bilgisi

            # Excel sayfasına pivot tabloyu yaz
            df_pivot.to_excel(writer, sheet_name=f"{sinif}. Sınıf")
            worksheet = writer.sheets[f"{sinif}. Sınıf"]

            # Hücre formatlarını ayarla
            cell_format = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
            worksheet.set_column('B:F', 20, cell_format)  # Sütun genişliğini ayarla

        writer.close()
        print(f"{dosya_adi} dosyasına yazıldı.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = DersProgramiUI()
    ui.show()
    sys.exit(app.exec_())