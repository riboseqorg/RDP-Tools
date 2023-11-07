
import gzip
from Bio.SeqIO.FastaIO import SimpleFastaParser

def get_read_count(header: str, format: str = 'seqREAD_xCOUNT') -> int:
    '''
    Extract the read count from the read header

    Args:
        header (str): Read header
        format (str, optional): The layout of the read file headers. Defaults to 'seqREAD_xCOUNT'.

    Raises:
        ValueError: If the header format is not recognized.

    Returns:
        int: The read count
    '''
    delimiter = format.split('READ')[1].split('COUNT')[0]
    read_count = header.split(delimiter)[1].split('COUNT')[0]
    return int(read_count)


def inflate_fasta(infile: str, outfile: str, format: str = 'seqREAD_xCOUNT') -> None:
    """
    Inflate the contents of a FASTA file based on the read count in the read name.

    Args:
        infile (str): The path to the input FASTA file.
        outfile (str): The path to the output file. Extension determines the output format. 
        format (str, optional): The layout of the read file headers. Defaults to 'seqREAD_xCOUNT'.
    Raises:
        ValueError: If the output format is not 'fasta' or 'fastq'.

    Returns:
        None
    """
    if any(outfile.endswith(ext) for ext in ['fa', 'fasta', 'fna']):
        out_format = 'fasta'
    elif any(outfile.endswith(ext) for ext in ['fq', 'fastq']):
        out_format = 'fastq'
    else:
        raise ValueError("Output format must be 'fasta' or 'fastq'")

    with open(infile, 'rb') as f:
        magic_number = f.read(2)
        if magic_number == b'\x1f\x8b':
            f = gzip.open(infile, 'rt')
        else:
            f.seek(0)
            f = open(infile, 'r')
        for header, sequence in SimpleFastaParser(f):
            read_count = get_read_count(header, format)
            with open(outfile, 'a') as out:
                for i in range(read_count):
                    if out_format == 'fasta':
                        out.write(f">{header}\n{sequence}\n")
                    elif out_format == 'fastq':
                        out.write(f"@{header}\n{sequence}\n+\n{'I'*len(sequence)}\n")


def inflate_bam(infile: str, format: str = 'seqREAD_xCOUNT') -> None:
    """
    Inflate the contents of a BAM file based on the read count in the read name.

    Args:
        infile (str): The path to the input BAM file.
        format (str, optional): The layout of the read headers. Defaults to 'seqREAD_xCOUNT'.

    Raises:
        ValueError: If the output format is not 'fasta' or 'fastq'.

    Returns:
        None
    """
    return None