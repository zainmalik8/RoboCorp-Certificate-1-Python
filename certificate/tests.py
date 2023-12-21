import unittest
from pathlib import Path
from dataclasses import asdict

from config import BotData
from lazy.project import Process


class CertificateTest(unittest.TestCase):
    process = driver = None

    @classmethod
    def setUpClass(cls):
        cls.process = Process(**asdict(BotData()))
        cls.driver = cls.process.browser
        cls.process.open_browser()

    def test010_site_name(self):
        self.assertEqual(self.driver.get_title(), "RobotSpareBin Industries Inc. - Intranet")

    def test020_login(self):
        self.assertTrue(self.process.login())

    def test030_download_file(self):
        self.process.download()
        sales_files = Path(Path(self.process.downloading_path) / "SalesData.xlsx")
        self.assertTrue(sales_files.exists())

    def test040_sheet_data(self):
        from RPA.Tables import Table
        self.process.sheet()
        self.assertIsInstance(self.process.sheet_data, Table)

    def test050_form_entries(self):
        self.process.form_entries()
        self.assertEqual(len(self.process.sheet_data), self.process.sales_entries)

    def test060_summary_screenshot(self):
        self.process.take_summary_screenshot()
        summary_ss = Path(Path(self.process.downloading_path) / "sales_summary.png")
        self.assertTrue(summary_ss.exists())

    def test070_results(self):
        self.process.result_into_pdf()
        sales_pdf = Path(Path(self.process.downloading_path) / "sales_results.pdf")
        self.assertTrue(sales_pdf.exists())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_browser()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(processTest)
    # unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: int(x > y) - int(x < y)
    # # Run the tests
    # unittest.TextTestRunner().run(suite)
    unittest.main()
