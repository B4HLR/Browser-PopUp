from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt, QTimer
import sys


app = QApplication(sys.argv) 
window = QMainWindow()
browser = QWebEngineView()

screen = app.primaryScreen()
geometry = screen.availableGeometry()

sizeX = int(geometry.width() * 0.2) # Define width as 20% of screen width
sizeY = int(geometry.height() * 0.2) # Define height as 20% of screen height


window.setFixedSize(sizeX, sizeY)
window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


url = QUrl("Link to your music page") # Just Work with YouTube Music or other websites is a POPup browser

browser.load(url)

def move_to_bottom_right():
    x = geometry.x() + geometry.width() - window.width()
    y = geometry.y() + geometry.height() - window.height()
    window.move(x, y)


QTimer.singleShot(0, move_to_bottom_right)
window.setCentralWidget(browser)
window.show()
sys.exit(app.exec())

