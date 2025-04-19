from tkinter import W, Grid
from kivy.lang import Builder
from kivy.app   import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from matplotlib import widgets
class Widgetexample(GridLayout):
    count=1
    my_text=StringProperty("1")
    text=StringProperty("CLICK")
    toggle_text=StringProperty("OFF")
    count_enable=BooleanProperty(False)
    switch_active=BooleanProperty(False)
    slider_text=StringProperty("value")
    
    def on_click(self):
        if self.count_enable==True:
            print("button clicked")
            self.count+=1
            self.my_text=str(self.count)

    def on_toggle_press(self,widget):
        print("toggle state:" + widget.state)
        if widget.state=="normal":
            widget.text="OFF"
            self.count_enable=False
        else:
            widget.text="ON"  
            self.count_enable=True 
    def on_active_switch(self,Widget):
        print("switch is active:"  + str(Widget.active))
    
    def on_slider(self,Widget):
        print("slider value:"+ str(int(Widget.value)))
        self.slider_text=str(int(Widget.value))

                         

class Myapp(App):
    def build(self):
        return Builder.load_file("D:\HP\MyKivyApp\TheGrid.kv")

if __name__=="__main__":
    Myapp().run()
