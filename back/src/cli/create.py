import click

from .cli import cli


@cli.group()
def create():
    pass


@create.command()
@click.option('--mail', prompt=True)
@click.option('--password', prompt=True)
@click.option('--admin/--no-admin', default=False)
def user(mail, password, admin):
    from web.managers import UsersManager, UserAlreadyRegistered
    manager = UsersManager()
    try:
        manager.create_user(mail, password, admin)
    except UserAlreadyRegistered:
        click.echo('User {} already registered'.format(mail))
