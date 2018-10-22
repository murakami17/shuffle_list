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
    
    def __init__(self):
        """
        Parameters
        ----------
        self.seeds: int
            Random seeds fixed for each instance of this class.
        self.shuffled_list: list of icons
            Shuffled list generated by make_shuffled_list method.
            The length of the list equals to the number of icons.
        """
        self.seeds = Shuffle_list.seeds
        Shuffle_list.change_random_seeds()
        self.shuffled_list = []
    
    @classmethod
    def change_random_seeds(cls):
        """
        Changes random seeds of the class.
        """
        cls.seeds += 1
    
    def make_shuffled_list(self, **icons_dic):
        """
        Makes shuffled list.
        
        Auguments
        ---------
        icons_dic: dictionary of icons and numbers.
            In the dictionary, key is an icon and value is int value,
            which means the number of icon.
            example - {"Mg": 72, "Al": 36, "Y": 36}
        
        Return
        ------
        self: Shuffle_list object
        """
        for key, value in icons_dic.items():
            for index in range(value):
                self.shuffled_list.append(key)
        
        random.shuffle(self.shuffled_list)
        
        return self
    
    def put_shuffled_list(self):
        """
        Puts shuffled list.
        """
        return str("\n".join(self.shuffled_list))
    

if __name__ == "__main__":
    shuffle_list_list = [
        Shuffle_list().make_shuffled_list(Mg=72, Al=36, Y=36),
        Shuffle_list().make_shuffled_list(Mg=72, Al=36, Y=36),
        Shuffle_list().make_shuffled_list(Mg=108,Al=18, Y=18),
        Shuffle_list().make_shuffled_list(Mg=108,Al=18, Y=18)
    ]
    
    for index, shuffle_list in enumerate(shuffle_list_list):
        print(str(index) + ":" + shuffle_list.put_shuffled_list() + "\n")
    
