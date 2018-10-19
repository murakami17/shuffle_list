# -*- coding: utf-8 -*-

import logging
import random


"""
Classes to shuffle and put icons with given distributions.
"""

__author__ = "Taku MURAKAMI"
__copyright__ = "Copyright (c) 2018, Taku MURAKAMI"
__version__ = "0.1.0"
__maintainer__ = "Taku MURAKAMI"
__email__ = "murakami.taku.17@shizuoka.ac.jp"
__status__ = "dev"
__date__ = "Oct 22, 2018"

logger = logging.getLogger(__name__)


class Shuffle_list:
    """
    Class to shuffle and put icons with given distributions.
    """
    
    def __init__(self):
        pass
    
    def make_shuffled_list(self, **icons_dic):
        """
        Makes shuffled list.
        
        Auguments
        ---------
        icons_dic: dictionary of icons and numbers.
            In the dictionary, key is an icon and value is int value,
            which means the number of icon.
            example - {"Mg": 72, "Al": 36, "Y": 36}
        """
        pass
    
    def put_shuffled_list(self):
        """
        Puts shuffled list.
        """
        pass
    

if __file__ == "__main__"
    pass
