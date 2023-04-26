def swap_sum(A, B):
    """
    Given two sorted integer arrays A and B, returns a pair of indices (A_i, B_i) 
    – one from A and one from B – such that after swapping these indices, 
    sum(B) == sum(A) + 10. 

    If more than one pair is found, return any one of them. 
    If such a pair does not exist, return None.
    
    suppose A = [1, 6, 50] and B = [4, 24, 35]

    Swapping 6 and 4 results in arrays (1, 4, 50)
    and (6, 24, 35); the elements of each list sum to 55 and 65. 
    Thus, you must return (1, 0) as you are expected
    to return the indices.

    swap_sum should run in time Θ(n), where n is the size of the 
    larger of the two lists. A and B should not be modified
    """

    # Calculate the sums of A and B
    sum_A = sum(A)
    sum_B = sum(B)

    # define difference
    diff = sum_B - sum_A - 10
    
    # base case
    if diff % 2 == 1:
        return None

    set_B = set(B)

    for i, a in enumerate(A):
        # Calculate the value that needs to be in B for the sum to be correct
        b = a + diff / 2
        # If that value is in B, return the indices
        if b in set_B:
            j = B.index(b)
            return (i, j)

    # edge case
    return None
