from __future__ import annotations
from abc import ABC, abstractmethod


class Dialog(ABC):
    def render(self):
        button = self.createButton()
        button.onClick()

    @abstractmethod
    def createButton(self) -> Button:
        pass


class WindowsDialog(Dialog):

    def createButton(self) -> Button:
        return WindowsButton()


class WebDialog(Dialog):

    def createButton(self) -> Button:
        return HTMLButton()


class Button(ABC):
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass


class WindowsButton(Button):
    def onClick(self):
        print('WindowsButton onClick')


class HTMLButton(Button):
    def onClick(self):
        print('HTMLButton onClick')


def client_code(dialog: Dialog) -> None:
    dialog.render()


if __name__ == "__main__":
    print("App: Launched with the WindowsDialog.")
    client_code(WindowsDialog())
    print("\n")

    print("App: Launched with the WebDialog.")
    client_code(WebDialog())
