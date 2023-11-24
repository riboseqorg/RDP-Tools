.. RDP-Tools documentation master file, created by
   sphinx-quickstart on Thu Nov 23 10:48:48 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to RDP-Tools's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

RDP-Tools
=========

RDP-Tools is a Python package for collapsing and inflating (de-collapsing) Ribosome Profiling data files obtained from RiboSeq.Org's (https://riboseq.org) Data Portal (https://rdp.ucc.ie).

It is also home to any future tools developed for interacting with RiboSeq.Org's Data Portal. 

Features
--------

  - File Collapsing:

   - FASTQ to Collapsed FASTA

  - File Inflating:

   - FASTA to Inflated FASTA 
   - FASTA to Inflated FASTQ
   - BAM to Inflated BAM 

Installation
------------

Install RDP-Tools by running:

   ``pip install RiboSeq-DP-Tools``

or:

   ``docker pull quay.io/jackcurragh/rdp-tools``


Usage
-----

RDP-Tools is intended to be used as a command line tool.

To collapse a FASTQ file, run:

   ``RDP-Tools collapse <input_FASTQ>``

To inflate a FASTA file, run:
   ``RDP-Tools inflate <input_FASTA>``

To inflate a FASTA to a FASTQ file, run:
   
   ``RDP-Tools inflate <input_FASTA> -o <output_file>.fastq/fq``

To inflate a BAM file, run:
      
   ``RDP-Tools inflate <input_BAM>``


Contribute
----------

- Issue Tracker: (github.com/riboseqorg/RDP-Tools/issues)
- Source Code: (github.com/riboseqorg/RDP-Tools)

Support
-------

If you are having issues, please let us know.
Our email is riboseqXYZ@gmail.com (remove the XYZ).

License
-------

The project is licensed under the MIT license.