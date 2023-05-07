import random

def knn_distance(arr, q, k):
    """
    Given an array of numbers, computes the distance between 
    a target q and the kth closest point to q in array
    and returns it along with the kth closest point

    q does not need to be in arr
    k should start at 1, such that knn_distance(arr, q, 1) 
    returns the distance between q and the point in arr closest to q 

    Implementation has an expected time of 
    Θ(n), where n is the size of the input list
    
    >>> knn_distance([3, 10, 52, 15], 19, 1)
    (4, 15)
    >>> knn_distance([3, 10, 52, 15,], 19, 2)
    (9, 10)
    >>> knn_distance([3, 10, 52, 15], 19, 3)
    (16, 3)

    Parameters
    ----------
    arr : list
        input array
    q : int
        given target
    k : int
        specifies the rank of the kth closest point
    
    Returns
    -------
    tuple : containing the Euclidean distance between 
        a target q and the kth closest point to q in array, 
        and the kth closest point itself
    """

    def partition(arr, left, right, pivot_index):
        pivot_distance = abs(arr[pivot_index] - q)
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if abs(arr[i] - q) < pivot_distance:
              arr[store_index], arr[i] = arr[i], arr[store_index]
              store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    
    def quickselect(arr, left, right, k):
        if left == right:
            return arr[left]
        
        pivot_index = random.randint(left, right)
        pivot_index = partition(arr, left, right, pivot_index)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, left, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, right, k)

    kth_closest = quickselect(arr, 0, len(arr) - 1, k - 1)
    distance = abs(kth_closest - q)
    return (distance, kth_closest)
  
print(knn_distance([3, 10, 52, 15], 19, 1))
print(knn_distance([3, 10, 52, 15,], 19, 2))
print(knn_distance([3, 10, 52, 15], 19, 3))
