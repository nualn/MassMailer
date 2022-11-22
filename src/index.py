from parser import parser

def main():
    user_string = input("Give a string with [1] somewhere:\n")
    user_dict = {
        "1": input("Type something to replace the previous [1]:\n")
    }
    print(parser.parse(user_string, user_dict))

if __name__ == "__main__":
    main()