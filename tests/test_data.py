# tests/test_data.py
from hillstrom_uplift.data import load


def test_shape_and_groups():
    df = load()
    assert len(df) == 64000
    assert set(df["treatment"].unique()) == {"control", "mens", "womens"}


def test_no_missing_in_key_columns():
    df = load()
    assert df[["visit", "conversion", "spend", "treatment"]].notna().all().all()
