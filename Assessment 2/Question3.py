def valid_palindrome(word):
    l=0
    r=len(word)-1
    while l<r:
        if word[l]!=word[r]:
            return False
        l+=1
        r-=1
    return True