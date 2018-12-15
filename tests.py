#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 02:06:20 2018

@author: monicaalvarenga
"""

#%%
#Create all the tests you find meaningful

from quality import Product
from quality import recalculate_quality

def test_potato():
    products = [Product("potato",-5),Product("potato",0),Product("potato",7),Product("potato",12),Product("potato",15)]
    for case in products:
        before = case.quality
        recalculate_quality(case)
        after = case.quality
        assert after  == before - 0.5 
        
def test_cheese():
    products = [Product("cheese",-5),Product("cheese",0),Product("cheese",7),Product("cheese",12),Product("cheese",15)]
    for case in products:
        before = case.quality
        recalculate_quality(case)
        after = case.quality
        assert  after == before - 2
#%%