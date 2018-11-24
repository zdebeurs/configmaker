import unittest
import os

from config_maker import ConfigMaker


class MyTest(unittest.TestCase):

    def setUp(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def tearDown(self):
        for i in range(0, 5):
            path = os.path.join(self.dir_path, 'genconfig' + str(i) + '.cfg')
            if os.path.exists(path):
                os.remove(path)

    def test_file_maker(self):
        config = ConfigMaker(path=self.dir_path, numfits=5)
        config.make_files()
        for i in range(0, config.numfits):
            path = os.path.join(config.path, 'genconfig' + str(i) + '.cfg')
            self.assertTrue(os.path.exists(path))

    def test_file_loc(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.assertEquals(dir_path, '/Users/Zoe/Documents/SOAP_2/config_maker')

    def test_file_content(self):
        config = ConfigMaker(path=self.dir_path, numfits=1)
        config.make_files()
        path = os.path.join(config.path, 'genconfig0.cfg')

        with open(path) as f:
            contents = f.read()
        self.assertIn('[main]', contents)
        self.assertIn('instrument_reso = 115000', contents)
        self.assertIn('nrho = 20', contents)
        self.assertIn('grid = 300', contents)
        self.assertIn('[star]', contents)

    def test_file_active_region(self):
        config = ConfigMaker(path=self.dir_path, numfits=1)
        self.assertTrue(isinstance(config.active_region, int))

    def test_active_regions_content(self):
        config = ConfigMaker(path=self.dir_path, numfits=1, active_region=4)
        self.assertEquals(config.active_regions.values(), [1, 1, 1, 1])
        config = ConfigMaker(path=self.dir_path, numfits=1, active_region=3)
        self.assertEquals(config.active_regions.values(), [1, 1, 1, 0])
        config = ConfigMaker(path=self.dir_path, numfits=1, active_region=2)
        self.assertEquals(config.active_regions.values(), [1, 1, 0, 0])
        config = ConfigMaker(path=self.dir_path, numfits=1, active_region=1)
        self.assertEquals(config.active_regions.values(), [1, 0, 0, 0])
        config = ConfigMaker(path=self.dir_path, numfits=1, active_region=0)
        self.assertEquals(config.active_regions.values(), [0, 0, 0, 0])
    # print(config.active_regions)


if __name__ == '__main__':
    unittest.main()
