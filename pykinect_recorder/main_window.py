import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QHBoxLayout, QMainWindow, QVBoxLayout, 
    QWidget, QTabWidget, QToolBar
)

from .renderer.components.toolbar import Toolbar
from .renderer.components.sidebar_tab import Sidebar
from .renderer.components.asidebar import Asidebar
from .renderer.components.viewer_sensors import SensorViewer
from .renderer.common_widgets import Label


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Azure Kinect Camera DK")
        self.setWindowIcon(QIcon(os.path.abspath("./renderer/public/kinect-sensor.ico")))
        self.initial_window()

    def initial_window(self) -> None:
        self.setFixedSize(1920, 1080)

        # toolbar
        self.toolbar = Toolbar()

        # frame Layout
        layout_frame = QHBoxLayout()
        layout_frame.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tab_sidebar = Sidebar()
        self.sensor_viewer = SensorViewer()
        self.asidebar = Asidebar()
        self.tab_sidebar.ToggleSign.connect(self.asidebar.toggle_hide)
        self.tab_sidebar.sidebar_explorer.Filepath.connect(self.sensor_viewer.playback)

        layout_frame.addWidget(self.tab_sidebar)
        layout_frame.addWidget(self.sensor_viewer)
        layout_frame.addWidget(self.asidebar)

        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_main.addWidget(self.toolbar)
        layout_main.addLayout(layout_frame)

        widget_main = QWidget(self)
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)
