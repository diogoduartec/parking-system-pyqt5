from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QBrush

import src.assets.styles.ListAutos as STYLES
from src.models.Vehicle import Vehicle

class ListAutos(QVBoxLayout):
    def __init__(self, vehicle_list):
        super().__init__()
        self.set_content(vehicle_list)
        self.button_delete = QPushButton('REGISTRAR SAÍDA DO VEÍCULO')
        self.button_delete.setStyleSheet(STYLES.button)
        self.addWidget(self.button_delete)

    def set_content(self, vehicle_list):
        self.list_autos = QListWidget()

        items = []
        for i in range(len(vehicle_list)):
            items.append(QListWidgetItem(vehicle_list[i]))
            self.list_autos.addItem(items[i])
            items[i].setForeground(QBrush(QColor('#FFFFFF')))

        self.addWidget(self.list_autos)
