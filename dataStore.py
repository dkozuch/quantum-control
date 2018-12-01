'''dataStore class
'''

import numpy as np
from collections import namedtuple

class DataStore(object):
    """A DataStore contains all data associated with a single path.

    Class DataStore provides a container to store data associated with a 
    single path specified by user. A DataStore object can be instantiated
    either with or without input argument. In the latter case, the object
    contains only predefined constants. Otherwise, a desired path processed
    by GUI_Interface can be used as input to instantiate a DataStore, and
    classes FieldSolver, NoiseAnalyzer, and Visualization can then access/
    save data within the DataStore for the desired path.
  
    Attributes:

        Const: A named tuple contains predefined constants in our quantum 
        system. Each constant can be accessed by its name as an attribute 
        of object Const. These include:
            -- m:       maximum energy quantum number
            -- B:       rotational constant in atomic units
            -- mu:      dipole moment in atomic units
            -- hbar:    reduced planck's constant
            -- K:       4pi * epsilon0
            -- w1:      first energy level spacing

        n: Number of time points.

        t: Time at each time points. A numpy ndarray of shape (n,).

        path_desired: User-specified desired path of dipole projection 
        described by x and y (in this order). A numpy ndarray of shape 
        (n,2).

        field: Control fields e_x and e_y at each time point calculated by 
        FieldSolver. A numpy ndarray of shape of (n,2).

        path_actual: Path of dipole projection described by x and y that is
        resulted from the control field. A numpy ndarray of shape (n,2).

        state: State described by (2m+1) basis at each time point. A numpy 
        ndarray of shape ((2m+1),n).

        noise_stat: A dictionary composed of the following two objects:
            -- "mean": mean x and y at each time point. A numpy ndarray of
            shape (n,2).
            -- "sd": standard deviation of x and y at each time point. A
            numpy ndarray of shape (n,2).

    """

    def __init__(self, txy_desired=None):
        """Initialize a DataStore instance.
        
        DataStore.Const is always initialized by class method init_const()
        with the predefined constants. Other class attributes are ini-
        tialized only when parameter txy_desired is not None.

        Parameters:

            txy_desired: Optional. A numpy ndarray of shape (n,3) where 
            each row contains (in this order) time, x projection and y 
            projection of path defined by user. 

        """
        
        self.Const = None
        self.init_Const()
       
        if txy_desired is not None:
            #attr calculated from input txy_desired
            self.n = txy_desired.shape[0] #number of time points
            self.t = txy_desired[:,0]
            self.path_desired = txy_desired[:,1:2]
            #attr initialized with all entries being zeros but of correct
            #shapes
            self.path_obs = np.zeros_like(self.path_desired)
            self.field = np.zeros((self.n, 2))
            self.state = np.zeros((2*self.Const.m+1, self.n))
            self.noise_stat = dict({
                "mean": np.zeros((self.n, 2)),
                "sd": np.zeros((self.n, 2))
                })


    def init_Const(self):
        """Called by __init__ to initialize attr Const."""

        Const = namedtuple('const',['m','B','mu','hbar','K','w1'])
        m = 8                       # maximum energy quantum number
        B = 4.4033e-24 / 4.36e-18   # Joules; rotational constant;
                                    # converted to atomic units
        mu = 2.3649e-30 / 8.48e-30  # Coulomb meters; dipole moment;
                                    # converted to atomic units
        hbar = 1.0                  # reduced planck's constant
        K = 1.0                     # 4pi*epsilon0
                                    # not seen else where in the .m file
        w1 = B/hbar                 # first energy level spacing
        self.Const = Const(m, B, mu, hbar, K, w1)



