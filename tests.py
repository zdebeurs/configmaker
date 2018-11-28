import unittest
import os

from config_maker import ConfigMaker


class MyTest(unittest.TestCase):

    def setUp(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def tearDown(self):
        for i in range(0, 5):
            path = os.path.join(self.dir_path, 'genconfig' + str(i) + '.cfg')
            '''if os.path.exists(path):
                os.remove(path)'''

    def test_file_maker(self):
        config = ConfigMaker(path=self.dir_path, numfits=5)
        config.make_files()
        for i in range(0, config.numfits):
            path = os.path.join(config.path, 'genconfig' + str(i) + '.cfg')
            self.assertTrue(os.path.exists(path))

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


if __name__ == '__main__':
    unittest.main()
