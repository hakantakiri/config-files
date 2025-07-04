#!/usr/bin/env python3
import sys
from app import utils

def main():
    print("Collecting dotfiles...")
    computer = sys.argv[1:][0]
    print(f"Collecting dotfiles for computer: {computer}")
    dotfiles = utils.get_dotfiles_by_computer(computer)
    for file in dotfiles:
        utils.copy_file(computer, file)

if __name__ == '__main__':
    main()