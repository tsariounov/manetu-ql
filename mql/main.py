"""Main module for example code to access the Manetu.io GraphQL interface."""

__copyright__ = """
Copyright (C) 2021 Manetu Inc.
Author: Alex Tsariounov <alext@manetu.com>

This is free software; please see the LICENSE file
for details and any restrictions.
"""

from mql.version import version
import argparse, importlib, sys

# parser declarations for common and all subcommands
parser = argparse.ArgumentParser(description=f'Manetu.io GraphQL interface, version {version}')

#  global options
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='increase verbose output')
parser.add_argument('-p', '--pat', action='store',
                    help='specify personal access token to use')
parser.add_argument('-j', '--jwt', action='store',
                    help='specify jwt to use')

#  the commands
subparsers = parser.add_subparsers(help='commands', dest='command')

#  schema command
schema_parser = subparsers.add_parser('schema', help='get schema from server')

#  getall command which gets all fields in an object
getall_parser = subparsers.add_parser('getall', help='get all fields for an object')
getall_parser.add_argument('object', action='store',
                           help='the object of interest')

# cmdline entry point and dispatcher
def main():
    args = parser.parse_args()

    if args.verbose:
        print(f'Manetu.io GraphQL interface, version {version}')
        if args.verbose > 1:
            print(f'dispatching command: "{args.command}", with verbosity of {args.verbose}')

    try:
        # first import the command
        cmd = importlib.import_module(f'mql.commands.{args.command}')

        # check for the pat
        if args.pat == None and args.jwt == None:
            print('no PAT or JWT specified, cannot login to manetu.io')
            # TODO: here is where we'll impl oauth logins
            sys.exit(1)

        # and now execute it
        cmd.dispatch(args)

    except SystemExit:
        raise

    except:
        print(f'Unexpected error for command: {args.command}, error: {sys.exc_info()[1]}')
        sys.exit(2)
