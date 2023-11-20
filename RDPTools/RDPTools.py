"""Console script for RiboMetric."""
import click
import os

from .collapse import collapse as collapse_reads
from .inflate import inflate_fasta, inflate_bam


def generate_collapse_filename(ctx, param, value):
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
    return 'output.collapsed.fasta'  # If --output and input_file are not specified, use '.fasta'


def generate_inflate_filename(ctx, param, value):
    '''
    Generate the output filename for the inflate command

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
        base_name, extension = os.path.splitext(input_filename)
        if extension == '.bam':
            return f"{base_name}.inflated.bam"
        else:
            return f"{base_name}.inflated.fa"
    return 'output.inflated.fasta'  # If --output and input_file are not specified, use '.fasta'


@click.group()
def rdp_tools():
    pass

@rdp_tools.command()
@click.argument('infile')
@click.option('--output', '-o', callback=generate_collapse_filename, help='Path to the output Fasta file')
@click.option('--format', '-f', default=f">seqREAD_xCOUNT", help='Custom header format')
@click.option('--compress', '-c', is_flag=True, help='Compress the output file')
def collapse(infile, output, format, compress):
    click.echo(f"Input file: {infile}")
    click.echo(f"Output file: {output}")
    click.echo("Collapsing...")
    collapse_reads(infile, output, format, compress)


@rdp_tools.command()
@click.argument('infile')
@click.option('--output', '-o', callback=generate_inflate_filename, help='Path to the output file')
@click.option('--format', '-f', default=f">seqREAD_xCOUNT", help='Custom header format')
@click.option('--compress', '-c', is_flag=True, help='Compress the output file')
def inflate(infile, output, format, compress):
    if output.endswith('bam'):
        if compress:
            click.echo("BAM files are already compressed. Ignoring --compress flag.")
        click.echo("Inflating...")
        inflate_bam(infile, output, format)
    else:
        click.echo("Inflating...")
        inflate_fasta(infile, output, format, compress)


@rdp_tools.command()
def query():
    click.echo("Running query command...")

if __name__ == '__main__':
    rdp_tools()