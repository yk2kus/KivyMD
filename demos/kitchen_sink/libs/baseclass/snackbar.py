from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.uix.button import MDFlatButton


class KitchenSinkSnackBar(Screen):
    snackbar = None
    _interval = 0

    def show_example_snackbar(self, snack_type):
        """Create and show instance Snackbar."""

        def callback(instance):
            from kivymd.toast import toast

            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.snackbar.duration + 0.5:
                anim = Animation(y=dp(10), d=0.2)
                anim.start(self.ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.snackbar = None

        from kivymd.uix.snackbar import Snackbar

        if snack_type == "simple":
            Snackbar(text="This is a snackbar!").open()
        elif snack_type == "button":
            snack = Snackbar(text="This is a snackbar")
            snack.buttons = [
                MDFlatButton(
                    text="WITH A BUTTON",
                    text_color=(1, 1, 1, 1),
                    on_release=callback,
                )
            ]
            snack.open()
        elif snack_type == "verylong":
            Snackbar(
                text="This is a very very very very very very very "
                "long snackbar!"
            ).open()
        elif snack_type == "padding":
            snack = Snackbar(text="This is a snackbar!", padding="20dp")
            snack.buttons = [
                MDFlatButton(
                    text="ACTION",
                    text_color=(1, 1, 1, 1),
                    on_release=callback,
                )
            ]
            snack.open()
        elif snack_type == "float":
            if not self.snackbar:
                self.snackbar = Snackbar(
                    text="This is a snackbar!",
                    duration=3,
                )
                self.snackbar.buttons = [
                    MDFlatButton(
                        text="ACTION",
                        text_color=(1, 1, 1, 1),
                        on_release=callback,
                    )
                ]
                self.snackbar.open()
                anim = Animation(y=dp(72), d=0.2)
                anim.bind(
                    on_complete=lambda *args: Clock.schedule_interval(
                        wait_interval, 0
                    )
                )
                anim.start(self.ids.button)
