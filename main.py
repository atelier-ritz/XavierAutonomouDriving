#!/usr/bin/env python
import sys
from callbacks import GUI
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
    
    
    
    
