import sys
from app import utils

def main():
    computer = sys.argv[1:][0]
    for file in utils.get_dotfiles_by_computer(computer):
        print(file)

if __name__ == '__main__':
    main()