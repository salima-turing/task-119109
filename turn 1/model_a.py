import unittest

class ResidencyComplianceTest(unittest.TestCase):

	def setUp(self):
		self.residency_data = [
			{"country": "USA", "years_resident": 5},
			{"country": "Canada", "years_resident": 2},
			{"country": "Mexico", "years_resident": 10},
			{"country": "France", "years_resident": 3},
		]

	def test_check_minimum_residency_requirement(self):
		min_years_by_country = {
			"USA": 2,
			"Canada": 1,
			"Mexico": 5,
			"France": 3,
		}

		for entry in self.residency_data:
			country = entry["country"]
			years_resident = entry["years_resident"]
			min_required = min_years_by_country.get(country, 0)
			self.assertGreaterEqual(years_resident, min_required,
				f"Residency requirement not met for {country}: {years_resident} < {min_required}")

if __name__ == '__main__':
	unittest.main()
