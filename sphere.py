import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name', default='sphere')
def start(name):
    """This tool helps to manage spheres."""
    click.echo('Start Raphael Sphere with name %s' % name)
