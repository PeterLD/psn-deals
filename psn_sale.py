import click

from utils import current_sales, get_deals, format_output, OUTPUT_FORMATS, TABLE_FORMAT

format_opt = (
    ['--format', '-f'],
    {
        'type': click.Choice(OUTPUT_FORMATS),
        'default': TABLE_FORMAT,
        'help': 'Output format.'
    }
)

@click.group()
def cli():
    """Simple command-line scraper for PSN sales."""
    pass

@cli.command()
@click.option(*format_opt[0], **format_opt[1])
def list(format):
    """Retrieves any currently running sales."""
    sales = []

    for i, sale in enumerate(current_sales()):
        sales.append([str(i + 1), sale['title'], sale['link']])

    click.echo(format_output(sales, headers=['ID', 'Sale', 'Link'], format=format))

@cli.command()
@click.argument('sale_id', type=int)
@click.option(*format_opt[0], **format_opt[1])
def sale(sale_id, format):
    """Retrieves deals for a given sale."""
    deals = []

    for deal in get_deals(sale_id):
        deals.append([deal['title'], deal['platform'], deal['type'], deal['original_price'], deal['sale_price'], deal['link']])

    click.echo(format_output(deals, headers=['Title', 'Platform', 'Type', 'Original Price', 'Sale Price', 'Link'], format=format))
