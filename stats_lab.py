import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------
# Question 1 – Generate & Plot Histograms (and return data)
# -----------------------------------

def normal_histogram(n):
    """
    Generate n samples from Normal(0,1),
    plot a histogram with 10 bins (with labels + title),
    and return the generated data.
    """
    data = np.random.normal(0,1,n)

    plt.hist(data, bins=10)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Normal(0,1) Distribution")

    return data


def uniform_histogram(n):
    """
    Generate n samples from Uniform(0,10),
    plot a histogram with 10 bins (with labels + title),
    and return the generated data.
    """
    data = np.random.uniform(0,10,n)
    
    plt.hist(data, bins=10)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Uniform(0,10) Distribution")
    plt.show()

    return data


def bernoulli_histogram(n):
    """
    Generate n samples from Bernoulli(0.5),
    plot histogram with 10 bins,
    and return the data.
    """
    
    random_values = np.random.uniform(0, 1, n)

    data = []
    
    for value in random_values:
        if value < 0.5:
            data.append(0)   # correct
        else:
            data.append(1)   # correct

    data = np.array(data)

    plt.hist(data, bins=10)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Bernoulli(0.5) Distribution")
    plt.show()

    return data


# -----------------------------------
# Question 2 – Sample Mean & Variance
# -----------------------------------

def sample_mean(data):
    """
    Compute sample mean.
    """
    total = 0
    count = 0

    for value in data:
        total += value
        count += 1

    return total / count


def sample_variance(data):
    """
    Compute sample variance using n-1 denominator.
    """
    mean = sample_mean(data)

    total = 0
    count = 0

    for value in data:
        total += (value - mean) ** 2
        count += 1

    return total / (count - 1)


# -----------------------------------
# Question 3 – Order Statistics
# -----------------------------------

def order_statistics(data):
    """
    Return:
    - min
    - max
    - median
    - 25th percentile (Q1)
    - 75th percentile (Q3)

    Use a consistent quartile definition. The tests for the fixed
    dataset [5,1,3,2,4] expect Q1=2 and Q3=4.
    """
    arr = list(data)
    n = len(arr)

    # Manual Bubble Sort (no built-in sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    minimum = arr[0]
    maximum = arr[-1]

    # Median
    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2

    # Quartiles (index-based method required by autograder)
    q1_index = n // 4
    q3_index = (3 * n) // 4

    q1 = arr[q1_index]
    q3 = arr[q3_index]

    return minimum, maximum, median, q1, q3


# -----------------------------------
# Question 4 – Sample Covariance
# -----------------------------------

def sample_covariance(x, y):
    """
    Compute sample covariance using n-1 denominator.
    """
    if len(x) != len(y):
        raise ValueError("x and y must have same length")

    mean_x = sample_mean(x)
    mean_y = sample_mean(y)

    total = 0
    n = len(x)

    for i in range(n):
        total += (x[i] - mean_x) * (y[i] - mean_y)

    return total / (n - 1)


# -----------------------------------
# Question 5 – Covariance Matrix
# -----------------------------------

def covariance_matrix(x, y):
    """
    Return 2x2 covariance matrix:
        [[var(x), cov(x,y)],
         [cov(x,y), var(y)]]
    """
    var_x = sample_variance(x)
    var_y = sample_variance(y)
    cov_xy = sample_covariance(x, y)

    return np.array([[var_x, cov_xy],
                     [cov_xy, var_y]])
