#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget

from src import *

class DrawArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setToolTip('This is a Draw Area!')
        self.reset()
        self.show()

    def reset(self):
        self.points = []
        self.figures = []
        self.last_point = None
        self.drawling = False
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        self.draw_figures(qp)
        qp.end()

    def draw_points(self, qp):
        pen = QPen(Qt.red)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(5)
        qp.setPen(pen)

        for point in self.points:
            qp.drawPoint(point)

    def draw_figures(self, qp):
        for fig in self.figures:
            fig.render(qp)

    def mousePressEvent(self, event):
        border_color = self.parent.sidebar.border_color_btn.color()
        bg_color = self.parent.sidebar.bg_color_btn.color()

        if not self.drawling:
            self.points = []
            self.update()
            self.drawling = True

        self.points.append(event.pos())
        if self.parent.active == Polygon.name():
            if len(self.points) == self.parent.num:
                self.figures.append(Polygon(self.points, border_color, bg_color))
                self.drawling = False
        elif len(self.points) > 2 and self.parent.active == PolyLine.name():
            if len(self.points) <= self.parent.num:
                self.figures[-1].add_segment(LineSegment(self.points[-2], self.points[-1], border_color))
            if len(self.points) == self.parent.num:
                self.drawling = False
        elif len(self.points) == 2:
            if self.parent.active == LineSegment.name():
                self.figures.append(LineSegment(*self.points, border_color))
            elif self.parent.active == Ray.name():
                self.figures.append(Ray(*self.points, border_color))
            elif self.parent.active == Line.name():
                self.figures.append(Line(*self.points, self.geometry(), border_color))
            elif self.parent.active == Circle.name():
                self.figures.append(Circle(*self.points, border_color, bg_color))
            elif self.parent.active == PolyLine.name():
                self.figures.append(PolyLine([LineSegment(*self.points, border_color)]))
                self.update()
                return
            elif self.parent.active == Polygon.name():
                self.figures.append(Polygon([LineSegment(*self.points, border_color)]))
                self.update()
                return
            else:
                self.update()
                return
            self.drawling = False
        elif len(self.points) == 3:
            if self.parent.active == Ellipse.name():
                self.figures.append(Ellipse(*self.points, border_color, bg_color))
            else:
                self.update()
                return
            self.drawling = False
        if len(self.points) >= self.parent.num:
            pass

        self.update()
