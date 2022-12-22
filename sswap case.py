def swap_case(s):
    newstring =""
    for i in range(len(s)):
        
        if s[i].islower():
            newstring+=s[i].upper()
        else:
            newstring+=s[i].lower()
    return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
