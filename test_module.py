import unittest
import pandas as pd
from main import sea_level_analysis

class SeaLevelAnalysisTestCase(unittest.TestCase):
    def test_sea_level_analysis(self):
        sea_level_analysis()
        # Check if the analysis completes without errors
        self.assertTrue(True)

    def test_dataset_import(self):
        data = pd.read_csv('epa-sea-level.csv')
        # Check if the dataset is imported correctly
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 134)

if __name__ == '__main__':
    unittest.main()
