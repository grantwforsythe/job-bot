#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO: add command line arguments to manipulate the data
# TODO: update the project description
# TODO: clean up the code
# TODO: add a docstring for the project
# TODO: update Docker file
# TODO: create a Jobs object
import sys
from urllib import response
from utils.utils import sqlite_connect
# from scripts.database import apply, view
from scripts.indeed import extract, transform

if __name__ == '__main__':

    while True:
        print('Options: ')
        print('1. Do you want to search Indeed?')
        print('2. Do you apply to any postings?')
        print('3. Do you want to view postings applied to?')
        print('4. Quit?')

        response = int(input('Response: '))
        
        if response == 1:
            title = input('Job title: ')
            location = input('Location: ')

            soup = extract(title, location)
            df = transform(soup)
            print(df.to_string())
        elif response == 2:
            pass
        elif response == 3:
            pass
        elif response == 4:
            print('Goodbye')
            sys.exit(0)
        else:
            print('Enter a vaild response')

