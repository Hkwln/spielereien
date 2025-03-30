import numpy as np

def main():
    length = int(input("Enter desired password length: "))
    numbers = input("Do you want to include numbers? (y/n): ").strip().lower() == 'y'
    special = input("Do you want to include special characters? (y/n): ").strip().lower() == 'y'
    print("Generated Password:", ''.join(createpassword(length, numbers, special)))

def createpassword(length, numbers, special):
    # My idea is to generate random numbers and convert them from ASCII into symbols
    # special: 33-47, 58-64, 91-96, 123-126
    # numbers: 48-57
    # normal: 65-90, 97-122
    #every character: 33-126
    # using ord() or chr() to convert ASCII
    password = []
    for _ in range(length):
        match (numbers, special):
            case (False, False):
                # Only normal characters
                character = chr(np.random.randint(65, 91)) if np.random.randint(0, 2) == 0 else chr(np.random.randint(97, 123))
            case (True, False):
                # Include numbers
                if np.random.randint(0, 3) == 0:
                    character = chr(np.random.randint(48, 58))
                else:
                    character = chr(np.random.randint(65, 91)) if np.random.randint(0, 2) == 0 else chr(np.random.randint(97, 123))
            case (False, True):
                # Include special characters
                if np.random.randint(0,3) == 0:
                    character = chr(np.random.choice([*range(33, 48), *range(58, 65), *range(91, 97), *range(123, 127)]))
                else:
                    character = chr(np.random.randint(65, 91)) if np.random.randint(0, 2) == 0 else chr(np.random.randint(97, 123))

            case (True, True):
                # Include numbers and special characters
                character = chr(np.random.randint(33, 127))
        password.append(character)
    return password

if __name__ == "__main__":
    main()