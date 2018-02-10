import click

from .cli import cli


@cli.group()
def get():
    pass


@get.command()
def users():
    from web.managers import UsersManager
    manager = UsersManager()
    click.echo(click.style('== Users ==', bold=True))
    click.echo(manager.get_all())
