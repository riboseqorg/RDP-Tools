"""Console script for RiboMetric."""
import click
import os

from RDPTools import RDPTools

def is_binary(file_path):
    '''
    Determine if a file is binary or text.

    Args:
        file_path (str): Path to file

    Returns:
        bool: True if file is binary, False if file is text
    '''
    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if b'\x00' in chunk:
                    return True
                if not chunk:
                    break
    except Exception:
        return False
    return False


def determine_file_mode(value):
    '''
    Determine the mode in which a file should be read in 

    Args:
        value (click.File): Click File object

    Returns:
        click.File: Click File object with correct mode
    '''
    if value is None:
        return None
    if is_binary(value):
        return click.File('rb')
    else:
        return click.File('r')


def generate_output_filename(ctx, param, value):
    '''
    Generate the output filename for the collapse command

    Args:
        ctx (click.Context): Click context object
        param (click.Parameter): Click parameter object
        value (str): Output filename

    Returns:
        str: Output filename
    '''
    if value is not None:
        return value  # If --output is specified, use the provided filename
    if ctx.params['infile']:
        input_filename = ctx.params['infile'].name
        # Generate the default output filename by replacing the extension
        base_name, _ = os.path.splitext(input_filename)
        return f"{base_name}.collapsed.fa"
    return '.fasta'  # If --output and input_file are not specified, use '.fasta'

    

@click.group()
def rdp_tools():
    pass

@rdp_tools.command()
@click.argument('infile', type=determine_file_mode)
@click.option('--output', '-o', callback=generate_output_filename, help='Path to the output Fasta file')
def collapse(infile, output):
    #print input and output
    print(infile)

    click.echo("Running collapse command...")
    rdp = RDPTools()

@rdp_tools.command()
@click.argument('infile', type=determine_file_mode)
@click.option('--output', '-o', callback=generate_output_filename, help='Path to the output Fasta file')
def inflate(infile, output):
    click.echo("Running inflate command...")

@rdp_tools.command()
def query():
    click.echo("Running query command...")

if __name__ == '__main__':
    rdp_tools()