# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialogButtonBox

from functions import functions, config
from interfase.Edit_window import Edit_Box


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        # MainWindow.setWindowIcon(QtGui.QIcon("resources/del_button.png"))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 550)
        MainWindow.setMinimumSize(QtCore.QSize(780, 550))
        MainWindow.setMaximumSize(QtCore.QSize(780, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.objFeeld = QtWidgets.QFrame(self.centralwidget)
        self.objFeeld.setEnabled(True)
        self.objFeeld.setGeometry(QtCore.QRect(-1, -1, 801, 552))
        self.objFeeld.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"background-image: url(resources/bg_5.png);\n")
        self.objFeeld.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.objFeeld.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.objFeeld.setObjectName("objFeeld")
        self.addButton = QtWidgets.QPushButton(self.objFeeld)
        self.addButton.setEnabled(True)
        self.addButton.setGeometry(QtCore.QRect(700, 490, 50, 50))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addButton.setStyleSheet("QPushButton {\n"
                                    "    background-image: url(resources/add_button.png);\n"
                                    "    border: none;\n"
                                    "    outline: none;\n"
                                    "    border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-image: url(resources/add_button_hover.png);\n"
                                    "    border: none;\n"
                                    "    outline: none;\n"
                                    "    border-radius: 10px;\n"
                                    "}")
        self.addButton.setText("")
        self.addButton.setObjectName("addButton")
        self.scrollArea = QtWidgets.QScrollArea(self.objFeeld)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 761, 470))
        self.scrollArea.setStyleSheet("border: none;\n"
"background: rgba(255, 255, 255, 0);")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 761, 650))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")

        self.sortPrior = QtWidgets.QPushButton(self.objFeeld)
        self.sortPrior.setGeometry(QtCore.QRect(315, 490, 50, 50))
        self.sortPrior.setStyleSheet("QPushButton {\n"
                                       "    background-image: url(resources/button_sort_prior_off.png);\n"
                                       "    border: none;\n"
                                       "    outline: none;\n"
                                       "    border-top-left-radius: 10px;"
                                       "    border-bottom-left-radius: 10px;"
                                       "}\n"
                                       "\n"
                                       "QPushButton:checked {\n"
                                       "    background-image: url(resources/button_sort_prior_on.png);\n"
                                       "    border: none;\n"
                                       "    outline: none;\n"
                                       "    border-top-left-radius: 10px;"
                                       "    border-bottom-left-radius: 10px;"
                                       "}")
        self.sortPrior.setCheckable(True)
        self.sortPrior.setChecked(True)
        config.sort_id = 1

        self.sortData = QtWidgets.QPushButton(self.objFeeld)
        self.sortData.setGeometry(QtCore.QRect(365, 490, 50, 50))
        self.sortData.setStyleSheet("QPushButton {\n"
                                     "    background-image: url(resources/button_sort_data_off.png);\n"
                                     "    border: none;\n"
                                     "    outline: none;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:checked {\n"
                                     "    background-image: url(resources/button_sort_data_on.png);\n"
                                     "    border: none;\n"
                                     "    outline: none;\n"
                                     "}")
        self.sortData.setCheckable(True)
        self.sortData.setChecked(False)

        self.sortName = QtWidgets.QPushButton(self.objFeeld)
        self.sortName.setGeometry(QtCore.QRect(415, 490, 50, 50))
        self.sortName.setStyleSheet("QPushButton {\n"
                                     "    background-image: url(resources/button_sort_a-z_off.png);\n"
                                     "    border: none;\n"
                                     "    outline: none;\n"
                                     "    border-top-right-radius: 10px;"
                                     "    border-bottom-right-radius: 10px;"
                                     "}\n"
                                     "\n"
                                     "QPushButton:checked {\n"
                                     "    background-image: url(resources/button_sort_a-z_on.png);\n"
                                     "    border: none;\n"
                                     "    outline: none;\n"
                                     "    border-top-right-radius: 10px;"
                                     "    border-bottom-right-radius: 10px;"
                                     "}")
        self.sortName.setCheckable(True)
        self.sortName.setChecked(False)

        self.buttonStory = QtWidgets.QPushButton(self.objFeeld)
        self.buttonStory.setGeometry(QtCore.QRect(30, 490, 50, 50))
        self.buttonStory.setStyleSheet("QPushButton {\n"
                                    "    background-image: url(resources/button_story_off.png);\n"
                                    "    border: none;\n"
                                    "    outline: none;\n"
                                    "    border-radius: 10px;"
                                    "}\n"
                                    "\n"
                                    "QPushButton:checked {\n"
                                    "    background-image: url(resources/button_story_on.png);\n"
                                    "    border: none;\n"
                                    "    outline: none;\n"
                                    "    border-radius: 10px;"
                                    "}")
        self.buttonStory.setCheckable(True)
        self.buttonStory.setChecked(False)

        self.del_button_story = QtWidgets.QPushButton(self.objFeeld)
        self.del_button_story.setGeometry(QtCore.QRect(700, 490, 50, 50))
        self.del_button_story.setStyleSheet("QPushButton {\n"
                                       "    background-image: url(resources/del_story.png);\n"
                                       "    border: none;\n"
                                       "    outline: none;\n"
                                       "    border-radius: 10px;"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-image: url(resources/del_story_hover.png);\n"
                                       "    border: none;\n"
                                       "    outline: none;\n"
                                       "    border-radius: 10px;"
                                       "}")
        self.del_button_story.setVisible(False)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.addButton.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def add_item(self, affairs_json):
        n = config.num_add
        self.Item_n = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.Item_n.setEnabled(True)
        if affairs_json["text"] != "":
            self.Item_n.setMinimumSize(QtCore.QSize(750, 110))
            self.Item_n.setMaximumSize(QtCore.QSize(750, 110))
        else:
            self.Item_n.setMinimumSize(QtCore.QSize(750, 82))
            self.Item_n.setMaximumSize(QtCore.QSize(750, 82))
        self.Item_n.setStyleSheet("background: none;")
        self.Item_n.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Item_n.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Item_n.setObjectName("Item_n")

        self.label_n_2 = QtWidgets.QLabel(self.Item_n)
        self.label_n_2.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                     "background-color: rgb(125, 232, 109);\n"
                                     "color: white;\n"
                                     "border-top-left-radius: 10px;")
        self.label_n_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_n_2.setObjectName("label_44")

        self.label_n_3 = QtWidgets.QLabel(self.Item_n)
        self.label_n_3.setGeometry(QtCore.QRect(40, 10, 691, 31))
        self.label_n_3.setStyleSheet("background-color: rgb(228, 247, 246);\n"
                                     "border-top-right-radius: 10px;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;"
                                     "padding-left: 20px;\n"
                                     "color: rgb(63, 63, 63)")
        self.label_n_3.setObjectName("label_45")
        self.verticalLayout.addWidget(self.Item_n)

        self.label_n_1 = QtWidgets.QLabel(self.Item_n)
        if affairs_json["text"] != "":
            self.label_n_1.setGeometry(QtCore.QRect(10, 40, 721, 61))
            self.label_n_1.setMinimumSize(QtCore.QSize(0, 61))
            self.label_n_1.setText(affairs_json["text"])
        else:
            self.label_n_1.setGeometry(QtCore.QRect(10, 40, 721, 31))
            self.label_n_1.setMinimumSize(QtCore.QSize(0, 10))
        self.label_n_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.label_n_1.setStyleSheet("background: rgba(225, 225, 225, 150);\n"
                                     "border-bottom-left-radius: 10px;\n"
                                     "border-bottom-right-radius: 10px;\n"
                                     "font-size: 15px;\n"
                                     "padding: 5px 15px 5px 15px;\n"
                                     "color: rgb(90, 90, 90)")
        self.label_n_1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_n_1.setScaledContents(False)
        self.label_n_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_n_1.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_n_1.setObjectName("label_43")

        if affairs_json["data"] != "":
            self.label_n_4 = QtWidgets.QLabel(self.Item_n)
            self.label_n_4.setGeometry(QtCore.QRect(601, 10, 130, 31))
            self.label_n_4.setStyleSheet("background-color: rgb(215, 236, 235);\n"
                                         "border-top-right-radius: 10px;\n"
                                         "border-top-left-radius: 5px;\n"
                                         "border-bottom-left-radius: 5px;\n"
                                         "font-size: 18px;\n"
                                         "padding-left: 2px;\n"
                                         "color: rgb(63, 63, 63)")
            self.label_n_4.setObjectName("label_45")
            self.verticalLayout.addWidget(self.Item_n)
            self.label_n_4.setText(affairs_json["data"])

        self.label_n_3.setText(affairs_json["name"])

        self.delButton = QtWidgets.QPushButton(self.Item_n)
        self.delButton.setGeometry(QtCore.QRect(705, 18, 15, 15))
        self.delButton.setStyleSheet("QPushButton {"
                                      "border: none;"
                                      "outline: none;"
                                      "background-color: rgb(169, 220, 170);"
                                      "background-image: url(resources/del_button.png);"
                                      "border-radius: 2px;"
                                      "}"
                                      "QPushButton:hover {"
                                      "border: none;"
                                      "outline: none;"
                                      "background-color: rgb(80, 172, 83);"
                                      "background-image: url(resources/del_button_hover.png);"
                                      "border-radius: 2px"
                                      "}")

        self.delButton.clicked.connect(lambda: self.del_box(n))

        self.settings_button = QtWidgets.QPushButton(self.Item_n)
        self.settings_button.setGeometry(QtCore.QRect(685, 18, 15, 15))
        self.settings_button.setStyleSheet("QPushButton {"
                                     "border: none;"
                                     "outline: none;"
                                     "background-image: url(resources/settings_button.png);"
                                     "border-radius: 2px;"
                                     "}"
                                     "QPushButton:hover {"
                                     "border: none;"
                                     "outline: none;"
                                     "background-image: url(resources/settings_button.png);"
                                     "border-radius: 2px"
                                     "}")
        # self.settings_button.clicked(functions.settings_button_clicked())
        self.settings_button.clicked.connect(lambda: self.settings_button_clicked(n))

        if affairs_json["priority"] == 1:
            self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                         "background-color: rgb(80, 172, 83);\n"
                                         "color: white;\n"
                                         "border-top-left-radius: 10px;")
        if affairs_json["priority"] == 2:
            self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                         "background-color: rgb(242, 177, 9);\n"
                                         "color: white;\n"
                                         "border-top-left-radius: 10px;")
        if affairs_json["priority"] == 3:
            self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                         "background-color: rgb(202, 71, 71);\n"
                                         "color: white;\n"
                                         "border-top-left-radius: 10px;")
        return self.Item_n

    def paint_story_box (self, affair):
        self.Item_n = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.Item_n.setEnabled(True)
        if affair["text"] != "":
            self.Item_n.setMinimumSize(QtCore.QSize(750, 110))
            self.Item_n.setMaximumSize(QtCore.QSize(750, 110))
        else:
            self.Item_n.setMinimumSize(QtCore.QSize(750, 82))
            self.Item_n.setMaximumSize(QtCore.QSize(750, 82))
        self.Item_n.setStyleSheet("background: none;")
        self.Item_n.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Item_n.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Item_n.setObjectName("Item_n")

        self.label_n_2 = QtWidgets.QLabel(self.Item_n)
        self.label_n_2.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                     "background-color: rgb(125, 232, 109);\n"
                                     "color: white;\n"
                                     "border-top-left-radius: 10px;")
        self.label_n_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_n_2.setObjectName("label_44")

        self.label_n_3 = QtWidgets.QLabel(self.Item_n)
        self.label_n_3.setGeometry(QtCore.QRect(40, 10, 691, 31))
        self.label_n_3.setStyleSheet("background-color: rgb(228, 247, 246);\n"
                                     "border-top-right-radius: 10px;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;"
                                     "padding-left: 20px;\n"
                                     "color: rgb(63, 63, 63)")
        self.label_n_3.setObjectName("label_45")
        self.verticalLayout.addWidget(self.Item_n)

        self.label_n_1 = QtWidgets.QLabel(self.Item_n)
        if affair["text"] != "":
            self.label_n_1.setGeometry(QtCore.QRect(10, 40, 721, 61))
            self.label_n_1.setMinimumSize(QtCore.QSize(0, 61))
            self.label_n_1.setText(affair["text"])
        else:
            self.label_n_1.setGeometry(QtCore.QRect(10, 40, 721, 31))
            self.label_n_1.setMinimumSize(QtCore.QSize(0, 10))
        self.label_n_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.label_n_1.setStyleSheet("background: rgba(225, 225, 225, 150);\n"
                                     "border-bottom-left-radius: 10px;\n"
                                     "border-bottom-right-radius: 10px;\n"
                                     "font-size: 15px;\n"
                                     "padding: 5px 15px 5px 15px;\n"
                                     "color: rgb(90, 90, 90)")
        self.label_n_1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_n_1.setScaledContents(False)
        self.label_n_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_n_1.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_n_1.setObjectName("label_43")

        if affair["priority"] == 1:
            self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                         "background-color: rgb(80, 172, 83);\n"
                                         "color: white;\n"
                                         "border-top-left-radius: 10px;")
        if affair["priority"] == 2:
            self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                         "background-color: rgb(242, 177, 9);\n"
                                         "color: white;\n"
                                         "border-top-left-radius: 10px;")
        if affair["priority"] == 3:
            self.label_n_2.setStyleSheet("font-size: 22px;\n"
                                         "background-color: rgb(202, 71, 71);\n"
                                         "color: white;\n"
                                         "border-top-left-radius: 10px;")

        if affair["data"] != "":
            self.label_n_4 = QtWidgets.QLabel(self.Item_n)
            self.label_n_4.setGeometry(QtCore.QRect(601, 10, 130, 31))
            self.label_n_4.setStyleSheet("background-color: rgb(215, 236, 235);\n"
                                         "border-top-right-radius: 10px;\n"
                                         "border-top-left-radius: 5px;\n"
                                         "border-bottom-left-radius: 5px;\n"
                                         "font-size: 18px;\n"
                                         "padding-left: 2px;\n"
                                         "color: rgb(63, 63, 63)")
            self.label_n_4.setObjectName("label_45")
            self.verticalLayout.addWidget(self.Item_n)
            self.label_n_4.setText(affair["data"])

        self.label_n_3.setText(affair["name"])

        self.Item_n.setVisible(False)

        return self.Item_n

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo"))

    def del_box(self, n):
        config.num_add = config.num_add - 1
        functions.del_affairs_json(n)
        self.add_affair_story()
        self.repaint_Box()

    def repaint_Box(self):
        config.num_add = -1
        config.affairs = functions.update_json()
        for x in config.affairs_mass:
            x.close()
        config.affairs_mass = []
        for x in config.affairs["affairs"]:
            config.num_add = config.num_add + 1
            config.affairs_mass.append(self.add_item(x))

    def show_affairs(self):
        for x in config.affairs_mass:
            x.setVisible(True)

    def hide_affairs(self):
        for x in config.affairs_mass:
            x.setVisible(False)

    def add_story(self):
        for affair in config.affairs_story["affairs"]:
            config.story_mass.append(self.paint_story_box(affair))

    def add_affair_story(self):
        config.affairs_story = functions.update_story_json()
        config.story_mass.append(self.paint_story_box(config.affairs_story["affairs"][-1]))

    def del_story(self):
        for box in config.story_mass:
            box.close()
        config.story_mass = []

    def show_story(self):
        for affair in config.story_mass:
            affair.setVisible(True)

    def hide_story(self):
        for affair in config.story_mass:
            affair.setVisible(False)

    def settings_button_clicked(self, n):
        edit = Edit_Box(n)

        edit.button_apply.clicked.connect(lambda: self.apply_clicked(edit, n))

        edit.exec()

    def apply_clicked(self, edit, n):
        if edit.checkRegulations():
            if edit.priority_1.isChecked():
                edit.priority = 1
            if edit.priority_2.isChecked():
                edit.priority = 2
            if edit.priority_3.isChecked():
                edit.priority = 3

            config.affairs = functions.new_affairs_json(config.affairs, edit.name.toPlainText(), edit.text.toPlainText(),
                                                        edit.data.toPlainText(), edit.priority)
            functions.del_affairs_json(n)

            if config.sort_id == 1:
                config.affairs = functions.sort_json_prior()
            if config.sort_id == 2:
                config.affairs = functions.sort_json_data()
            if config.sort_id == 3:
                config.affairs = functions.sort_json_name()
            self.repaint_Box()
            edit.close()

