#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget

from ui.DrawArea import DrawArea
from ui.SideBar import SideBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.draw_area = DrawArea(self)
        self.sidebar = SideBar(self)
        self.init_widgets()

    def init_widgets(self):
        self.setWindowTitle('Paint')
        self.setGeometry(150, 100, 900, 600)
        self.setFixedSize(self.size())

        self.sidebar.resize(300, self.size().height())

        self.draw_area.move(170, 0)
        self.draw_area.resize(self.size())

        self.show()
