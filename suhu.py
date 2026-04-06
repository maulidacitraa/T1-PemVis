import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                                QLabel, QLineEdit, QPushButton, QFrame, QMessageBox)
from PySide6.QtCore import Qt

class KonversiSuhuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.setFixedSize(450, 480)
        self.setStyleSheet("background-color: #f8f9fa;")

        layout_utama = QVBoxLayout()
        layout_utama.setContentsMargins(25, 20, 25, 25)
        layout_utama.setSpacing(15)

        self.lbl_header = QLabel("KONVERSI SUHU")
        self.lbl_header.setAlignment(Qt.AlignCenter)
        self.lbl_header.setFixedHeight(60)
        self.lbl_header.setStyleSheet("""
            background-color: #3498db;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 5px;
        """)

        self.lbl_instruksi = QLabel("Masukkan Suhu (Celsius):")
        self.lbl_instruksi.setStyleSheet("font-size: 14px; color: #333;")

        self.input_celsius = QLineEdit()
        self.input_celsius.setPlaceholderText("Contoh: 100")
        self.input_celsius.setFixedHeight(45)
        self.input_celsius.setStyleSheet("""
            QLineEdit {
                border: 1.5px solid #2ecc71;
                border-radius: 6px;
                padding: 5px 10px;
                font-size: 16px;
                background-color: #f0fff4;
            }
        """)

        layout_tombol = QHBoxLayout()
        layout_tombol.setSpacing(10)

        self.btn_fahrenheit = self.buat_tombol("Fahrenheit")
        self.btn_kelvin = self.buat_tombol("Kelvin")
        self.btn_reamur = self.buat_tombol("Reamur")

        layout_tombol.addWidget(self.btn_fahrenheit)
        layout_tombol.addWidget(self.btn_kelvin)
        layout_tombol.addWidget(self.btn_reamur)

        self.frame_hasil = QFrame()
        self.frame_hasil.setFixedHeight(120)
        self.frame_hasil.setStyleSheet("""
            QFrame {
                background-color: #d1e9ff;
                border-left: 5px solid #004a99;
                border-radius: 8px;
            }
        """)
        
        layout_hasil_internal = QVBoxLayout(self.frame_hasil)
        
        self.lbl_judul_hasil = QLabel("Hasil Konversi:")
        self.lbl_judul_hasil.setStyleSheet("font-weight: bold; font-size: 14px; color: #004a99; border: none;")
        
        self.lbl_teks_hasil = QLabel("-")
        self.lbl_teks_hasil.setStyleSheet("font-size: 15px; color: #333; border: none;")
        self.lbl_teks_hasil.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout_hasil_internal.addWidget(self.lbl_judul_hasil)
        layout_hasil_internal.addWidget(self.lbl_teks_hasil)

        self.btn_fahrenheit.clicked.connect(lambda: self.hitung("F"))
        self.btn_kelvin.clicked.connect(lambda: self.hitung("K"))
        self.btn_reamur.clicked.connect(lambda: self.hitung("R"))

        layout_utama.addWidget(self.lbl_header)
        layout_utama.addWidget(self.lbl_instruksi)
        layout_utama.addWidget(self.input_celsius)
        layout_utama.addLayout(layout_tombol)
        layout_utama.addSpacing(10)
        layout_utama.addWidget(self.frame_hasil)
        layout_utama.addStretch()

        self.setLayout(layout_utama)

    def buat_tombol(self, teks):
        tombol = QPushButton(teks)
        tombol.setFixedHeight(50)
        tombol.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 6px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f6391;
            }
        """)
        return tombol

    def hitung(self, tipe):
        try:
            celsius = float(self.input_celsius.text().replace(',', '.'))
            
            if tipe == "F":
                hasil = (celsius * 9/5) + 32
                satuan = "Fahrenheit"
            elif tipe == "K":
                hasil = celsius + 273.15
                satuan = "Kelvin"
            else: 
                hasil = celsius * 4/5
                satuan = "Reamur"

            self.lbl_teks_hasil.setText(f"{celsius} Celsius = {hasil:,.2f} {satuan}")
        
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Silakan masukkan angka suhu yang valid!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhuApp()
    window.show()
    sys.exit(app.exec())