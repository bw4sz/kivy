from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox



        
class TutorialApp(App):
    def build(self):
        
        #create overall layout
        b = BoxLayout(orientation='vertical',spacing=0)
        
        #sublayout
        b2 = BoxLayout(orientation='horizontal')
        
        #lets work from top to bottom
        #filechooser, we'll get there.
        
        #########################
        ####Mog sensitivity slider
        #########################
        
        mogbox = BoxLayout(orientation='horizontal',spacing=10)
        
        moglabel=Label(text="How much background variation [eg. wind, waves, debris] do you expect in your video?",font_size=15)
        moglearn = Slider(min=0, max=5, value=3,size_hint=(.7,1))
        
        #define high
        moglow=Label(text="No Movement",font_size=10,size_hint=(.15,1))

        #define low
        moghigh=Label(text="Extreme movement",font_size=10,size_hint=(.15,1))
        
        #add to overall layout
        b.add_widget(moglabel)
        b.add_widget(mogbox)
        
        #add slider and labels to sublayout
        mogbox.add_widget(moglow)
        mogbox.add_widget(moglearn)
        mogbox.add_widget(moghigh)
        
        #######################
        #Tolerance slider
        #######################
        
        tolbox = BoxLayout(orientation='horizontal',spacing=10)
        
        tollabel=Label(text="How quickly does your organism move",font_size=15)
        tollearn = Slider(min=0, max=5, value=3,size_hint=(.7,1))
        
        #define high
        tollow=Label(text="Slow",font_size=10,size_hint=(.15,1))

        #define low
        tolhigh=Label(text="Fast",font_size=10,size_hint=(.15,1))
        
        #add slider and labels to sublayout
        tolbox.add_widget(tollow)
        tolbox.add_widget(tollearn)
        tolbox.add_widget(tolhigh)
        
        #add to overall layout
        b.add_widget(tollabel)
        b.add_widget(tolbox)           
        
        #########################
        #Cropping checkbox
        #########################
        
        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')
        
        crop = CheckBox()
        crop.bind(active=on_checkbox_active)        
        
        #add to layout        
        b2.add_widget(crop)
        
        ####################
        #Minimum size
        ####################
        
        #it can be either enter or draw
        ms=BoxLayout()
        mslabel=Label(text="What is the expected size of your smallest object of interest")
        mstext=TextInput(text="Enter numeric decimal (0.03) or to draw your object, check the box")
        
        draw = CheckBox()
        draw.bind(active=on_checkbox_active)  
        
        ms.add_widget(mslabel)
        
        draw_crop=BoxLayout(orientation='horizontal')
        draw_crop.add_widget(mstext)
        draw_crop.add_widget(draw)
        
        #add to overall layout
        b.add_widget(ms)        
        b.add_widget(draw_crop)

        
        #add sublayouts to main layout
        b.add_widget(b2)
        
        #Run!
        t = Button(text='Run',font_size=40, height=200)
        b.add_widget(t)
        
        return b

if __name__ == "__main__":
    TutorialApp().run()