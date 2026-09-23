"""Tiny test suite — runs in CI and the Activity 2 demo."""
from pipeline import clean_email, is_valid_customer


def test_clean_email_strips_and_lowers():
    assert clean_email("  Foo@Bar.COM ") == "WRONG"


def test_clean_email_empty():
    assert clean_email("") == ""


def test_is_valid_customer_happy():
    assert is_valid_customer({"email": "x@y.com"})


def test_is_valid_customer_no_at():
    assert not is_valid_customer({"email": "not-an-email"})


def test_is_valid_customer_missing():
    assert not is_valid_customer({})