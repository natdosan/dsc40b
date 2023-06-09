def learn_theta(data, colors):
    """
    Finds the threshold that separates blue and red points. 
    Returns the maximum blue point value.

    Parameters
    ----------
    data : list
        list of input nums
    colors : list
        of strings that gives the color of each point i in data

    Returns
    -------
    max_blue : int 
        single number θ such that all of the blue points are ≤ θ and 
        all of the red points are > θ

    # Blue points are less than red points, blue points appearing before red ones.
    >>> learn_theta([1, 2, 3, 4, 5], ['blue', 'blue', 'red', 'red', 'red'])
    2

    # Blue points are less than red points, blue points appearing after red ones.
    >>> learn_theta([5, 4, 3, 2, 1], ['red', 'red', 'red', 'blue', 'blue'])
    2

    # All blue points are equal and less than the red points.
    >>> learn_theta([1, 1, 1, 2, 2], ['blue', 'blue', 'blue', 'red', 'red'])
    1

    # One red point equals to the maximum blue point.
    >>> learn_theta([1, 1, 1, 1, 1], ['blue', 'blue', 'blue', 'blue', 'red'])
    1

    # Blue and red points are distributed in an increasing pattern.
    >>> learn_theta([5, 10, 15, 20, 25], ['blue', 'blue', 'blue', 'red', 'red'])
    15
    """
    # Initialize the maximum value for blue points to negative infinity
    max_blue = float('-inf')

    # Iterate over all data points
    for i in range(len(data)):
        # If the point is blue and larger than the current maximum, update the maximum
        if colors[i] == 'blue' and data[i] > max_blue:
            max_blue = data[i]

    # Return the maximum value of blue points
    return max_blue

def compute_ell(data, colors, theta):
    """
    Computes the loss function L(θ) for the given data and colors at a 
    specific threshold theta.

    Parameters
    ----------
    data : list
        list of input nums
    colors : list
        of strings that gives the color of each point i in data
    theta : float
        threshold for loss

    Returns
    -------
    loss : int 
        loss of the function

    >>> compute_ell([1.5, 2.5, 3.5, 4.5], ['blue', 'blue', 'red', 'red'], 3)
    0

    # Edge case: All points are exactly at the threshold
    >>> compute_ell([2.0, 2.0, 2.0, 2.0], ['blue', 'blue', 'red', 'red'], 2.0)
    2

    # Edge case: The threshold is lower than all points
    >>> compute_ell([1.5, 2.5, 3.5, 4.5], ['blue', 'blue', 'red', 'red'], 1.0)
    2

    # Edge case: The threshold is higher than all points
    >>> compute_ell([1.5, 2.5, 3.5, 4.5], ['blue', 'blue', 'red', 'red'], 5.0)
    2

    # Normal case: Threshold correctly separates colors
    >>> compute_ell([1.5, 2.5, 3.5, 4.5], ['blue', 'blue', 'red', 'red'], 2.5)
    0
    
    # Larger odd-sized inputs
    >>> compute_ell([1, 2, 3, 4, 5, 6, 7], ['blue', 'blue', 'blue', 'red', 'red', 'red', 'red'], 4)
    1

    >>> compute_ell([1, 2, 3, 4, 5, 6, 7], ['blue', 'blue', 'blue', 'red', 'red', 'red', 'red'], 3)
    0

    # Larger even-sized inputs
    >>> compute_ell([1, 2, 3, 4, 5, 6, 7, 8], ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red'], 4)
    0

    >>> compute_ell([1, 2, 3, 4, 5, 6, 7, 8], ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red'], 3)
    1
    """

    num_red_less_than_theta = sum(1 for i in range(len(data)) if data[i] <= theta and colors[i] == 'red')
    num_blue_greater_than_theta = sum(1 for i in range(len(data)) if data[i] > theta and colors[i] == 'blue')
    return num_red_less_than_theta + num_blue_greater_than_theta


def minimize_ell(data, colors):
    """
    Returns a floating-point number which minimizes the loss L for the particular dataset.

    Parameters
    ----------
    data : list
        of unique real numbers
    colors : list
        with each color corresponding to the respective data point

    Returns
    -------
    min_theta : float
        A real number which is the threshold that minimizes the loss.

    >>> minimize_ell([1, 2, 3, 4, 5, 6, 7], ['blue', 'blue', 'blue', 'red', 'red', 'red', 'red'])
    3.5
    """
    min_loss = float('inf')
    min_theta = None
    for i in range(len(data) - 1):
        theta = (data[i] + data[i+1]) / 2
        loss = compute_ell(data, colors, theta)
        if loss < min_loss:
            min_loss = loss
            min_theta = theta
    return min_theta


def minimize_ell_sorted(data, colors):
    """
    Returns a floating-point number which minimizes the loss L for the sorted data and color

    Parameters
    ----------
    data : list
        of unique real numbers sorted in ascending order
    colors : list
        colors, with each color corresponding to the respective data point

    Returns
    -------
    min_theta : float
        A real number which is the threshold that minimizes the loss.

    >>> minimize_ell_sorted([1, 2, 3, 4, 5, 6, 7], ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red'])
    4

    >>> data = [1, 2, 3, 4, 5, 6]
    >>> colors = ['blue', 'blue', 'blue', 'red', 'red', 'red']
    >>> minimize_ell_sorted(data, colors)
    3

    >>> data = []
    >>> colors = []
    >>> minimize_ell_sorted(data, colors)
    0
    
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> colors = ['blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red']
    >>> minimize_ell_sorted(data, colors)
    5
    """
    if not data or not colors:
        return 0

    min_loss = float('inf')
    min_theta = None

    # number of 'blue' points greater than current data point
    blue_gt_theta = len(data) / 2

    # number of 'red' points less than or equal to current data point
    red_le_theta = 0

    for i, color in enumerate(colors):
        if i > 0:
            # If the current data point is red, increase red_le_theta
            if color == 'red':
                red_le_theta += 1
            # If the current data point is blue, decrease blue_gt_theta
            else:
                blue_gt_theta -= 1

        loss = red_le_theta + blue_gt_theta

        if loss < min_loss:
            min_loss = loss
            min_theta = data[i]

    return min_theta