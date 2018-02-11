from .cli import cli


@cli.group()
def delete():
    pass


@delete.command()
def users():
    from web.managers import UsersManager
    manager = UsersManager()
    manager.delete_users_table()


@delete.command()
def matchs():
    from web.managers import MatchsManager
    manager = MatchsManager()
    manager.delete_matchs_table()
