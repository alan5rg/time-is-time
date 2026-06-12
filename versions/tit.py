'''
(Time is Time v.1.0)
Descripción de funciones:

Cronómetro: Controlado por un QTimer, va incrementando el tiempo cada segundo y lo
    muestra en pantalla.

Una Hora Countdown: Puedes configurar un temporizador regresivo en minutos (de 1 a 60)
    al llegar a cero reproduce un sonido de alarma usando paplay.

Alarma Horaria: Configurás la hora en que querés que suene la alarma, cuando llega esa
    hora reproduce un sonido de alarma usando paplay.
'''
import sys
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTabWidget, QSpinBox, QTimeEdit)
from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtGui
import os
import qdarkstyle
from qdarkstyle import load_stylesheet, LightPalette, DarkPalette

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("tit v.1.0 (Time is Time)")
        self.setGeometry(100, 100, 445, 150)

        # Icono de aplicación
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   
        self.setWindowIcon(QtGui.QIcon(self.IconPath + os.path.sep + 'tit.png'))

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

        self.tabs.addTab(self.tab_cronometro, "Cronómetro")
        self.tabs.addTab(self.tab_countdown, "Una Hora Countdown")
        self.tabs.addTab(self.tab_alarma, "Alarma Horaria")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
        self.show()

    # Cronómetro
    def cronometro_ui(self):
        layout = QVBoxLayout()
        self.time_display = QLabel("00:00:00")
        layout.addWidget(self.time_display)
        
        hbox = QHBoxLayout()
        self.start_btn = QPushButton("Iniciar/Continuar")
        self.pause_btn = QPushButton("Pausar")
        self.reset_btn = QPushButton("Detener y Reiniciar")
        self.update_button_cronometro_states(start_enabled=True, pause_enabled=False, reset_enabled=False)

        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.pause_btn)
        hbox.addWidget(self.reset_btn)

        layout.addLayout(hbox)
        self.tab_cronometro.setLayout(layout)
        
        self.cronometro_timer = QTimer(self)
        self.cronometro_timer.timeout.connect(self.update_cronometro)
        self.time_elapsed = QTime(0, 0, 0)

        self.start_btn.clicked.connect(self.start_cronometro)
        self.pause_btn.clicked.connect(self.pause_cronometro)
        self.reset_btn.clicked.connect(self.reset_cronometro)
    
    def start_cronometro(self):
        self.cronometro_timer.start(1000)  # 1 segundo
        self.update_button_cronometro_states(start_enabled=False, pause_enabled=True, reset_enabled=True)

    def pause_cronometro(self):
        self.cronometro_timer.stop()
        self.update_button_cronometro_states(start_enabled=True, pause_enabled=False, reset_enabled=True)

    def reset_cronometro(self):
        self.cronometro_timer.stop()
        self.time_elapsed = QTime(0, 0, 0)
        self.time_display.setText("00:00:00")
        self.update_button_cronometro_states(start_enabled=True, pause_enabled=False, reset_enabled=False)

    def update_cronometro(self):
        self.time_elapsed = self.time_elapsed.addSecs(1)
        self.time_display.setText(self.time_elapsed.toString("hh:mm:ss"))
    
    def update_button_cronometro_states(self, start_enabled, pause_enabled, reset_enabled):
        self.start_btn.setDisabled(not start_enabled)
        self.pause_btn.setDisabled(not pause_enabled)
        self.reset_btn.setDisabled(not reset_enabled)

    # One Hour Minutes Countdown Timer
    def countdown_ui(self):
        self.not_on_pause = True
        layout = QVBoxLayout()
        self.countdown_display = QLabel("00:00")
        layout.addWidget(self.countdown_display)

        self.time_input = QSpinBox()
        self.time_input.setRange(1, 60)  # 1 minuto a 1 horas
        self.time_input.setSuffix(" min")
        layout.addWidget(self.time_input)

        hbox = QHBoxLayout()
        self.start_countdown_btn = QPushButton("Iniciar/Continuar")
        self.pause_countdown_btn = QPushButton("Pausar")
        self.reset_countdown_btn = QPushButton("Detener y Reiniciar")
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

    # Alarma Horaria
    def alarma_ui(self):
        layout = QVBoxLayout()
        self.alarma_time = QTimeEdit(QTime.currentTime())
        layout.addWidget(self.alarma_time)

        self.set_alarma_btn = QPushButton("Configurar Alarma")
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
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))
    ex = TimerApp()
    sys.exit(app.exec_())
