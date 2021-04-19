#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 08:33:30 2021

@author: xs0004173
"""
#Q1
#My solution 68ms 5.88%

def romanToInt(self, s: str) -> int:
        
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        def rule(i: str, j: str) -> tuple:
            if i == "V" and j == "I":
                return (4,True)
            elif i == "X" and j == "I":
                return (9,True)
            elif i == "L" and j == "X":
                return (40, True)
            elif i == "C" and j == "X":
                return (90, True)
            elif i == "D" and j == "C":
                return (400, True)
            elif i == "M" and j == "C":
                return (900, True)
        
        values = 0
        isContiune = False
        
        for i, element in enumerate(s[::-1]):
            if isContiune:
                isContiune = False
                continue
            else:
                if i+1 < len(s):
                    value = rule(element, s[-2-i])
                    if value == None:
                        values = values + dic[element]
                        isContiune = False
                    elif value[1]:
                        values = values + value[0]
                        isContiune = value[1]
                else:
                    values = values + dic[element]
        return values      
         
"""Best Solution 40ms 91.73% 待討論是否會有錯誤


def romanToInt(self, s: str) -> int:
    
        r = 0
        
        values = dict(
        I = 1,
        V = 5,
        X = 10,
        L = 50,
        C = 100,
        D = 500,
        M = 1000)
        
        roman = [values[i] for i in s]
        
        for i, elt in enumerate(roman):
            try:
                if roman[i + 1] > elt:
                    roman[i] = - roman[i]
            except IndexError:
                pass
        r = sum(roman)
        return(r)
"""  
#Q2
def longestCommonPrefix(self, strs: list[str]) -> str:
    
    if not strs: return ""
    
    result = ""
    minStrs = min(strs)
    maxStrs = max(strs)
    
    for i, element in enumerate(minStrs):
        if element == maxStrs[i]:
            result = result + element
        else:
            break
    return result