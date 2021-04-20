"""Get all attributes for a particular object."""

__copyright__ = """
Copyright (C) 2021 Manetu Inc.
Author: Alex Tsariounov <alext@manetu.com>

This is free software; please see the LICENSE file
for details and any restrictions.
"""

def doit(args):
    if args.verbose > 0:
        print(f'executing "getall" command, verbosity {args.verbose}')
