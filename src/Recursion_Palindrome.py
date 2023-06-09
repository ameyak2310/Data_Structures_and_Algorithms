"""
Is Palindrome ?
"""

def is_Palindrome(s):
    """Checks if Palindrome
    Args:
        s (str): String
    Returns:
        result(bool) : if Palindrome True else False
    """   
    if len(s) <= 1:
        result = True
    else:
        result = s[0] == s[-1] and is_Palindrome(s[1:-1])
        
    return result
        
print('\n___OUTPUT___')
print(is_Palindrome('abcdeyedcba'),'\n')
