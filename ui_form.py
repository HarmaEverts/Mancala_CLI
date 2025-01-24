# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Mancala_UI(object):
    def setupUi(self, Mancala_UI):
        if not Mancala_UI.objectName():
            Mancala_UI.setObjectName(u"Mancala_UI")
        Mancala_UI.resize(636, 195)
        self.gridLayout_2 = QGridLayout(Mancala_UI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_player_b = QLineEdit(Mancala_UI)
        self.label_player_b.setObjectName(u"label_player_b")

        self.horizontalLayout.addWidget(self.label_player_b)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_rules = QPushButton(Mancala_UI)
        self.button_rules.setObjectName(u"button_rules")

        self.horizontalLayout.addWidget(self.button_rules)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_player_a = QLineEdit(Mancala_UI)
        self.label_player_a.setObjectName(u"label_player_a")
        self.label_player_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_player_a)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.store_b = QPushButton(Mancala_UI)
        self.store_b.setObjectName(u"store_b")
        self.store_b.setMinimumSize(QSize(101, 141))

        self.horizontalLayout_4.addWidget(self.store_b)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pocket_b3 = QPushButton(Mancala_UI)
        self.pocket_b3.setObjectName(u"pocket_b3")
        self.pocket_b3.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_3.addWidget(self.pocket_b3)

        self.pocket_b5 = QPushButton(Mancala_UI)
        self.pocket_b5.setObjectName(u"pocket_b5")
        self.pocket_b5.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_3.addWidget(self.pocket_b5)

        self.pocket_b4 = QPushButton(Mancala_UI)
        self.pocket_b4.setObjectName(u"pocket_b4")
        self.pocket_b4.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_3.addWidget(self.pocket_b4)

        self.pocket_b6 = QPushButton(Mancala_UI)
        self.pocket_b6.setObjectName(u"pocket_b6")
        self.pocket_b6.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_3.addWidget(self.pocket_b6)

        self.pocket_b2 = QPushButton(Mancala_UI)
        self.pocket_b2.setObjectName(u"pocket_b2")
        self.pocket_b2.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_3.addWidget(self.pocket_b2)

        self.pocket_b1 = QPushButton(Mancala_UI)
        self.pocket_b1.setObjectName(u"pocket_b1")
        self.pocket_b1.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_3.addWidget(self.pocket_b1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pocket_a5 = QPushButton(Mancala_UI)
        self.pocket_a5.setObjectName(u"pocket_a5")
        self.pocket_a5.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_2.addWidget(self.pocket_a5)

        self.pocket_a3 = QPushButton(Mancala_UI)
        self.pocket_a3.setObjectName(u"pocket_a3")
        self.pocket_a3.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_2.addWidget(self.pocket_a3)

        self.pocket_a4 = QPushButton(Mancala_UI)
        self.pocket_a4.setObjectName(u"pocket_a4")
        self.pocket_a4.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_2.addWidget(self.pocket_a4)

        self.pocket_a2 = QPushButton(Mancala_UI)
        self.pocket_a2.setObjectName(u"pocket_a2")
        self.pocket_a2.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_2.addWidget(self.pocket_a2)

        self.pocket_a1 = QPushButton(Mancala_UI)
        self.pocket_a1.setObjectName(u"pocket_a1")
        self.pocket_a1.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_2.addWidget(self.pocket_a1)

        self.pocket_a6 = QPushButton(Mancala_UI)
        self.pocket_a6.setObjectName(u"pocket_a6")
        self.pocket_a6.setMinimumSize(QSize(61, 51))

        self.horizontalLayout_2.addWidget(self.pocket_a6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.store_a = QPushButton(Mancala_UI)
        self.store_a.setObjectName(u"store_a")
        self.store_a.setMinimumSize(QSize(101, 141))

        self.horizontalLayout_4.addWidget(self.store_a)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Mancala_UI)

        QMetaObject.connectSlotsByName(Mancala_UI)
    # setupUi

    def retranslateUi(self, Mancala_UI):
        Mancala_UI.setWindowTitle(QCoreApplication.translate("Mancala_UI", u"Mancala_UI", None))
        self.label_player_b.setText(QCoreApplication.translate("Mancala_UI", u"Player B", None))
        self.button_rules.setText(QCoreApplication.translate("Mancala_UI", u"Read Mancala rules", None))
        self.label_player_a.setText(QCoreApplication.translate("Mancala_UI", u"Player A", None))
        self.store_b.setText(QCoreApplication.translate("Mancala_UI", u"Store B", None))
        self.pocket_b3.setText(QCoreApplication.translate("Mancala_UI", u"B3", None))
        self.pocket_b5.setText(QCoreApplication.translate("Mancala_UI", u"B5", None))
        self.pocket_b4.setText(QCoreApplication.translate("Mancala_UI", u"B4", None))
        self.pocket_b6.setText(QCoreApplication.translate("Mancala_UI", u"B6", None))
        self.pocket_b2.setText(QCoreApplication.translate("Mancala_UI", u"B2", None))
        self.pocket_b1.setText(QCoreApplication.translate("Mancala_UI", u"B1", None))
        self.pocket_a5.setText(QCoreApplication.translate("Mancala_UI", u"A5", None))
        self.pocket_a3.setText(QCoreApplication.translate("Mancala_UI", u"A3", None))
        self.pocket_a4.setText(QCoreApplication.translate("Mancala_UI", u"A4", None))
        self.pocket_a2.setText(QCoreApplication.translate("Mancala_UI", u"A2", None))
        self.pocket_a1.setText(QCoreApplication.translate("Mancala_UI", u"A1", None))
        self.pocket_a6.setText(QCoreApplication.translate("Mancala_UI", u"A6", None))
        self.store_a.setText(QCoreApplication.translate("Mancala_UI", u"Store A", None))
    # retranslateUi

