from PIL import Image
from customtkinter import CTkImage
import os
from config.paths import ICON_DIR

def load_image(dark_path, light_park, size=(30,30)):
    return CTkImage(
        dark_image=Image.open(dark_path),
        light_image=Image.open(light_park),
        size=size
    )

def get_icon_path(name):
    return os.path.join(ICON_DIR, f"{name}.ico")
    