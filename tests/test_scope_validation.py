from dharma.network.scope_validation import ScopeValidation
def test_ok():
 s=ScopeValidation();assert s.allowed({"read"},"read")
def test_fail():
 s=ScopeValidation();assert not s.allowed({"read"},"write")
def test_two():
 s=ScopeValidation();assert s.allowed({"read","write"},"write")
def test_empty():
 s=ScopeValidation();assert not s.allowed(set(),"x")
def test_many():
 s=ScopeValidation();assert s.allowed(set("abc"),"a")
def test_missing():
 s=ScopeValidation();assert not s.allowed({"x"},"y")
def test_same():
 s=ScopeValidation();assert s.allowed({"z"},"z")
def test_bool():
 s=ScopeValidation();assert isinstance(s.allowed({"a"},"a"),bool)
def test_one():
 s=ScopeValidation();assert s.allowed({"1"},"1")
def test_case():
 s=ScopeValidation();assert not s.allowed({"Read"},"read")
def test_space():
 s=ScopeValidation();assert s.allowed({"a b"},"a b")
def test_symbol():
 s=ScopeValidation();assert s.allowed({"*"},"*")
