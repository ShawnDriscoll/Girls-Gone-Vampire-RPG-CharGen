#
#   Girls Gone Vampire Character Generator
#
#######################################################

"""
GGV Chargen 0.0.1 Beta
-----------------------------------------------------------------------

This program generates characters for the Girls Gone Vampire RPG.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
from mainwindow import Ui_MainWindow
from aboutdialog import Ui_aboutDialog
from alertdialog import Ui_alertDialog
from savedialog import Ui_saveDialog
import sys
import os
import logging
import json
from fpdf import FPDF

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'GGV CharGen 0.0.1 (Beta)'
__expired_tag__ = False

class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self):
        '''
        Open the About dialog window
        '''
        super().__init__()
        log.info('PyQt5 aboutDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 aboutDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the About dialog window
        '''
        log.info('PyQt5 aboutDialog closing...')
        self.close()

class alertDialog(QDialog, Ui_alertDialog):
    def __init__(self):
        '''
        Open the Alert dialog window
        '''
        super().__init__()
        log.info('PyQt5 alertDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 alertDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the Alert dialog window
        '''
        log.info('PyQt5 alertDialog closing...')
        self.close()

class saveDialog(QDialog, Ui_saveDialog):
    def __init__(self):
        '''
        Open the Save dialog window
        '''
        super().__init__()
        log.info('PyQt5 saveDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.saveOKButton.clicked.connect(self.acceptOKButtonClicked)
        self.saveDisplay.setText('Character saved.')
        log.info('PyQt5 saveDialog initialized.')

    def acceptOKButtonClicked(self):
        '''
        Close the Save dialog window
        '''
        log.info('PyQt5 saveDialog closing...')
        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        Display the main app window.
        Connect all the buttons to their functions.
        Initialize their value ranges.
        '''
        super().__init__()
        log.info('PyQt5 MainWindow initializing...')
        self.setupUi(self)
        self.actionAbout_GGV_CharGen.triggered.connect(self.actionAbout_triggered)
        self.actionQuitProg.triggered.connect(self.actionQuitProg_triggered)
        self.clearButton.clicked.connect(self.clearButton_clicked)
        self.actionClear.triggered.connect(self.clearButton_clicked)
        self.loadButton.clicked.connect(self.loadButton_clicked)
        self.actionLoad.triggered.connect(self.loadButton_clicked)
        self.saveButton.clicked.connect(self.saveButton_clicked)
        self.actionSave.triggered.connect(self.saveButton_clicked)
        self.printButton.clicked.connect(self.printButton_clicked)
        self.actionPrint.triggered.connect(self.printButton_clicked)
        self.actionVisit_Blog.triggered.connect(self.Visit_Blog)
        self.actionFeedback.triggered.connect(self.Feedback)
        self.actionOverview.triggered.connect(self.Overview_menu)
        self.bodyScore.valueChanged.connect(self.bodyScore_valueChanged)
        self.mindScore.valueChanged.connect(self.mindScore_valueChanged)
        self.spiritScore.valueChanged.connect(self.spiritScore_valueChanged)
        self.bodyScore.setDisabled(True)
        self.mindScore.setDisabled(True)
        self.spiritScore.setDisabled(True)
        self.agilitySkill.setDisabled(True)
        self.beautySkill.setDisabled(True)
        self.strengthSkill.setDisabled(True)
        self.knowledgeSkill.setDisabled(True)
        self.perceptionSkill.setDisabled(True)
        self.technologySkill.setDisabled(True)
        self.charismaSkill.setDisabled(True)
        self.empathySkill.setDisabled(True)
        self.focusSkill.setDisabled(True)
        self.boxingSkill.setDisabled(True)
        self.meleeSkill.setDisabled(True)
        self.rangedSkill.setDisabled(True)
        self.artSkill.setDisabled(True)
        self.languagesSkill.setDisabled(True)
        self.scienceSkill.setDisabled(True)
        self.dodgeSkill.setDisabled(True)
        self.parrySkill.setDisabled(True)
        self.strikeSkill.setDisabled(True)
        self.blessSkill.setDisabled(True)
        self.exorcismSkill.setDisabled(True)
        self.healingSkill.setDisabled(True)
        self.demonologySkill.setDisabled(True)
        self.metamorphosisSkill.setDisabled(True)
        self.necromancySkill.setDisabled(True)
        self.clairvoyanceSkill.setDisabled(True)
        self.psychokinesisSkill.setDisabled(True)
        self.telepathySkill.setDisabled(True)
        self.saveButton.setDisabled(True)
        self.actionSave.setDisabled(True)
        self.printButton.setDisabled(True)
        self.actionPrint.setDisabled(True)
        self.cultBox.setDisabled(True)
        self.roleBox.setDisabled(True)
        self.coverBox.setDisabled(True)
        self.xpEdit.setDisabled(True)
        self.agilitySkill.valueChanged.connect(self.agilitySkill_valueChanged)
        self.beautySkill.valueChanged.connect(self.beautySkill_valueChanged)
        self.strengthSkill.valueChanged.connect(self.strengthSkill_valueChanged)
        self.knowledgeSkill.valueChanged.connect(self.knowledgeSkill_valueChanged)
        self.perceptionSkill.valueChanged.connect(self.perceptionSkill_valueChanged)
        self.technologySkill.valueChanged.connect(self.technologySkill_valueChanged)
        self.charismaSkill.valueChanged.connect(self.charismaSkill_valueChanged)
        self.empathySkill.valueChanged.connect(self.empathySkill_valueChanged)
        self.focusSkill.valueChanged.connect(self.focusSkill_valueChanged)
        self.boxingSkill.valueChanged.connect(self.boxingSkill_valueChanged)
        self.meleeSkill.valueChanged.connect(self.meleeSkill_valueChanged)
        self.rangedSkill.valueChanged.connect(self.rangedSkill_valueChanged)
        self.artSkill.valueChanged.connect(self.artSkill_valueChanged)
        self.languagesSkill.valueChanged.connect(self.languagesSkill_valueChanged)
        self.scienceSkill.valueChanged.connect(self.scienceSkill_valueChanged)
        self.dodgeSkill.valueChanged.connect(self.dodgeSkill_valueChanged)
        self.parrySkill.valueChanged.connect(self.parrySkill_valueChanged)
        self.strikeSkill.valueChanged.connect(self.strikeSkill_valueChanged)
        self.blessSkill.valueChanged.connect(self.blessSkill_valueChanged)
        self.exorcismSkill.valueChanged.connect(self.exorcismSkill_valueChanged)
        self.healingSkill.valueChanged.connect(self.healingSkill_valueChanged)
        self.demonologySkill.valueChanged.connect(self.demonologySkill_valueChanged)
        self.metamorphosisSkill.valueChanged.connect(self.metamorphosisSkill_valueChanged)
        self.necromancySkill.valueChanged.connect(self.necromancySkill_valueChanged)
        self.clairvoyanceSkill.valueChanged.connect(self.clairvoyanceSkill_valueChanged)
        self.psychokinesisSkill.valueChanged.connect(self.psychokinesisSkill_valueChanged)
        self.telepathySkill.valueChanged.connect(self.telepathySkill_valueChanged)

        self.encumbered_checkBox.setDisabled(True)
        self.charnameEdit.setText('Sample Char')
        self.rewardDisplay.setText('None')
        self.encumbered_flag = False
        self.encumbered_checkBox.toggled.connect(self.encumbered_checkBox_changed)
        self.encumbered_checkBox.setChecked(self.encumbered_flag)
        self.armorDisplay.setPlainText('None')
        self.weaponDisplay.setPlainText('None')
        self.starting_items = 'None'
        self.itemsDisplay.setPlainText(self.starting_items)
        self.specialDisplay.setPlainText('None')
        self.traitsDisplay.setPlainText('')
        self.backstoryDisplay.setPlainText('')
        self.notesDisplay.setPlainText('')

        self.gender_choice = ['Choose', 'Male', 'Female']
        for i in self.gender_choice:
            self.genderBox.addItem(i)
        self.genderBox.setCurrentIndex(0)
        self.genderBox.currentIndexChanged.connect(self.genderBox_changed)

        self.cultBox.addItem('Choose')
        self.cultBox.setCurrentIndex(0)
        self.cultBox.currentIndexChanged.connect(self.cultBox_changed)

        self.role_choice = ['Choose', 'Servant', 'Steward', 'Advisor', 'Guardian', 'Expert', 'Assassin', 'Psychic', 'Acolyte', 'Student']
        self.role_skill = ['', 'Body', 'Mind', 'Spirit', 'Combat', 'Strange', 'Martial', 'Psionics', 'Divine', 'Occult']
        self.role_item = ['', 'Kit of Choice', 'Nice Watch', 'Flask', 'Pistol', 'Briefcase', 'Sword', 'Tarot Cards', 'Ceremonial Robes', 'Grimoire (blank)']
        for i in self.role_choice:
            self.roleBox.addItem(i)
        self.roleBox.setCurrentIndex(0)
        self.roleBox.currentIndexChanged.connect(self.roleBox_changed)

        self.cover_choice = ['Choose', 'Driver', 'Celebrity', 'Athlete', 'Journalist', 'Detective', 'Engineer', 'Actor', 'Psychologist', 'Security', 'Enforcer', 'Thief', 'Cop', 'Painter', 'Ambassador', 'Doctor', 'Fortune Teller']
        self.cover_bonus = ['', 'Agility', 'Beauty', 'Strength', 'Knowledge', 'Perception', 'Technology', 'Charisma', 'Empathy', 'Focus', 'Boxing', 'Melee', 'Ranged', 'Art', 'Languages', 'Science', 'Clairvoyance']
        self.cover_clothes = ['', 'Cheap Suit', 'Fashionable Clothing', 'Track Suit', 'Cheap Suit', 'Plain Clothes', 'Denim Outfit', 'Fashionable Clothing', 'Nice Suit', 'Uniform', 'Dark Clothes', 'Plain Clothes', 'Uniform', 'Fashionable Clothes', 'Uniform', 'Dark Clothes', 'Uniform', 'Fashionable Clothing', 'Nice Suit', 'Medical Uniform', 'Beatnik Outfit']
        for i in self.cover_choice:
            self.coverBox.addItem(i)
        self.coverBox.setCurrentIndex(0)
        self.coverBox.currentIndexChanged.connect(self.coverBox_changed)

        self.gender_not_chosen = True
        self.cult_not_chosen = True
        self.role_not_chosen = True
        self.choosing_extra_8_skills = False
        self.cover_not_chosen = True
        self.skilling_up = False
        self.attributing_up = False
        self.is_martial = False
        self.is_divine = False
        self.is_occult = False
        self.is_psionic = False
        self.is_vampire = 'No'

        self.char_level = 1
        self.levelDisplay.setText(str(self.char_level))

        self.char_xp = 0
        self.xpEdit.setText(str(self.char_xp))
        self.xpEdit.textChanged.connect(self.xpValue_changed)

        self.level_achieved = 100
        self.next_level = 200

        self.scoreCap = 3
        self.skillCap = 3

        self.bodyScore.setMaximum(self.scoreCap)
        self.mindScore.setMaximum(self.scoreCap)
        self.spiritScore.setMaximum(self.scoreCap)
        self.agilitySkill.setMaximum(self.skillCap)
        self.beautySkill.setMaximum(self.skillCap)
        self.strengthSkill.setMaximum(self.skillCap)
        self.knowledgeSkill.setMaximum(self.skillCap)
        self.perceptionSkill.setMaximum(self.skillCap)
        self.technologySkill.setMaximum(self.skillCap)
        self.charismaSkill.setMaximum(self.skillCap)
        self.empathySkill.setMaximum(self.skillCap)
        self.focusSkill.setMaximum(self.skillCap)
        self.boxingSkill.setMaximum(self.skillCap)
        self.meleeSkill.setMaximum(self.skillCap)
        self.rangedSkill.setMaximum(self.skillCap)
        self.artSkill.setMaximum(self.skillCap)
        self.languagesSkill.setMaximum(self.skillCap)
        self.scienceSkill.setMaximum(self.skillCap)
        self.dodgeSkill.setMaximum(self.skillCap)
        self.parrySkill.setMaximum(self.skillCap)
        self.strikeSkill.setMaximum(self.skillCap)
        self.blessSkill.setMaximum(self.skillCap)
        self.exorcismSkill.setMaximum(self.skillCap)
        self.healingSkill.setMaximum(self.skillCap)
        self.demonologySkill.setMaximum(self.skillCap)
        self.metamorphosisSkill.setMaximum(self.skillCap)
        self.necromancySkill.setMaximum(self.skillCap)
        self.clairvoyanceSkill.setMaximum(self.skillCap)
        self.psychokinesisSkill.setMaximum(self.skillCap)
        self.telepathySkill.setMaximum(self.skillCap)

        self.game_name = 'Girls Gone Vampire'
        self.char_folder = 'Girls Gone Vampire Characters'
        self.file_extension = '.tps'
        self.file_format = 3.2

        # Set the About menu item
        self.popAboutDialog = aboutDialog()

        # Set the Alert menu item
        self.popAlertDialog=alertDialog()

        # Set the Save menu item
        self.popSaveDialog=saveDialog()

        log.info('PyQt5 MainWindow initialized.')

        if __expired_tag__ is True:
            '''
            Beta for this app has expired!
            '''
            log.warning(__app__ + ' expiration detected...')
            self.alert_window()
            '''
            display alert message and disable all the things
            '''
            self.clearButton.setDisabled(True)
            self.actionClear.setDisabled(True)
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.loadButton.setDisabled(True)
            self.actionLoad.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
            self.actionVisit_Blog.setDisabled(True)
            self.actionFeedback.setDisabled(True)
            self.actionOverview.setDisabled(True)
            self.actionAbout_GGV_CharGen.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.additional1Display.setDisabled(True)
            self.agilitySkill.setDisabled(True)
            self.beautySkill.setDisabled(True)
            self.strengthSkill.setDisabled(True)
            self.knowledgeSkill.setDisabled(True)
            self.perceptionSkill.setDisabled(True)
            self.technologySkill.setDisabled(True)
            self.charismaSkill.setDisabled(True)
            self.empathySkill.setDisabled(True)
            self.focusSkill.setDisabled(True)
            self.boxingSkill.setDisabled(True)
            self.meleeSkill.setDisabled(True)
            self.rangedSkill.setDisabled(True)
            self.artSkill.setDisabled(True)
            self.languagesSkill.setDisabled(True)
            self.scienceSkill.setDisabled(True)
            self.dodgeSkill.setDisabled(True)
            self.parrySkill.setDisabled(True)
            self.strikeSkill.setDisabled(True)
            self.blessSkill.setDisabled(True)
            self.exorcismSkill.setDisabled(True)
            self.healingSkill.setDisabled(True)
            self.demonologySkill.setDisabled(True)
            self.metamorphosisSkill.setDisabled(True)
            self.necromancySkill.setDisabled(True)
            self.clairvoyanceSkill.setDisabled(True)
            self.psychokinesisSkill.setDisabled(True)
            self.telepathySkill.setDisabled(True)
            self.additional2Display.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderBox.setDisabled(True)
            self.cultBox.setDisabled(True)
            self.roleBox.setDisabled(True)
            self.coverBox.setDisabled(True)
            self.xpEdit.setDisabled(True)
            self.rewardDisplay.setDisabled(True)
            self.levelDisplay.setDisabled(True)
            self.armorDisplay.setDisabled(True)
            self.weaponDisplay.setDisabled(True)
            self.itemsDisplay.setDisabled(True)
            self.specialDisplay.setDisabled(True)
            self.traitsDisplay.setDisabled(True)
            self.backstoryDisplay.setDisabled(True)
            self.notesDisplay.setDisabled(True)
            self.encumbered_checkBox.setDisabled(True)
        else:
            '''
            Create .tpsrpg folder and tps.ini file the first time this program is run.
            Also, create the save folder for this program to save its .tps files in.
            '''
            self.temp_dir = os.path.expanduser('~')
            os.chdir(self.temp_dir)
            if not os.path.exists('.tpsrpg'):
                os.mkdir('.tpsrpg')
            os.chdir(self.temp_dir + '\.tpsrpg')
            if not os.path.exists(self.char_folder):
                os.mkdir(self.char_folder)
                log.info(self.char_folder + ' folder created')
            if not os.path.exists('tps.ini'):
                with open('tps.ini', 'w') as f:
                    f.write('[CharGen Folders]\n')
                    f.write(self.char_folder + '\n')
                log.info('tps.ini created and initialized')
            else:
                self.contains_foldername = False
                with open('tps.ini', 'r') as f:
                    if self.char_folder in f.read():
                        self.contains_foldername = True
                if not self.contains_foldername:
                    with open('tps.ini', 'a') as f:
                        f.write(self.char_folder + '\n')
                    log.info(self.char_folder + ' added to TPS folder list')

    #   Initialize Attribute Scores
    
        self.body = 0
        self.mind = 1
        self.spirit = 2

        self.attribute_name = ['BODY', 'MIND', 'SPIRIT']
        self.attribute_score = [1, 1, 1]

    #   Initialize Status Levels

        self.health = 0
        self.sanity = 1
        self.morale = 2

        self.status_name = ['HEALTH', 'SANITY', 'MORALE']
        self.status_level = [2, 2, 2]

        self.bodyScore.setValue(self.attribute_score[self.body])
        self.mindScore.setValue(self.attribute_score[self.mind])
        self.spiritScore.setValue(self.attribute_score[self.spirit])
        self.tempbodyScore = self.bodyScore.value()
        self.tempmindScore = self.mindScore.value()
        self.tempspiritScore = self.spiritScore.value()

        self.additional_attribute_points = 0
        self.additional1Display.setText('')

        self.healthDisplay.setText(str(self.status_level[self.health] + self.attribute_score[self.body]))
        self.sanityDisplay.setText(str(self.status_level[self.sanity] + self.attribute_score[self.mind]))
        self.moraleDisplay.setText(str(self.status_level[self.morale] + self.attribute_score[self.spirit]))        

    #   Initialize Skill Levels

        self.additional_skill_points = 0
        self.agilitySkill.setValue(0)
        self.beautySkill.setValue(0)
        self.strengthSkill.setValue(0)
        self.knowledgeSkill.setValue(0)
        self.perceptionSkill.setValue(0)
        self.technologySkill.setValue(0)
        self.charismaSkill.setValue(0)
        self.empathySkill.setValue(0)
        self.focusSkill.setValue(0)
        self.boxingSkill.setValue(0)
        self.meleeSkill.setValue(0)
        self.rangedSkill.setValue(0)
        self.artSkill.setValue(0)
        self.languagesSkill.setValue(0)
        self.scienceSkill.setValue(0)
        self.dodgeSkill.setValue(0)
        self.parrySkill.setValue(0)
        self.strikeSkill.setValue(0)
        self.blessSkill.setValue(0)
        self.exorcismSkill.setValue(0)
        self.healingSkill.setValue(0)
        self.demonologySkill.setValue(0)
        self.metamorphosisSkill.setValue(0)
        self.necromancySkill.setValue(0)
        self.clairvoyanceSkill.setValue(0)
        self.psychokinesisSkill.setValue(0)
        self.telepathySkill.setValue(0)
        self.tempagilitySkill = self.agilitySkill.value()
        self.tempbeautySkill = self.beautySkill.value()
        self.tempstrengthSkill = self.strengthSkill.value()
        self.tempknowledgeSkill = self.knowledgeSkill.value()
        self.tempperceptionSkill = self.perceptionSkill.value()
        self.temptechnologySkill = self.technologySkill.value()
        self.tempcharismaSkill = self.charismaSkill.value()
        self.tempempathySkill = self.empathySkill.value()
        self.tempfocusSkill = self.focusSkill.value()
        self.tempboxingSkill = self.boxingSkill.value()
        self.tempmeleeSkill = self.meleeSkill.value()
        self.temprangedSkill = self.rangedSkill.value()
        self.tempartSkill = self.artSkill.value()
        self.templanguagesSkill = self.languagesSkill.value()
        self.tempscienceSkill = self.scienceSkill.value()
        self.tempdodgeSkill = self.dodgeSkill.value()
        self.tempparrySkill = self.parrySkill.value()
        self.tempstrikeSkill = self.strikeSkill.value()
        self.tempblessSkill = self.blessSkill.value()
        self.tempexorcismSkill = self.exorcismSkill.value()
        self.temphealingSkill = self.healingSkill.value()
        self.tempdemonologySkill = self.demonologySkill.value()
        self.tempmetamorphosisSkill = self.metamorphosisSkill.value()
        self.tempnecromancySkill = self.necromancySkill.value()
        self.tempclairvoyanceSkill = self.clairvoyanceSkill.value()
        self.temppsychokinesisSkill = self.psychokinesisSkill.value()
        self.temptelepathySkill = self.telepathySkill.value()
        
    #   Initialize Movement and Range

        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')

    def encumbered_checkBox_changed(self):
        self.encumbered_flag = self.encumbered_checkBox.isChecked()
        red_flag = False
        temp_encumbrance = 1 + self.bodyScore.value() + self.strengthSkill.value()
        temp_movement = 1 + self.bodyScore.value() + self.agilitySkill.value()
        temp_range = 1 + self.bodyScore.value() + self.strengthSkill.value()
        if int(self.healthDisplay.text()) > 1 and not self.encumbered_flag:
            log.debug('Character can move fine.')
        elif int(self.healthDisplay.text()) == 1:
            red_flag = True
            temp_movement = temp_movement // 2
            temp_range = temp_range // 2
            log.debug("Wounded character's movement is cut in half.")
        elif int(self.healthDisplay.text()) < 1:
            red_flag = True
            temp_movement = 0
            temp_range = 0
            log.debug("Character can't move.")
        if self.encumbered_flag:
            red_flag = True
            temp_movement = temp_movement // 2
            temp_range = temp_range // 2
            log.debug("Encumbered character's movement is cut in half.")
        self.encumbranceDisplay.setText(str(temp_encumbrance) + ' items')
        if self.encumbered_flag:
            self.encumberedStatus.setText('<span style=" color:#ff0000;">Encumbered</span>')
        else:
            self.encumberedStatus.setText('')
        if red_flag:
            self.movementDisplay.setText('<span style=" color:#ff0000;">' + str(temp_movement) + ' spaces</span>')
            self.rangeDisplay.setText('<span style=" color:#ff0000;">' + str(temp_range) + ' miles</span>')
        else:
            self.movementDisplay.setText(str(temp_movement) + ' spaces')
            self.rangeDisplay.setText(str(temp_range) + ' miles')

    def clearButton_clicked(self):
        '''
        Clear all the fields
        '''
        log.info('Clear all fields')
        self.status_level = [2, 2, 2]

        self.bodyScore.setValue(self.attribute_score[self.body])
        self.mindScore.setValue(self.attribute_score[self.mind])
        self.spiritScore.setValue(self.attribute_score[self.spirit])
        self.tempbodyScore = self.bodyScore.value()
        self.tempmindScore = self.mindScore.value()
        self.tempspiritScore = self.spiritScore.value()

        #self.additional_attribute_points = 3
        self.additional1Display.setText('')

        self.healthDisplay.setText(str(self.status_level[self.health] + self.attribute_score[self.body]))
        self.sanityDisplay.setText(str(self.status_level[self.sanity] + self.attribute_score[self.mind]))
        self.moraleDisplay.setText(str(self.status_level[self.morale] + self.attribute_score[self.spirit]))

        self.scoreCap = 3
        self.skillCap = 3

        self.bodyScore.setMaximum(self.scoreCap)
        self.mindScore.setMaximum(self.scoreCap)
        self.spiritScore.setMaximum(self.scoreCap)
        self.agilitySkill.setMaximum(self.skillCap)
        self.beautySkill.setMaximum(self.skillCap)
        self.strengthSkill.setMaximum(self.skillCap)
        self.knowledgeSkill.setMaximum(self.skillCap)
        self.perceptionSkill.setMaximum(self.skillCap)
        self.technologySkill.setMaximum(self.skillCap)
        self.charismaSkill.setMaximum(self.skillCap)
        self.empathySkill.setMaximum(self.skillCap)
        self.focusSkill.setMaximum(self.skillCap)
        self.boxingSkill.setMaximum(self.skillCap)
        self.meleeSkill.setMaximum(self.skillCap)
        self.rangedSkill.setMaximum(self.skillCap)
        self.artSkill.setMaximum(self.skillCap)
        self.languagesSkill.setMaximum(self.skillCap)
        self.scienceSkill.setMaximum(self.skillCap)
        self.dodgeSkill.setMaximum(self.skillCap)
        self.parrySkill.setMaximum(self.skillCap)
        self.strikeSkill.setMaximum(self.skillCap)
        self.blessSkill.setMaximum(self.skillCap)
        self.exorcismSkill.setMaximum(self.skillCap)
        self.healingSkill.setMaximum(self.skillCap)
        self.demonologySkill.setMaximum(self.skillCap)
        self.metamorphosisSkill.setMaximum(self.skillCap)
        self.necromancySkill.setMaximum(self.skillCap)
        self.clairvoyanceSkill.setMaximum(self.skillCap)
        self.psychokinesisSkill.setMaximum(self.skillCap)
        self.telepathySkill.setMaximum(self.skillCap)
        self.agilitySkill.setValue(0)
        self.beautySkill.setValue(0)
        self.strengthSkill.setValue(0)
        self.knowledgeSkill.setValue(0)
        self.perceptionSkill.setValue(0)
        self.technologySkill.setValue(0)
        self.charismaSkill.setValue(0)
        self.empathySkill.setValue(0)
        self.focusSkill.setValue(0)
        self.boxingSkill.setValue(0)
        self.meleeSkill.setValue(0)
        self.rangedSkill.setValue(0)
        self.artSkill.setValue(0)
        self.languagesSkill.setValue(0)
        self.scienceSkill.setValue(0)
        self.dodgeSkill.setValue(0)
        self.parrySkill.setValue(0)
        self.strikeSkill.setValue(0)
        self.blessSkill.setValue(0)
        self.exorcismSkill.setValue(0)
        self.healingSkill.setValue(0)
        self.demonologySkill.setValue(0)
        self.metamorphosisSkill.setValue(0)
        self.necromancySkill.setValue(0)
        self.clairvoyanceSkill.setValue(0)
        self.psychokinesisSkill.setValue(0)
        self.telepathySkill.setValue(0)
        self.tempagilitySkill = self.agilitySkill.value()
        self.tempbeautySkill = self.beautySkill.value()
        self.tempstrengthSkill = self.strengthSkill.value()
        self.tempknowledgeSkill = self.knowledgeSkill.value()
        self.tempperceptionSkill = self.perceptionSkill.value()
        self.temptechnologySkill = self.technologySkill.value()
        self.tempcharismaSkill = self.charismaSkill.value()
        self.tempempathySkill = self.empathySkill.value()
        self.tempfocusSkill = self.focusSkill.value()
        self.tempboxingSkill = self.boxingSkill.value()
        self.tempmeleeSkill = self.meleeSkill.value()
        self.temprangedSkill = self.rangedSkill.value()
        self.tempartSkill = self.artSkill.value()
        self.templanguagesSkill = self.languagesSkill.value()
        self.tempscienceSkill = self.scienceSkill.value()
        self.tempdodgeSkill = self.dodgeSkill.value()
        self.tempparrySkill = self.parrySkill.value()
        self.tempstrikeSkill = self.strikeSkill.value()
        self.tempblessSkill = self.blessSkill.value()
        self.tempexorcismSkill = self.exorcismSkill.value()
        self.temphealingSkill = self.healingSkill.value()
        self.tempdemonologySkill = self.demonologySkill.value()
        self.tempmetamorphosisSkill = self.metamorphosisSkill.value()
        self.tempnecromancySkill = self.necromancySkill.value()
        self.tempclairvoyanceSkill = self.clairvoyanceSkill.value()
        self.temppsychokinesisSkill = self.psychokinesisSkill.value()
        self.temptelepathySkill = self.telepathySkill.value()

        #self.deptBox.setCurrentIndex(0)

        self.skilling_up = False
        self.attributing_up = False
        self.is_martial = False
        self.is_divine = False
        self.is_occult = False
        self.is_psionic = False
        self.is_vampire = 'No'

        self.agilitySkill.setDisabled(True)
        self.beautySkill.setDisabled(True)
        self.strengthSkill.setDisabled(True)
        self.knowledgeSkill.setDisabled(True)
        self.perceptionSkill.setDisabled(True)
        self.technologySkill.setDisabled(True)
        self.charismaSkill.setDisabled(True)
        self.empathySkill.setDisabled(True)
        self.focusSkill.setDisabled(True)
        self.boxingSkill.setDisabled(True)
        self.meleeSkill.setDisabled(True)
        self.rangedSkill.setDisabled(True)
        self.artSkill.setDisabled(True)
        self.languagesSkill.setDisabled(True)
        self.scienceSkill.setDisabled(True)
        self.dodgeSkill.setDisabled(True)
        self.parrySkill.setDisabled(True)
        self.strikeSkill.setDisabled(True)
        self.blessSkill.setDisabled(True)
        self.exorcismSkill.setDisabled(True)
        self.healingSkill.setDisabled(True)
        self.demonologySkill.setDisabled(True)
        self.metamorphosisSkill.setDisabled(True)
        self.necromancySkill.setDisabled(True)
        self.clairvoyanceSkill.setDisabled(True)
        self.psychokinesisSkill.setDisabled(True)
        self.telepathySkill.setDisabled(True)

        self.char_level = 1
        self.levelDisplay.setText(str(self.char_level))
        self.xpEdit.setDisabled(True)
        self.char_xp = 0
        self.xpEdit.setText(str(self.char_xp))
        self.level_achieved = 100
        self.next_level = 200

        self.encumbered_checkBox.setDisabled(True)
        self.encumbered_flag = False
        self.encumbered_checkBox.setChecked(self.encumbered_flag)
        self.charnameEdit.setText('Sample Char')
        self.charnameEdit.setDisabled(False)
        self.ageEdit.setText('')
        self.ageEdit.setDisabled(False)
        self.genderBox.setCurrentIndex(0)
        self.genderBox.setDisabled(False)
        self.gender = ''
        self.gender_not_chosen = True
        self.cultBox.clear()
        self.cultBox.addItem('Choose')
        self.cult_not_chosen = True
        self.cultBox.setCurrentIndex(0)
        self.cultBox.setDisabled(True)
        self.role_not_chosen = True
        self.roleBox.setCurrentIndex(0)
        self.roleBox.setDisabled(True)
        self.choosing_extra_8_skills = False
        self.cover_not_chosen = True
        self.coverBox.setCurrentIndex(0)
        self.coverBox.setDisabled(True)
        self.rewardDisplay.setText('None')
        self.healthStatus.setText('')
        self.sanityStatus.setText('')
        self.moraleStatus.setText('')
        self.bodyScore.setDisabled(True)
        self.mindScore.setDisabled(True)
        self.spiritScore.setDisabled(True)
        self.armorDisplay.setPlainText('None')
        self.weaponDisplay.setPlainText('None')
        self.itemsDisplay.setPlainText('None')
        self.specialDisplay.setPlainText('None')
        self.traitsDisplay.setPlainText('')
        self.backstoryDisplay.setPlainText('')
        self.notesDisplay.setPlainText('')

        self.additional_skill_points = 0
        self.additional2Display.setText('')

    def bodyScore_valueChanged(self):
        '''
        A Body Score was entered.
        Add/substract from additional Attribute points.
        '''
        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
        self.additional_attribute_points += self.tempbodyScore - self.bodyScore.value()
        if self.additional_attribute_points >= 0:
            self.additional1Display.setText(str(self.additional_attribute_points))
        else:
            self.additional1Display.setText('<span style=" color:#ff0000;">' + str(self.additional_attribute_points) + '</span>')
        self.tempbodyScore = self.bodyScore.value()
        self.healthDisplay.setText(str(self.status_level[self.health] + self.bodyScore.value()))
        if self.additional_attribute_points == 0:
            self.bodyScore.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.additional1Display.setText('')
            self.xpEdit.setDisabled(False)
            self.encumbered_checkBox.setDisabled(False)
            self.saveButton.setDisabled(False)
            self.actionSave.setDisabled(False)
            self.printButton.setDisabled(False)
            self.actionPrint.setDisabled(False)
            if self.attributing_up:
                self.attributing_up = False

    def mindScore_valueChanged(self):
        '''
        A Mind Score was entered.
        Add/substract from additional Attribute points.
        '''
        self.additional_attribute_points += self.tempmindScore - self.mindScore.value()
        if self.additional_attribute_points >= 0:
            self.additional1Display.setText(str(self.additional_attribute_points))
        else:
            self.additional1Display.setText('<span style=" color:#ff0000;">' + str(self.additional_attribute_points) + '</span>')
        self.tempmindScore = self.mindScore.value()
        self.sanityDisplay.setText(str(self.status_level[self.sanity] + self.mindScore.value()))
        if self.additional_attribute_points == 0:
            self.bodyScore.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.additional1Display.setText('')
            self.xpEdit.setDisabled(False)
            self.encumbered_checkBox.setDisabled(False)
            self.saveButton.setDisabled(False)
            self.actionSave.setDisabled(False)
            self.printButton.setDisabled(False)
            self.actionPrint.setDisabled(False)
            if self.attributing_up:
                self.attributing_up = False

    def spiritScore_valueChanged(self):
        '''
        A Spirit Score was entered.
        Add/substract from additional Attribute points.
        '''
        self.additional_attribute_points += self.tempspiritScore - self.spiritScore.value()
        if self.additional_attribute_points >= 0:
            self.additional1Display.setText(str(self.additional_attribute_points))
        else:
            self.additional1Display.setText('<span style=" color:#ff0000;">' + str(self.additional_attribute_points) + '</span>')
        self.tempspiritScore = self.spiritScore.value()
        self.moraleDisplay.setText(str(self.status_level[self.morale] + self.spiritScore.value()))
        if self.additional_attribute_points == 0:
            self.bodyScore.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.additional1Display.setText('')
            self.xpEdit.setDisabled(False)
            self.encumbered_checkBox.setDisabled(False)
            self.saveButton.setDisabled(False)
            self.actionSave.setDisabled(False)
            self.printButton.setDisabled(False)
            self.actionPrint.setDisabled(False)
            if self.attributing_up:
                self.attributing_up = False
    
    def agilitySkill_valueChanged(self):
        '''
        An Agility Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
        self.additional_skill_points += self.tempagilitySkill - self.agilitySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempagilitySkill = self.agilitySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.dodgeSkill.setDisabled(True)
                self.parrySkill.setDisabled(True)
                self.strikeSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            
    
    def beautySkill_valueChanged(self):
        '''
        A Beauty Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempbeautySkill - self.beautySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempbeautySkill = self.beautySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)

    def strengthSkill_valueChanged(self):
        '''
        A Strength Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
        self.additional_skill_points += self.tempstrengthSkill - self.strengthSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempstrengthSkill = self.strengthSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def knowledgeSkill_valueChanged(self):
        '''
        A Knowledge Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempknowledgeSkill - self.knowledgeSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempknowledgeSkill = self.knowledgeSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def perceptionSkill_valueChanged(self):
        '''
        A Perception Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempperceptionSkill - self.perceptionSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempperceptionSkill = self.perceptionSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def technologySkill_valueChanged(self):
        '''
        A Technology Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temptechnologySkill - self.technologySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temptechnologySkill = self.technologySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
        
    def charismaSkill_valueChanged(self):
        '''
        A Charisma Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempcharismaSkill - self.charismaSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempcharismaSkill = self.charismaSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def empathySkill_valueChanged(self):
        '''
        An Empathy Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempempathySkill - self.empathySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempempathySkill = self.empathySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def focusSkill_valueChanged(self):
        '''
        A Focus Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempfocusSkill - self.focusSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempfocusSkill = self.focusSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def boxingSkill_valueChanged(self):
        '''
        A Boxing Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempboxingSkill - self.boxingSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempboxingSkill = self.boxingSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def meleeSkill_valueChanged(self):
        '''
        A Melee Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempmeleeSkill - self.meleeSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempmeleeSkill = self.meleeSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def rangedSkill_valueChanged(self):
        '''
        A Ranged Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temprangedSkill - self.rangedSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temprangedSkill = self.rangedSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def artSkill_valueChanged(self):
        '''
        A Art Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempartSkill - self.artSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempartSkill = self.artSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def languagesSkill_valueChanged(self):
        '''
        A Languages Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.templanguagesSkill - self.languagesSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.templanguagesSkill = self.languagesSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def scienceSkill_valueChanged(self):
        '''
        A Science Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempscienceSkill - self.scienceSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempscienceSkill = self.scienceSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def dodgeSkill_valueChanged(self):
        '''
        A Dodge Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempdodgeSkill - self.dodgeSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempdodgeSkill = self.dodgeSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)

    def parrySkill_valueChanged(self):
        '''
        A Parry Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempparrySkill - self.parrySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempparrySkill = self.parrySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)

    def strikeSkill_valueChanged(self):
        '''
        A Strike Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempstrikeSkill - self.strikeSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempstrikeSkill = self.strikeSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def blessSkill_valueChanged(self):
        '''
        A Bless Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempblessSkill - self.blessSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempblessSkill = self.blessSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def exorcismSkill_valueChanged(self):
        '''
        A Exorcism Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempexorcismSkill - self.exorcismSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempexorcismSkill = self.exorcismSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def healingSkill_valueChanged(self):
        '''
        A Healing Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temphealingSkill - self.healingSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temphealingSkill = self.healingSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def demonologySkill_valueChanged(self):
        '''
        A Demonology Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempdemonologySkill - self.demonologySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempdemonologySkill = self.demonologySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def metamorphosisSkill_valueChanged(self):
        '''
        A Metamorphosis Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempmetamorphosisSkill - self.metamorphosisSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempmetamorphosisSkill = self.metamorphosisSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def necromancySkill_valueChanged(self):
        '''
        A Necromancy Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempnecromancySkill - self.necromancySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempnecromancySkill = self.necromancySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def clairvoyanceSkill_valueChanged(self):
        '''
        A Clairvoyance Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempclairvoyanceSkill - self.clairvoyanceSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempclairvoyanceSkill = self.clairvoyanceSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def psychokinesisSkill_valueChanged(self):
        '''
        A Psychokinesis Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temppsychokinesisSkill - self.psychokinesisSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temppsychokinesisSkill = self.psychokinesisSkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def telepathySkill_valueChanged(self):
        '''
        A Telepathy Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temptelepathySkill - self.telepathySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temptelepathySkill = self.telepathySkill.value()
        if self.additional_skill_points == 0:
            if self.skilling_up:
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                        self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                        self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setDisabled(True)
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setDisabled(True)
                self.artSkill.setDisabled(True)
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.skilling_up = False
            else:
                if self.role_not_chosen:
                    self.roleBox.setDisabled(False)
                else:
                    if self.choosing_extra_8_skills == False:
                        self.choosing_extra_8_skills = True
                        self.additional_skill_points = 8
                        self.additional2Display.setText(str(self.additional_skill_points))
                        self.agilitySkill.setDisabled(False)
                        self.beautySkill.setDisabled(False)
                        self.strengthSkill.setDisabled(False)
                        self.knowledgeSkill.setDisabled(False)
                        self.perceptionSkill.setDisabled(False)
                        self.technologySkill.setDisabled(False)
                        self.charismaSkill.setDisabled(False)
                        self.empathySkill.setDisabled(False)
                        self.focusSkill.setDisabled(False)
                        self.boxingSkill.setDisabled(False)
                        self.meleeSkill.setDisabled(False)
                        self.rangedSkill.setDisabled(False)
                        self.artSkill.setDisabled(False)
                        self.languagesSkill.setDisabled(False)
                        self.scienceSkill.setDisabled(False)
                    else:
                        self.agilitySkill.setDisabled(True)
                        self.beautySkill.setDisabled(True)
                        self.strengthSkill.setDisabled(True)
                        self.knowledgeSkill.setDisabled(True)
                        self.perceptionSkill.setDisabled(True)
                        self.technologySkill.setDisabled(True)
                        self.charismaSkill.setDisabled(True)
                        self.empathySkill.setDisabled(True)
                        self.focusSkill.setDisabled(True)
                        self.boxingSkill.setDisabled(True)
                        self.meleeSkill.setDisabled(True)
                        self.rangedSkill.setDisabled(True)
                        self.artSkill.setDisabled(True)
                        self.languagesSkill.setDisabled(True)
                        self.scienceSkill.setDisabled(True)
                        self.dodgeSkill.setDisabled(True)
                        self.parrySkill.setDisabled(True)
                        self.strikeSkill.setDisabled(True)
                        self.blessSkill.setDisabled(True)
                        self.exorcismSkill.setDisabled(True)
                        self.healingSkill.setDisabled(True)
                        self.demonologySkill.setDisabled(True)
                        self.metamorphosisSkill.setDisabled(True)
                        self.necromancySkill.setDisabled(True)
                        self.clairvoyanceSkill.setDisabled(True)
                        self.psychokinesisSkill.setDisabled(True)
                        self.telepathySkill.setDisabled(True)
                        self.coverBox.setDisabled(False)
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    #self.saveButton.setDisabled(False)
                    #self.actionSave.setDisabled(False)
        else:
            if self.skilling_up:
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
            else:
                self.roleBox.setDisabled(True)
                self.encumbered_checkBox.setDisabled(True)
                self.charnameEdit.setDisabled(True)
                self.rewardDisplay.setText('None')
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
    
    def genderBox_changed(self):
        '''
        A gender was chosen for the character
        '''
        if self.gender_not_chosen:
            if self.genderBox.currentIndex() == 0:
                self.gender = ''
                self.gender_not_chosen = True
                self.cult_not_chosen = True
                self.cultBox.setDisabled(True)
            else:
                self.gender = self.gender_choice[self.genderBox.currentIndex()]
                self.genderBox.setDisabled(True)
                self.gender_not_chosen = True
                self.cult_not_chosen = True
                self.cultBox.setDisabled(False)
                self.cultBox.clear()
                if self.gender == 'Male':
                    self.cult_choice = ['Choose', 'Hantu Belian', 'Blood Knight', 'Utopian Legion', 'Personality']
                    self.cult_skill = ['', 'Occult', 'Divine', 'Mind', 'Body']
                else:
                    self.cult_choice = ['Choose', 'Boeotian Club', 'Hantu Belian', 'Goddess Cult', 'Utopian Legion', 'Personality']
                    self.cult_skill = ['', 'Strange', 'Occult', 'Spirit', 'Mind', 'Body']
                for i in self.cult_choice:
                    self.cultBox.addItem(i)
                self.cultBox.setCurrentIndex(0)
                self.gender_not_chosen = False                                    
    
    def cultBox_changed(self):
        '''
        A cult was chosen for the character
        '''
        if self.gender_not_chosen == False:
            if self.cult_not_chosen:
                if self.cultBox.currentIndex() == 0:
                    self.cult = ''
                    self.cult_not_chosen = True
                    #self.bodyScore.setDisabled(True)
                    #self.mindScore.setDisabled(True)
                    #self.spiritScore.setDisabled(True)
                else:
                    self.cult = self.cult_choice[self.cultBox.currentIndex()]
                    self.cultSkills = self.cult_skill[self.cultBox.currentIndex()]
                    self.cultBox.setDisabled(True)
                    self.cult_not_chosen = False
                    #self.bodyScore.setDisabled(False)
                    #self.mindScore.setDisabled(False)
                    #self.spiritScore.setDisabled(False)
                    self.additional_skill_points = 3
                    self.additional2Display.setText(str(self.additional_skill_points))
                    # Pick skills from cult
                    if self.cultSkills == 'Strange':
                        self.artSkill.setDisabled(False)
                        self.artSkill.setMaximum(4)
                        self.languagesSkill.setDisabled(False)
                        self.languagesSkill.setMaximum(4)
                        self.scienceSkill.setDisabled(False)
                        self.scienceSkill.setMaximum(4)
                    if self.cultSkills == 'Occult':
                        self.demonologySkill.setDisabled(False)
                        self.demonologySkill.setMaximum(4)
                        self.metamorphosisSkill.setDisabled(False)
                        self.metamorphosisSkill.setMaximum(4)
                        self.necromancySkill.setDisabled(False)
                        self.necromancySkill.setMaximum(4)
                    if self.cultSkills == 'Spirit':
                        self.charismaSkill.setDisabled(False)
                        self.charismaSkill.setMaximum(4)
                        self.empathySkill.setDisabled(False)
                        self.empathySkill.setMaximum(4)
                        self.focusSkill.setDisabled(False)
                        self.focusSkill.setMaximum(4)
                    if self.cultSkills == 'Divine':
                        self.blessSkill.setDisabled(False)
                        self.blessSkill.setMaximum(4)
                        self.exorcismSkill.setDisabled(False)
                        self.exorcismSkill.setMaximum(4)
                        self.healingSkill.setDisabled(False)
                        self.healingSkill.setMaximum(4)
                    if self.cultSkills == 'Mind':
                        self.knowledgeSkill.setDisabled(False)
                        self.knowledgeSkill.setMaximum(4)
                        self.perceptionSkill.setDisabled(False)
                        self.perceptionSkill.setMaximum(4)
                        self.technologySkill.setDisabled(False)
                        self.technologySkill.setMaximum(4)
                    if self.cultSkills == 'Body':
                        self.agilitySkill.setDisabled(False)
                        self.agilitySkill.setMaximum(4)
                        self.beautySkill.setDisabled(False)
                        self.beautySkill.setMaximum(4)
                        self.strengthSkill.setDisabled(False)
                        self.strengthSkill.setMaximum(4)
                    

                    #self.roleBox.setDisabled(False)

    
    def roleBox_changed(self):
        '''
        A role was chosen for the character
        '''
        #self.cultBox.setDisabled(True)
        if self.cult_not_chosen == False:
            if self.role_not_chosen:
                if self.roleBox.currentIndex() == 0:
                    self.role = ''
                    self.role_not_chosen = True
                else:
                    self.role = self.role_choice[self.roleBox.currentIndex()]
                    self.roleSkills = self.role_skill[self.roleBox.currentIndex()]
                    self.itemsDisplay.setPlainText(self.role_item[self.roleBox.currentIndex()])
                    self.roleBox.setDisabled(True)
                    self.role_not_chosen = False
                    self.additional_skill_points = 3
                    self.additional2Display.setText(str(self.additional_skill_points))

                    # Pick skills from role
                    if self.roleSkills == 'Body':
                        self.agilitySkill.setDisabled(False)
                        self.agilitySkill.setMaximum(4)
                        self.beautySkill.setDisabled(False)
                        self.beautySkill.setMaximum(4)
                        self.strengthSkill.setDisabled(False)
                        self.strengthSkill.setMaximum(4)
                    if self.roleSkills == 'Mind':
                        self.knowledgeSkill.setDisabled(False)
                        self.knowledgeSkill.setMaximum(4)
                        self.perceptionSkill.setDisabled(False)
                        self.perceptionSkill.setMaximum(4)
                        self.technologySkill.setDisabled(False)
                        self.technologySkill.setMaximum(4)
                    if self.roleSkills == 'Spirit':
                        self.charismaSkill.setDisabled(False)
                        self.charismaSkill.setMaximum(4)
                        self.empathySkill.setDisabled(False)
                        self.empathySkill.setMaximum(4)
                        self.focusSkill.setDisabled(False)
                        self.focusSkill.setMaximum(4)
                    if self.roleSkills == 'Combat':
                        self.boxingSkill.setDisabled(False)
                        self.boxingSkill.setMaximum(4)
                        self.meleeSkill.setDisabled(False)
                        self.meleeSkill.setMaximum(4)
                        self.rangedSkill.setDisabled(False)
                        self.rangedSkill.setMaximum(4)
                    if self.roleSkills == 'Strange':
                        self.artSkill.setDisabled(False)
                        self.artSkill.setMaximum(4)
                        self.languagesSkill.setDisabled(False)
                        self.languagesSkill.setMaximum(4)
                        self.scienceSkill.setDisabled(False)
                        self.scienceSkill.setMaximum(4)
                    if self.roleSkills == 'Martial':
                        self.dodgeSkill.setDisabled(False)
                        self.dodgeSkill.setMaximum(4)
                        self.parrySkill.setDisabled(False)
                        self.parrySkill.setMaximum(4)
                        self.strikeSkill.setDisabled(False)
                        self.strikeSkill.setMaximum(4)
                    if self.roleSkills == 'Psionics':
                        self.clairvoyanceSkill.setDisabled(False)
                        self.clairvoyanceSkill.setMaximum(4)
                        self.psychokinesisSkill.setDisabled(False)
                        self.psychokinesisSkill.setMaximum(4)
                        self.telepathySkill.setDisabled(False)
                        self.telepathySkill.setMaximum(4)
                    if self.roleSkills == 'Divine':
                        self.blessSkill.setDisabled(False)
                        self.blessSkill.setMaximum(4)
                        self.exorcismSkill.setDisabled(False)
                        self.exorcismSkill.setMaximum(4)
                        self.healingSkill.setDisabled(False)
                        self.healingSkill.setMaximum(4)
                    if self.roleSkills == 'Occult':
                        self.demonologySkill.setDisabled(False)
                        self.demonologySkill.setMaximum(4)
                        self.metamorphosisSkill.setDisabled(False)
                        self.metamorphosisSkill.setMaximum(4)
                        self.necromancySkill.setDisabled(False)
                        self.necromancySkill.setMaximum(4)
                
    def coverBox_changed(self):
        '''
        A cover was chosen for the character
        '''
        if self.role_not_chosen == False:
            if self.cover_not_chosen:
                if self.coverBox.currentIndex() == 0:
                    self.cover = ''
                    self.cover_not_chosen = True
                else:
                    self.cover = self.cover_choice[self.coverBox.currentIndex()]
                    self.skill_bonus = self.cover_bonus[self.coverBox.currentIndex()]
                    self.armorDisplay.setPlainText(self.cover_clothes[self.coverBox.currentIndex()])
                    self.coverBox.setDisabled(True)
                    self.cover_not_chosen = False

                    # Add skill bonus from cover
                    if self.skill_bonus == 'Agility':
                        self.agilitySkill.setMaximum(5)
                        self.agilitySkill.setValue(self.agilitySkill.value() + 1)
                    if self.skill_bonus == 'Beauty':
                        self.beautySkill.setMaximum(5)
                        self.beautySkill.setValue(self.beautySkill.value() + 1)
                    if self.skill_bonus == 'Strength':
                        self.strengthSkill.setMaximum(5)
                        self.strengthSkill.setValue(self.strengthSkill.value() + 1)
                    if self.skill_bonus == 'Knowledge':
                        self.knowledgeSkill.setMaximum(5)
                        self.knowledgeSkill.setValue(self.knowledgeSkill.value() + 1)
                    if self.skill_bonus == 'Perception':
                        self.perceptionSkill.setMaximum(5)
                        self.perceptionSkill.setValue(self.perceptionSkill.value() + 1)
                    if self.skill_bonus == 'Technology':
                        self.technologySkill.setMaximum(5)
                        self.technologySkill.setValue(self.technologySkill.value() + 1)
                    if self.skill_bonus == 'Charisma':
                        self.charismaSkill.setMaximum(5)
                        self.charismaSkill.setValue(self.charismaSkill.value() + 1)
                    if self.skill_bonus == 'Empathy':
                        self.empathySkill.setMaximum(5)
                        self.empathySkill.setValue(self.empathySkill.value() + 1)
                    if self.skill_bonus == 'Focus':
                        self.focusSkill.setMaximum(5)
                        self.focusSkill.setValue(self.focusSkill.value() + 1)
                    if self.skill_bonus == 'Boxing':
                        self.boxingSkill.setMaximum(5)
                        self.boxingSkill.setValue(self.boxingSkill.value() + 1)
                    if self.skill_bonus == 'Melee':
                        self.meleeSkill.setMaximum(5)
                        self.meleeSkill.setValue(self.meleeSkill.value() + 1)
                    if self.skill_bonus == 'Ranged':
                        self.rangedSkill.setMaximum(5)
                        self.rangedSkill.setValue(self.rangedSkill.value() + 1)
                    if self.skill_bonus == 'Art':
                        self.artSkill.setMaximum(5)
                        self.artSkill.setValue(self.artSkill.value() + 1)
                    if self.skill_bonus == 'Languages':
                        self.languagesSkill.setMaximum(5)
                        self.languagesSkill.setValue(self.languagesSkill.value() + 1)
                    if self.skill_bonus == 'Science':
                        self.scienceSkill.setMaximum(5)
                        self.scienceSkill.setValue(self.scienceSkill.value() + 1)
                    if self.skill_bonus == 'Clairvoyance':
                        self.clairvoyanceSkill.setMaximum(5)
                        self.clairvoyanceSkill.setValue(self.clairvoyanceSkill.value() + 1)
                    self.additional2Display.setText('')
                    self.additional_skill_points = 0
                    self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                            self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                            self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                            self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                            self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                            self.dodgeSkill.value() + self.parrySkill.value() + self.strikeSkill.value() +
                            self.blessSkill.value() + self.exorcismSkill.value() + self.healingSkill.value() +
                            self.demonologySkill.value() + self.metamorphosisSkill.value() + self.necromancySkill.value() +
                            self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                    
                    # Unlock attribute assignments
                    self.additional_attribute_points = 3
                    self.additional1Display.setText(str(self.additional_attribute_points))
                    self.bodyScore.setDisabled(False)
                    self.mindScore.setDisabled(False)
                    self.spiritScore.setDisabled(False)
    
    def xpValue_changed(self):
        current_xp = self.xpEdit.text()
        if current_xp == '':
            current_xp = 0
        else:
            current_xp = current_xp.strip('-')
            current_xp = current_xp.strip('+')
            if current_xp != '0':
                current_xp = current_xp.lstrip('0')
            current_xp = int(eval(current_xp))
        if self.char_level < 9 and current_xp >= self.level_achieved and current_xp < self.next_level:
            self.char_xp = current_xp - self.level_achieved
            self.xpEdit.setText(str(self.char_xp))
            self.char_level += 1
            self.levelDisplay.setText(str(self.char_level))
            if self.level_achieved == 100:
                self.additional_skill_points = 1
                self.additional2Display.setText(str(self.additional_skill_points))
                self.skilling_up = True
                self.skillCap = 3
                if self.agilitySkill.value() <= self.skillCap:
                    self.agilitySkill.setMaximum(self.skillCap)
                if self.beautySkill.value() <= self.skillCap:
                    self.beautySkill.setMaximum(self.skillCap)
                if self.strengthSkill.value() <= self.skillCap:
                    self.strengthSkill.setMaximum(self.skillCap)
                if self.knowledgeSkill.value() <= self.skillCap:
                    self.knowledgeSkill.setMaximum(self.skillCap)
                if self.perceptionSkill.value() <= self.skillCap:
                    self.perceptionSkill.setMaximum(self.skillCap)
                if self.technologySkill.value() <= self.skillCap:
                    self.technologySkill.setMaximum(self.skillCap)
                if self.charismaSkill.value() <= self.skillCap:
                    self.charismaSkill.setMaximum(self.skillCap)
                if self.empathySkill.value() <= self.skillCap:
                    self.empathySkill.setMaximum(self.skillCap)
                if self.focusSkill.value() <= self.skillCap:
                    self.focusSkill.setMaximum(self.skillCap)
                if self.boxingSkill.value() <= self.skillCap:
                    self.boxingSkill.setMaximum(self.skillCap)
                if self.meleeSkill.value() <= self.skillCap:
                    self.meleeSkill.setMaximum(self.skillCap)
                if self.rangedSkill.value() <= self.skillCap:
                    self.rangedSkill.setMaximum(self.skillCap)
                if self.artSkill.value() <= self.skillCap:
                    self.artSkill.setMaximum(self.skillCap)
                if self.languagesSkill.value() <= self.skillCap:
                    self.languagesSkill.setMaximum(self.skillCap)
                if self.scienceSkill.value() <= self.skillCap:
                    self.scienceSkill.setMaximum(self.skillCap)
                if self.dodgeSkill.value() <= self.skillCap:
                    self.dodgeSkill.setMaximum(self.skillCap)
                if self.parrySkill.value() <= self.skillCap:
                    self.parrySkill.setMaximum(self.skillCap)
                if self.strikeSkill.value() <= self.skillCap:
                    self.strikeSkill.setMaximum(self.skillCap)
                if self.blessSkill.value() <= self.skillCap:
                    self.blessSkill.setMaximum(self.skillCap)
                if self.exorcismSkill.value() <= self.skillCap:
                    self.exorcismSkill.setMaximum(self.skillCap)
                if self.healingSkill.value() <= self.skillCap:
                    self.healingSkill.setMaximum(self.skillCap)
                if self.demonologySkill.value() <= self.skillCap:
                    self.demonologySkill.setMaximum(self.skillCap)
                if self.metamorphosisSkill.value() <= self.skillCap:
                    self.metamorphosisSkill.setMaximum(self.skillCap)
                if self.necromancySkill.value() <= self.skillCap:
                    self.necromancySkill.setMaximum(self.skillCap)
                if self.psychokinesisSkill.value() <= self.skillCap:
                    self.psychokinesisSkill.setMaximum(self.skillCap)
                if self.clairvoyanceSkill.value() <= self.skillCap:
                    self.clairvoyanceSkill.setMaximum(self.skillCap)
                if self.telepathySkill.value() <= self.skillCap:
                    self.telepathySkill.setMaximum(self.skillCap)
                self.agilitySkill.setDisabled(False)
                self.beautySkill.setDisabled(False)
                self.strengthSkill.setDisabled(False)
                self.knowledgeSkill.setDisabled(False)
                self.perceptionSkill.setDisabled(False)
                self.technologySkill.setDisabled(False)
                self.charismaSkill.setDisabled(False)
                self.empathySkill.setDisabled(False)
                self.focusSkill.setDisabled(False)
                self.boxingSkill.setDisabled(False)
                self.meleeSkill.setDisabled(False)
                self.rangedSkill.setDisabled(False)
                self.artSkill.setDisabled(False)
                self.languagesSkill.setDisabled(False)
                self.scienceSkill.setDisabled(False)
                if self.is_martial:
                    self.dodgeSkill.setDisabled(False)
                    self.parrySkill.setDisabled(False)
                    self.strikeSkill.setDisabled(False)
                if self.is_divine:
                    self.blessSkill.setDisabled(False)
                    self.exorcismSkill.setDisabled(False)
                    self.healingSkill.setDisabled(False)
                if self.is_occult:
                    self.demonologySkill.setDisabled(False)
                    self.metamorphosisSkill.setDisabled(False)
                    self.necromancySkill.setDisabled(False)
                if self.is_psionic:
                    self.clairvoyanceSkill.setDisabled(False)
                    self.psychokinesisSkill.setDisabled(False)
                    self.telepathySkill.setDisabled(False)
                self.xpEdit.setDisabled(True)
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
                self.level_achieved = 200
                self.next_level = 500
            elif self.level_achieved == 200:
                self.additional_skill_points = 2
                self.additional2Display.setText(str(self.additional_skill_points))
                self.skilling_up = True
                self.skillCap = 4
                if self.agilitySkill.value() <= self.skillCap:
                    self.agilitySkill.setMaximum(self.skillCap)
                if self.beautySkill.value() <= self.skillCap:
                    self.beautySkill.setMaximum(self.skillCap)
                if self.strengthSkill.value() <= self.skillCap:
                    self.strengthSkill.setMaximum(self.skillCap)
                if self.knowledgeSkill.value() <= self.skillCap:
                    self.knowledgeSkill.setMaximum(self.skillCap)
                if self.perceptionSkill.value() <= self.skillCap:
                    self.perceptionSkill.setMaximum(self.skillCap)
                if self.technologySkill.value() <= self.skillCap:
                    self.technologySkill.setMaximum(self.skillCap)
                if self.charismaSkill.value() <= self.skillCap:
                    self.charismaSkill.setMaximum(self.skillCap)
                if self.empathySkill.value() <= self.skillCap:
                    self.empathySkill.setMaximum(self.skillCap)
                if self.focusSkill.value() <= self.skillCap:
                    self.focusSkill.setMaximum(self.skillCap)
                if self.boxingSkill.value() <= self.skillCap:
                    self.boxingSkill.setMaximum(self.skillCap)
                if self.meleeSkill.value() <= self.skillCap:
                    self.meleeSkill.setMaximum(self.skillCap)
                if self.rangedSkill.value() <= self.skillCap:
                    self.rangedSkill.setMaximum(self.skillCap)
                if self.artSkill.value() <= self.skillCap:
                    self.artSkill.setMaximum(self.skillCap)
                if self.languagesSkill.value() <= self.skillCap:
                    self.languagesSkill.setMaximum(self.skillCap)
                if self.scienceSkill.value() <= self.skillCap:
                    self.scienceSkill.setMaximum(self.skillCap)
                if self.dodgeSkill.value() <= self.skillCap:
                    self.dodgeSkill.setMaximum(self.skillCap)
                if self.parrySkill.value() <= self.skillCap:
                    self.parrySkill.setMaximum(self.skillCap)
                if self.strikeSkill.value() <= self.skillCap:
                    self.strikeSkill.setMaximum(self.skillCap)
                if self.blessSkill.value() <= self.skillCap:
                    self.blessSkill.setMaximum(self.skillCap)
                if self.exorcismSkill.value() <= self.skillCap:
                    self.exorcismSkill.setMaximum(self.skillCap)
                if self.healingSkill.value() <= self.skillCap:
                    self.healingSkill.setMaximum(self.skillCap)
                if self.demonologySkill.value() <= self.skillCap:
                    self.demonologySkill.setMaximum(self.skillCap)
                if self.metamorphosisSkill.value() <= self.skillCap:
                    self.metamorphosisSkill.setMaximum(self.skillCap)
                if self.necromancySkill.value() <= self.skillCap:
                    self.necromancySkill.setMaximum(self.skillCap)
                if self.psychokinesisSkill.value() <= self.skillCap:
                    self.psychokinesisSkill.setMaximum(self.skillCap)
                if self.clairvoyanceSkill.value() <= self.skillCap:
                    self.clairvoyanceSkill.setMaximum(self.skillCap)
                if self.telepathySkill.value() <= self.skillCap:
                    self.telepathySkill.setMaximum(self.skillCap)
                self.agilitySkill.setDisabled(False)
                self.beautySkill.setDisabled(False)
                self.strengthSkill.setDisabled(False)
                self.knowledgeSkill.setDisabled(False)
                self.perceptionSkill.setDisabled(False)
                self.technologySkill.setDisabled(False)
                self.charismaSkill.setDisabled(False)
                self.empathySkill.setDisabled(False)
                self.focusSkill.setDisabled(False)
                self.boxingSkill.setDisabled(False)
                self.meleeSkill.setDisabled(False)
                self.rangedSkill.setDisabled(False)
                self.artSkill.setDisabled(False)
                self.languagesSkill.setDisabled(False)
                self.scienceSkill.setDisabled(False)
                if self.is_martial:
                    self.dodgeSkill.setDisabled(False)
                    self.parrySkill.setDisabled(False)
                    self.strikeSkill.setDisabled(False)
                if self.is_divine:
                    self.blessSkill.setDisabled(False)
                    self.exorcismSkill.setDisabled(False)
                    self.healingSkill.setDisabled(False)
                if self.is_occult:
                    self.demonologySkill.setDisabled(False)
                    self.metamorphosisSkill.setDisabled(False)
                    self.necromancySkill.setDisabled(False)
                if self.is_psionic:
                    self.clairvoyanceSkill.setDisabled(False)
                    self.psychokinesisSkill.setDisabled(False)
                    self.telepathySkill.setDisabled(False)
                self.xpEdit.setDisabled(True)
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
                self.level_achieved = 500
                self.next_level = 1000
            elif self.level_achieved == 500:
                self.additional_attribute_points = 1
                self.additional1Display.setText(str(self.additional_attribute_points))
                self.attributing_up = True
                self.scoreCap = 3
                self.bodyScore.setMaximum(self.scoreCap)
                self.mindScore.setMaximum(self.scoreCap)
                self.spiritScore.setMaximum(self.scoreCap)
                self.bodyScore.setDisabled(False)
                self.mindScore.setDisabled(False)
                self.spiritScore.setDisabled(False)
                self.xpEdit.setDisabled(True)
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
                self.level_achieved = 1000
                self.next_level = 2000
            elif self.level_achieved == 1000:
                self.additional_skill_points = 3
                self.additional2Display.setText(str(self.additional_skill_points))
                self.skilling_up = True
                self.skillCap = 5
                self.agilitySkill.setMaximum(self.skillCap)
                self.beautySkill.setMaximum(self.skillCap)
                self.strengthSkill.setMaximum(self.skillCap)
                self.knowledgeSkill.setMaximum(self.skillCap)
                self.perceptionSkill.setMaximum(self.skillCap)
                self.technologySkill.setMaximum(self.skillCap)
                self.charismaSkill.setMaximum(self.skillCap)
                self.empathySkill.setMaximum(self.skillCap)
                self.focusSkill.setMaximum(self.skillCap)
                self.boxingSkill.setMaximum(self.skillCap)
                self.meleeSkill.setMaximum(self.skillCap)
                self.rangedSkill.setMaximum(self.skillCap)
                self.artSkill.setMaximum(self.skillCap)
                self.languagesSkill.setMaximum(self.skillCap)
                self.scienceSkill.setMaximum(self.skillCap)
                self.dodgeSkill.setMaximum(self.skillCap)
                self.parrySkill.setMaximum(self.skillCap)
                self.strikeSkill.setMaximum(self.skillCap)
                self.blessSkill.setMaximum(self.skillCap)
                self.exorcismSkill.setMaximum(self.skillCap)
                self.healingSkill.setMaximum(self.skillCap)
                self.demonologySkill.setMaximum(self.skillCap)
                self.metamorphosisSkill.setMaximum(self.skillCap)
                self.necromancySkill.setMaximum(self.skillCap)
                self.psychokinesisSkill.setMaximum(self.skillCap)
                self.clairvoyanceSkill.setMaximum(self.skillCap)
                self.telepathySkill.setMaximum(self.skillCap)
                self.agilitySkill.setDisabled(False)
                self.beautySkill.setDisabled(False)
                self.strengthSkill.setDisabled(False)
                self.knowledgeSkill.setDisabled(False)
                self.perceptionSkill.setDisabled(False)
                self.technologySkill.setDisabled(False)
                self.charismaSkill.setDisabled(False)
                self.empathySkill.setDisabled(False)
                self.focusSkill.setDisabled(False)
                self.boxingSkill.setDisabled(False)
                self.meleeSkill.setDisabled(False)
                self.rangedSkill.setDisabled(False)
                self.artSkill.setDisabled(False)
                self.languagesSkill.setDisabled(False)
                self.scienceSkill.setDisabled(False)
                if self.is_martial:
                    self.dodgeSkill.setDisabled(False)
                    self.parrySkill.setDisabled(False)
                    self.strikeSkill.setDisabled(False)
                if self.is_divine:
                    self.blessSkill.setDisabled(False)
                    self.exorcismSkill.setDisabled(False)
                    self.healingSkill.setDisabled(False)
                if self.is_occult:
                    self.demonologySkill.setDisabled(False)
                    self.metamorphosisSkill.setDisabled(False)
                    self.necromancySkill.setDisabled(False)
                if self.is_psionic:
                    self.clairvoyanceSkill.setDisabled(False)
                    self.psychokinesisSkill.setDisabled(False)
                    self.telepathySkill.setDisabled(False)
                self.xpEdit.setDisabled(True)
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
                self.level_achieved = 2000
                self.next_level = 5000
            elif self.level_achieved == 2000:
                self.additional_attribute_points = 1
                self.additional1Display.setText(str(self.additional_attribute_points))
                self.attributing_up = True
                self.scoreCap = 4
                self.bodyScore.setMaximum(self.scoreCap)
                self.mindScore.setMaximum(self.scoreCap)
                self.spiritScore.setMaximum(self.scoreCap)
                self.bodyScore.setDisabled(False)
                self.mindScore.setDisabled(False)
                self.spiritScore.setDisabled(False)
                self.xpEdit.setDisabled(True)
                self.saveButton.setDisabled(True)
                self.actionSave.setDisabled(True)
                self.printButton.setDisabled(True)
                self.actionPrint.setDisabled(True)
                self.level_achieved = 5000
                self.next_level = 10000
            
        print('Next XP level:', self.level_achieved, '    Skilling up:', self.skilling_up, '    Attributing up:', self.attributing_up)
    
    def loadButton_clicked(self):
        '''
        Load a .tps file for an already saved character.
        The file is stored in JSON format.
        '''
        self.filename = QFileDialog.getOpenFileName(self, 'Open TPS Character File', self.char_folder, 'TPS files (*' + self.file_extension + ')')
        if self.filename[0] != '':
            log.info('Loading ' + self.filename[0])
            with open(self.filename[0], 'r') as json_file:
                self.char_data = json.load(json_file)
                self.format_read = self.char_data['Fileformat']
                log.info('File format is: ' + str(self.format_read))
                self.scoreCap = self.char_data['Scorecap']
                self.bodyScore.setMaximum(self.scoreCap)
                self.mindScore.setMaximum(self.scoreCap)
                self.spiritScore.setMaximum(self.scoreCap)
                self.skillCap = self.char_data['Skillcap']
                self.agilitySkill.setMaximum(self.skillCap)
                self.beautySkill.setMaximum(self.skillCap)
                self.strengthSkill.setMaximum(self.skillCap)
                self.knowledgeSkill.setMaximum(self.skillCap)
                self.perceptionSkill.setMaximum(self.skillCap)
                self.technologySkill.setMaximum(self.skillCap)
                self.charismaSkill.setMaximum(self.skillCap)
                self.empathySkill.setMaximum(self.skillCap)
                self.focusSkill.setMaximum(self.skillCap)
                self.boxingSkill.setMaximum(self.skillCap)
                self.meleeSkill.setMaximum(self.skillCap)
                self.rangedSkill.setMaximum(self.skillCap)
                self.artSkill.setMaximum(self.skillCap)
                self.languagesSkill.setMaximum(self.skillCap)
                self.scienceSkill.setMaximum(self.skillCap)
                self.dodgeSkill.setMaximum(self.skillCap)
                self.parrySkill.setMaximum(self.skillCap)
                self.strikeSkill.setMaximum(self.skillCap)
                self.blessSkill.setMaximum(self.skillCap)
                self.exorcismSkill.setMaximum(self.skillCap)
                self.healingSkill.setMaximum(self.skillCap)
                self.demonologySkill.setMaximum(self.skillCap)
                self.metamorphosisSkill.setMaximum(self.skillCap)
                self.necromancySkill.setMaximum(self.skillCap)
                self.psychokinesisSkill.setMaximum(self.skillCap)
                self.clairvoyanceSkill.setMaximum(self.skillCap)
                self.telepathySkill.setMaximum(self.skillCap)
                self.charnameEdit.setText(self.char_data['Name'])
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setText(self.char_data['Age'])
                self.ageEdit.setDisabled(False)
                self.gender = self.char_data['Gender']
                self.gender_not_chosen = False
                self.genderBox.setCurrentIndex(self.gender_choice.index(self.gender))
                self.genderBox.setDisabled(True)
                self.cult = self.char_data['Cult']
                self.cult_not_chosen = False
                if self.gender == 'Male':
                    self.cult_choice = ['Choose', 'Hantu Belian', 'Blood Knight', 'Utopian Legion', 'Personality']
                else:
                    self.cult_choice = ['Choose', 'Boeotian Club', 'Hantu Belian', 'Goddess Cult', 'Utopian Legion', 'Personality']
                for i in self.cult_choice:
                    self.cultBox.addItem(i)
                self.cultBox.setCurrentIndex(self.cult_choice.index(self.cult))
                self.cultBox.setDisabled(True)
                self.role = self.char_data['Role']
                self.role_not_chosen = False
                self.roleBox.setCurrentIndex(self.role_choice.index(self.role))
                self.roleBox.setDisabled(True)
                self.cover = self.char_data['Cover']
                self.cover_not_chosen = False
                self.coverBox.setCurrentIndex(self.cover_choice.index(self.cover))
                self.coverBox.setDisabled(True)
                self.xpEdit.setDisabled(False)
                self.bodyScore.setValue(self.char_data['BODY'])
                self.bodyScore.setDisabled(True)
                self.mindScore.setValue(self.char_data['MIND'])
                self.mindScore.setDisabled(True)
                self.spiritScore.setValue(self.char_data['SPIRIT'])
                self.spiritScore.setDisabled(True)
                self.healthStatus.setText('')
                self.sanityStatus.setText('')
                self.moraleStatus.setText('')
                self.encumberedStatus.setText('')
                self.encumbered_flag = self.char_data['Encumbered']
                self.encumbered_checkBox.setChecked(self.encumbered_flag)
                self.healthDisplay.setText(self.char_data['HEALTH'])
                if self.healthDisplay.text() == '2':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.healthDisplay.text() == '1':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.healthDisplay.text() == '0':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Incapacitated</span>')
                    log.debug('Character is incapacitated!')
                if int(self.healthDisplay.text()) < 0:
                    self.healthStatus.setText('<span style=" color:#ff0000;">Expire</span>')
                    log.debug('Character has expired!')
                self.sanityDisplay.setText(self.char_data['SANITY'])
                if self.sanityDisplay.text() == '2':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.sanityDisplay.text() == '1':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.sanityDisplay.text() == '0':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Erratic</span>')
                    log.debug('Character is erratic!')
                if int(self.sanityDisplay.text()) < 0:
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Snap</span>')
                    log.debug('Character has snapped!')
                self.moraleDisplay.setText(self.char_data['MORALE'])
                if self.moraleDisplay.text() == '2':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.moraleDisplay.text() == '1':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.moraleDisplay.text() == '0':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">In Fear</span>')
                    log.debug('Character is in fear!')
                if int(self.moraleDisplay.text()) < 0:
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Submit</span>')
                    log.debug('Character has submit!')
                self.additional1Display.setText('')
                self.agilitySkill.setValue(self.char_data['Agility'])
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setValue(self.char_data['Beauty'])
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setValue(self.char_data['Strength'])
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setValue(self.char_data['Knowledge'])
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setValue(self.char_data['Perception'])
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setValue(self.char_data['Technology'])
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setValue(self.char_data['Charisma'])
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setValue(self.char_data['Empathy'])
                self.empathySkill.setDisabled(True)
                self.focusSkill.setValue(self.char_data['Focus'])
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setValue(self.char_data['Boxing'])
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setValue(self.char_data['Melee'])
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setValue(self.char_data['Ranged'])
                self.rangedSkill.setDisabled(True)
                self.artSkill.setValue(self.char_data['Art'])
                self.artSkill.setDisabled(True)
                self.languagesSkill.setValue(self.char_data['Languages'])
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setValue(self.char_data['Science'])
                self.scienceSkill.setDisabled(True)
                self.blessSkill.setValue(self.char_data['Bless'])
                self.blessSkill.setDisabled(True)
                self.exorcismSkill.setValue(self.char_data['Exorcism'])
                self.exorcismSkill.setDisabled(True)
                self.healingSkill.setValue(self.char_data['Healing'])
                self.healingSkill.setDisabled(True)
                self.demonologySkill.setValue(self.char_data['Demonology'])
                self.demonologySkill.setDisabled(True)
                self.metamorphosisSkill.setValue(self.char_data['Metamorphosis'])
                self.metamorphosisSkill.setDisabled(True)
                self.necromancySkill.setValue(self.char_data['Necromancy'])
                self.necromancySkill.setDisabled(True)
                self.clairvoyanceSkill.setValue(self.char_data['Clairvoyance'])
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setValue(self.char_data['Psychokinesis'])
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setValue(self.char_data['Telepathy'])
                self.telepathySkill.setDisabled(True)
                self.additional2Display.setText('')
                self.rewardDisplay.setText(self.char_data['Reward'])
                self.is_martial = self.char_data['Is_Martial']
                self.is_divine = self.char_data['Is_Divine']
                self.is_occult = self.char_data['Is_Occult']
                self.is_psionic = self.char_data['Is_Psionic']
                self.is_vampire = self.char_data['Is_Vampire']
                red_flag = False
                temp_encumbrance = 1 + self.bodyScore.value() + self.strengthSkill.value()
                temp_movement = 1 + self.bodyScore.value() + self.agilitySkill.value()
                temp_range = 1 + self.bodyScore.value() + self.strengthSkill.value()
                if int(self.healthDisplay.text()) > 1 and not self.encumbered_flag:
                    log.debug('Character can move fine.')
                elif int(self.healthDisplay.text()) == 1:
                    red_flag = True
                    temp_movement = temp_movement // 2
                    temp_range = temp_range // 2
                    log.debug("Wounded character's movement is cut in half.")
                elif int(self.healthDisplay.text()) < 1:
                    red_flag = True
                    temp_movement = 0
                    temp_range = 0
                    log.debug("Character can't move.")
                if self.encumbered_flag:
                    red_flag = True
                    temp_movement = temp_movement // 2
                    temp_range = temp_range // 2
                    log.debug("Encumbered character's movement is cut in half.")
                self.encumbranceDisplay.setText(str(temp_encumbrance) + ' items')
                if self.encumbered_flag:
                    self.encumberedStatus.setText('<span style=" color:#ff0000;">Encumbered</span>')
                else:
                    self.encumberedStatus.setText('')
                if red_flag:
                    self.movementDisplay.setText('<span style=" color:#ff0000;">' + str(temp_movement) + ' spaces</span>')
                    self.rangeDisplay.setText('<span style=" color:#ff0000;">' + str(temp_range) + ' miles</span>')
                else:
                    self.movementDisplay.setText(str(temp_movement) + ' spaces')
                    self.rangeDisplay.setText(str(temp_range) + ' miles')
                self.encumbered_checkBox.setDisabled(False)
                self.armorDisplay.setPlainText(self.char_data['ARMOR'])
                self.weaponDisplay.setPlainText(self.char_data['WEAPON'])
                self.itemsDisplay.setPlainText(self.char_data['ITEMS'])
                self.specialDisplay.setPlainText(self.char_data['SPECIAL'])
                self.traitsDisplay.setPlainText(self.char_data['TRAITS'])
                self.backstoryDisplay.setPlainText(self.char_data['BACKSTORY'])
                self.notesDisplay.setPlainText(self.char_data['NOTES'])
                self.char_level = self.char_data['Level']
                self.levelDisplay.setText(str(self.char_level))
                self.char_xp = self.char_data['XP']
                self.xpEdit.setText(str(self.char_xp))
                self.level_achieved = self.char_data['Level_Achieved']
                self.next_level = self.char_data['Next_Level']
                print('Loaded', self.level_achieved)
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)

    def saveButton_clicked(self):
        '''
        Save the .tps file for a generated or edited character.
        The name of the saved file is the name of the character.
        The file is stored in JSON format.
        '''
        if self.charnameEdit.text() == '':
            print('NO NAME!')
            log.debug("Can't save because of NO NAME!")
        else:
            json_file_out = open(self.char_folder + '/' + self.charnameEdit.text() + self.file_extension, 'w')
            self.char_data = {}
            self.char_data['Fileformat'] = self.file_format
            self.char_data['Scorecap'] = self.scoreCap
            self.char_data['Skillcap'] = self.skillCap
            self.char_data['Name'] = self.charnameEdit.text()
            self.char_data['Age'] = self.ageEdit.text()
            self.char_data['Gender'] = self.gender
            self.char_data['Reward'] = self.rewardDisplay.text()
            self.char_data['Is_Martial'] = self.is_martial
            self.char_data['Is_Divine'] = self.is_divine
            self.char_data['Is_Occult'] = self.is_occult
            self.char_data['Is_Psionic'] = self.is_psionic
            self.char_data['Is_Vampire'] = self.is_vampire
            self.char_data['Encumbered'] = self.encumbered_flag
            self.char_data['BODY'] = self.bodyScore.value()
            self.char_data['MIND'] = self.mindScore.value()
            self.char_data['SPIRIT'] = self.spiritScore.value()
            self.char_data['HEALTH'] = self.healthDisplay.text()
            self.char_data['SANITY'] = self.sanityDisplay.text()
            self.char_data['MORALE'] = self.moraleDisplay.text()
            self.char_data['Agility'] = self.agilitySkill.value()
            self.char_data['Beauty'] = self.beautySkill.value()
            self.char_data['Strength'] = self.strengthSkill.value()
            self.char_data['Knowledge'] = self.knowledgeSkill.value()
            self.char_data['Perception'] = self.perceptionSkill.value()
            self.char_data['Technology'] = self.technologySkill.value()
            self.char_data['Charisma'] = self.charismaSkill.value()
            self.char_data['Empathy'] = self.empathySkill.value()
            self.char_data['Focus'] = self.focusSkill.value()
            self.char_data['Boxing'] = self.boxingSkill.value()
            self.char_data['Melee'] = self.meleeSkill.value()
            self.char_data['Ranged'] = self.rangedSkill.value()
            self.char_data['Art'] = self.artSkill.value()
            self.char_data['Languages'] = self.languagesSkill.value()
            self.char_data['Science'] = self.scienceSkill.value()
            self.char_data['Dodge'] = self.dodgeSkill.value()
            self.char_data['Parry'] = self.parrySkill.value()
            self.char_data['Strike'] = self.strikeSkill.value()
            self.char_data['Bless'] = self.blessSkill.value()
            self.char_data['Exorcism'] = self.exorcismSkill.value()
            self.char_data['Healing'] = self.healingSkill.value()
            self.char_data['Demonology'] = self.demonologySkill.value()
            self.char_data['Metamorphosis'] = self.metamorphosisSkill.value()
            self.char_data['Necromancy'] = self.necromancySkill.value()
            self.char_data['Clairvoyance'] = self.clairvoyanceSkill.value()
            self.char_data['Psychokinesis'] = self.psychokinesisSkill.value()
            self.char_data['Telepathy'] = self.telepathySkill.value()
            self.char_data['Cult'] = self.cult
            self.char_data['Role'] = self.role
            self.char_data['Cover'] = self.cover
            self.char_data['ARMOR'] = self.armorDisplay.toPlainText()
            self.char_data['WEAPON'] = self.weaponDisplay.toPlainText()
            self.char_data['ITEMS'] = self.itemsDisplay.toPlainText()
            self.char_data['SPECIAL'] = self.specialDisplay.toPlainText()
            self.char_data['TRAITS'] = self.traitsDisplay.toPlainText()
            self.char_data['BACKSTORY'] = self.backstoryDisplay.toPlainText()
            if self.is_psionic:
                self.initial_note = 'Psionic.'
            else:
                self.initial_note = 'Not psionic.'
            if 'psionic' not in self.notesDisplay.toPlainText() and 'Psionic' not in self.notesDisplay.toPlainText():
                if self.notesDisplay.toPlainText() == '':
                    self.notesDisplay.setPlainText(self.initial_note)
                else:
                    self.notesDisplay.setPlainText(self.notesDisplay.toPlainText() + '\n' + self.initial_note)
            self.char_data['NOTES'] = self.notesDisplay.toPlainText()
            self.char_data['Level'] = self.char_level
            self.char_data['XP'] = self.char_xp
            self.char_data['Level_Achieved'] = self.level_achieved
            self.char_data['Next_Level'] = self.next_level
            json.dump(self.char_data, json_file_out, ensure_ascii=True)
            json_file_out.close()
            log.info('Character saved as ' + self.charnameEdit.text() + self.file_extension + ' in file format ' + str(self.file_format))
            self.printButton.setDisabled(False)
            self.actionPrint.setDisabled(False)
            self.popSaveDialog.show()
    
    def printButton_clicked(self):
        '''
        Print the character as a PDF.
        '''
        print('Printing character sheet...')
        pdf = FPDF(orientation='P', unit='in', format='Letter')
        pdf.add_page()
        pdf.image(name=CURRENT_DIR + '\\ggv_logo.png')
        pdf.add_font(family='Times New Roman', style='', fname=r'C:\Windows\Fonts\times.ttf')
        pdf.add_font(family='Times New Roman', style='B', fname=r'C:\Windows\Fonts\timesbd.ttf')
        pdf.set_font('Times New Roman', 'B', 20)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt=self.game_name)
        pdf.ln()
        pdf.set_font('Times New Roman', '', 16)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='Name: ' + self.charnameEdit.text())
        pdf.ln()
        pdf.cell(txt='Gender: ' + self.gender + '        Age: ' + self.ageEdit.text())
        pdf.ln()
        pdf.cell(txt='Cult: ' + self.cult + '        Role: ' + self.role)
        pdf.ln()
        pdf.cell(txt='Cover: ' + self.cover)
        pdf.ln()
        pdf.cell(txt='Reward: ' + str(self.rewardDisplay.text()) + '        Level: ' + str(self.char_level) + '        XP: ' + str(self.char_xp))
        pdf.ln()
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='     Limits')
        pdf.ln()
        pdf.cell(txt='ENCUMBRANCE: ' + str(1 + self.bodyScore.value() + self.strengthSkill.value()))
        pdf.ln()
        pdf.cell(txt='MOVE/COMBAT: ' + str(1 + self.bodyScore.value() + self.agilitySkill.value()))
        pdf.ln()
        pdf.cell(txt='MOVE/TRAVEL: ' + str(1 + self.bodyScore.value() + self.strengthSkill.value()))
        pdf.ln()
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='     Attributes')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt='BODY: ' + str(self.bodyScore.value()))
        pdf.ln()
        pdf.cell(txt='MIND: ' + str(self.mindScore.value()))
        pdf.ln()
        pdf.cell(txt='SPIRIT: ' + str(self.spiritScore.value()))
        pdf.ln()
        pdf.set_font('Times New Roman', '', 16)
        pdf.cell(txt='     Status')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt='HEALTH: ' + str(self.healthDisplay.text()))
        pdf.ln()
        pdf.cell(txt='SANITY: ' + str(self.sanityDisplay.text()))
        pdf.ln()
        pdf.cell(txt='MORALE: ' + str(self.moraleDisplay.text()))
        pdf.ln()
        pdf.set_font('Times New Roman', '', 16)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='Body Skills')
        pdf.ln()
        pdf.cell(txt='   Agility: ' + str(self.agilitySkill.value()))
        pdf.ln()
        pdf.cell(txt='   Beauty: ' + str(self.beautySkill.value()))
        pdf.ln()
        pdf.cell(txt='   Strength: ' + str(self.strengthSkill.value()))
        pdf.ln()
        pdf.cell(txt='Mind Skills')
        pdf.ln()
        pdf.cell(txt='   Knowledge: ' + str(self.knowledgeSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Perception: ' + str(self.perceptionSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Technology: ' + str(self.technologySkill.value()))
        pdf.ln()
        pdf.cell(txt='Spirit Skills')
        pdf.ln()
        pdf.cell(txt='   Charisma: ' + str(self.charismaSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Empathy: ' + str(self.empathySkill.value()))
        pdf.ln()
        pdf.cell(txt='   Focus: ' + str(self.focusSkill.value()))
        pdf.ln()
        pdf.add_page()
        pdf.set_font('Times New Roman', '', 10)
        pdf.cell(txt=self.game_name + '   ...continuing with character: ' + self.charnameEdit.text())
        pdf.ln()
        pdf.set_font('Times New Roman', '', 16)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='Combat Skills')
        pdf.ln()
        pdf.cell(txt='   Boxing: ' + str(self.boxingSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Melee: ' + str(self.meleeSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Ranged: ' + str(self.rangedSkill.value()))
        pdf.ln()
        pdf.cell(txt='Strange Skills')
        pdf.ln()
        pdf.cell(txt='   Art: ' + str(self.artSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Languages: ' + str(self.languagesSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Science: ' + str(self.scienceSkill.value()))
        pdf.ln()
        pdf.cell(txt='Martial Skills')
        pdf.ln()
        pdf.cell(txt='   Dodge: ' + str(self.dodgeSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Parry: ' + str(self.parrySkill.value()))
        pdf.ln()
        pdf.cell(txt='   Strike: ' + str(self.strikeSkill.value()))
        pdf.ln()
        pdf.cell(txt='Divine Skills')
        pdf.ln()
        pdf.cell(txt='   Bless: ' + str(self.blessSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Exorcism: ' + str(self.exorcismSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Healing: ' + str(self.healingSkill.value()))
        pdf.ln()
        pdf.cell(txt='Occult Skills')
        pdf.ln()
        pdf.cell(txt='   Demonology: ' + str(self.demonologySkill.value()))
        pdf.ln()
        pdf.cell(txt='   Metamorphosis: ' + str(self.metamorphosisSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Necromancy: ' + str(self.necromancySkill.value()))
        pdf.ln()
        pdf.cell(txt='Psionic Skills')
        pdf.ln()
        pdf.cell(txt='   Clairvoyance: ' + str(self.clairvoyanceSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Psychokinesis: ' + str(self.psychokinesisSkill.value()))
        pdf.ln()
        pdf.cell(txt='   Telepathy: ' + str(self.telepathySkill.value()))
        pdf.ln()
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='ARMOR:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        pdf.cell(txt=self.armorDisplay.toPlainText())
        pdf.ln()
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='WEAPON:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        pdf.cell(txt=self.weaponDisplay.toPlainText())
        pdf.ln()
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='ITEMS:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        some_text = self.itemsDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 12:
                for i in range(12):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = some_text[12:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = ''
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='SPECIAL:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        pdf.cell(txt=self.specialDisplay.toPlainText())
        pdf.ln()
        pdf.add_page()
        pdf.set_font('Times New Roman', '', 10)
        pdf.cell(txt=self.game_name + '   ...continuing with character: ' + self.charnameEdit.text())
        pdf.ln()
        pdf.set_font('Times New Roman', '', 16)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt='PERSONALITY / APPEARANCE:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        some_text = self.traitsDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 12:
                for i in range(12):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = some_text[12:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = ''
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='BACKSTORY:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        some_text = self.backstoryDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 12:
                for i in range(12):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = some_text[12:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = ''
        pdf.set_font('Times New Roman', '', 18)
        pdf.cell(txt=' ')
        pdf.ln()
        pdf.cell(txt='NOTES:')
        pdf.ln()
        pdf.set_font('Times New Roman', '', 14)
        some_text = self.notesDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 12:
                for i in range(12):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = some_text[12:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words)
                pdf.ln()
                some_text = ''

        pdf.output(CURRENT_DIR + '/Characters/' + self.charnameEdit.text() + '.pdf')
        print('...to folder: ' + CURRENT_DIR + '/Characters/' + self.charnameEdit.text() + '.pdf')
        log.info('Character printed as ' + self.charnameEdit.text() + '.pdf')

    def Visit_Blog(self):
        '''
        open web browser to blog URL
        '''
        os.startfile('http://shawndriscoll.blogspot.com')
        
    def Feedback(self):
        '''
        open an email letter to send as feedback to the author
        '''
        os.startfile('mailto:shawndriscoll@hotmail.com?subject=Feedback: ' + __app__ + ' for Total Party Skills RPG')
    
    def Overview_menu(self):
        '''
        open this app's PDF manual
        '''
        log.info(__app__ + ' looking for PDF manual...')
        os.startfile(CURRENT_DIR + '\\ggv_chargen_manual.pdf')
        log.info(__app__ + ' found PDF manual. Opening...')

    def actionAbout_triggered(self):
        '''
        open the About window
        '''
        log.info(__app__ + ' show about...')
        self.popAboutDialog.show()

    def alert_window(self):
        '''
        open the Alert window
        '''
        log.warning(__app__ + ' show Beta expired PyQt5 alertDialog...')
        self.popAlertDialog.show()

    def actionQuitProg_triggered(self):
        '''
        select "Quit" from the drop-down menu
        '''
        log.info(__app__ + ' quiting...')
        log.info(__app__ + ' DONE.')
        self.close()

def get_script_folder():
    # path of main .py or .exe when converted with pyinstaller
    if getattr(sys, 'frozen', False):
        script_path = os.path.dirname(sys.executable)
    else:
        script_path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    return script_path

if __name__ == '__main__':
    
    '''
    Technically, this program starts right here when run.
    If this program is imported instead of run, none of the code below is executed.
    '''

    log = logging.getLogger('GGV_Chargen')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    if not os.path.exists('Characters'):
        os.mkdir('Characters')
    
    fh = logging.FileHandler('Logs/ggv_chargen.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s', datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    
    log.info('Logging started.')
    log.info(__app__ + ' starting...')
    
    trange = time.localtime()

    log.info(__app__ + ' started, and running...')

    if trange[0] > 2023 or trange[1] > 12:
        __expired_tag__ = True
        __app__ += ' [EXPIRED]'
        
    app = QApplication(sys.argv)

    mainApp = MainWindow()
    mainApp.show()
    
    CURRENT_DIR = get_script_folder()
    log.info('Working Folder: ' + CURRENT_DIR)

    app.exec_()
