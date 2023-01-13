codeword = "engineering"

for x in codeword:
    your_codeword1 = input("Enter a codeword: ")
    if your_codeword1 != codeword:
        print("Wrong codeword, 2 attempts left")
    else: print("Success"); break

    your_codeword2 = input("Enter a codeword: ")
    if your_codeword2 != codeword:
        print("Wrong codeword, 1 attempt left")
    else: print("Success"); break

    your_codeword3 = input("Enter a codeword: ")
    if your_codeword3 != codeword:
        print("Access denied")
        exit()
    else:
        print("Success"); break