================
RDP-Tools
================


.. .. image:: https://img.shields.io/pypi/v/RiboMetric.svg
..         :target: https://pypi.python.org/pypi/RiboMetric

.. .. image:: https://readthedocs.org/projects/RiboMetric/badge/?version=latest
..         :target: https://RiboMetric.readthedocs.io/en/latest/?version=latest
..         :alt: Documentation Status

.. .. image:: https://pyup.io/repos/github/JackCurragh/RiboMetric/shield.svg
..      :target: https://pyup.io/repos/github/JackCurragh/RiboMetric/
..      :alt: Updates


A python command-line utility for programmatically interacting with RiboSeq.Orgs Data Portal 


* Free software: MIT license
* Documentation: https://RDP-Tools.readthedocs.io.


Installation
------------

Install RDP-Tools by running:
.. code-block:: console
   pip install RiboSeq-DP-Tools

or:
.. code-block:: console
   docker pull quay.io/jackcurragh/rdp-tools


Usage
-----

RDP-Tools is intended to be used as a command line tool.

To collapse a FASTQ file, run:
.. code-block:: console
   RDP-Tools collapse <input_FASTQ>

To inflate a FASTA file, run:
.. code-block:: console
    
    RDP-Tools inflate <input_FASTA>

To inflate a FASTA to a FASTQ file, run:
.. code-block:: console
   RDP-Tools inflate <input_FASTA> -o <output_file>.fastq/fq

To inflate a BAM file, run:
.. code-block:: console

    RDP-Tools inflate <input_BAM>
    

For more information on how to use RDP-Tools, see the documentation_ or use :code:`--help`

.. _documentation: https://rdp-tools.readthedocs.io/en/latest/?version=latest


