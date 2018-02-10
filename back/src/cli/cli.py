import click


@click.group()
def cli():
    click.echo(click.style('== BPLeague CLI ==', bold=True))
