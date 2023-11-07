"""Console script for RiboMetric."""
import click
import os

from RDPTools import RDPTools
from collapse import collapse as collapse_reads


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
        input_filename = ctx.params['infile']
        # Generate the default output filename by replacing the extension
        base_name, _ = os.path.splitext(input_filename)
        return f"{base_name}.collapsed.fa"
    return '.fasta'  # If --output and input_file are not specified, use '.fasta'


@click.group()
def rdp_tools():
    pass

@rdp_tools.command()
@click.argument('infile')
@click.option('--output', '-o', callback=generate_output_filename, help='Path to the output Fasta file')
@click.option('--format', '-f', default=f">seqREAD_xCOUNT", help='Custom header format')
def collapse(infile, output, format):
    click.echo(f"Input file: {infile}")
    click.echo(f"Output file: {output}")
    click.echo("Running collapse command...")
    collapse_reads(infile, output, format)


@rdp_tools.command()
@click.argument('infile')
@click.option('--output', '-o', callback=generate_output_filename, help='Path to the output Fasta file')
def inflate(infile, output):
    click.echo("Running inflate command...")


@rdp_tools.command()
def query():
    click.echo("Running query command...")

if __name__ == '__main__':
    rdp_tools()