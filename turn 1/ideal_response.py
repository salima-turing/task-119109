import unittest
from typing import Dict, Any

def check_residency_compliance(person: Dict[str, Any]) -> bool:
    # Your residency compliance logic goes here
    # For simplicity, let's use some example criteria
    required_years_in_country: int = 2
    if person['country'] == 'USA' and person['years_in_country'] >= required_years_in_country:
        return True
    return False

class TestResidencyCompliance(unittest.TestCase):
    def test_us_residency_compliance_met(self) -> None:
        """Test for US residency compliance with sufficient years"""
        person: Dict[str, Any] = {
            'country': 'USA',
            'years_in_country': 3
        }
        self.assertTrue(check_residency_compliance(person), "US resident with 3 years should be compliant")

    def test_us_residency_compliance_not_met(self) -> None:
        """Test for US residency compliance with insufficient years"""
        person: Dict[str, Any] = {
            'country': 'USA',
            'years_in_country': 1
        }
        self.assertFalse(check_residency_compliance(person), "US resident with 1 year should not be compliant")

    def test_non_us_residency_compliance(self) -> None:
        """Test for non-US residency compliance"""
        person: Dict[str, Any] = {
            'country': 'Canada',
            'years_in_country': 5
        }
        self.assertFalse(check_residency_compliance(person), "Non-US resident should not be compliant")

if __name__ == '__main__':
    unittest.main()
