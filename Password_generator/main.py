import numpy as np

def main():
    length = int(input("Enter desired password length"))
    numbers = input("do you want to include numbers? (y/n):").strip().lower() == 'y'
    special = input("do you want to include special characters? (y/n)").strip.lower() == 'y'
    print(createpassword(length, numbers, special))

def createpassword(length, numbers, special):
    #My idea is to generate random numbers and convert them from ascii into the symbol
    #special: 33-47, 58-64, 91-60, 123-126, 128-159, 161-172
    #numbers 48-57
    #normal:65-90, 97-122
    # using ord() or chr() to convert ascii 
    password = []
    count = np.random(1,100)
    for i in length:
        match (numbers, special):
            case (False, False):
                # Only normal characters
                character = chr(np.random.randint(65, 91)) if count % 2 == 0 else chr(np.random.randint(97, 123))
            case (True, False):
                # Include numbers
                character = chr(np.random.randint(48, 58)) if count % 3 == 0 else chr(np.random.randint(65, 91)) if count % 2 == 0 else chr(np.random.randint(97, 123))
            case (False, True):
                # Include special characters
                character = chr(np.random.choice([*range(33, 48), *range(58, 65), *range(91, 97), *range(123, 127)]))
            case (True, True):
                # Include numbers and special characters
                character = chr(np.random.choice([*range(33, 48), *range(58, 65), *range(91, 97), *range(123, 127), *range(48, 58), *range(65, 91), *range(97, 123)]))
        password.append(character)
        return password
if __name__ == "__main__":
    main()