# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
import addonHandler
import gui
import globalVars
from gui.nvdaControls import CustomCheckListBox
from scriptHandler import script
import core
import winsound
import wx
import os
from threading import Thread
import fnmatch

# For translation
addonHandler.initTranslation()

# List containing all the add-ons
lista = list(addonHandler.getAvailableAddons())
IS_WIN_on = False
# Creation of a GlobalPlugin class, derived from globalPluginHandler.GlobalPlugin.
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Creating the constructor of the newly created GlobalPlugin class.
	def __init__(self):
		# Call of the constructor of the parent class.
		super(GlobalPlugin, self).__init__()
		self._MainWindows = None

		if globalVars.appArgs.secure:
			return

		# Creation of our menu.
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		# Translators: Name of the item in the tools menu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&Cambiador de fechas para los manifiestos"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_cricricri, self.menuItem)

	def terminate(self):
		try:
			if not self._MainWindows:
				self._MainWindows.Destroy()
		except (AttributeError, RuntimeError):
			pass

	@script(gesture=None, description= _("Mostrar la ventana para cambiar la fecha  a los manifiestos de los complementos"), category= _("cricricri"))
	def script_cricricri(self, event):
# Calling the main window of the plug-in

		if IS_WIN_on == False:
			if not self._MainWindows:
				self._MainWindows = MainWindows(gui.mainFrame)

			if not self._MainWindows.IsShown():
				gui.mainFrame.prePopup()
				self._MainWindows.Show()

# Creating the Main Window of the Plug-in
class MainWindows(wx.Dialog):

# Function taken from the add-on emoticons to center the window
	def _calculatePosition(self, width, height):
		w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
		h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
		# Centre of the screen
		x = w / 2
		y = h / 2
		# Minus application offset
		x -= (width / 2)
		y -= (height / 2)
		return (x, y)

	def __init__(self, parent):
		WIDTH = 800
		HEIGHT = 600
		pos = self._calculatePosition(WIDTH, HEIGHT)

		# Translators: Title of the plug-in in the main dialogue
		super(MainWindows, self).__init__(parent, -1, title=_("Cambiador de fechas para los manifiestos"), pos = pos, size = (WIDTH, HEIGHT))

		Panel = wx.Panel(self)

		# Translators: Label that identifies the list of add-ons
		label1 = wx.StaticText(Panel, wx.ID_ANY, label=_("&Lista de complementos / Fecha en el manifiesto:"))
		self.myListBox = CustomCheckListBox(Panel, 2)

		for i in lista:
			ver = i.manifest["lastTestedNVDAVersion"]
			verFin = ".".join(str(e) for e in ver)
			self.myListBox.Append("{} - {}".format(i.manifest["summary"], verFin))
		self.myListBox.SetSelection(0)
		self.myListBox.SetFocus()
		self.Bind(wx.EVT_LISTBOX, self.OnSelection, self.myListBox)

		# Translators: Button name to select all add-ons
		self.selectionAllBTN = wx.Button(Panel, wx.ID_ANY, _("&Seleccionar todos"))
		self.Bind(wx.EVT_BUTTON, self.onselectionAllBTN, self.selectionAllBTN)

		# Translators: Button name to deselect all add-ons
		self.unselectionAllBTN = wx.Button(Panel, wx.ID_ANY, _("&Deseleccionar todos"))
		self.Bind(wx.EVT_BUTTON, self.onUnselectionAllBTN, self.unselectionAllBTN)

		self.diccionarioMayor = {0:"2021", 1:"2022", 2:"2023", 3:"2024", 4:"2025", 5:"2026", 6:"2027", 7:"2028", 8:"2029", 9:"2030"}
		self.mayor = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
		self.diccionarioMenor = {0:"1", 1:"2", 2:"3", 3:"4"}
		self.menor = ["1", "2", "3", "4"] 
		self.revision = ["0", "1", "2", "3", "4", "5"]

		labelMayor = wx.StaticText(Panel, wx.ID_ANY, _("Seleccione versión Mayor:"))
		self.choiceMayor = wx.Choice(Panel, wx.ID_ANY, choices = self.mayor)
		self.choiceMayor.SetSelection(0)

		labelMenor = wx.StaticText(Panel, wx.ID_ANY, _("Seleccione versión Menor:"))
		self.choiceMenor = wx.Choice(Panel, wx.ID_ANY, choices = self.menor)
		self.choiceMenor.SetSelection(0)

		labelRevision = wx.StaticText(Panel, wx.ID_ANY, _("Seleccione una revisión:"))
		self.choiceRevision = wx.Choice(Panel, wx.ID_ANY, choices = self.revision)
		self.choiceRevision.SetSelection(0)

		self.generateAddon = wx.Button(Panel, wx.ID_ANY, _("&Aplicar cambios a los manifiestos"))
		self.Bind(wx.EVT_BUTTON, self.onGenerate, self.generateAddon)

		# Translators: Exit button name
		self.closeBTN = wx.Button(Panel, wx.ID_CANCEL, _("&Cerrar"))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)

		sizeV = wx.BoxSizer(wx.VERTICAL)
		sizeH1 = wx.BoxSizer(wx.HORIZONTAL)
		sizeH2 = wx.BoxSizer(wx.HORIZONTAL)
		sizeH3 = wx.BoxSizer(wx.HORIZONTAL)

		sizeV.Add(label1, 0, wx.EXPAND)
		sizeV.Add(self.myListBox, 1, wx.EXPAND|wx.ALL, 5)

		sizeH1.Add(self.selectionAllBTN, 2, wx.CENTER)
		sizeH1.Add(self.unselectionAllBTN, 2, wx.CENTER)

		sizeV.Add(sizeH1, 0, wx.CENTER)

		sizeH2.Add(labelMayor, 0)
		sizeH2.Add(self.choiceMayor, 1, wx.EXPAND)
		sizeH2.Add(labelMenor, 0)
		sizeH2.Add(self.choiceMenor, 1, wx.EXPAND)
		sizeH2.Add(labelRevision, 0)
		sizeH2.Add(self.choiceRevision, 1, wx.EXPAND)

		sizeV.Add(sizeH2, 0, wx.EXPAND)

		sizeH3.Add(self.generateAddon, 2, wx.CENTER)
		sizeH3.Add(self.closeBTN, 2, wx.CENTER)

		sizeV.Add(sizeH3, 0, wx.CENTER)

		Panel.SetSizer(sizeV)

	def OnSelection(self, event):
		pass

	def onselectionAllBTN(self, event):
		num = self.myListBox.GetCount()
		for i in range(num):
			self.myListBox.Check(	i, True)
		self.myListBox.SetSelection(0)
		self.myListBox.SetFocus()

	def onUnselectionAllBTN(self, event):
		self.myListBox.Clear()
		for i in lista:
			ver = i.manifest["lastTestedNVDAVersion"]
			verFin = ".".join(str(e) for e in ver)
			self.myListBox.Append("{} - {}".format(i.manifest["summary"], verFin))
		self.myListBox.SetSelection(0)
		self.myListBox.SetFocus()

	def onGenerate(self, event):
		selection = [i for i in range(self.myListBox.GetCount()) if self.myListBox.IsChecked(i)]
		if len(selection) == 0:
			# Translators: Error message warning that no add-on was selected
			gui.messageBox(_("Necesita seleccionar por lo menos un complemento."),
				# Translators: Title of the dialog box no add-ons selected, Error
				_("Error"), wx.ICON_ERROR)
			self.myListBox.SetFocus()
		else:
			mayor = self.diccionarioMayor.get(self.choiceMayor.GetSelection())
			menor = self.diccionarioMenor.get(self.choiceMenor.GetSelection())
			revision = self.choiceRevision.GetSelection()
			hilo =ThreadLaunch(selection, mayor, menor, revision)
			hilo.start()
			self.onClose(None)

	def onClose(self, event):
		self.Destroy()
		gui.mainFrame.postPopup()

class ThreadLaunch(Thread):
	def __init__(self, selection, mayor, menor, revision):
		super(ThreadLaunch, self).__init__()

		self.selection = selection
		self.mayor = mayor
		self.menor = menor
		self.revision = revision

		self.daemon = True

	def run(self):
		def LaunchDialog(selection, mayor, menor, revision):
			self._MainWindows = ProgressThread(gui.mainFrame, selection, mayor, menor, revision)
			gui.mainFrame.prePopup()
			self._MainWindows.Show()

		wx.CallAfter(LaunchDialog, self.selection, self.mayor, self.menor, self.revision)

class GeneratingThread(Thread):
	def __init__(self, frame, selection, mayor, menor, revision):

		super(GeneratingThread, self).__init__()

		self.frame = frame
		self.selection = selection
		self.mayor = mayor
		self.menor = menor
		self.revision = revision

		self.daemon = True
		self.start()

	def findReplace(self, directory, find, replace, filePattern):
		for path, dirs, files in os.walk(os.path.abspath(directory)):
			for filename in fnmatch.filter(files, filePattern):
				filepath = os.path.join(path, filename)
				with open(filepath, 'r', errors="ignore") as file:
					fileContent = file.readlines()
				for lineIndex in range(len(fileContent)):
					if (find in fileContent[lineIndex]):
						fileContent[lineIndex] = replace
						with open(filepath, 'w', errors="ignore") as tableFile:
							tableFile.writelines(fileContent)
						break

	def run(self):
		try:
			for i in self.selection:
				self.findReplace(lista[i].path, "lastTestedNVDAVersion", "lastTestedNVDAVersion = {}.{}.{}\n".format(self.mayor, self.menor, self.revision), "manifest.ini")
				wx.CallAfter(self.frame.next, i)
			msg = \
_("""Se cambiaron los manifiestos correctamente.

Para que la acción tenga efecto NVDA tiene que reiniciarse.

¿Desea reiniciar NVDA ahora?""")
			wx.CallAfter(self.frame.done, msg)
		except Exception as e:
			msg = \
_("""Se produjo el siguiente error al cambiar los manifiestos:

{}

Si el problema persiste informe al autor del complemento CRICRICRI dándole este error.""").format(e)
			wx.CallAfter(self.frame.error, msg)

class ProgressThread(wx.Dialog):

	def __init__(self, frame, selection, mayor, menor, revision):

		# Translators: Title of the progress dialog
		super(ProgressThread, self).__init__(None, -1, title=_("Cambiando manifiestos"))

		self.Centre()

		global IS_WIN_on
		IS_WIN_on = True

		panel=wx.Panel(self)

		self.Bind(wx.EVT_CLOSE, self.onNull)
		# Translators: Tag that asks the user to wait
		label = wx.StaticText(panel, wx.ID_ANY, label=_("Espere por favor..."))
		self.progressBar=wx.Gauge(panel, wx.ID_ANY, range=len(selection), style = wx.GA_HORIZONTAL)
		label.SetFocus()

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(label, 0, wx.EXPAND)
		sizer.Add(self.progressBar, 0, wx.EXPAND)
		panel.SetSizer(sizer)

		GeneratingThread(self, selection, mayor, menor, revision)

	def next(self, event):
		self.progressBar.SetValue(event)

	def done(self, event):
		winsound.MessageBeep(0)
		global IS_WIN_on
		IS_WIN_on = False
		MsgBox = wx.MessageDialog(None, event, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = MsgBox.ShowModal()
		if ret == wx.ID_YES:
			MsgBox.Destroy
			core.restart()
			self.Destroy()
			gui.mainFrame.postPopup()
		else:
			MsgBox.Destroy
			self.Destroy()
			gui.mainFrame.postPopup()

	def error(self, event):
		winsound.MessageBeep(16)
		global IS_WIN_on
		IS_WIN_on = False
		gui.messageBox(event,

			# Translators: Title of the dialog box, could not be completed. Error
			_("Error"), wx.ICON_ERROR)
		self.Destroy()
		gui.mainFrame.postPopup()

	def onNull(self, event):
		pass