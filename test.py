import unittest
import main
import os
from dotenv import load_dotenv

load_dotenv()

class TestViewer(unittest.TestCase):

  zenpy_client = main.login(os.environ.get("EMAIL"), os.environ.get("TOKEN"), os.environ.get("SUBDOMAIN"))

  def test_login(self):
    self.assertTrue(main.login_status())

  def test_num_tickets(self):
    self.assertEqual(len(main.get_tickets(self.zenpy_client)), 100)

if __name__ == "__main__":
  unittest.main()