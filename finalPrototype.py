import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import os
import sys
import time
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PacketCaptureThread(QThread):
    packet_received = pyqtSignal(object)
    #scan_requested = pyqtSignal(str)
    

    def __init__(self):
        QThread.__init__(self)
        self.pathName=''
    
    def run(self):
        #sniff(filter="arp", prn=self.handle_packet, store=0)    
        self.command = "inotifywait -m -e modify,delete --format '%w %f' "+ self.pathName
        self.process = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = self.process.stdout.readline()
        self.handle_packet(output)

    def handle_packet(self, packet):
        output=packet.strip()
        self.packet_received.emit(output)

    def assignePathname(self,name):
        self.pathName=name

class Widget(QMainWindow):
    # On click functions
    def __init__(self):
        super().__init__()
        loadUi("gui.ui", self)
        self.packet_capture_thread = PacketCaptureThread()
        self.monitor.clicked.connect(self.start)
        self.delete2.clicked.connect(self.deletion)
        #self.delete2.clicked.connect(self.deletion)
        #self.event_handler = Widget()
        self.path = sys.argv[1] if len(sys.argv) > 1 else '.'
        
                
    def start(self):
        self.pathName = self.lineEdit2.text()
        self.textEdit1.append("[*] Monitoring initiated in the path "+ self.pathName)
        
        self.packet_capture_thread.assignePathname(self.pathName)
        self.packet_capture_thread.packet_received.connect(self.detection)
        self.packet_capture_thread.start()

    def detection(self,packet):
        self.pathName = self.lineEdit2.text()
        if packet:
            #print(packet)
            st=str(packet)
            self.textEdit1.append(st)
            command = "./detect2.sh "+self.pathName
            #print(command)
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            #print(result.stdout)
            #print(result.stderr)
            #print(result.stdout)
            self.textEdit2.append(result.stdout)
            self.textEdit2.append(result.stderr)
            command = "./detect2.sh "+ self.pathName +" | awk '$2 ~ /\.py$/ {print $2}' | awk 'FNR == 1 { print }'"
            #print(command)
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip()

            #print(output)
            self.lineEdit.setText(output)
    def deletion(self):
        self.fileName=self.lineEdit.text()
        self.textEdit1.append("Deleting file ransomware file"+self.fileName)
        os.remove(self.fileName)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Widget()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(903)
    widget.setFixedHeight(674)
    widget.show()
    app.exec_()
    
