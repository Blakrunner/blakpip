import subprocess
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

def install_packages(args):
    if not args:
        print("Usage: blakpip install <package1> <package2> ... OR -r requirements.txt")
        sys.exit(1)

    def run_install(pkg):
        if pkg == "-r" and args[args.index(pkg) + 1].endswith(".txt"):
            req_file = args[args.index(pkg) + 1]
            print(f"Installing from {req_file} using {cpu_cores} threads...")
            with open(req_file, 'r') as f:
                pkgs = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            with ThreadPoolExecutor(max_workers=cpu_cores) as executor:
                executor.map(lambda p: subprocess.run([sys.executable, "-m", "pip", "install", p]), pkgs)
        else:
            with ThreadPoolExecutor(max_workers=cpu_cores) as executor:
                executor.map(lambda p: subprocess.run([sys.executable, "-m", "pip", "install", p]), args)

    cpu_cores = multiprocessing.cpu_count()
    run_install(args[0] if args[0] == "-r" else None)
