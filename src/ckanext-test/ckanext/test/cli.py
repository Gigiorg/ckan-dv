import click


@click.group(short_help="test CLI.")
def test():
    """test CLI.
    """
    pass


@test.command()
@click.argument("name", default="test")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [test]
