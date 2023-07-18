def Longest_Palindromic_Substring(string):
    while True:
        if string==string[::-1]:
            return string
        else:
            string=string[1:]
if __name__ == '__main__':
    x=input()
    print(Longest_Palindromic_Substring(x))
"""
Longest Palindromic substring
"""
