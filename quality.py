#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 02:00:36 2018

@author: monicaalvarenga
"""

#%%
#We have a function that calculates the degrading quality of different
#products in a shop.


class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
        
        
def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
#%%