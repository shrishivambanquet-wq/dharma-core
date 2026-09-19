from dharma.network.renewal import SessionRenewal
from dharma.network.token import SessionToken


def test_new_token():
    old = SessionToken.create()
    new = SessionRenewal(old).renew()
    assert new.value != old.value


def test_changed():
    assert SessionRenewal(SessionToken.create()).changed()


def test_short_exists():
    assert len(SessionRenewal(SessionToken.create()).renew().short()) == 8


def test_type():
    assert isinstance(SessionRenewal(SessionToken.create()).renew(), SessionToken)


def test_not_empty():
    assert SessionRenewal(SessionToken.create()).renew().value != ""
