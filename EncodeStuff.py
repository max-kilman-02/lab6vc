#Max Kilman
def encode(x):
    password = ""
    for char in x:
        dig = int(char)+10
        dig = (dig+3)%10
        password += str(dig)
    return password
def decode(x):
    # add decode here
def main():
    raw = ""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        select = int(input("Please enter an option: "))
        if select == 1:
            raw = input("Please enter your password to encode: ")
            raw = encode(raw)
            print("Your password has been encoded and stored!")
        elif select == 2:
            print(f"The encoded password is {raw}, and the original password is {decode(raw)}")
        elif select == 3:
            break
if __name__ == "__main__":
    main()