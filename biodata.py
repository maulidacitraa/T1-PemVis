import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                                QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QFrame)
from PySide6.QtCore import Qt

class FormMahasiswa(QWidget):
    """Jendela utama untuk input biodata mahasiswa."""

    def __init__(self):
        super().__init__()
        self.konfigurasi_antarmuka()
        self.inisialisasi_sinyal()

    def konfigurasi_antarmuka(self):
        """Menyusun komponen UI dan styling."""
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(400, 500)
        self.setMinimumSize(350, 450)
        
        self.atur_posisi_tengah()

        tata_letak_utama = QVBoxLayout()
        tata_letak_utama.setSpacing(12)
        tata_letak_utama.setContentsMargins(20, 20, 20, 20)

        self.label_nama = QLabel("Nama Lengkap:")
        self.edit_nama = QLineEdit()
        self.edit_nama.setPlaceholderText("Masukkan Nama Lengkap")

        self.label_nim = QLabel("NIM:")
        self.edit_nim = QLineEdit()
        self.edit_nim.setPlaceholderText("Masukkan NIM")
    
        self.label_kelas = QLabel("Kelas:")
        self.edit_kelas = QLineEdit()
        self.edit_kelas.setPlaceholderText("Contoh: TI-2A")
        
        self.label_gender = QLabel("Jenis Kelamin:")
        self.pilih_gender = QComboBox()
        self.pilih_gender.addItems(["-- Pilih Jenis Kelamin --", "Laki-laki", "Perempuan"])

        tata_letak_tombol = QHBoxLayout()
        self.tombol_submit = QPushButton("Tampilkan")
        self.tombol_clear = QPushButton("Reset")
        self.tombol_submit.setObjectName("btn_tampilkan")
        self.tombol_clear.setObjectName("btn_reset")
        
        tata_letak_tombol.addWidget(self.tombol_submit)
        tata_letak_tombol.addWidget(self.tombol_clear)
        tata_letak_tombol.addStretch()

        self.bingkai_hasil = QFrame()
        self.bingkai_hasil.setObjectName("result_frame")
        layout_hasil = QVBoxLayout(self.bingkai_hasil)
        
        self.teks_output = QLabel("")
        self.teks_output.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout_hasil.addWidget(self.teks_output)
        self.bingkai_hasil.setVisible(False)

        tata_letak_utama.addWidget(self.label_nama)
        tata_letak_utama.addWidget(self.edit_nama)
        tata_letak_utama.addWidget(self.label_nim)
        tata_letak_utama.addWidget(self.edit_nim)
        tata_letak_utama.addWidget(self.label_kelas)
        tata_letak_utama.addWidget(self.edit_kelas)
        tata_letak_utama.addWidget(self.label_gender)
        tata_letak_utama.addWidget(self.pilih_gender)
        tata_letak_utama.addLayout(tata_letak_tombol)
        tata_letak_utama.addSpacing(10)
        tata_letak_utama.addWidget(self.bingkai_hasil)
        tata_letak_utama.addStretch()

        self.setLayout(tata_letak_utama)
        self.terapkan_gaya_visual()

    def terapkan_gaya_visual(self):
        """Mengatur desain aplikasi melalui QSS."""
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
                font-size: 13px;
            }
            QLineEdit, QComboBox {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #28a745;
            }
            QPushButton#btn_tampilkan {
                background-color: #3498db;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                border: none;
            }
            QPushButton#btn_tampilkan:hover {
                background-color: #2980b9;
            }
            QPushButton#btn_reset {
                background-color: #95a5a6;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                border: none;
            }
            QPushButton#btn_reset:hover {
                background-color: #7f8c8d;
            }
            QFrame#result_frame {
                background-color: #d4edda;
                border-left: 4px solid #28a745;
                border-radius: 2px;
                padding: 5px;
            }
            QLabel {
                color: #333;
            }
        """)

    def inisialisasi_sinyal(self):
        """Menghubungkan event klik tombol ke fungsi terkait."""
        self.tombol_submit.clicked.connect(self.proses_tampilkan)
        self.tombol_clear.clicked.connect(self.proses_reset)

    def proses_tampilkan(self):
        """Validasi input dan mencetak data ke panel hasil."""
        val_nama = self.edit_nama.text().strip()
        val_nim = self.edit_nim.text().strip()
        val_kelas = self.edit_kelas.text().strip()
        val_jk = self.pilih_gender.currentText()
        index_jk = self.pilih_gender.currentIndex()

        if not val_nama or not val_nim or not val_kelas or index_jk == 0:
            QMessageBox.warning(self, "Peringatan", "Pastikan semua kolom terisi dengan benar!")
            return

        format_teks = (
            f"<b>DATA BIODATA</b><br><br>"
            f"Nama: {val_nama}<br>"
            f"NIM: {val_nim}<br>"
            f"Kelas: {val_kelas}<br>"
            f"Jenis Kelamin: {val_jk}"
        )
        
        self.teks_output.setText(format_teks)
        self.bingkai_hasil.setVisible(True)

    def proses_reset(self):
        """Membersihkan form input."""
        self.edit_nama.clear()
        self.edit_nim.clear()
        self.edit_kelas.clear()
        self.pilih_gender.setCurrentIndex(0)
        
        self.teks_output.clear()
        self.bingkai_hasil.setVisible(False)

    def atur_posisi_tengah(self):
        """Menempatkan aplikasi di tengah layar pengguna."""
        geo_layar = QApplication.primaryScreen().geometry()
        titik_x = (geo_layar.width() - self.width()) // 2
        titik_y = (geo_layar.height() - self.height()) // 2
        self.move(titik_x, titik_y)

if __name__ == "__main__":
    app_biodata = QApplication(sys.argv)
    form_utama = FormMahasiswa()
    form_utama.show()
    sys.exit(app_biodata.exec())