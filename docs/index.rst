.. RDP-Tools documentation master file, created by
   sphinx-quickstart on Thu Nov 23 10:48:48 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to RDP-Tools's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


RDP-Tools
=========

RDP-Tools is a Python package for collapsing and inflating (de-collapsing) Ribosome Profiling data files obtained from RiboSeq.Org's (https://riboseq.org) Data Portal (https://rdp.ucc.ie).

It is also home to any future tools developed for interacting with RiboSeq.Org's Data Portal. 

Features
--------

File Collapsing:
   - FASTQ to Collapsed FASTA

File Inflating:
   - FASTA to Inflated FASTA 
   - FASTA to Inflated FASTQ
   - BAM to Inflated BAM 
   
  
Installation
------------

Install RDP-Tools by running:

   .. code-block:: bash

      pip install RiboSeq-DP-Tools

or:

   .. code-block:: bash

      docker pull quay.io/jackcurragh/rdp-tools


Usage
-----

RDP-Tools is intended to be used as a command line tool.

To collapse a FASTQ file, run:

   .. code-block:: bash

      RDP-Tools collapse input.fastq

To inflate a FASTA file, run:

   .. code-block:: bash

      RDP-Tools inflate input.fasta

To inflate a FASTA to a FASTQ file, run:

   .. code-block:: bash

      RDP-Tools inflate input.fasta -o output.fastq/fq

To inflate a BAM file, run:

   .. code-block:: bash

      RDP-Tools inflate input.bam


Contribute
----------

- Issue Tracker: (https://github.com/riboseqorg/RDP-Tools/issues)
- Source Code: (https://github.com/riboseqorg/RDP-Tools)

Support
-------

If you are having issues, please let us know.
Our email is riboseqXYZ@gmail.com (remove the XYZ).

License
-------

The project is licensed under the MIT license.