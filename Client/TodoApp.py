import requests
from tkinter import *
from tkinter import messagebox

BASE = "http://127.0.0.1:5000/"
root = Tk()
root.title("Todo Assistant")
root.geometry("1024x960")

class TK():
	def __init__(self,master):
		appFrame = Frame(master).pack()
		self.label1 = Label(appFrame, text = "Username:")
		self.label1.pack(anchor=CENTER)
		self.entry1 = Entry(appFrame, width = 20)
		self.entry1.focus_set()
		self.entry1.pack(anchor = CENTER)
		self.label2 = Label(appFrame, text = "Password:")
		self.label2.pack(anchor = CENTER)
		self.entry2 = Entry(appFrame, width = 20)
		self.entry2.focus_set()
		self.entry2.pack(anchor = CENTER)
		self.button1 = Button(appFrame, text = "Login", command = lambda: self.login(master,self.entry1.get(),self.entry2.get()))
		self.button1.pack()
		self.button2 = Button(appFrame, text = "Register", command = lambda: self.register(master))
		self.button2.pack()


	def login(self,master,username,password):
		if username and password == "" or username and password == " ":
			messagebox.showerror("Error","Please Enter Characters")
		else:
			response = requests.put(BASE + "login", json = {"Username": username, "Password": password})
			try:
				if response.json()["message"] == "Invalid Username":
					messagebox.showerror("Error","Invalid Username")
				elif response.json()["message"] == "Incorrect Password":
					messagebox.showerror("Error", "Invalid Password")
				else:
					pass
			except:
				token = response.json().get("token")
				self.startTheProgramme(master, token)

	def startTheProgramme(self,master,token):
		self.label1.pack_forget()
		self.entry1.pack_forget()
		self.label2.pack_forget()
		self.entry2.pack_forget()
		self.button1.pack_forget()
		self.button2.pack_forget()
		appFrame = Frame(master).pack()
		self.button4 = Button(master, text ="Logout", command = lambda: self.logout(master))
		self.button4.pack(side = RIGHT, anchor = NE)
		self.button = Button(master, text ="Add", command = lambda: self.addText(master,token))
		self.button.pack(side = RIGHT, anchor = NE)
		self.button1 = Button(master, text ="Remove", command = lambda: self.removeText(master, token))
		self.button1.pack(side = RIGHT, anchor = NE)
		self.button2 = Button(master, text ="Change Status", command = lambda: self.changeStatus(master, token))
		self.button2.pack(side = RIGHT, anchor = NE)
		self.activeLabels = 0 
		self.radiobuttons = []
		self.label = Label(master, text = "", state = DISABLED)
		self.label.pack()
		self.label1 = Label(master, text = "", state = DISABLED)
		self.label1.pack()
		self.label2 = Label(master, text = "", state = DISABLED)
		self.label2.pack()
		self.label3 = Label(master, text = "", state = DISABLED)
		self.label3.pack()
		self.label4 = Label(master, text = "", state = DISABLED)
		self.label4.pack()
		self.label5 = Label(master, text = "", state = DISABLED)
		self.label5.pack()
		self.label6 = Label(master, text = "", state = DISABLED)
		self.label6.pack()
		self.label7 = Label(master, text = "", state = DISABLED)
		self.label7.pack()
		self.label8 = Label(master, text = "", state = DISABLED)
		self.label8.pack()
		self.label9 = Label(master, text = "", state = DISABLED)
		self.label9.pack()
		self.labels = []
		self.labels.append(self.label)
		self.labels.append(self.label1)
		self.labels.append(self.label2)
		self.labels.append(self.label3)
		self.labels.append(self.label4)
		self.labels.append(self.label5)
		self.labels.append(self.label6)
		self.labels.append(self.label7)
		self.labels.append(self.label8)
		self.labels.append(self.label9)

		self.displayText(token)

	def register(self,master):
		newFrame = Frame(master).pack()
		self.button1.pack_forget()
		self.button2.pack_forget()
		self.label3 = Label(newFrame, text = "Repeat Password:")
		self.label3.pack(anchor=CENTER)
		self.entry3 = Entry(newFrame, width = 20)
		self.entry3.focus_set()
		self.entry3.pack(anchor=CENTER)
		self.button3 = Button(newFrame, text = "Register", command = lambda: self.rgData(master,self.entry1.get(),self.entry2.get(),self.entry3.get()))
		self.button3.pack()
		self.button5 = Button(newFrame, text = "Back", command = lambda: self.back(master))
		self.button5.pack()


	def back(self,master):
		self.label1.pack_forget()
		self.entry1.pack_forget()
		self.label2.pack_forget()
		self.entry2.pack_forget()
		self.label3.pack_forget()
		self.entry3.pack_forget()
		self.button3.pack_forget()
		self.button5.pack_forget()
		TK(master)


	def rgData(self,master,username,password,repeatedpassword):
		if username == "" or username == " ":
			messagebox.showerror("Error","Please Enter Characters")

		elif password == "" or password == " ":
			messagebox.showerror("Error", "Please Enter Characters")

		elif password != repeatedpassword:
			messagebox.showerror("Error", "Passwords don't match")

		else:
			if len(username)>=6 and len(username)<=32:
				if len(password)>=6 and len(password)<=32:
						response = requests.put(BASE + "register", json = {"Username": username, "Password": password})
						if response.json() == {"message":"Username already exists"}:
							messagebox.showerror("Error","Username already exists")
						else:
							self.label1.pack_forget()
							self.entry1.pack_forget()
							self.label2.pack_forget()
							self.entry2.pack_forget()
							self.label3.pack_forget()
							self.entry3.pack_forget()
							self.button3.pack_forget()
							self.button5.pack_forget()
							TK(master)
				else:
					messagebox.showerror("Error","Password should be minimum 6 and maximum 32 characters long")
			else:
				messagebox.showerror("Error","username should be minimum 6 and maximum 32 characters long")

	def removeText(self,master,token):
		self.button.configure(state = DISABLED)
		self.button1.configure(state = DISABLED)
		self.button2.configure(state = DISABLED)
		self.button4.configure(state = DISABLED)
		newFrame = Frame(master).pack()
		self.selection = IntVar()
		placementY = 2

		for i in range(self.activeLabels):
			self.radioButton = Radiobutton(newFrame, text =f"{i+1})", variable = self.selection, value = f"{i+1}")
			self.radioButton.place(x = 10, y = placementY)
			self.radiobuttons.append(self.radioButton)
			placementY += 22

		self.removeSelected = Button(newFrame, text = "Remove Selected", command = lambda: self.rmSelected(master, token, self.selection.get()))
		self.removeSelected.pack(side = BOTTOM)
		self.closeRemove = Button(newFrame, text = "Cancel", command = self.closeRemoveWidgets)
		self.closeRemove.pack(side = BOTTOM)

	def closeRemoveWidgets(self):
		self.button.configure(state = ACTIVE)
		self.button1.configure(state = ACTIVE)
		self.button2.configure(state = ACTIVE)
		self.button4.configure(state = ACTIVE)
		for i in range(len(self.radiobuttons)):
			self.radiobuttons[i].place_forget()

		self.removeSelected.pack_forget()
		self.closeRemove.pack_forget()

	def logout(self,master):
		self.button.pack_forget()
		self.button1.pack_forget()
		self.button2.pack_forget()
		self.button4.pack_forget()
		self.label.pack_forget()
		self.label1.pack_forget()
		self.label2.pack_forget()
		self.label3.pack_forget()
		self.label4.pack_forget()
		self.label5.pack_forget()
		self.label6.pack_forget()
		self.label7.pack_forget()
		self.label8.pack_forget()
		self.label9.pack_forget()

		TK(master)


	def rmSelected(self,master,token,target):
		if target == 0:
			messagebox.showerror("No Data", "Nothing was selected")
		else:
			response = requests.delete(BASE, json = {"token":token, "target":target})
			self.clearTheList()
			self.displayText(token)
			for i in range(len(self.radiobuttons)):
				self.radiobuttons[i].place_forget()

			newFrame = Frame(master).pack()
			placementY = 2

			for i in range(self.activeLabels):
				self.radioButton = Radiobutton(newFrame, text =f"{i+1})", variable = self.selection, value = f"{i+1}")
				self.radioButton.place(x = 10, y = placementY)
				self.radiobuttons.append(self.radioButton)
				placementY += 22




	def clearTheList(self):
		self.activeLabels=0
		for i in enumerate(self.labels):
			self.labels[i[0]].configure(text = "")

	def displayText(self,token):
		try:
			self.activeLabels = 0 
			todoTextList = []
			todoStatusList = []
			response = requests.get(BASE, json = {"token":token})
			data = response.json()
			
			items = data.get(list(data)[0])

			for i in items:
				todoTextList.append(list(i)[0])
				todoStatusList.append(i.get(list(i)[0]))

			for i in range(len(todoTextList)):
				if todoStatusList[i] == 0:
					self.labels[i].configure(text = f"{todoTextList[i]}                              STATUS: To Be Done", state = NORMAL)
					self.activeLabels += 1
				else:
					self.labels[i].configure(text = f"{todoTextList[i]}                              STATUS: Done", state = NORMAL)
					self.activeLabels += 1
			
		except:
			pass


	def addText(self,master,token):
		self.button.configure(state = DISABLED)
		self.button1.configure(state = DISABLED)
		self.button2.configure(state = DISABLED)
		self.button4.configure(state = DISABLED)
		textFrame = Frame(master).pack()
		self.userEntry = Entry(textFrame, width = 40)
		self.userEntry.focus_set()
		self.userEntry.pack(pady=12,padx=10,side= BOTTOM)
		self.save = Button(textFrame, text = "Save", command = lambda: self.getText(token, self.userEntry.get()))
		self.save.pack(side=BOTTOM)
		self.close = Button(textFrame, text = "Cancel", command = self.closeAddWidgets)
		self.close.pack(side= BOTTOM)
		

	def closeAddWidgets(self):
		self.button.configure(state = ACTIVE)
		self.button1.configure(state = ACTIVE)
		self.button2.configure(state = ACTIVE)
		self.button4.configure(state = ACTIVE)
		self.userEntry.pack_forget()
		self.save.pack_forget()
		self.close.pack_forget()

	def getText(self,token,text):
		charCount = 0
		for i in text:
			if i == " ":
				charCount+=1
			else:
				pass
		if charCount == len(text):
			messagebox.showerror("ERROR", "Please enter characters!")
		elif text == "":
			messagebox.showerror("ERROR", "Please enter characters!")
		
		else:
			if len(text) >=6 and len(text)<=100:
				response = requests.put(BASE, json = {"token":token, "text":text})
				try:
					if response.json().get("message") == "Token has expired":
						messagebox.showerror("Error","Token has expired please login again!")
				except:
					self.displayText(token)
			else:
				messagebox.showerror("Error","Text should be minimum 6 and maximum 100 characters long")


	def changeStatus(self,master,token):
		self.button.configure(state = DISABLED)
		self.button1.configure(state = DISABLED)
		self.button2.configure(state = DISABLED)
		self.button4.configure(state = DISABLED)
		newFrame = Frame(master).pack()
		self.selection = IntVar()
		
		placementY = 2
		for i in range(self.activeLabels):
			self.radioButton = Radiobutton(newFrame, text =f"{i+1})", variable = self.selection, value = f"{i+1}")
			self.radioButton.place(x = 10, y = placementY)
			self.radiobuttons.append(self.radioButton)
			placementY += 22

		self.markAsDone = Button(newFrame, text = "Mark as Done", command = lambda: self.statusDone(master,token,self.selection.get()))
		self.markAsDone.pack(side = BOTTOM)
		self.closeStatus = Button(newFrame, text = "Cancel", command = self.closeStatusWidgets)
		self.closeStatus.pack(side = BOTTOM)


	def closeStatusWidgets(self):
		self.button.configure(state = ACTIVE)
		self.button1.configure(state = ACTIVE)
		self.button2.configure(state = ACTIVE)
		self.button4.configure(state = ACTIVE)
		for i in range(len(self.radiobuttons)):
			self.radiobuttons[i].place_forget()

		self.markAsDone.pack_forget()
		self.closeStatus.pack_forget()

	def statusDone(self,master,token,target):
		if target == 0:
			messagebox.showerror("No Data", "Nothing was selected")
		else:
			response = requests.patch(BASE, json = {"token":token, "target":target})
			self.clearTheList()
			self.displayText(token)
			for i in range(len(self.radiobuttons)):
				self.radiobuttons[i].place_forget()

			newFrame = Frame(master).pack()
			placementY = 2

			for i in range(self.activeLabels):
				self.radioButton = Radiobutton(newFrame, text =f"{i+1})", variable = self.selection, value = f"{i+1}")
				self.radioButton.place(x = 10, y = placementY)
				self.radiobuttons.append(self.radioButton)
				placementY += 22

start = TK(root)

root.mainloop()

