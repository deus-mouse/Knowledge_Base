from __future__ import annotations
from abc import ABC, abstractmethod


class Button(ABC):
    def render(self):
        pass

    def onClick(self):
        pass


class WindowsButton(Button):
    def onClick(self):
        print('WindowsButton onClick')


class MacOSButton(Button):
    def onClick(self):
        print('MacOSButton onClick')


class Slider(ABC):
    def render(self):
        pass

    def takeMove(self):
        pass


class WindowsSlider(Slider):
    def takeMove(self):
        print('WindowsSlider takeMove')


class MacOSSlider(Slider):
    def takeMove(self):
        print('MacOSSlider takeMove')


class Dialog(ABC):
    def __init__(self):
        self.createButton()
        self.createSlider()

    def render(self):
        self.button.onClick()
        self.slider.takeMove()

    @abstractmethod
    def createButton(self) -> Button:
        self.button = Button()
        return self.button

    @abstractmethod
    def createSlider(self) -> Slider:
        self.slider = Slider()
        return self.slider


class WindowsDialog(Dialog):
    def render(self):
        self.button.onClick()
        self.slider.takeMove()

    def createButton(self) -> WindowsButton:
        self.button = WindowsButton()
        return self.button

    def createSlider(self) -> WindowsSlider:
        self.slider = WindowsSlider()
        return self.slider


class MacOSDialog(Dialog):
    def render(self):
        self.button.onClick()
        self.slider.takeMove()

    def createButton(self) -> MacOSButton:
        self.button = MacOSButton()
        return self.button

    def createSlider(self) -> MacOSSlider:
        self.slider = MacOSSlider()
        return self.slider


def client_code(dialog: Dialog):
    my_dialog = dialog()
    my_dialog.render()


if __name__ == '__main__':
    client_code(WindowsDialog)
    client_code(MacOSDialog)

