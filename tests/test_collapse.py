
from RDPTools.collapse import collapse

import gzip
import hashlib


def test_collapse_fq():
    collapse(
        'tests/test_data/reads.fq',
        'tests/test_data/reads.collapsed.fq',
    )
    with open('tests/test_data/reads.collapsed.fq', 'rb') as f:
        m = hashlib.md5()
        m.update(f.read())
        assert m.hexdigest() == '1d2cc643a8ca7642e68964fae580b56b'

def test_collapse_fq_gz():
    collapse(
        'tests/test_data/reads.fq.gz',
        'tests/test_data/reads.collapsed.fq.gz',
    )
    
    # these files must be read differently as gzip files from python automatically
    # add the metadata (no -n flag) so MD5 hashes will not match
    with gzip.open('tests/test_data/reads.collapsed.fq.gz', 'rb') as f:
        content = f.read()
    
    md5_hash = hashlib.md5(content).hexdigest()
    assert md5_hash == '1d2cc643a8ca7642e68964fae580b56b'

def test_collapse_format():
    collapse(
        'tests/test_data/reads.fq',
        'tests/test_data/reads.collapsed.fq',
        format='>testREADtestCOUNT',
    )
    with open('tests/test_data/reads.collapsed.fq', 'rb') as f:
        m = hashlib.md5()
        m.update(f.read())
        assert m.hexdigest() == 'd05b84c78663ef7b5455561bae4de704'

