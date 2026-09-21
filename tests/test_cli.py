"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import subprocess
import sys


def test_search_person():
    out = subprocess.check_output(
        [sys.executable, "-m", "dharma.cli", "search", "Paresh"],
        text=True,
    )
    assert "Paresh Somani" in out


def test_search_org():
    out = subprocess.check_output(
        [sys.executable, "-m", "dharma.cli", "search", "Somani"],
        text=True,
    )
    assert "Somani Caterers" in out


def test_case_insensitive():
    out = subprocess.check_output(
        [sys.executable, "-m", "dharma.cli", "search", "PARESH"],
        text=True,
    )
    assert "Paresh Somani" in out


def test_partial():
    out = subprocess.check_output(
        [sys.executable, "-m", "dharma.cli", "search", "Cater"],
        text=True,
    )
    assert "Somani Caterers" in out


def test_missing():
    out = subprocess.check_output(
        [sys.executable, "-m", "dharma.cli", "search", "Ghost"],
        text=True,
    )
    assert out.strip() == ""
