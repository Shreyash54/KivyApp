from tkinter import Grid
from kivy.lang import Builder
from kivy.app   import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


class Widgetexample(GridLayout):
    count=1
    my_text=StringProperty("1")
    text=StringProperty("click me")

    def on_click(self):
        print("clicked me")
        self.count+=1
        self.my_text=str(self.count)
    
    
class Myaspp(App):
    def build(self):
        return Builder.load_file("D:\HP\MyKivyApp\TheGrid.kv")
if __name__=="__main__":
    Myaspp().run()
