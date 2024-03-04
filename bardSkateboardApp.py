import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Define the user class
class User:
    def __init__(self, name, profile_picture, uploads):
        self.name = name
        self.profile_picture = profile_picture
        self.uploads = uploads

# Define the app class
class SkateboardingApp(App):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def build(self):
        # Create the main layout
        main_layout = GridLayout(cols=1, spacing=10)

        # Create the header
        header = FloatLayout()
        header_label = Label(text="Skateboarding App", font_size=30)
        header.add_widget(header_label)

        # Create the profile section
        profile_section = FloatLayout()
        profile_image = Image(source=self.user.profile_picture)
        profile_name = Label(text=self.user.name)
        profile_section.add_widget(profile_image)
        profile_section.add_widget(profile_name)

        # Create the uploads section
        uploads_section = ScrollView()
        uploads_grid = GridLayout(cols=1, spacing=10)
        for upload in self.user.uploads:
            upload_image = Image(source=upload)
            uploads_grid.add_widget(upload_image)
        uploads_section.add_widget(uploads_grid)

        # Create the follow section
        follow_section = FloatLayout()
        follow_button = Button(text="Follow")
        follow_section.add_widget(follow_button)

        # Create the award section
        award_section = FloatLayout()
        award_button = Button(text="Award")
        award_section.add_widget(award_button)

        # Add all of the sections to the main layout
        main_layout.add_widget(header)
        main_layout.add_widget(profile_section)
        main_layout.add_widget(uploads_section)
        main_layout.add_widget(follow_section)
        main_layout.add_widget(award_section)

        return main_layout

# Run the app
if __name__ == "__main__":
    # Create a user
    user = User("Your Name", "profile_picture.jpg", ["upload1.jpg", "upload2.jpg"])

    # Create the app
    SkateboardingApp(user).run()

