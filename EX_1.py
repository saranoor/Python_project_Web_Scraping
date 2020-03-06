# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:42:56 2019

@author: skm
"""
#if __name__ == "__main__":
# Imports if necessary 
#import sys
import argparse
parser=argparse.ArgumentParser(description='Take the file') 
parser.add_argument('filename', help='what the argument holds', type=str)
args=parser.parse_args()
print(args.filename)
  