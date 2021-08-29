# -*- coding: utf-8 -*-

"""
GUI file generated using Qt Designer and manual changes done extensively.
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # <-------------------- Main Window -------------------->
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/logo_final.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #071E3D;\n"
"color: rgb(33, 230, 193);\n"
"\n"
"")
        # <-------------------- Central Window -------------------->
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # <-------------------- Clockwise 90 deg rotation -------------------->
        self.button_shortcut_clockwise = QtWidgets.QPushButton(self.centralwidget)
        self.button_shortcut_clockwise.setGeometry(QtCore.QRect(930, 680, 31, 31))
        self.button_shortcut_clockwise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shortcut_clockwise.setToolTipDuration(-1)
        self.button_shortcut_clockwise.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_shortcut_clockwise.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/cw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shortcut_clockwise.setIcon(icon1)
        self.button_shortcut_clockwise.setObjectName("button_shortcut_clockwise")

        # <-------------------- Anticlockwise 90 deg rotation -------------------->
        self.button_shortcut_anticlockwise = QtWidgets.QPushButton(self.centralwidget)
        self.button_shortcut_anticlockwise.setGeometry(QtCore.QRect(890, 680, 31, 31))
        self.button_shortcut_anticlockwise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shortcut_anticlockwise.setToolTipDuration(-1)
        self.button_shortcut_anticlockwise.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_shortcut_anticlockwise.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/ccw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shortcut_anticlockwise.setIcon(icon2)
        self.button_shortcut_anticlockwise.setIconSize(QtCore.QSize(20, 20))
        self.button_shortcut_anticlockwise.setShortcut("")
        self.button_shortcut_anticlockwise.setObjectName("button_shortcut_anticlockwise")

        # <-------------------- Line to separate menu bar from MainWindow -------------------->
        self.menu_separator = QtWidgets.QFrame(self.centralwidget)
        self.menu_separator.setGeometry(QtCore.QRect(0, -10, 1191, 20))
        self.menu_separator.setStyleSheet("color: rgb(33, 230, 193);")
        self.menu_separator.setLineWidth(2)
        self.menu_separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.menu_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menu_separator.setObjectName("menu_separator")

        # <-------------------- QGraphicView to display the image -------------------->
        self.image_view_graphics = QtWidgets.QGraphicsView(self.centralwidget)
        self.image_view_graphics.setGeometry(QtCore.QRect(10, 10, 951, 661))
        self.image_view_graphics.setStyleSheet("border: 1px solid #21e6c1;")
        self.image_view_graphics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_view_graphics.setObjectName("image_view_graphics")

        # <-------------------- Button to load image -------------------->
        self.button_load_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_load_image.setGeometry(QtCore.QRect(10, 680, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_load_image.setFont(font)
        self.button_load_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_load_image.setToolTipDuration(-1)
        self.button_load_image.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"")
        self.button_load_image.setObjectName("button_load_image")

        # <-------------------- Button to save image -------------------->
        self.button_save_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_image.setGeometry(QtCore.QRect(180, 680, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_save_image.setFont(font)
        self.button_save_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_save_image.setToolTipDuration(-1)
        self.button_save_image.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_save_image.setObjectName("button_save_image")

        # <-------------------- Button to undo one operation -------------------->
        self.button_undo_one = QtWidgets.QPushButton(self.centralwidget)
        self.button_undo_one.setGeometry(QtCore.QRect(320, 680, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_undo_one.setFont(font)
        self.button_undo_one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_undo_one.setToolTipDuration(-1)
        self.button_undo_one.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_undo_one.setObjectName("button_undo_one")

        # <-------------------- Button to undo all operations -------------------->
        self.button_undo_all = QtWidgets.QPushButton(self.centralwidget)
        self.button_undo_all.setGeometry(QtCore.QRect(430, 680, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_undo_all.setFont(font)
        self.button_undo_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_undo_all.setToolTipDuration(-1)
        self.button_undo_all.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_undo_all.setObjectName("button_undo_all")

        # <-------------------- Button to rotate image by specified degrees -------------------->
        self.button_shortcut_custom_rotate = QtWidgets.QPushButton(self.centralwidget)
        self.button_shortcut_custom_rotate.setGeometry(QtCore.QRect(840, 680, 31, 31))
        self.button_shortcut_custom_rotate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shortcut_custom_rotate.setToolTipDuration(-1)
        self.button_shortcut_custom_rotate.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_shortcut_custom_rotate.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/custom_rotate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shortcut_custom_rotate.setIcon(icon3)
        self.button_shortcut_custom_rotate.setIconSize(QtCore.QSize(30, 30))
        self.button_shortcut_custom_rotate.setShortcut("")
        self.button_shortcut_custom_rotate.setObjectName("button_shortcut_custom_rotate")
        # <-------------------- Image Manipulation label -------------------->
        self.label_image_manip = QtWidgets.QLabel(self.centralwidget)
        self.label_image_manip.setGeometry(QtCore.QRect(970, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_image_manip.setFont(font)
        self.label_image_manip.setStyleSheet("border: 1px solid rgb(33, 230, 193);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.label_image_manip.setObjectName("label_image_manip")
        # <-------------------- Histogram Equalization -------------------->
        self.button_equalize_histogram = QtWidgets.QPushButton(self.centralwidget)
        self.button_equalize_histogram.setGeometry(QtCore.QRect(970, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_equalize_histogram.setFont(font)
        self.button_equalize_histogram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_equalize_histogram.setToolTipDuration(-1)
        self.button_equalize_histogram.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_equalize_histogram.setObjectName("button_equalize_histogram")

        # <-------------------- Gamma Correction -------------------->
        self.button_gamma_correction = QtWidgets.QPushButton(self.centralwidget)
        self.button_gamma_correction.setGeometry(QtCore.QRect(970, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_gamma_correction.setFont(font)
        self.button_gamma_correction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_gamma_correction.setToolTipDuration(-1)
        self.button_gamma_correction.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_gamma_correction.setObjectName("button_gamma_correction")

        # <-------------------- Logarithmic Transform -------------------->
        self.button_log_transform = QtWidgets.QPushButton(self.centralwidget)
        self.button_log_transform.setGeometry(QtCore.QRect(970, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_log_transform.setFont(font)
        self.button_log_transform.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_log_transform.setToolTipDuration(-1)
        self.button_log_transform.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_log_transform.setObjectName("button_log_transform")

        # <-------------------- Blurring -------------------->
        self.button_blur = QtWidgets.QPushButton(self.centralwidget)
        self.button_blur.setGeometry(QtCore.QRect(970, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_blur.setFont(font)
        self.button_blur.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_blur.setToolTipDuration(-1)
        self.button_blur.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_blur.setObjectName("button_blur")

        # <-------------------- Sharpening -------------------->
        self.button_sharpen = QtWidgets.QPushButton(self.centralwidget)
        self.button_sharpen.setGeometry(QtCore.QRect(970, 290, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_sharpen.setFont(font)
        self.button_sharpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sharpen.setToolTipDuration(-1)
        self.button_sharpen.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_sharpen.setObjectName("button_sharpen")

        # <-------------------- Invert Colors -------------------->
        self.button_invert = QtWidgets.QPushButton(self.centralwidget)
        self.button_invert.setGeometry(QtCore.QRect(970, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_invert.setFont(font)
        self.button_invert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_invert.setToolTipDuration(-1)
        self.button_invert.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_invert.setObjectName("button_invert")

        # <-------------------- Flip image diagonally -------------------->
        self.button_shortcut_invert_diagonal = QtWidgets.QPushButton(self.centralwidget)
        self.button_shortcut_invert_diagonal.setGeometry(QtCore.QRect(790, 680, 31, 31))
        self.button_shortcut_invert_diagonal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shortcut_invert_diagonal.setToolTipDuration(-1)
        self.button_shortcut_invert_diagonal.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_shortcut_invert_diagonal.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/diagonal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shortcut_invert_diagonal.setIcon(icon4)
        self.button_shortcut_invert_diagonal.setIconSize(QtCore.QSize(30, 30))
        self.button_shortcut_invert_diagonal.setShortcut("")
        self.button_shortcut_invert_diagonal.setObjectName("button_shortcut_invert_diagonal")

        # <-------------------- Flip image horizontally -------------------->
        self.button_shortcut_invert_left_right = QtWidgets.QPushButton(self.centralwidget)
        self.button_shortcut_invert_left_right.setGeometry(QtCore.QRect(740, 680, 31, 31))
        self.button_shortcut_invert_left_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shortcut_invert_left_right.setToolTipDuration(-1)
        self.button_shortcut_invert_left_right.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_shortcut_invert_left_right.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/left_right_arrows..png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shortcut_invert_left_right.setIcon(icon5)
        self.button_shortcut_invert_left_right.setIconSize(QtCore.QSize(30, 30))
        self.button_shortcut_invert_left_right.setShortcut("")
        self.button_shortcut_invert_left_right.setObjectName("button_shortcut_invert_left_right")

        # <-------------------- Flip image vertically -------------------->
        self.button_shortcut_invert_up_down = QtWidgets.QPushButton(self.centralwidget)
        self.button_shortcut_invert_up_down.setGeometry(QtCore.QRect(690, 680, 31, 31))
        self.button_shortcut_invert_up_down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_shortcut_invert_up_down.setToolTipDuration(-1)
        self.button_shortcut_invert_up_down.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_shortcut_invert_up_down.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/up_down_arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_shortcut_invert_up_down.setIcon(icon6)
        self.button_shortcut_invert_up_down.setIconSize(QtCore.QSize(30, 30))
        self.button_shortcut_invert_up_down.setShortcut("")
        self.button_shortcut_invert_up_down.setObjectName("button_shortcut_invert_up_down")

        # <-------------------- Generate Random Images -------------------->
        self.label_random = QtWidgets.QLabel(self.centralwidget)
        self.label_random.setGeometry(QtCore.QRect(970, 530, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_random.setFont(font)
        self.label_random.setStyleSheet("border: 1px solid rgb(33, 230, 193);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.label_random.setObjectName("label_random")
        self.button_random_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_random_image.setGeometry(QtCore.QRect(970, 570, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_random_image.setFont(font)
        self.button_random_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_random_image.setToolTipDuration(-1)
        self.button_random_image.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_random_image.setObjectName("button_random_image")
        # <-------------------- Get specific channel (R/G/B) -------------------->
        self.button_get_channel = QtWidgets.QPushButton(self.centralwidget)
        self.button_get_channel.setGeometry(QtCore.QRect(970, 410, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_get_channel.setFont(font)
        self.button_get_channel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_get_channel.setToolTipDuration(-1)
        self.button_get_channel.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_get_channel.setObjectName("button_get_channel")
        # <-------------------- Image to Grayscale -------------------->
        self.button_grayscale = QtWidgets.QPushButton(self.centralwidget)
        self.button_grayscale.setGeometry(QtCore.QRect(970, 470, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_grayscale.setFont(font)
        self.button_grayscale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_grayscale.setToolTipDuration(-1)
        self.button_grayscale.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_grayscale.setObjectName("button_grayscale")

        # <-------------------- Load a cat image 😺 -------------------->
        self.button_cat = QtWidgets.QPushButton(self.centralwidget)
        self.button_cat.setGeometry(QtCore.QRect(970, 630, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.button_cat.setFont(font)
        self.button_cat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_cat.setToolTipDuration(-1)
        self.button_cat.setStyleSheet("QPushButton{background-color: #21E6C1;\n"
"color: rgb(20, 40, 80);\n"
"border-radius: 10px;}\n"
"QPushButton:hover{background-color: #96BAFF; }\n"
"QPushButton:pressed { background-color: #278EA5;}\n"
"\n"
"")
        self.button_cat.setObjectName("button_cat")

        # <-------------------- Logo -------------------->
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(20, 740, 250, 99))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("Images/logo.jpg"))
        self.label_logo.setObjectName("label_logo")

        # <-------------------- Author - Eeshaan Jain -------------------->
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(280, 750, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_author.setFont(font)
        self.label_author.setOpenExternalLinks(True)
        self.label_author.setObjectName("label_author")

        # <-------------------- Project Github link -------------------->
        self.label_github = QtWidgets.QLabel(self.centralwidget)
        self.label_github.setGeometry(QtCore.QRect(280, 780, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_github.setFont(font)
        self.label_github.setOpenExternalLinks(True)
        self.label_github.setObjectName("label_github")
        self.label_github_link = QtWidgets.QLabel(self.centralwidget)
        self.label_github_link.setGeometry(QtCore.QRect(350, 780, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_github_link.setFont(font)
        self.label_github_link.setOpenExternalLinks(True)
        self.label_github_link.setObjectName("label_github_link")

        # <-------------------- Project Name -------------------->
        self.label_project_title = QtWidgets.QLabel(self.centralwidget)
        self.label_project_title.setGeometry(QtCore.QRect(280, 810, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_project_title.setFont(font)
        self.label_project_title.setOpenExternalLinks(True)
        self.label_project_title.setObjectName("label_project_title")

        # <-------------------- EE610 -------------------->
        self.label_ee610 = QtWidgets.QLabel(self.centralwidget)
        self.label_ee610.setGeometry(QtCore.QRect(820, 730, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_ee610.setFont(font)
        self.label_ee610.setOpenExternalLinks(True)
        self.label_ee610.setObjectName("label_ee610")

        # <-------------------- EE610_Report -------------------->
        self.label_ee610_report = QtWidgets.QLabel(self.centralwidget)
        self.label_ee610_report.setGeometry(QtCore.QRect(820, 810, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_ee610_report.setFont(font)
        self.label_ee610_report.setOpenExternalLinks(True)
        self.label_ee610_report.setObjectName("label_ee610_report")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setStyleSheet("QMenuBar{color: rgb(33, 230, 193);\n"
"font: 8pt \"Cascadia Code\";}")
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_load_image = QtWidgets.QAction(MainWindow)
        self.action_load_image.setObjectName("action_load_image")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_jpeg = QtWidgets.QAction(MainWindow)
        self.action_jpeg.setObjectName("action_jpeg")
        self.action_save_image = QtWidgets.QAction(MainWindow)
        self.action_save_image.setObjectName("action_save_image")
        self.menu_file.addAction(self.action_load_image)
        self.menu_file.addAction(self.action_save_image)
        self.menu_file.addAction(self.action_quit)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImProME - Image Processing Made Easy"))
        self.button_shortcut_clockwise.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Rotate clockwise by 90 degrees</span></p></body></html>"))
        self.button_shortcut_clockwise.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.button_shortcut_anticlockwise.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Rotate counter clockwise by 90 degrees</span></p></body></html>"))
        self.button_shortcut_anticlockwise.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.button_load_image.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Load New Image</span><br/></p></body></html>"))
        self.button_load_image.setText(_translate("MainWindow", "Load New Image"))
        self.button_load_image.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.button_save_image.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Save Image</span></p></body></html>"))
        self.button_save_image.setText(_translate("MainWindow", "Save Image"))
        self.button_save_image.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.button_undo_one.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Undo last change</span><br/></p></body></html>"))
        self.button_undo_one.setText(_translate("MainWindow", "Undo"))
        self.button_undo_one.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.button_undo_all.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Undo all changes</span><br/></p></body></html>"))
        self.button_undo_all.setText(_translate("MainWindow", "Revert"))
        self.button_undo_all.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.button_shortcut_custom_rotate.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Rotate by specified degrees</span><br/></p></body></html>"))
        self.label_image_manip.setText(_translate("MainWindow", " Image Manipulations"))
        self.button_equalize_histogram.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Perform Histogram Equalization</span></p></body></html>"))
        self.button_equalize_histogram.setText(_translate("MainWindow", "Equalize Histogram"))
        self.button_gamma_correction.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Perform Gamma Correction</span></p></body></html>"))
        self.button_gamma_correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.button_log_transform.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Perform Log Transform</span></p></body></html>"))
        self.button_log_transform.setText(_translate("MainWindow", "Logarithmic Transform"))
        self.button_blur.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Blur the Image</span></p></body></html>"))
        self.button_blur.setText(_translate("MainWindow", "Blur"))
        self.button_sharpen.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Sharpen the Image</span></p></body></html>"))
        self.button_sharpen.setText(_translate("MainWindow", "Sharpen"))
        self.button_invert.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Invert colors of the Image</span></p></body></html>"))
        self.button_invert.setText(_translate("MainWindow", "Invert"))
        self.button_shortcut_invert_diagonal.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Flip image diagonally</span><br/></p></body></html>"))
        self.button_shortcut_invert_left_right.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Flip image horizontally</span><br/></p></body></html>"))
        self.button_shortcut_invert_up_down.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Flip image vertically</span><br/></p></body></html>"))
        self.label_random.setText(_translate("MainWindow", "       Random"))
        self.button_random_image.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Generate a Random Image</span><span style=\" font-style:italic;\"><br/></span></p></body></html>"))
        self.button_random_image.setText(_translate("MainWindow", "Generate Random Image"))
        self.button_random_image.setShortcut(_translate("MainWindow", "R"))
        self.button_get_channel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Get a specific channel of the Image</span></p></body></html>"))
        self.button_get_channel.setText(_translate("MainWindow", "Get Channel"))
        self.button_grayscale.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Convert the Image to Grayscale</span></p></body></html>"))
        self.button_grayscale.setText(_translate("MainWindow", "Convert to Grayscale"))
        self.button_cat.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#142850;\">Load a Cat Image</span><span style=\" font-style:italic;\"><br/></span></p></body></html>"))
        self.button_cat.setText(_translate("MainWindow", "Load a Cat Image"))
        self.button_cat.setShortcut(_translate("MainWindow", "C"))
        self.label_author.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Author: Eeshaan Jain</span></p></body></html>"))
        self.label_github.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Github: </span></p></body></html>"))
        self.label_github_link.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.github.com/EeshaanJain/ImageProcessingGUI\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#21E6C1;\">EeshaanJain</span></a></p></body></html>"))
        self.label_project_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">ImProME: Image Processing Made Easy</span></p></body></html>"))
        self.label_ee610.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">This project is done as a part of </span></p><p><span style=\" font-size:9pt; font-weight:600;\">Assignment 1 of EE 610: Image Processing</span></p></body></html>"))
        self.label_ee610_report.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.github.com/EeshaanJain/ImageProcessingGUI/19D070022_Assignment1_Report.pdf\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#21E6C1;\">Link to the Report</span></a></p></body></html>"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.action_load_image.setText(_translate("MainWindow", "Load Image"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.action_jpeg.setText(_translate("MainWindow", "*.jpeg"))
        self.action_save_image.setText(_translate("MainWindow", "Save Image"))


