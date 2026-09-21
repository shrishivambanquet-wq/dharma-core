from dharma.network.reference_lock import ReferenceLock
def test_lock():
 r=ReferenceLock(); r.lock("1"); assert r.current()=="1"
def test_default():
 assert ReferenceLock().current() is None
def test_overwrite():
 r=ReferenceLock(); r.lock("1"); r.lock("2"); assert r.current()=="2"
def test_string():
 r=ReferenceLock(); r.lock("v1"); assert r.current()=="v1"
def test_many():
 r=ReferenceLock(); [r.lock(str(i)) for i in range(5)]; assert r.current()=="4"
def test_none():
 assert ReferenceLock().current() is None
def test_type():
 r=ReferenceLock(); r.lock("x"); assert isinstance(r.current(),str)
def test_same():
 r=ReferenceLock(); r.lock("a"); assert r.current()=="a"
def test_again():
 r=ReferenceLock(); r.lock("z"); assert r.current()=="z"
def test_last():
 r=ReferenceLock(); r.lock("last"); assert r.current()=="last"
def test_keep():
 r=ReferenceLock(); r.lock("1"); assert r.current()=="1"
def test_final():
 r=ReferenceLock(); r.lock("final"); assert r.current()=="final"
