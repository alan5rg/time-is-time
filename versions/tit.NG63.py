import sys
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTabWidget, QSpinBox, QTimeEdit)
from PyQt5.QtWidgets import QTextEdit, QTableView, QAbstractItemView
from PyQt5.QtCore import QTimer, QTime, QThread, pyqtSignal, QDate
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QColor
import requests
import calendar
from datetime import datetime
import random
import os
import qdarkstyle
from qdarkstyle import load_stylesheet, DarkPalette
import pandas as pd

class TimeThread(QThread):
    update_time_signal = pyqtSignal(str, str)  # Now emits two strings

    def run(self):
        while True:
            current_time = QTime.currentTime().toString("hh:mm:ss")
            current_date = QDate.currentDate()
            day_name = current_date.toString("dddd")[:3]  # Abbreviated day name
            day_number = current_date.day()
            month_name = current_date.toString("MMMM")[:3]  # Abbreviated month name
            date_string = f"{day_name} {day_number} {month_name}."
            self.update_time_signal.emit(current_time, date_string)
            time.sleep(1)

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("tit.NG63 (Time is Time)")
        self.setGeometry(100, 100, 800, 340)
        #self.setFixedSize(640, 340)
        
        # Icono de aplicación
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   
        self.setWindowIcon(QtGui.QIcon(self.IconPath + os.path.sep + 'tit.png'))

        # Especial UI transparente
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # siempre arriba
        self.setAttribute(Qt.WA_TranslucentBackground)  # Fondo transparente
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # Clicks pasan a través de la parte transparente

        # Hacer que los widgets sean transparentes
        transparent_palette = QtGui.QPalette()
        transparent_palette.setColor(QtGui.QPalette.Base, Qt.transparent)
        transparent_palette.setColor(QtGui.QPalette.Window, Qt.transparent)
        self.setPalette(transparent_palette)

        # Aplicar estilos 
        self.setStyleSheet("""
            QWidget {
                background: transparent;
            }
            QSpinBox {
                font-family: "Arial";
                font-size: 46pt;
                font-weight: bold;
                color: white;
                background-color: #333;
                border: 1px solid #444;
                padding: 5px;
            }
            QLabel {
                background: transparent;
                border: none;
                font-family: "Arial";
                font-size: 46pt;
                font-weight: bold;
                color: white;
            }
            QTextEdit {
                font-size: 14pt;
                font-family: Arial;
                font-weight: bold;
                border: none;
                background: transparent;
            }
            QLineEdit {
                font-family: "Arial";
                font-size: 22pt;
                font-weight: bold;
                color: white;
                background-color: #333;
                border: 1px solid #444;
                padding: 5px;
                background: transparent;
                border: none;
            }
            QTimeEdit {
                font-family: "Arial";
                font-size: 46pt;
                font-weight: bold;
                color: white;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

        # Tabs (Pestañas)
        self.tabs = QTabWidget(self)
        
        # Tab Cronómetro
        self.tab_cronometro = QWidget()
        self.cronometro_ui()

        # Tab Countdown Timer
        self.tab_countdown = QWidget()
        self.countdown_ui()

        # Tab Alarma Horaria
        self.tab_alarma = QWidget()
        self.alarma_ui()

        # Tab Hora Actual
        self.tab_hora = QWidget()
        self.hora_ui()

        # Tab Mes Calendario
        self.tab_mes_calendario = QWidget()
        self.mes_calendario_ui()

        # Tab Donar
        self.tab_donar = QWidget()
        self.donar_ui()

        self.tabs.addTab(self.tab_cronometro, "Cronómetro")
        self.tabs.addTab(self.tab_countdown, "Una Hora Countdown")
        self.tabs.addTab(self.tab_alarma, "Alarma Horaria")
        self.tabs.addTab(self.tab_hora, "Hora Actual")
        self.tabs.addTab(self.tab_mes_calendario, "Mes Calendario")
        self.tabs.addTab(self.tab_donar, "Donar")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.tabs.setTabPosition(QTabWidget.South)

        self.tabs.setCurrentIndex(3)  # Seleccionar la pestaña "Hora Actual"

        self.tabs.setStyleSheet("QTabWidget::pane { background: transparent; border: none; }")
        self.tabs.setAttribute(Qt.WA_TranslucentBackground)
        # Aplicar transparencia a los widgets dentro de las pestañas
        for i in range(self.tabs.count()):
            self.tabs.widget(i).setAttribute(Qt.WA_TranslucentBackground)
            self.tabs.widget(i).setPalette(transparent_palette)

        
        # Aplicar transparencia a otros widgets
        self.setStyleSheet("""
            QLabel, QSpinBox, QTextEdit, QLineEdit, QTimeEdit, QPushButton {
                background: transparent;
                border: none;
            }
        """)
        
        self.show()

    # Cronómetro ********************************************************************************
    def cronometro_ui(self):
        self.tiempo = 0  # Décimas de segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizarTiempo)
        
        self.label = QLabel("00:00:00.0", self)
        self.boton_iniciar = QPushButton("Iniciar/Continuar", self)
        self.boton_detener = QPushButton("Detener", self)
        self.boton_reiniciar = QPushButton("Reiniciar", self)
        
        self.boton_iniciar.clicked.connect(self.iniciarCronometro)
        self.boton_detener.clicked.connect(self.detenerCronometro)
        self.boton_reiniciar.clicked.connect(self.reiniciarCronometro)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.boton_iniciar)
        layout.addWidget(self.boton_detener)
        layout.addWidget(self.boton_reiniciar)
        self.setLayout(layout)

        self.tab_cronometro.setLayout(layout)
        
    def iniciarCronometro(self):
        if not self.timer.isActive():
            self.timer.start(100)  # Cada 100 ms (décima de segundo)
        
    def detenerCronometro(self):
        self.timer.stop()
        
    def reiniciarCronometro(self):
        self.timer.stop()
        self.tiempo = 0
        self.actualizarEtiqueta()
        
    def actualizarTiempo(self):
        self.tiempo += 1
        self.actualizarEtiqueta()
        
    def actualizarEtiqueta(self):
        horas = (self.tiempo // 36000) % 24
        minutos = (self.tiempo // 600) % 60
        segundos = (self.tiempo // 10) % 60
        decimas = self.tiempo % 10
        self.label.setText(f"{horas:02}:{minutos:02}:{segundos:02}.{decimas}")

    # One Hour Minutes Countdown Timer ********************************************************************************
    def countdown_ui(self):
        self.not_on_pause = True
        layout = QVBoxLayout()
        self.countdown_display = QLabel("00:00")
        layout.addWidget(self.countdown_display)

        self.time_input = QSpinBox()
        self.time_input.setRange(1, 60)  # 1 minuto a 1 hora
        self.time_input.setSuffix(" min")
        layout.addWidget(self.time_input)

        hbox = QHBoxLayout()
        self.start_countdown_btn = QPushButton("Iniciar/Continuar", self)
        self.pause_countdown_btn = QPushButton("Pausar", self)
        self.reset_countdown_btn = QPushButton("Detener y Reiniciar", self)
        self.update_button_countdown_states(start_enabled=True, pause_enabled=False, reset_enabled=False)

        hbox.addWidget(self.start_countdown_btn)
        hbox.addWidget(self.pause_countdown_btn)
        hbox.addWidget(self.reset_countdown_btn)

        layout.addLayout(hbox)
        self.tab_countdown.setLayout(layout)

        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.remaining_time = 0

        self.start_countdown_btn.clicked.connect(self.start_countdown)
        self.pause_countdown_btn.clicked.connect(self.pause_countdown)
        self.reset_countdown_btn.clicked.connect(self.reset_countdown)
    
    def start_countdown(self):
        if self.not_on_pause:
            self.remaining_time = self.time_input.value() * 60
        self.countdown_timer.start(1000)
        self.time_input.setDisabled(True)
        self.update_button_countdown_states(start_enabled=False, pause_enabled=True, reset_enabled=True)

    def pause_countdown(self):
        self.countdown_timer.stop()
        self.not_on_pause = False
        self.update_button_countdown_states(start_enabled=True, pause_enabled=False, reset_enabled=True)

    def reset_countdown(self):
        self.countdown_timer.stop()
        self.stop_countdown()

    def update_countdown(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            mins, secs = divmod(self.remaining_time, 60)
            self.countdown_display.setText(f"{mins:02}:{secs:02}")
        else:
            self.countdown_timer.stop()
            os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")
            self.stop_countdown()

    def stop_countdown(self):
        self.countdown_display.setText("00:00")
        self.remaining_time = 0
        self.not_on_pause = True
        self.time_input.setDisabled(False)
        self.update_button_countdown_states(start_enabled=True, pause_enabled=False, reset_enabled=False)
    
    def update_button_countdown_states(self, start_enabled, pause_enabled, reset_enabled):
        self.start_countdown_btn.setDisabled(not start_enabled)
        self.pause_countdown_btn.setDisabled(not pause_enabled)
        self.reset_countdown_btn.setDisabled(not reset_enabled)

    # Alarma Horaria ********************************************************************************
    def alarma_ui(self):
        layout = QVBoxLayout()
        self.alarma_time = QTimeEdit(QTime.currentTime())
        layout.addWidget(self.alarma_time)

        self.set_alarma_btn = QPushButton("Configurar Alarma", self)
        layout.addWidget(self.set_alarma_btn)
        
        self.tab_alarma.setLayout(layout)

        self.alarma_timer = QTimer(self)
        self.alarma_timer.timeout.connect(self.check_alarma)

        self.set_alarma_btn.clicked.connect(self.start_alarma)

    def start_alarma(self):
        self.alarma_timer.start(1000)
        self.alarma_time.setDisabled(True)
        self.set_alarma_btn.setText("Eliminar Alarma")
        self.set_alarma_btn.clicked.disconnect()
        self.set_alarma_btn.clicked.connect(self.delete_alarma)

    def check_alarma(self):
        current_time = QTime.currentTime().toString("hh:mm")
        set_time = self.alarma_time.time().toString("hh:mm")
        if current_time == set_time:
            self.alarma_timer.stop()
            os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")
            self.stop_alarma()    

    def delete_alarma(self):
        self.alarma_timer.stop()
        self.stop_alarma()

    def stop_alarma(self):
        self.alarma_time.setDisabled(False)
        self.set_alarma_btn.setText("Configurar Alarma")
        self.set_alarma_btn.clicked.disconnect()
        self.set_alarma_btn.clicked.connect(self.start_alarma)

    # Hora Actual ********************************************************************************
    def hora_ui(self):
        layout = QVBoxLayout()
        self.hora_display = QLabel("00:00:00")
        self.hora_display.setAlignment(Qt.AlignCenter)  
        self.date_display = QLabel("")  # New label for date
        self.date_display.setAlignment(Qt.AlignCenter)  
        self.frase_display = QTextEdit("Cargando frase...")  # Label para la frase
        self.frase_display.setReadOnly(True)  # No editable
        self.frase_display.setFixedHeight(60)  # Ajuste de altura (3 líneas aprox.)
        self.frase_display.setAlignment(Qt.AlignCenter)  
        layout.addWidget(self.hora_display)
        layout.addWidget(self.date_display)  # Add date label below time
        layout.addWidget(self.frase_display)
        self.tab_hora.setLayout(layout)

        # Iniciar hilo para actualizar la hora
        self.time_thread = TimeThread()
        self.time_thread.update_time_signal.connect(self.update_hora)
        self.time_thread.start()

        # Iniciar temporizador para actualizar la frase cada 30 segundos
        self.frase_timer = QTimer()
        self.frase_timer.timeout.connect(self.update_frase)
        self.frase_timer.start(10000)  # 10,000 ms = 10 segundos

        # Primera frase al iniciar
        self.update_frase()
    
    def update_hora(self, current_time):
        self.hora_display.setText(current_time)
    
    def update_hora(self, current_time, current_date):
        self.hora_display.setText(current_time)
        self.date_display.setText(current_date)

    # <Función para obtener una frase aleatoria>
    def obtener_frase(self):
        url = "https://zenquotes.io/api/random"
        try:
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                frase = respuesta.json()[0]['q']
                frase_es = self.traducir_frase(frase)
                return (f"{frase_es}")  # Retorna solo la frase
        except requests.RequestException:
            return "No se pudo obtener una frase."

    # <Función para traducir la frase al español con Google Translate>
    def traducir_frase(self, frase):
        time.sleep(0.033)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q={requests.utils.quote(frase)}"
        try:
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                traduccion = respuesta.json()[0][0][0]
                return traduccion
            else:
                return "No se pudo traducir la frase."
        except requests.RequestException:
            return "No se pudo traducir la frase."

    def update_frase(self):
        time.sleep(0.033)
        frase = self.obtener_frase()
        self.frase_display.setText(f"@ {frase}")

    # Calendario ********************************************************************************
    def mes_calendario_ui(self):
        layout = QVBoxLayout()
        
        self.line_edit_mes = QLineEdit(self)
        #self.line_edit_mes.setText("El calendario es una danza cósmica entre el tiempo y la eternidad, un reflejo de nuestro intento por ordenar lo infinito.Cada mes encierra sus misterios númericos en la matriz elemental del universo de las causalidades...")
        self.line_edit_mes.setReadOnly(True)

        self.table_view = QTableView(self)
        self.table_view.setFixedSize(710, 180)
        self.table_view.verticalHeader().setVisible(False)

        layout.addWidget(self.line_edit_mes)
        layout.addWidget(self.table_view)
        self.tab_mes_calendario.setLayout(layout)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.update_calendar()

    def update_calendar(self):
        # Obtener el mes y año actual
        now = datetime.now()
        año, mes, dia_actual = now.year, now.month, now.day
        
        # Obtener el nombre del mes
        nombre_mes = f"{calendar.month_name[mes]} {año}" #calendar.month_name[mes]
        self.line_edit_mes.setText(nombre_mes)

        # Obtener la matriz del calendario
        calendario = calendar.monthcalendar(año, mes)
        
        # Convertir a DataFrame con encabezados
        df = pd.DataFrame(calendario, columns=["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"])
        df = df.replace(0, '')  # Reemplazar ceros por strings vacíos para mejorar estética

        # Crear el modelo para QTableView
        model = QStandardItemModel(df.shape[0], df.shape[1])
        model.setHorizontalHeaderLabels(df.columns)
        
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QStandardItem(str(df.iat[row, col]))
                model.setItem(row, col, item)

                 # Seleccionar el día actual
                if df.iat[row, col] == dia_actual:
                    item.setBackground(QColor('#259ae9'))  # Color de fondo para el día actual (puedes cambiarlo)
        
        self.table_view.setModel(model)

    # Donar ********************************************************************************
    def donar_ui(self):
        layout = QVBoxLayout()
        self.texto_donar = QTextEdit("Envia USDT via red BEP20 a:")
        self.texto_donar.setAlignment(Qt.AlignCenter)  
        self.texto_donar.setReadOnly(True)  # No editable
        self.dir_usdt = QTextEdit("0x750346a0776d34af9ff407e55bec5d458cc9f755")  # Donate Address
        self.dir_usdt.setAlignment(Qt.AlignCenter)
        self.dir_usdt.setReadOnly(True)  # No editable
        layout.addWidget(self.texto_donar)
        layout.addWidget(self.dir_usdt)
        self.tab_donar.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))
    ex = TimerApp()
    sys.exit(app.exec_())


