from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
import random

class PasswordGeneratorApp(App):
    def __init__(self, **kwargs):
        super(PasswordGeneratorApp, self).__init__(**kwargs)
        self.upper = "QWERTYUIOPASDFGHZXCVBJNKML"
        self.lower = "qwertyuiopalskdjfhgmznxbcv"
        self.number = "0123456789"
        self.symbol = "£$%^&*<|¬|,.,<>"
        self.string = self.lower + self.upper + self.number + self.symbol

    def build(self):
        self.password_entry = TextInput(multiline=False, password=True, background_color=(0.9, 0.9, 0.9, 1))
        self.generate_button = Button(text="Generate Password", on_press=self.generate_password, background_color=(0, 0.7, 0, 1))
        self.save_button = Button(text="Save Password", on_press=self.save_password, background_color=(0.8, 0, 0, 1))
        self.show_password_checkbox = CheckBox(active=False)
        self.show_password_checkbox.bind(active=self.toggle_show_password)
        self.warning_label = Label(text="Amit Acharya is the Developer of this app.", color=(0.8, 0, 0, 1), italic=True)
        self.warning_button = Button(text="Show Warning", on_press=self.show_warning, background_color=(0.8, 0, 0, 1))

        layout = BoxLayout(orientation="vertical", spacing=10)
        layout.add_widget(Label(text="Your password is:", color=(0.12, 0.44, 0.55, 1), font_size=14))
        layout.add_widget(self.password_entry)
        layout.add_widget(self.generate_button)
        layout.add_widget(self.save_button)
        layout.add_widget(Label(text="Show Password", color=(0, 0.7, 0, 1), font_size=25))
        layout.add_widget(self.show_password_checkbox)
        layout.add_widget(self.warning_label)
        layout.add_widget(self.warning_button)

        return layout

    def generate_password(self, instance):
        length = 9
        password = "".join(random.sample(self.string, length))
        self.password_entry.text = password

    def save_password(self, instance):
        password_to_save = self.password_entry.text.strip()
        if not password_to_save:
            self.show_message("Empty Password", "No password to save.")
            return

        content = BoxLayout(orientation="vertical")
        file_chooser = FileChooserListView()
        content.add_widget(file_chooser)

        popup = Popup(title="Save Password", content=content, size_hint=(0.8, 0.8))
        save_button = Button(text="Save", size_hint_y=None, height=40)
        save_button.bind(on_press=lambda x: self.save_to_file(file_chooser.path, password_to_save, popup))
        content.add_widget(save_button)

        popup.open()

    def save_to_file(self, file_path, password, popup):
        try:
            with open(file_path, "w") as file:
                file.write(password)
            self.show_message("Success", "Password saved successfully.")
        except Exception as e:
            self.show_message("Error", f"Error while saving the password: {e}")
        finally:
            popup.dismiss()

    def show_warning(self, instance):
        self.show_message("Warning", "Make sure to save your password securely. We are not responsible for any loss of data.")

    def show_message(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def toggle_show_password(self, instance, value):
        if value:
            self.password_entry.password = False
        else:
            self.password_entry.password = True


if __name__ == "__main__":
    PasswordGeneratorApp().run()
