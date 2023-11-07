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

To install RDP-Tools:

.. code-block:: console

    $ pip install RDP-Tools

Usage
------------

Collapse a a FASTQ file to a FASTA file:

.. code-block:: console

    $ RDP-Tools collapse 
    
Re-inflate a collapsed file (FASTA/BAM)

.. code-block:: console

    $ RDP-Tools inflate 

For more information on how to use RiboMetric, see the documentation_ or use :code:`--help`

.. _documentation: https://ribometric.readthedocs.io/en/latest/?version=latest


