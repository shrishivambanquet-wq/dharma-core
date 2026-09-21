from dharma.network.compatibility_vectors import CompatibilityVectors
v=CompatibilityVectors()
A={"protocol":"1","features":["a","b"]}
B={"protocol":"1","features":["b","c"]}
C={"protocol":"2","features":["b"]}
def test_protocol(): assert v.compatible(A,B)
def test_fail(): assert not v.compatible(A,C)
def test_shared(): assert v.shared(A,B)==["b"]
def test_empty(): assert v.shared(A,C)==["b"]
def test_same(): assert v.shared(A,A)==["a","b"]
def test_many(): assert len(v.shared(A,B))==1
def test_type(): assert isinstance(v.shared(A,B),list)
def test_sort(): assert v.shared({"protocol":"1","features":["b","a"]},A)==["a","b"]
def test_dup(): assert v.shared({"protocol":"1","features":["a","a"]},A)==["a"]
def test_bool(): assert isinstance(v.compatible(A,B),bool)
def test_keys(): assert "protocol" in A
def test_features(): assert "features" in A
