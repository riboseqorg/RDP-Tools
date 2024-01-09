# RDP-Tools

`RDP-Tools` is a Python package for collapsing and inflating (de-collapsing) Ribosome Profiling data files obtained from [RiboSeq.Org's Data Portal](https://riboseq.org) and [RDP (RiboSeq Data Portal)](https://rdp.ucc.ie).

It also facilitates querying the RiboSeq Data Portal database to programmatically identify samples of interest and subsequently facilitate file download. 

## Features

#### File Collapsing:

- FASTQ to Collapsed FASTA

#### File Inflating:

- FASTA to Inflated FASTA
- FASTA to Inflated FASTQ
- BAM to Inflated BAM

#### Programmatic Database Interaction 
- Query Metadata
- Fetch Download Links
- Return Database Fields 

## Installation

Install `RDP-Tools` by running:

``` bash 
pip install RiboSeq-DP-Tools
```

or:

``` bash
docker pull quay.io/jackcurragh/rdp-tools

```

## Collapse

`RDP-Tools` collapse functionality takes a FASTQ file of Ribo-Seq reads and returns a file in FASTA format that is significantly smaller without losing any sequence information. 

Each identical Ribo-Seq read is only stored once and the number of occurrences of each read is stored in the FASTA header. Due to the nature of the short Ribo-Seq reads and their tendency to originate from a relatively low diversity set of genomic regions (CDSs) this collapsing significantly reduces file sizes and processing load. It is advised that collapsing is carried out post-QC (eg. with FastQC) as quality information is dropped from the outputted files.

#### Usage

To collapse a FASTQ file, run:

``` bash
RDP-Tools collapse input.fastq

```

## Inflate

Although collapsing Ribo-Seq reads lightens the computational load of data processing it can not be done at the expense of the usefulness of the resulting files. In order to ensure the files on RiboSeq.Org are usable in downstream applications, `RDP-Tools` also provides 'inflation' functionality. Essentially, this returns a file from its collapsed state, where each unique read gets one entry, back to where each entry in the file represents one sequenced RPF. 

#### Usage
To inflate a FASTA file, run:

``` bash
RDP-Tools inflate input.fasta
```
To inflate a FASTA to a FASTQ file (perfect sequencing quality is assigned), run:

``` bash
RDP-Tools inflate input.fasta -o output.fastq/fq
```
To inflate a BAM file, run:

``` bash
RDP-Tools inflate input.bam
```

## Database 

RDP-Tools also lets the user query the RDPs database of existing Ribo-Seq data. This facilitates the programmatic finding and fetching of Ribo-Seq read and alignment files. 

#### Usage
To get the all of the fields related to Ribo-Seq samples;

``` bash
RDP-Tools database sample-fields 
```
To get the metadata for all Ribo-Seq samples whose tissue is labeled as Lung, do:

``` bash
RDP-Tools database samples --query TISSUE=Lung 
```
To specify the fields returned for the samples that match a query, do:

``` bash
RDP-Tools database samples --query TISSUE=Lung --fields TISSUE,CELL_LINE
```
To increase or decrease the number of entries returned (default: 100), do: 

``` bash
RDP-Tools database samples --query TISSUE=Lung --fields TISSUE,CELL_LINE --limit 1000000
```
## Contribute

- Issue Tracker: [github.com/riboseqorg/RDP-Tools/issues](https://github.com/riboseqorg/RDP-Tools/issues)
- Source Code: [github.com/riboseqorg/RDP-Tools](https://github.com/riboseqorg/RDP-Tools)

## Support

If you are having issues, please let us know. Our email is riboseqXYZ@gmail.com (remove the XYZ).

## License

The project is licensed under the MIT license.