from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image

#For hyperlinks
import webbrowser
        
def help_site(instance):
    webbrowser.open("https://github.com/bw4sz/OpenCV_HummingbirdsMotion/wiki")

def help_site(instance):
    webbrowser.open("https://github.com/bw4sz/OpenCV_HummingbirdsMotion/issues")

def on_check_roi(checkbox, value):
    if value:
        self.set_ROI=True
    else:
        self.set_ROI=False

#Drawing checkbox
def on_check_draw(checkbox, value):
    if value:
        self.drawSmall
    else:
        self.drawSmall

class MainScreen(BoxLayout):
    pass

class MotionMeerkatApp(App):
    def build(self):
        return MainScreen()
        
if __name__ == "__main__":
    MotionMeerkatApp().run()
    
