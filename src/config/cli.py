from typer import Typer

from src.infra.cli import qrcode

def init_app(app: Typer):
    app.add_typer(qrcode.app, name='qrcode')
