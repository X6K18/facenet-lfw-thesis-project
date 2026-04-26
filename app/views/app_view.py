import customtkinter as ctk
import os 

from views.main_view import MainView
from utils.assets import load_image, get_icon_path
from config.paths import IMAGE_DIR

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class AppView(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Huit Face")
        self.geometry("1400x750")
        self.iconbitmap(get_icon_path("horus"))
        
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1400 // 2)
        y = (self.winfo_screenheight() // 2) - (750 // 2)
        self.geometry(f"1400x750+{x}+{y}")

        # layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.load_assets()
        self.setup_sidebar()
        self.setup_main_view()
    
    # method load assets
    def load_assets(self):
        self.home_image = load_image(
            os.path.join(IMAGE_DIR, "home_dark.png"),
            os.path.join(IMAGE_DIR, "home_light.png"),
            size=(30,30)
        )
    
    # method sidebar UI 
    def setup_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, fg_color="transparent")
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(0, weight=1)

        self.home_btn = ctk.CTkButton(self.sidebar, text="Home", image=self.home_image, compound="left")
        self.home_btn.grid(row=0, column=0, pady=10, padx=10)
    
    # method main view UI 
    def setup_main_view(self):
        self.main_view = MainView(self)
        self.main_view.grid(row=0, column=1, sticky="nsew")
    
    # method controller binding
    def set_controller(self, controllers):
        self.controller = controllers
    
    def bind_events(self):
        self.home_btn.configure(command=self.controller.show_home)

        
