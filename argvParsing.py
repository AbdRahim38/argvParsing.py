#!/usr/bin/env python3
# Parsing Command line parameters
# format to run ./argvParsing.py [argv]

import sys #give you access to the things that are passed into this script.

print(f"First argument |{sys.argv[1]}|")

# call DBS bank system and pass in sys.argv[1]
print(f"Transfer $|{sys.argv[2]}| to my own bank")
