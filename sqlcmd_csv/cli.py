from .core import FixedWidthSplitter
import click
import pandas as pd

@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def cli(input, output):
    """Convert output from microsoft's sqlcmd to valid csv.
    Solve https://stackoverflow.com/questions/425379/how-to-export-data-as-csv-format-from-sql-server-using-sqlcmd
    Usage:
    sqlcmd ... -o out.txt
    sqlcmd_csv out.txt out.csv
    """
    result = input.readlines()
    sp = FixedWidthSplitter(result[1])
    header = sp.split(result[0])
    body = sp.split(result[2:-3])
    df = pd.DataFrame(body, columns=header)
    df.to_csv(output)
