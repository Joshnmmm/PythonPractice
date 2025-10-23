def swap_case(s):
    finalString = ""
    for letters in s:
        if letters.isupper() is True:
            newCase = letters.lower()
            finalString += newCase
        else:
            newCase = letters.upper()
            finalString += newCase
    return(finalString)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)