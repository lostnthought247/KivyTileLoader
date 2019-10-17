from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class SampleObject(Widget):
    def __init__(self, num, loc=(200 ,200), **kwargs):
        super(SampleObject, self).__init__(**kwargs)
        self.loc = loc
        self.num = num
        self.name = str("obj" + str(self.num))

class TileGame(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(TileGame, self).__init__(**kwargs)
        self.game_objects = []
        self.build_objects()
        self.display_objects()

    def build_objects(self):
        n = 1
        loc = (0,0)
        for i in range(4):
            object = SampleObject(n, loc)
            n += 1
            loc = (loc[0] + 200, loc[1] + 200)
            self.game_objects.append(object)

        print(self.game_objects)
        for object in self.game_objects:
            print("-------")
            print(object.num)
            print(object.loc)

    def display_objects(self):
        for i, object in enumerate(self.game_objects):
            self.game_objects[i].button = Button(text=str(object.num), pos=(object.pos), size_hint=(.2,.2), pos_hint={'x':(object.pos[1]/Window.width)})
            self.add_widget(self.game_objects[i].button)


class GameApp(App):
    def build(self):
        return TileGame()



if __name__ == '__main__':
    GameApp().run()
