import click

from .cli import cli


@cli.group()
def create():
    pass


@create.command()
@click.option('--mail', prompt=True)
@click.option('--firstname', prompt=True)
@click.option('--lastname', prompt=True)
@click.option('--admin/--no-admin', default=False)
def user(mail, firstname, lastname, admin):
    from web.managers import UsersManager, UserAlreadyRegistered
    manager = UsersManager()
    try:
        manager.create_user(mail, firstname, lastname, admin)
    except UserAlreadyRegistered:
        click.echo('User {} already registered'.format(mail))
