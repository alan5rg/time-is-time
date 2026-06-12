# -*- coding: utf-8 -*-
#tit.NG66.Ei2C.py
# Monkey Python Coding Circus by ALan RG.Systemas & Team Cangurera
"""
una lección de elegancia al mismísimo Papa Gregorio XIII
🦎🕰️🗓️🚀🔥🧉
"""
# ROOT CAUSE ANALYSIS
#
# Hipótesis inicial:
#   - Qt renderiza lento
#   - Python es lento
#   - El segundero consume CPU
#   - La transparencia rompe el espacio-tiempo
#
# Diagnóstico final:
#   Falta de Geckonismo™
# (todo lo demas es puro Mito de loros que repiten burradas)
#
# Solución:
#   (╯°□°）╯︵ ┻━┻
# (chau consultas a la web...)
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

geckoappversion = "v.NG66.Ei2C"

class TimeThread(QThread):
    """
    Al sacar el lazo del tiempo del hilo principal de la interfaz,
    nos aseguramos de que el renderizado no se ahogue,
    eliminando ese mito de que "Python o Qt son lentos.
    """
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

class TimeisTime(QWidget):
    def __init__(self):
        super().__init__()
        self.version = (f"TiT {geckoappversion} (Time is Time)")
        self.setWindowTitle(self.version)
        self.setGeometry(100, 100, 800, 340)
        #self.setFixedSize(640, 340)
        
        # Icono de aplicación
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   
        self.setWindowIcon(QtGui.QIcon(self.IconPath + os.path.sep + 'tit.png'))

        # El Delorean arranca clavado en el "Presente" de la máquina
        self.current_calendar_year = datetime.now().year
        self.current_calendar_month = datetime.now().month
        
        # Especial UI transparente
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # siempre arriba
        self.setAttribute(Qt.WA_TranslucentBackground)  # Fondo transparente
        
        # Hacer que los widgets sean transparentes
        self.transparent_palette = QtGui.QPalette()
        self.transparent_palette.setColor(QtGui.QPalette.Base, Qt.transparent)
        self.transparent_palette.setColor(QtGui.QPalette.Window, Qt.transparent)
        self.setPalette(self.transparent_palette)

        # Aplicar estilos 
        self.setStyleSheet("""
            QWidget {
                background: transparent;
            }
            QSpinBox {
                font-family: "Arial";
                font-size: 96pt;
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
                font-size: 96pt;
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
                font-size: 96pt;
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

        # Iniciamos la Interfaz de Usuario
        self.initUI()
    
    def initUI(self):
        """ Interfaz de Usuario basada en QTabWidget"""

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
            self.tabs.widget(i).setPalette(self.transparent_palette)
        
        # Aplicar transparencia a otros widgets
        self.setStyleSheet("""
            QLabel, QSpinBox, QTextEdit, QLineEdit, QTimeEdit, QPushButton {
                background: transparent;
                border: none;
            }
        """)
        
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # siempre arriba
        self.show()

    # ********************************************************************************
    # *** Cronómetro *****************************************************************
    # ********************************************************************************
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

    # ********************************************************************************
    # *** One Hour Minutes Countdown Timer *******************************************
    # ********************************************************************************
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

    # ********************************************************************************
    # *** Alarma Horaria *************************************************************
    # ********************************************************************************
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

    # ********************************************************************************
    # *** Hora Actual ****************************************************************
    # ********************************************************************************
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
        self.frase_timer.start(8000)  # 10,000 ms = 10 segundos

        # Primera frase al iniciar
        self.update_frase()
    
    def update_hora(self, current_time, current_date):
        #NOva Fix 02/03/26 12:51
        self.hora_display.setText(current_time)
        self.date_display.setText(current_date)
        self.setWindowTitle(f"{current_date} | {current_time} | {self.version}")

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
        """ Eliminamos la Frase porque genera Lagueos horribles"""
        #time.sleep(0.233)
        #frase = self.obtener_frase()
        #self.frase_display.setText(f"@ {frase}")
        self.frase_display.setText("(╯°□°）╯︵ ┻━┻")

    # ********************************************************************************
    # *** Calendario Ei2 *************************************************************
    # ********************************************************************************
    def mes_calendario_ui(self):
        """
        "El calendario es una danza cósmica entre el tiempo y la eternidad,
            un reflejo de nuestro intento por ordenar lo infinito.
        Cada mes encierra sus misterios númericos en la matriz elemental del universo de las causalidades..."
        
        Y ahora podemos viajar a cualquier año del multiverso con un par de clicks
        y saber si es Lunes, Miércoles o Juernes ⏪◀🕰️▶⏩🦎
        """
        layout = QVBoxLayout()
        
        # --- 🚀 CONTROL DE TRANSPORTE TEMPORAL (La botonera del Delorean) ---
        transport_layout = QHBoxLayout()
        
        btn_year_prev = QPushButton('⏪ Año')
        btn_month_prev = QPushButton('◀ Mes')
        
        self.line_edit_mes = QLineEdit(self)
        self.line_edit_mes.setReadOnly(True)
        self.line_edit_mes.setAlignment(Qt.AlignCenter) # Centrado para que quede simétrico
        
        btn_month_next = QPushButton('Mes ▶')
        btn_year_next = QPushButton('Año ⏩')
        
        # Conexiones chamánicas a la lógica de salto temporal
        btn_year_prev.clicked.connect(lambda: self.navigate_calendar(year_delta=-1))
        btn_month_prev.clicked.connect(lambda: self.navigate_calendar(month_delta=-1))
        btn_month_next.clicked.connect(lambda: self.navigate_calendar(month_delta=1))
        btn_year_next.clicked.connect(lambda: self.navigate_calendar(year_delta=1))
        
        # Ensamblamos la fila de control
        transport_layout.addWidget(btn_year_prev)
        transport_layout.addWidget(btn_month_prev)
        transport_layout.addWidget(self.line_edit_mes, stretch=1) # El texto se expande en el centro
        transport_layout.addWidget(btn_month_next)
        transport_layout.addWidget(btn_year_next)
        # ---------------------------------------------------------------------

        self.table_view = QTableView(self)
        self.table_view.setFixedSize(710, 215) # Ajustamos apenas el alto para darle aire a los botones
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Agregamos los bloques al layout principal
        layout.addLayout(transport_layout)
        layout.addWidget(self.table_view)
        self.tab_mes_calendario.setLayout(layout)

        self.update_calendar()

    def navigate_calendar(self, year_delta=0, month_delta=0):
        """ Maneja el salto cuántico en los meses y años calculando los desbordes """
        self.current_calendar_year += year_delta
        self.current_calendar_month += month_delta
        
        # Control de desborde matemático:
        # Si retrocedemos del mes 1 (Enero), pasamos al mes 12 (Diciembre) del año anterior
        if self.current_calendar_month < 1:
            self.current_calendar_month = 12
            self.current_calendar_year -= 1
        # Si avanzamos del mes 12 (Diciembre), pasamos al mes 1 (Enero) del año siguiente
        elif self.current_calendar_month > 12:
            self.current_calendar_month = 1
            self.current_calendar_year += 1
            
        self.update_calendar()

    def update_calendar(self):
        # 🦎 Desacoplado: Ahora leemos el estado del Delorean
        # el Trasport que rompe el continuo espacio-tiempo con elegancia
        año = self.current_calendar_year
        mes = self.current_calendar_month
        
        # El día real de HOY solo lo usamos para pintar el casillero si estamos parados en el mes presente
        now = datetime.now()
        real_year, real_month, real_day = now.year, now.month, now.day
        
        # Obtener el nombre del mes (¡Ojo! calendar.month_name a veces viene en inglés por defecto, 
        # pero con el formateo de DataFrame en español queda hermoso en los headers)
        nombre_mes = f"{calendar.month_name[mes].capitalize()} {año}"
        self.line_edit_mes.setText(nombre_mes)

        # Obtener la matriz del calendario basada en las variables de navegación
        calendario = calendar.monthcalendar(año, mes)
        
        # Convertir a DataFrame con encabezados
        df = pd.DataFrame(calendario, columns=["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"])
        df = df.replace(0, '')  # Estética Geckónica

        # Crear el modelo para QTableView
        model = QStandardItemModel(df.shape[0], df.shape[1])
        model.setHorizontalHeaderLabels(df.columns)
        
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                dia_celda = df.iat[row, col]
                item = QStandardItem(str(dia_celda))
                model.setItem(row, col, item)

                # Respeto absoluto al Presente del GeckoPS (Unica coordenada espacio-tiempo en dónde realmente vivimos):
                # 🎯 Pintar el día actual SÓLO si el viaje temporal coincide con el "Presente Real"
                if dia_celda == real_day and año == real_year and mes == real_month:
                    item.setBackground(QColor('#259ae9')) # Celeste clásico de foco
                    item.setForeground(QColor('white'))   # Texto blanco para que resalte
        
        self.table_view.setModel(model)
 
    # ********************************************************************************
    # *** Donar **********************************************************************
    # ********************************************************************************
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
    ex = TimeisTime()
    sys.exit(app.exec_())

