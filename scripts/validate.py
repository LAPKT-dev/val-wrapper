#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2022 Anubhav Singh
"""

import sys
from val_wrapper import val_main

if __name__ == '__main__':
    sys.exit(val_main("Validate", sys.argv[1:]))
