#!/usr/bin/env python3
""" Command line tool to quiz the user on memorization of texts. """

import argparse
import cmd
import pathlib

class QuizShell(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
    intro = 'Welcome to the memorization quiz. Type help or ? to list commands.\n'
    prompt = '(quiz)'

    def do_list(self):
        """List the available texts to memorize."""
    
    def do_quit(self):
        """Exit the program."""
        self.close()
        

def main(location: pathlib.Path):
    """_summary_
    """
    print(f"Looking in {location}...")
    QuizShell().cmdloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Memorization Quiz',
                                     description='Quiz user on textual memorization')
    parser.add_argument('location', nargs='?', default='./samples', type=pathlib.Path, help='location of memorization texts')
    args = parser.parse_args()
    main(args.location)
