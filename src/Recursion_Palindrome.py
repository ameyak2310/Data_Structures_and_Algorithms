"""
Palindrom Check
"""
# %% Function


def is_palindrome(payload):
    """ Check is entered string is a Palindrome
    Args:
        payload (String): String to check for Palindrome
    Returns:
        result(Boolean) : True or False
    """
    assert isinstance(payload, str), "Warning: Entered payload not a string"
    payload = str(payload).lower().strip()
    if len(payload) <= 1:
        result = True
    else:
        result = payload[0] == payload[-1] and is_palindrome(payload[1:-1])
    return result


# %% Call
PAYLOAD_STRING = "AooAo"
print("\n******************************")
print(f"String -> {PAYLOAD_STRING} : Palindrome = {is_palindrome(PAYLOAD_STRING)}")
print("******************************\n")

# %%
