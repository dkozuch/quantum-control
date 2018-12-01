'''dataStore class
'''

import numpy as np

class DataStore(object):
    """Class DataStore:
    Attributes:

        _n: number of time points.

        time: A column vector of time points. n-by-1 numpy ndarray

        path_desired: n-by-2

        path_actual: n-by-2

        field: n-by-2

        state: (2m+1)-by-n

        noise_stat: a list of two n-by-2 numpy ndarrays corresponding 
        to x and y. Each contains mean and standard deviation at each
        time point.

    """
    def __init__(self, txy_desired=None):
        """Parameters:

        """

        if txy_desired is not None:
            self._txy_desired = txy_desired
            self.n = txy_desired.shape[0] #number of time points
            self.t = np.zeros(self._n)
            self.path_desired = txy_desired[:,1:2]
            self.path_obs = np.zeros_like(self._path_desired)
            self.field = np.zeros([self._n, 2])
            self.state = np.zeros([2*self.Const.m+1, n])
            # self.noise_stat = [np.zeros]
       




