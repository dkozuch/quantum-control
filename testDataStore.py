'''testDataStore.py
'''

import unittest
import numpy as np
from dataStore import DataStore

class test_DataStore(unittest.TestCase):

    def test_noInput(self):
        """Instantiate DataStore object without input."""

        data = DataStore()
        #check if attr Const exists
        self.assertIn('Const',vars(data))

        #check if following names of constant exist
        para = ['m','B','mu','K','hbar','w1']
        for key in para:
            self.assertIn(key,data.Const._fields)

    def test_withInput(self):
        """Instantiate DataStore object with input using fake txy_desired."""

        #create a fake yet correct input txy_desired which is a 5x3 ndarray
        txy_desired = np.array([np.arange(5), np.arange(1,6), np.arange(11,16)]).T
        data = DataStore(txy_desired)
        self.assertEqual(data.n, txy_desired.shape[0])
        np.testing.assert_array_equal(data.t, txy_desired[:,0])
        np.testing.assert_array_equal(data.path_desired, txy_desired[:,1:2])
        self.assertEqual(data.path_obs.shape, txy_desired[:,1:2].shape)
        self.assertEqual(data.state.shape, (2*data.Const.m+1, data.n))
        self.assertEqual(len(data.noise_stat), 2)
        for key in data.noise_stat:
            self.assertEqual(data.noise_stat[key].shape, (data.n, 2))

