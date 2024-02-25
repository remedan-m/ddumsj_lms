# create a basic form 
import customtkinter as ctk
import tkinter as tk
import requests


# Sets the appearance of the window
ctk.set_appearance_mode("Dark") 

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue 
ctk.set_default_color_theme("dark-blue") 

# Dimensions of the window
appWidth, appHeight = 600, 600


# App Class
class App(ctk.CTk):
	# The layout of the window will be written
	# in the init function itself
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Sets the title of the window to "App"
		self.title("User Detail info") 
		# Sets the dimensions of the window to 600x600
		self.geometry(f"{appWidth}x{appHeight}") 
		
		self.head_textLeble = ctk.CTkLabel(self, text="Fill the Form below")
		self.head_textLeble.grid(row=8, column=1,
						   padx=20, pady=20)

		# Id number Label
		self.Id_numberLabel = ctk.CTkLabel(self, text="Id Number")
		self.Id_numberLabel.grid(row=0, column=0,
						padx=20, pady=20,
						sticky="ew")

		# id number Entry Field
		self.Id_numberEntry = ctk.CTkEntry(self,
							placeholder_text="12456")
		self.Id_numberEntry.grid(row=0, column=1,
						columnspan=3, padx=20,
						pady=20, sticky="ew")

		# first name Label
		self.first_nameLabel = ctk.CTkLabel(self,
								text="First Name")
		self.first_nameLabel.grid(row=1, column=0,
							padx=20, pady=20,
							sticky="ew")

		# first name Entry Field
		self.first_nameEntry = ctk.CTkEntry(self,
						placeholder_text="Abdellah")
		self.first_nameEntry.grid(row=1, column=1,
							columnspan=3, padx=20,
							pady=20, sticky="ew")
		# last name Label
		self.last_nameLabel = ctk.CTkLabel(self,
								text="Last Name")
		self.last_nameLabel.grid(row=2, column=0,
							padx=20, pady=20,
							sticky="ew")

		# last name Entry Field
		self.last_nameEntry = ctk.CTkEntry(self,
						placeholder_text="hamad")
		self.last_nameEntry.grid(row=2, column=1,
							columnspan=3, padx=20,
							pady=20, sticky="ew")

		

		# Gender Label
		self.genderLabel = ctk.CTkLabel(self,
								text="Gender")
		self.genderLabel.grid(row=3, column=0, 
							padx=20, pady=20,
							sticky="ew")

		# Gender Radio Buttons
		self.genderVar = tk.StringVar(value="male/female")
		'''
		self.genderVar,
												value="He is"
		'''


		self.maleRadioButton = ctk.CTkRadioButton(self,
								text="Male",
								variable=self.genderVar,
								value="Male")
		self.maleRadioButton.grid(row=3, column=1,
								padx=20, pady=20,
								sticky="ew")

		self.femaleRadioButton = ctk.CTkRadioButton(self,
									text="Female",
									variable=self.genderVar,
									value="Female")
		self.femaleRadioButton.grid(row=3, column=2,
									padx=20, pady=20,
									sticky="ew")
		
		# contact Label
		self.contactLabel = ctk.CTkLabel(self, text="Contact")
		self.contactLabel.grid(row=4, column=0,
						padx=20, pady=20,
						sticky="ew")

		# contact Entry Field
		self.contactEntry = ctk.CTkEntry(self,
							placeholder_text="0920104583")
		self.contactEntry.grid(row=4, column=1,
						columnspan=3, padx=20,
						pady=20, sticky="ew")
		
		# address/dorm block/number Lable
		self.addressLable = ctk.CTkLabel(self, text='Address')
		self.addressLable.grid(row=5, column=0,
						 padx=20, pady=20,
						 sticky="ew")
		
		# address/dorm block/number Entry Field
		self.addressEntry = ctk.CTkEntry(self, 
								   placeholder_text="white house/1")
		self.addressEntry.grid(row=5, column=1,
						columnspan=3, padx=20,
						 pady=20, sticky="ew" )
		
		# department Lable
		self.departmentLable = ctk.CTkLabel(self, text='Department')
		self.departmentLable.grid(row=6, column=0,
						 padx=20, pady=20,
						 sticky="ew")
		
		# department Entry Field
		self.departmentEntry = ctk.CTkEntry(self, 
								   placeholder_text="computer science, mathimatics,...")
		self.departmentEntry.grid(row=6, column=1,
						columnspan=3, padx=20,
						 pady=20, sticky="ew" )
		

		# submit the form  Button
		self.submit_formButton = ctk.CTkButton(self,
										 text="Submit Form",
										 command=self.submit_form)
		self.submit_formButton.grid(row=7, column=1,
										columnspan=2, padx=20, 
										pady=20, sticky="ew")
		
	def submit_form(self):
			# Get the user input from the form
			id_number = self.Id_numberEntry.get()
			first_name = self.first_nameEntry.get()
			last_name = self.last_nameEntry.get()
			gender = self.genderVar.get()
			contact = self.contactEntry.get()
			address = self.addressEntry.get()
			department = self.departmentEntry.get()

			url = "http://127.0.0.1:8080/users/register/"

			data = {"Id_number": id_number,
		   			"first_name": first_name,
					"last_name": last_name,
					"gender": gender,
					"contact": contact,
					"address": address,
					"department": department,
		   
		   
		   }			
			
			try:
				# sending the http post request
				response = requests.post(url,data=data)

				# check the response status code
				if response.status_code == 200:
					return("successfully submitted!")
				
				else:
					return("unsuccessfull submittion!")
				
			except requests.RequestException as e:
				return("Error:", e)
			

	
	


		
	
		


if __name__ == "__main__":
	app = App()
	# Used to run the application
	app.mainloop()	 
