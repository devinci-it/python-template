import click
from prompts.select import single_select, multi_select

@click.group()
def cli():
    pass

@cli.command()
def example_single_select():
    options = ['Option 1', 'Option 2', 'Option 3']
    prompt = "Select an option using arrow keys:"
    select_command = single_select(prompt, options)
    select_command()

@cli.command()
def example_multi_select():
    options = ['Option 1', 'Option 2', 'Option 3']
    prompt = "Select multiple options using arrow keys:"
    select_command = multi_select(prompt, options)
    select_command()

if __name__ == '__main__':
    cli()
