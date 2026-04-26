from customtkinter import CTkLabel, CTkButton, CTkScrollableFrame

class HomePage(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color="transparent")
        
        self.label = CTkLabel(self, text="Welcome to Huit Face!", font=("Arial", 24))
        self.label.grid(row=0, column=0, pady=20, padx=20)

