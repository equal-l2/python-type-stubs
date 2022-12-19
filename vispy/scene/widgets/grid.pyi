from vispy.scene.widgets.widget import Widget

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.


import numpy as np

from vispy.geometry import Rect
from .widget import Widget
from .viewbox import ViewBox

from kiwisolver import Solver, Variable, UnsatisfiableConstraint

class Grid(Widget):
    def __init__(self, spacing: int = 6, **kwargs): ...
    def __getitem__(self, idxs): ...
    def add_widget(
        self,
        widget: None | Widget = None,
        row: int | None = None,
        col: int | None = None,
        row_span: int = 1,
        col_span: int = 1,
        **kwargs
    ): ...
    def remove_widget(self, widget: Widget): ...
    def resize_widget(self, widget: Widget, row_span: int, col_span: int): ...
    def _prepare_draw(self, view): ...
    def add_grid(
        self,
        row: int | None = None,
        col: int | None = None,
        row_span: int = 1,
        col_span: int = 1,
        **kwargs
    ): ...
    def add_view(
        self,
        row: int | None = None,
        col: int | None = None,
        row_span: int = 1,
        col_span: int = 1,
        **kwargs
    ): ...
    def next_row(self): ...
    @property
    def grid_size(self): ...
    @property
    def layout_array(self): ...
    def __repr__(self): ...
    @staticmethod
    def _add_total_width_constraints(solver, width_grid, _var_w): ...
    @staticmethod
    def _add_total_height_constraints(solver, height_grid, _var_h): ...
    @staticmethod
    def _add_gridding_width_constraints(solver, width_grid): ...
    @staticmethod
    def _add_gridding_height_constraints(solver, height_grid): ...
    @staticmethod
    def _add_stretch_constraints(
        solver, width_grid, height_grid, grid_widgets, widget_grid
    ): ...
    @staticmethod
    def _add_widget_dim_constraints(
        solver, width_grid, height_grid, total_var_w, total_var_h, grid_widgets
    ): ...
    def _recreate_solver(self): ...
    def _update_child_widget_dim(self): ...
    @property
    def _widget_grid(self): ...
