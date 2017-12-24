import click

from utils import current_sales

@click.group()
def cli():
    """Simple command-line scraper for PSN sales."""
    pass

@cli.command()
@click.option('--delimiter', default='\t', help='Delimiter to be used for output values.')
@click.option('--out', type=click.File('w'), default='-', help='File to output values to.')
def current(delimiter, out):
    sales = [delimiter.join(['#', 'sale', 'link'])]

    for i, sale in enumerate(current_sales()):
        sales.append(delimiter.join([str(i), sale['name'], sale['href']]))

    click.echo('\n'.join(sales), file=out)
