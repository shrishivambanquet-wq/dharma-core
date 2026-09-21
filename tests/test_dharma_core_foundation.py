"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.dharma_core_foundation import DharmaCoreFoundation
d=DharmaCoreFoundation()
def test_version(): assert d.version()=="1.0.0-rc1"
def test_ready(): assert d.ready()
def test_bool(): assert isinstance(d.ready(),bool)
def test_string(): assert isinstance(d.version(),str)
def test_same(): assert d.version()=="1.0.0-rc1"
def test_again(): assert d.ready()
def test_repeat(): assert d.ready()
def test_value(): assert d.VERSION=="1.0.0-rc1"
def test_type(): assert type(d.version()) is str
def test_true(): assert d.ready()
def test_keep(): assert d.version().startswith("1.")
def test_final(): assert d.version()=="1.0.0-rc1"
