"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.conformance_suite import ConformanceSuite
c=ConformanceSuite()
def test_all(): assert c.run([1,1])
def test_fail(): assert not c.run([1,0])
def test_passed(): assert c.passed([1,0,1])==2
def test_total(): assert c.total([1,0,1])==3
def test_empty(): assert c.run([])
def test_zero(): assert c.passed([])==0
def test_many(): assert c.total(list(range(5)))==5
def test_true(): assert c.run([True])
def test_false(): assert not c.run([False])
def test_bool(): assert isinstance(c.run([True]),bool)
def test_int(): assert c.passed([True,True])==2
def test_mix(): assert c.total([True,False])==2
