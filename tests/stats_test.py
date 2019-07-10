import logging
logging.getLogger().setLevel(logging.DEBUG)
logging.debug('hi from the logger!')

import unittest
import os
import sys
import yaml
#importing numpy causes debugging to stop working! Actually seems like any C based python packages causes the debugger to fail.
#import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, '..', 'silverpieces'))
import functions  
from utilities import *

class TestStatMethods(unittest.TestCase):

    def test_dummy(self):
        functions.test()        
        self.assertEqual(1, 1)

    def test_dummy_data_shape(self):        
        t,x,y,src_data=get_data_src_seq(nt=5,nx=3,ny=2)
        f=create_file(t,'t',x,'latitude',y,'longitude',src_data,'band')
        band=read_var(f.name,'band')        
        self.assertEqual(band.shape, (5, 3, 2))

    def test_monthly_mean(self):
        print("current Directory is:",os.getcwd())
        with open("./tests/testArg.yaml", 'r') as stream:
            try:
                args_file = yaml.safe_load(stream)
                t,x,y,src_data=get_data_src_seq(nt=365,nx=3,ny=2)
                f=create_file(t,'time',x,'latitude',y,'longitude',src_data,'band')

                #replace the product name with filename with dumm data
                args_file['Args']['product'] = f.name
                functions.monthly_mean(args_file)
            except yaml.YAMLError as exc:
                print(exc)

if __name__ == '__main__':
    unittest.main()
    