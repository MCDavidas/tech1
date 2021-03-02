from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import QPoint

from src.PolyLine import PolyLine
from src.Figure import Figure


class Polygon(PolyLine, Figure):
    def __init__(self, segments=[], border_color=Qt.black, bg_color=Qt.black):
        PolyLine.__init__(self, segments)
        Figure.__init__(self, None, border_color)
        self.bg_color = bg_color

    @staticmethod
    def name():
        return 'Polygon'

    def get_bg_color(self):
        return self.bg_color

    def set_bg_color(self, value):
        self.bg_color = value

    def render(self, qp):
        qp.setPen(self.get_pen())
        qp.setBrush(self.get_bg_color())

        points = QPolygon([elem for elem in self.segments])

        qp.drawPolygon(points)
