import unittest
import main

class TestMain (unittest.TestCase):

    def test_get_all_domains(self):
        self.assertIsInstance(main.get_all_domains(), list) #This will check if the function will return a list

    def test_check_if_phishing(self):
        self.assertEqual(main.check_if_phishing("secure-bank-login.co.uk"), {"phishing": False, "domain": "secure-bank-login.co.uk"})

    def test_add_phishing_domain(self):
        self.assertEqual(main.add_phishing_domain("test-phish.co.uk", "user@email.com"), "Domain added successfully")

    def test_remove_phishing_domain(self):
        self.assertIn("Domain", main.remove_phishing_domain(1))

if __name__ == "__main__":
    unittest.main()