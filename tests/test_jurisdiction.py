"""Tests for EEZ jurisdiction tagging (the ISO2/ISO3 foreign-flag logic)."""

from __future__ import annotations

from seavigil.jurisdiction import is_foreign


def test_is_foreign_mixed_code_formats():
    # EEZ sovereign arrives as ISO3; vessel flag may be ISO2 (AIS) or ISO3 (SAR).
    assert is_foreign("AU", "AUS") is False        # ISO2 flag vs ISO3 sovereign, same country
    assert is_foreign("AUS", "AUS") is False        # ISO3 flag vs ISO3 sovereign, same country
    assert is_foreign("CN", "AUS") is True          # Chinese vessel in Australia's EEZ
    assert is_foreign("CHN", "ECU") is True          # ISO3 foreign vessel


def test_is_foreign_undetermined():
    assert is_foreign("", "AUS") is None             # unknown flag (anonymized / dark)
    assert is_foreign(None, "AUS") is None
    assert is_foreign("AU", "") is None              # unknown EEZ
    assert is_foreign("AU", None) is None
