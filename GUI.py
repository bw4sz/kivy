from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox

#For hyperlinks
import webbrowser
        
class MotionMeerkatApp(App):
    def build(self):
                
        #create overall layout
        b = BoxLayout(orientation='vertical',spacing=0)
        
        #MotionMeerkat
        top = BoxLayout(orientation='vertical',spacing=-1,size_hint=(.25,1))
        t1=Label(text="MotionMeerkat V2.0",font_size=12)
        t2=Button(text="Help",font_size=10)
        
        def help_site(instance):
            webbrowser.open("https://github.com/bw4sz/OpenCV_HummingbirdsMotion/wiki")
        t2.bind(on_press=help_site)
        
        t3=Button(text="Submit Issue",font_size=10)
        def help_site(instance):
            webbrowser.open("https://github.com/bw4sz/OpenCV_HummingbirdsMotion/issues")
        t3.bind(on_press=help_site)        
        top.add_widget(t1)
        top.add_widget(t2)
        top.add_widget(t3)
        
        
        #lets work from top to bottom
        #filechooser, we'll get there.
        
        #Input file
        #########################
        fc=TextInput(text="Input File or Folder",font_size=20,size_hint=(1,.5))
        banner = BoxLayout(orientation='horizontal',size_hint=(.8,1))
        banner.add_widget(top)
        banner.add_widget(fc)
        
        #add banner to overall 
        b.add_widget(banner)
        
        #########################
        #########################
        ####Mog sensitivity slider
        #########################
        
        mogbox = BoxLayout(orientation='horizontal',spacing=10)
        
        moglabel=Label(text="How much background variation [eg. wind, waves, debris] do you expect in your video?",font_size=15,size_hint=(1,1))
        moglearn = Slider(min=0, max=5, value=3,size_hint=(.7,1),step=1)
        
        #define high
        moglow=Label(text="No Movement",font_size=13.5,size_hint=(.15,1))

        #define low
        moghigh=Label(text="Extreme movement",font_size=13.5,size_hint=(.15,1))
        
        #Define output
        mogout=Label(font_size=20,size_hint=(.1,1))
        
        def on_call(instance, value):
            mogout.text = str(int(moglearn.value))
            
        moglearn.bind(value=on_call)
        
        #add to overall layout
        b.add_widget(moglabel)
        b.add_widget(mogbox)  
        
        #add slider and labels to sublayout
        mogbox.add_widget(moglow)
        mogbox.add_widget(moglearn)
        mogbox.add_widget(moghigh)
        mogbox.add_widget(mogout)
        
        #######################
        #Tolerance slider
        #######################
        
        tolbox = BoxLayout(orientation='horizontal',spacing=10)
        tollabel=Label(text="How quickly does your organism move?",font_size=15,size_hint=(1,0.6))
        tollearn = Slider(min=0, max=5, value=3,size_hint=(.7,1),step=1)
        
        #define high
        tollow=Label(text="Slow",font_size=13.5,size_hint=(.15,1))

        #define low
        tolhigh=Label(text="Fast",font_size=13.5,size_hint=(.15,1))
        
        #Define output
        tolout=Label(font_size=20,size_hint=(.1,1))
        
        def on_call(instance, value):
            tolout.text = str(int(tollearn.value))
            
        tollearn.bind(value=on_call)
        
        #add slider and labels to sublayout
        tolbox.add_widget(tollow)
        tolbox.add_widget(tollearn)
        tolbox.add_widget(tolhigh)
        tolbox.add_widget(tolout)
        
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
        
        ####################
        #Minimum size
        ####################
        
        # OVerall Text Layout
        ms=BoxLayout(size_hint=(1,.05))
        
        #Overall Action Layout
        draw_crop=BoxLayout(orientation='horizontal',pos_hint={'center_x':0.52})
        
        #label for layours
        mins_layout_label=BoxLayout()
        
        #labels
        drawl=Label(text="Minimum object size (% frame)",font_size=13)
        checkl=Label(text="Draw your object size on screen",font_size=13)
        roil=Label(text="Crop area of motion detection?",font_size=13)
        
        #Add to layout
        mins_layout_label.add_widget(drawl)
        mins_layout_label.add_widget(checkl)
        
        ms.add_widget(mins_layout_label)
        ms.add_widget(roil)        

        #Just a layout for the text box
        mins_layout_action=BoxLayout()
        
        mstext=TextInput(text="0.03",size_hint=(.4,.4),pos_hint={'center_y':0.5})   
        orlabel=Label(text="Or",font_size=11,size_hint=(0.3,1),pos=(100,100))
        
        draw = CheckBox()
        draw.bind(active=on_checkbox_active)  
        
        #add to layout       
        mins_layout_action.add_widget(mstext)
        mins_layout_action.add_widget(orlabel)
        mins_layout_action.add_widget(draw)
        
        draw_crop.add_widget(mins_layout_action)
        draw_crop.add_widget(crop)
        
        #add to overall layout
        b.add_widget(ms)        
        b.add_widget(draw_crop)
        
        #Run!
        t = Button(text='Run',font_size=40,size_hint=(1,.7))
        b.add_widget(t)
        
        return b

if __name__ == "__main__":
    MotionMeerkatApp().run()