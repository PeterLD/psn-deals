import click
from tabulate import tabulate

from utils import current_sales, get_deals

@click.group()
def cli():
    """Simple command-line scraper for PSN sales."""
    pass

@cli.command()
@click.option('--delimiter', default='\t', help='Delimiter to be used for output values.')
@click.option('--out', type=click.File('w'), default='-', help='File to output values to.')
def current(delimiter, out):
    """Retrieves any currently running sales."""
    sales = []

    for i, sale in enumerate(current_sales()):
        sales.append([str(i + 1), sale['title'], sale['link']])

    click.echo(tabulate(sales, headers=['ID', 'Sale', 'Link']))

@cli.command()
@click.argument('sale_id', type=int)
def sale(sale_id):
    """Retrieves deals for a given sale."""
    deals = []

    for deal in get_deals(sale_id):
        deals.append([deal['title'], deal['platform'], deal['type'], deal['original_price'], deal['sale_price'], deal['link']])

    click.echo(tabulate(deals, headers=['Title', 'Platform', 'Type', 'Original Price', 'Sale Price', 'Link']))
