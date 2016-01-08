#!/usr/bin/env python
#-*- config: utf-8 -*-
# Config file for cyk.py
# list here all rules of your language:
# Example rules: 
# S -> AB | CA
# A -> BB | b
# B -> CA | c
# C -> AC | a
#
# List the rules in the following format:
#rules = {'S': ['AB','CA'],'A': ['BB','b'], 'B': ['CA','a'], 'C': ['AC','a']}
rules = {'S': [('NP','VP')],'NP': [('DET','N'), ('NP','PP')], 'PP': [('P','NP')], 'VP': [('V', 'NP'), ('VP', 'PP')], 'DET': [('the')], 'N': [('man'), ('woman'), ('telescope'), ('hill')], 'P': [('with')], 'V' : [('saw')], 'P': [('on')]}

