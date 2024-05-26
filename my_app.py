from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
import requests, json


def find_weather():
    respons = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={text_box.toPlainText()}&appid=key&lang=ru&units=metric").json()
    result = ""
    result = result + "Город: " + str(respons["name"]) + '\n'
    result = result + "Состояние погоды: "
    result = result + "Текущая температура: " + str(respons["main"]["temp"]) + '°C' + '\n'
    result = result + "Температура ночью: " + str(respons["main"]["temp_min"]) + '°C' + '\n'
    result = result + "Температура днем: " + str(respons["main"]["temp_max"]) + '°C' + '\n'
    result = result + "Скорость ветра: " + str(respons["wind"]["speed"]) + ' км/ч' + '\n'
    result = result + "️Влажность " + str(respons["main"]["humidity"]) + '%' + '\n'
    result = result + "️Давление " + str(respons["main"]["pressure"]) + ' м.р.с.' + '\n'
    result_weather.setText(result)

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('погода')
mw.resize(500, 300)
mw.move(250, 250)

line = QVBoxLayout()
text_box = QTextEdit()
text_box.setFixedSize(250, 50)
button = QPushButton('Найти')
result_weather = QLabel('результат')

line.addWidget(text_box, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.addWidget(result_weather, alignment=Qt.AlignCenter)

mw.setLayout(line)

button.clicked.connect(find_weather)

mw.show()
app.exec_()
