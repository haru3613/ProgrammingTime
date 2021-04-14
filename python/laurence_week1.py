#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:12:50 2021

@author: xs0004173
"""

def valid_parentheses(string):
    count = 0
    for i in string:
        if "(" in i:
            count += 1
        elif ")" in i:
            count -= 1
            if count < 0:
                return False
    return count == 0

        
   