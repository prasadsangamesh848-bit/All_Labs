
import pytest

from electricity_bill import energy_charge, late_fee, subsidy


# ENERGY CHARGE TEST CASES

def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200

def test_boundary_100_units():
    assert energy_charge(100, "domestic") == 350

def test_medium_usage():
    assert energy_charge(200, "domestic") == 850

def test_boundary_300_units():
    assert energy_charge(300, "domestic") == 1350

def test_high_usage():
    assert energy_charge(400, "domestic") == 2150

def test_commercial_connection():
    assert energy_charge(50, "commercial") == 450

def test_invalid_connection():
    with pytest.raises(ValueError):
        energy_charge(50, "industrial")

def test_negative_units():
    with pytest.raises(ValueError):
        energy_charge(-10, "domestic")


# LATE FEE TEST CASES

def test_paid_on_time():
    assert late_fee(500, 0) == 0

def test_negative_late_days():
    assert late_fee(500, -5) == 0

def test_late_payment_within_15_days():
    assert late_fee(500, 10) == 50

def test_late_payment_after_15_days():
    assert late_fee(500, 20) == 100

def test_high_bill_late_payment():
    assert late_fee(3000, 20) == 250

def test_bill_exactly_2000():
    assert late_fee(2000, 20) == 100


# SUBSIDY TEST CASES

def test_senior_citizen_subsidy():
    assert subsidy(50, True, False) == 50

def test_non_senior_no_solar():
    assert subsidy(50, False, False) == 0

def test_solar_subsidy():
    assert subsidy(150, False, True) == 100

def test_senior_and_solar_subsidy():
    assert subsidy(50, True, True) == 150

def test_solar_above_300_units():
    assert subsidy(350, False, True) == 0

def test_senior_above_100_units():
    assert subsidy(150, True, False) == 0

def test_exactly_100_units_senior():
    assert subsidy(100, True, False) == 50

def test_exactly_300_units_solar():
    assert subsidy(300, False, True) == 100
