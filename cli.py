from sys import argv
import pull.main as pull

def main():
    if argv[1] == "pull":
        pull.check(argv[2:])
    else: 
        print(f"'{argv[1]}' isn't a valid parameter")

if __name__ == '__main__':
    main()
