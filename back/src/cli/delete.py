from .cli import cli


@cli.group()
def delete():
    pass


@delete.command()
def users():
    from web.managers import UsersManager
    manager = UsersManager()
    manager.delete_users_table()
