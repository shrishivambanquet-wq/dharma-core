from dharma.network.payload_cipher import PayloadCipher

KEY = "demo-session-key"

def test_encrypt_changes_text():
    assert PayloadCipher.encrypt(KEY, "hello") != "hello"

def test_round_trip():
    c = PayloadCipher.encrypt(KEY, "hello dharma")
    assert PayloadCipher.decrypt(KEY, c) == "hello dharma"

def test_same_input_same_output():
    assert PayloadCipher.encrypt(KEY, "abc") == PayloadCipher.encrypt(KEY, "abc")

def test_different_key():
    assert PayloadCipher.encrypt("k1", "abc") != PayloadCipher.encrypt("k2", "abc")

def test_empty():
    assert PayloadCipher.decrypt(KEY, PayloadCipher.encrypt(KEY, "")) == ""

def test_long_message():
    msg = "Dharma" * 100
    assert PayloadCipher.decrypt(KEY, PayloadCipher.encrypt(KEY, msg)) == msg

def test_hex_output():
    int(PayloadCipher.encrypt(KEY, "test"), 16)

def test_unicode():
    msg = "नमस्ते Dharma"
    assert PayloadCipher.decrypt(KEY, PayloadCipher.encrypt(KEY, msg)) == msg
