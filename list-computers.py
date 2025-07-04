from app import utils

def main():
    for computer in utils.get_computers():
        print(computer)

if __name__ == "__main__":
    main()