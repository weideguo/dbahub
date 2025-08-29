"""
pip install reflex

mkdir my_app_name
cd my_app_name
reflex init
reflex run

reflex run --env prod --frontend-only

# 需要bun运行环境
"""

iimport reflex as rx


class State(rx.State):
    """The app state."""

    prompt = ""
    image_url = ""
    processing = False
    complete = False

    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")

        self.processing, self.complete = True, False
        yield
        self.image_url = "https://github.githubassets.com/favicons/favicon.svg"
        self.processing, self.complete = False, True


def index():
    return rx.center(
        rx.vstack(
            rx.heading("some head tile", font_size="1.5em"),
            rx.input(
                placeholder="Enter a prompt..",
                on_blur=State.set_prompt,
                width="25em",
            ),
            rx.button(
                "Generate Image",
                on_click=State.get_image,
                width="25em",
                loading=State.processing
            ),
            rx.cond(
                State.complete,
                rx.image(src=State.image_url, width="20em"),
            ),
            align="center",
        ),
        width="100%",
        height="100vh",
    )

app = rx.App()
app.add_page(index, title="Reflex demo")

