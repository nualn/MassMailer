from parser import parser

def main():
    dummy_string = "Lorem [i] dolor sit amet, consectetuer [a] elit."
    dummy_dict = {
        "i": "ipsum", 
        "a": "consectetuer adipiscing elit."
    }
    print(parser.parse(dummy_string, dummy_dict))

if __name__ == "__main__":
    main()