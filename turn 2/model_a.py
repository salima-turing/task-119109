import unittest
from compliance_checker import ComplianceChecker

class TestComplianceChecker(unittest.TestCase):

	def setUp(self):
		self.checker = ComplianceChecker()

	def test_compliance_with_country_a(self):
		# Define the residency requirements for Country A
		requirements = {
			"min_years_residency": 2,
			"required_documents": ["passport", "residency_permit"]
		}

		# Test data for a resident of Country A
		resident_data = {
			"country": "Country A",
			"years_residency": 3,
			"documents_provided": ["passport", "residency_permit", "birth_certificate"]
		}

		self.assertTrue(self.checker.check_compliance(resident_data, requirements))

	def test_compliance_with_country_b(self):
		requirements = {
			"min_years_residency": 5,
			"required_documents": ["passport", "work_permit", "tax_id"]
		}

		resident_data = {
			"country": "Country B",
			"years_residency": 7,
			"documents_provided": ["passport", "work_permit", "tax_id", "driver_s_license"]
		}

		self.assertTrue(self.checker.check_compliance(resident_data, requirements))

	if __name__ == '__main__':
		unittest.main()
