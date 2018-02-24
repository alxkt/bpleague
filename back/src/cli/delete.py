import click

from .cli import cli


@cli.group()
def delete():
    pass


@delete.command()
@click.option('--id', prompt=True)
def match(id):
    from web.managers import MatchsManager
    manager = MatchsManager(user_id=0)
    manager.delete_matchs(id)
