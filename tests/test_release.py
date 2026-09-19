from dharma.core.release import DharmaRelease


def test_banner():
    assert DharmaRelease().banner() == "Dharma v0.1-alpha"


def test_alpha():
    assert DharmaRelease().is_alpha()


def test_frozen():
    assert DharmaRelease().frozen


def test_protocol_level():
    assert DharmaRelease().protocol_level == 30


def test_name():
    assert DharmaRelease().name == "Dharma"
