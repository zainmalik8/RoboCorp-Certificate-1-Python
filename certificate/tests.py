import unittest
from pathlib import Path
from dataclasses import asdict

from config import BotData
from lazy.project import Certificate


class CertificateTest(unittest.TestCase):
    certificate = driver = None

    @classmethod
    def setUpClass(cls):
        cls.certificate = Certificate(**asdict(BotData()))
        cls.driver = cls.certificate.browser
        cls.certificate.open_browser()

    def test010_site_name(self):
        self.assertEqual(self.driver.get_title(), "RobotSpareBin Industries Inc. - Intranet")

    def test020_login(self):
        self.assertTrue(self.certificate.login())

    def test030_download_file(self):
        self.certificate.download()
        sales_files = Path(Path(self.certificate.downloading_path) / "SalesData.xlsx")
        self.assertTrue(sales_files.exists())

    def test040_sheet_data(self):
        from RPA.Tables import Table
        self.certificate.sheet()
        self.assertIsInstance(self.certificate.sheet_data, Table)

    def test050_form_entries(self):
        self.certificate.form_entries()
        self.assertEqual(len(self.certificate.sheet_data), self.certificate.sales_entries)

    def test060_summary_screenshot(self):
        self.certificate.take_summary_screenshot()
        summary_ss = Path(Path(self.certificate.downloading_path) / "sales_summary.png")
        self.assertTrue(summary_ss.exists())

    def test070_results(self):
        self.certificate.result_into_pdf()
        sales_pdf = Path(Path(self.certificate.downloading_path) / "sales_results.pdf")
        self.assertTrue(sales_pdf.exists())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_browser()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(CertificateTest)
    # unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: int(x > y) - int(x < y)
    # # Run the tests
    # unittest.TextTestRunner().run(suite)
    unittest.main()
