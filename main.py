import sys
import random
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
        self.dersler.append({"kod": ders_adi, "online": 0, "sinif": int(ders_sinifi), "sure": int(ders_suresi)})
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
        ders_programi = {}

        renkler = [
            '#FFD1DC', '#C5CAE9', '#FF9AA2', '#B3E5FC', '#98F6DA',
            '#D5D387', '#DCE775', '#FF4B65', '#80CBC4', '#8CA8F5',
            '#D1C4E9', '#FFB7B2', '#A69079', '#CAB6B6', '#B2DFDB',
            '#8FF792', '#957A68', '#FFF9C4', '#81D4FA', '#FFE0B2',
            '#FFCCBC', '#D7CCC8', '#F5F5F5', '#E0E0E0', '#CFD8DC',
            '#E1BEE7', '#FFAB91', '#FFCC80', '#CEC7C8', '#FFEB3B',
            '#FF3A59', '#A5D6A7', '#FFECB3', '#CE93D8', '#FF8A80'
        ]
        renk_index = 0

        for ders in cizelge:
            sinif = ders['sinif']
            gun = ders['gun']
            saat = ders['saat']
            sure = ders['sure']

            if sinif not in ders_programi:
                ders_programi[sinif] = {}
            if gun not in ders_programi[sinif]:
                ders_programi[sinif][gun] = {}
            if saat not in ders_programi[sinif][gun]:
                ders_programi[sinif][gun][saat] = []

            ders_programi[sinif][gun][saat].append(ders)

        writer = pd.ExcelWriter(dosya_adi, engine='xlsxwriter')
        workbook = writer.book
        saat_araligi = [f"{h}:00" for h in range(9, 17)]

        for sinif, sinif_dersler in ders_programi.items():
            worksheet = workbook.add_worksheet(f"Sınıf {sinif}")
            writer.sheets[f"Sınıf {sinif}"] = worksheet

            # Sütun başlıkları
            for col_index, gun in enumerate(["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]):
                worksheet.write(0, col_index + 1, gun)

            # Saat satır başlıkları
            for row_index, saat in enumerate(saat_araligi):
                worksheet.write(row_index + 1, 0, saat)

            for gun_index, gun in enumerate(["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]):
                if gun in sinif_dersler:
                    for saat, ders_listesi in sinif_dersler[gun].items():
                        row_index = saat - 9 + 1  # Saat aralığını satır indeksine çevir
                        for ders_index, ders in enumerate(ders_listesi):
                            col_index = gun_index + 1  # Gün sütun indeksine çevir

                            # Sıralı renk seçimi
                            cell_format = workbook.add_format({
                                'bg_color': renkler[renk_index % len(renkler)],
                                'border': 1,
                                'align': 'center',
                                'valign': 'vcenter'
                            })
                            renk_index += 1

                            if ders['sure'] == 3:
                                worksheet.write(row_index, col_index, f"{ders['ders_kodu']} {ders['ders']}", cell_format)
                                worksheet.write(row_index + 1, col_index, ders['ogretmen'], cell_format)
                                worksheet.write(row_index + 2, col_index, f"{ders['derslik']}", cell_format)
                            elif ders['sure'] == 2:
                                worksheet.write(row_index, col_index, f"{ders['ders_kodu']} {ders['ders']} - {ders['derslik']}", cell_format)
                                worksheet.write(row_index + 1, col_index, ders['ogretmen'], cell_format)
                            elif ders['sure'] == 1:
                                worksheet.write(row_index, col_index, f"{ders['ders_kodu']} {ders['ders']} -  {ders['derslik']} - {ders['ogretmen']}", cell_format)

        writer.close()
        print(f"{dosya_adi} dosyasına yazıldı.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = DersProgramiUI()
    ui.show()
    sys.exit(app.exec_())