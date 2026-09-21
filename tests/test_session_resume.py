from dharma.network.session_resume import SessionResume

def test_default():
    assert SessionResume("s1").state()=="ACTIVE"

def test_interrupt():
    s=SessionResume("s1"); s.interrupt()
    assert s.state()=="INTERRUPTED"

def test_resume():
    s=SessionResume("s1"); s.interrupt()
    assert s.resume("s1")

def test_resume_state():
    s=SessionResume("s1"); s.interrupt(); s.resume("s1")
    assert s.state()=="ACTIVE"

def test_wrong_id():
    s=SessionResume("s1"); s.interrupt()
    assert not s.resume("bad")

def test_preserve_id():
    assert SessionResume("abc").session_id=="abc"

def test_double_resume():
    s=SessionResume("x"); s.interrupt()
    s.resume("x")
    assert s.resume("x")

def test_active_again():
    s=SessionResume("z"); s.interrupt(); s.resume("z")
    assert s.active
