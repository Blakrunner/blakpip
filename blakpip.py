#!/usr/bin/env python3

import sys
from blakpip_core import install_packages

def main():
    install_packages(sys.argv[1:])

if __name__ == "__main__":
    main()
