#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen


class Figure:
    def __init__(self, location=None, border_color=Qt.black):
        self.location = location
        self.border_color = border_color if border_color else Qt.black

    def render(self, qp):
        pass

    def get_pen(self):
        return QPen(self.get_border_color(), 2, Qt.SolidLine)

    def get_location(self):
        return self.location

    def set_location(self, value):
        self.location = value

    def get_border_color(self):
        return self.border_color

    def set_border_color(self, value):
        self.border_color = value
