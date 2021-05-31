#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO: add command line arguments to manipulate the data
# TODO: update the project description
# TODO: clean up the code
# TODO: add a docstring for the project
# TODO: update Docker file
# TODO: create a Jobs object
from utils.utils import sqlite_connect
# from scripts.database import apply, view
from scripts.indeed import extract, transform

if __name__ == '__main__':
    soup = extract('Data Analyst', 'Toronto')

    df = transform(soup)

    print(df.to_string())
