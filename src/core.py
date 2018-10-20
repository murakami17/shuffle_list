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
    
    seeds = 0
    random.seed(seeds)
    
    def __init__(self):
        """
        Parameters
        ----------
        self.shuffled_list: list of icons
            Shuffled list generated by make_shuffled_list method.
            The length of the list equals to the number of icons.
        """
        pass
    
    @classmethod
    def change_random_seed(cls):
        """
        Changes random seeds of the class.
        """
        cls.seeds += 1
        random.seed(seeds)
    
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
