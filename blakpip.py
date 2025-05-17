#!/usr/bin/env python3

import sys
from blakpip_core import install_packages

if __name__ == "__main__":
    install_packages(sys.argv[1:])
