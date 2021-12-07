import click

####
@click.command()
@click.argument('location')
@click.option('--apikey', '-a', help='your API key')
@click.option('--humidity', is_flag=True)
@click.option('--numbers', default=1, show_default=True, help='number of results')
@click.option('--range', nargs=2, type=(int, int), default=[None]*2) #2 argumenty
@click.option('--verbose', '-v', count=True) # -v -vv -vvvv
@click.option('--units',  type=click.Choice(['IMPERIAL', 'METRIC'], case_sensitive=False), default='METRIC')
def main(location, apikey, humidity, units, numbers, range, verbose ):
    """
    This is text displayed after --help option
    """
    print(f"Location = {location}")
    print(f"Humidity = {humidity}")
    print(f"Metric = {units}")
    print(f"API key = {apikey}")
    print(f"Numer of results = {numbers}")
    print(f"Range = {range}")
    print(f"Verbose count = {verbose}")


if __name__ == "__main__":
    main()