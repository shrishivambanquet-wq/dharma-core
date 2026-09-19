from dharma.network.compatibility import Compatibility


def test_same_version():
    assert Compatibility().supports("0.1")


def test_wrong_version():
    assert not Compatibility().supports("0.2")


def test_negotiate_success():
    assert Compatibility().negotiate("0.1") == "0.1"


def test_negotiate_fail():
    assert Compatibility().negotiate("9.9") is None


def test_local_version():
    assert Compatibility().local_version == "0.1"
