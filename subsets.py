import heapq
def sorted_subset_sums(numbers: set):
    # Put your iterator/generator here. 
    """
    from the problem statement:
    >>> from itertools import takewhile, islice
    >>> list(sorted_subset_sums([1,2,4]))
    [0, 1, 2, 3, 4, 5, 6, 7]

    >>> list(sorted_subset_sums([1,2,3]))
    [0, 1, 2, 3, 3, 4, 5, 6]

    >>> list(sorted_subset_sums([2,3,4]))
    [0, 2, 3, 4, 5, 6, 7, 9]

    >>> list(islice(sorted_subset_sums(range(100)),5))
    [0, 0, 1, 1, 2]

    >>> list(takewhile(lambda x:x<=6, sorted_subset_sums(range(1,100))))
    [0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6]

    >>> list(zip(range(5), sorted_subset_sums(range(100))))
    [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2)]

    """
    s= sorted(numbers)
    n= len(s)
    heap=[(0, 0)]
    while heap:
        curr_sum, i = heapq.heappop(heap)
        yield curr_sum
        if i < n:
            heapq.heappush(heap, (curr_sum + s[i], i + 1))
            if i > 0:
                heapq.heappush(heap, (curr_sum + s[i] - s[i - 1], i + 1))
                
                
if __name__ == '__main__':
    # from itertools import takewhile, islice
    # for i in eval(input()):
    #     print(i, end=", ")
    import doctest
    doctest.testmod(verbose=True)
    
