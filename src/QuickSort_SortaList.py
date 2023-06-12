"""
Quick Sort Algo rithm for sorting a list
"""
# %% Quick Sort function
def quicksort(payload):
    """Fucntion to sort a list
    Based on  Quick Sort Algorithm
    Hint:Comparing based on 'pivot' value is faster.

    Args:
        payload (list): List to be sorted

    Returns:
        sorted_payload(list): Sorted List
    """
    assert isinstance(payload, list), "Error: Entered payload is not a list"
    if len(payload) <= 1:
        sorted_payload = payload
    else:
        pivot = payload[0]
        small = [item for item in payload[1:] if item < pivot]
        big = [item for item in payload[1:] if item >= pivot]
        sorted_payload = quicksort(small) + [pivot] + quicksort(big)

    return sorted_payload


# %% Function Call
PAYLOAD = [1, 1, 66, 3, 2, 400, 5, -999, 1000]
func = quicksort

print("\n******************************")
print(f"Sorted List = {quicksort(PAYLOAD)}")
print("******************************\n")
