import numpy as np
import configparser
import math as m
import os

from collections import OrderedDict


class ConfigMaker:

    def __init__(self, path=None, numfits=None, active_region=None):
        self.path = path or os.path.dirname(os.path.realpath(__file__))
        self.config = configparser.ConfigParser()
        self.numfits = numfits or 0
        self.active_region = (
            np.random.randint(0, 5, size=1)[0]
            if active_region is None else active_region)
        self.config['main'] = self.config_main
        self.config['star'] = self.config_star
        self.config['active_regions'] = self.config_active_regions
        self.config['output']= self.config_output

    @property
    def active_regions(self):
        active_regions = OrderedDict()
        active_regions.update(check1=0)
        active_regions.update(check2=0)
        active_regions.update(check3=0)
        active_regions.update(check4=0)
        for i in range(0, self.active_region):
            active_regions['check{}'.format(i + 1)] = 1
        return active_regions

    def as_dict(self):
        return {}

    def make_files(self):
        for i in range(0, self.numfits):
            with open('genconfig' + str(i) + '.cfg', 'w') as configfile:
                self.config.write(configfile)

    @property
    def config_main(self):
        return {'grid': '300', 'nrho': '20', 'instrument_reso': '115000'}

    @property
    def config_star(self):
        ir = (np.random.uniform(0, 100, size=1)) / 100
        inclination_angle = m.acos(ir)
        psi = (np.random.uniform(0, 100, size=1)) / 100
        tdiff_spot = np.random.uniform(200, 2000, size=1)
        return {
            'radius_sun': '696000',
            'radius': '1.0',
            'prot': '25.05',
            'I': inclination_angle,
            'psi': psi.item(0),
            'Tstar': '5778',
            'Tdiff_spot': tdiff_spot.item(0),
            'limb1': '0.29',
            'limb2': '0.34'}

    @property
    def config_active_regions(self):
        act_reg_type = np.random.randint(0, 2, size=4)
        long_active_region = np.random.randint(0, 360, size=4)
        lat_active_region = np.random.randint(-90, 90, size=4)
        size_active_region = np.random.uniform(0.001, 0.20, size=4)
        return dict(
            act_reg_type1=act_reg_type[0],
            act_reg_type2=act_reg_type[1],
            act_reg_type3=act_reg_type[2],
            act_reg_type4=act_reg_type[3],

            long1=long_active_region[0],
            long2=long_active_region[1],
            long3=long_active_region[2],
            long4=long_active_region[3],

            lat1=lat_active_region[0],
            lat2=lat_active_region[1],
            lat3=lat_active_region[2],
            lat4=lat_active_region[3],

            size1=m.log(10**size_active_region[0], 10),
            size2=m.log(10**size_active_region[1], 10),
            size3=m.log(10**size_active_region[2], 10),
            size4=m.log(10**size_active_region[3], 10),
            **self.active_regions)

    @property
    def config_output(self):
        return {
            'ph_step': '1',
            'ph_in': 'None'}
