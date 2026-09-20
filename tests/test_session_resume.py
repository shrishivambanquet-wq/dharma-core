from dharma.network.session_resume import SessionResume


def test_resume_returns_true():
    assert SessionResume("s1").resume()


def test_active():
    assert SessionResume("s1").active()


def test_session_id():
    assert SessionResume("abc").session_id == "abc"


def test_last_seen_exists():
    assert SessionResume("s1").last_seen > 0


def test_resume_updates_time():
    s = SessionResume("s1")
    before = s.last_seen
    s.resume()
    assert s.last_seen >= before
