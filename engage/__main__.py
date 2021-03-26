import click

from . import Engage


@click.group()
def cli():
  pass

@cli.command()
def run():
  app = Engage()
  app.run()

if __name__ == "__main__":
  cli()
