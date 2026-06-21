from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Input, Static
from core import download_video, download_audio, get_downloads_path


TITLE = """
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""


class Downloader(App):
    CSS_PATH = './style/base.tcss'
    BINDINGS = [Binding('ctrl+q', 'quit', 'Sair da aplicação')]

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static(TITLE)
            widget_input = Input(placeholder='Insira a URL do vídeo', id='entry')
            widget_input.border_title = 'URL'
            yield widget_input
            with Horizontal():
                yield Button('Baixar vídeo', id='video')
                yield Button('Baixar áudio', id='audio')
        yield Footer()

    def get_url(self) -> str:
        return self.query_one('#entry', Input).value

    def set_empty(self):
        input_widget = self.query_one('#entry', Input)
        input_widget.value = ''

    @on(Button.Pressed, '#video')
    def download_video(self):
        url = self.get_url()
        if url == '':
            self.notify('Informe a [bold u]URL[/bold u] do vídeo', severity='error')
            return

        self.set_empty()
        result = download_video(url)
        if result[0]:
            self.notify(
                f'O vídeo [bold]{result[1]}[/bold] foi baixado com sucesso em [bold]{get_downloads_path()}[/bold]'
            )
        else:
            self.notify(f'Não foi possível baixar o vídeo [bold]{result[1]}[/bold]', severity='error')

    @on(Button.Pressed, '#audio')
    def download_audio(self):
        url = self.get_url()
        if url == '':
            self.notify('Informe a [bold u]URL[/bold u] do vídeo', severity='error')
            return

        self.set_empty()
        self.set_empty()
        result = download_audio(url)
        if result[0]:
            self.notify(
                f'O áudio [bold]{result[1]}[/bold] foi baixado com sucesso em [bold]{get_downloads_path()}[/bold]'
            )
        else:
            self.notify(f'Não foi possível baixar o áudio [bold]{result[1]}[/bold]', severity='error')


if __name__ == '__main__':
    Downloader().run()
