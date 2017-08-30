#! /usr/bin/python3


def scalar_fibonacci(n):
    """
    Given a nonnegative integer n, return the nth Fibonacci number.  For example:

    >>> scalar_fibonacci(0)
    0
    >>> scalar_fibonacci(1)
    1
    >>> scalar_fibonacci(2)
    1
    >>> scalar_fibonacci(3)
    2
    >>> scalar_fibonacci(4)
    3
    >>> scalar_fibonacci(5)
    5
    >>> scalar_fibonacci(35)
    9227465
    """
    return 0  # stub


def vector_fibonacci(n):
    """
    Given a positive integer n, return a tuple containing the (n-1)th Fibonacci number and the nth Fibonacci number.
    For example:

    >>> vector_fibonacci(1)
    (0, 1)
    >>> vector_fibonacci(2)
    (1, 1)
    >>> vector_fibonacci(3)
    (1, 2)
    >>> vector_fibonacci(4)
    (2, 3)
    >>> vector_fibonacci(5)
    (3, 5)
    >>> vector_fibonacci(35)
    (5702887, 9227465)
    >>> vector_fibonacci(350)
    (3865462327928467072415604609040860366007401579690263197296200323999931849, 6254449428820551641549772190170184190608177514674331726439961915653414425)
    """
    return 0, 1  # stub


def maximal_repetition_free_prefix(sequence):
    """
    Given a sequence, return its longest repetition-free prefix.  For example:

    >>> maximal_repetition_free_prefix([])
    []
    >>> maximal_repetition_free_prefix([5])
    [5]
    >>> maximal_repetition_free_prefix([5, 4])
    [5, 4]
    >>> maximal_repetition_free_prefix([5, 5])
    [5]
    >>> maximal_repetition_free_prefix([5, 4, 5])
    [5, 4]
    >>> maximal_repetition_free_prefix([5, 4, 5, 3])
    [5, 4]
    >>> maximal_repetition_free_prefix([3, 2, 1, 2, 4])
    [3, 2, 1]

    """
    return []  # stub


def maximal_repetition_free_subsequence(sequence):
    """
    Given a sequence, return the last of its longest repetition-free subsequences.  For example:

    >>> maximal_repetition_free_subsequence([])
    []
    >>> maximal_repetition_free_subsequence([5])
    [5]
    >>> maximal_repetition_free_subsequence([5, 4])
    [5, 4]
    >>> maximal_repetition_free_subsequence([5, 4, 5])
    [4, 5]
    >>> maximal_repetition_free_subsequence([5, 4, 5, 3])
    [4, 5, 3]
    >>> maximal_repetition_free_subsequence([3, 2, 1, 2, 4])
    [1, 2, 4]
    >>> maximal_repetition_free_subsequence([1, 2, 1, 2, 1, 2, 1])
    [2, 1]
    """
    return []  # stub


def maximal_repetition_free_subsequence_version_2(sequence):
    """
    Given a sequence, return the last of its longest repetition-free subsequences.  For example:

    >>> maximal_repetition_free_subsequence_version_2([])
    []
    >>> maximal_repetition_free_subsequence_version_2([5])
    [5]
    >>> maximal_repetition_free_subsequence_version_2([5, 4])
    [5, 4]
    >>> maximal_repetition_free_subsequence_version_2([5, 4, 5])
    [4, 5]
    >>> maximal_repetition_free_subsequence_version_2([5, 4, 5, 3])
    [4, 5, 3]
    >>> maximal_repetition_free_subsequence_version_2([3, 2, 1, 2, 4])
    [1, 2, 4]
    >>> maximal_repetition_free_subsequence_version_2([1, 2, 1, 2, 1, 2, 1])
    [2, 1]
    """
    result = []
    for start in range(len(sequence)):
        for end in range(start + 1, len(sequence) + 1):
            if end - start >= len(result):
                if len(set(sequence[start:end])) == end - start:
                    result = sequence[start:end]
    return result


def maximal_repetition_free_subsequence_version_3(sequence):
    """
    Given a sequence, return the last of its longest repetition-free subsequences.  For example:

    >>> maximal_repetition_free_subsequence_version_3([])
    []
    >>> maximal_repetition_free_subsequence_version_3([5])
    [5]
    >>> maximal_repetition_free_subsequence_version_3([5, 4])
    [5, 4]
    >>> maximal_repetition_free_subsequence_version_3([5, 4, 5])
    [4, 5]
    >>> maximal_repetition_free_subsequence_version_3([5, 4, 5, 3])
    [4, 5, 3]
    >>> maximal_repetition_free_subsequence_version_3([3, 2, 1, 2, 4])
    [1, 2, 4]
    >>> maximal_repetition_free_subsequence_version_3([1, 2, 1, 2, 1, 2, 1])
    [2, 1]
    """
    return []  # stub