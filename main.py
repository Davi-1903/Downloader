from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class Downloader(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()


if __name__ == '__main__':
    Downloader().run()
