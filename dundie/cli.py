import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie"))
def main():
    """Dunder Mifflin Rewards System.

    This cli application controls DM rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database

    - Validates data
    - Parses the file
    - Loads to database
    """

    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "created", "e-mail"]
    for header in headers:
        table.add_column(header, style="magenta")
    result = core.load(filepath)
    for person in result:
        table.add_row(
            *[str(value) for value in person.values()]
        )  # pois agora recebe um dict

    console = Console()
    console.print(table)
