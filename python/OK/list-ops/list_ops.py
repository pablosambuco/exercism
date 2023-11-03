"""list ops"""


def append(list1, list2):
    """
    given two lists, add all items in the second list to the end of the
    first list
    """
    new_list = list1 + list2
    return new_list


def concat(lists):
    """
    given a series of lists, combine all items in all lists into one
    flattened list
    """
    new_list = []
    for list1 in lists:
        for element in list1:
            if element not in new_list:
                new_list.append(element)
    return new_list


def filter(function, testlist):
    """
    given a predicate and a list, return the list of all items for which
    `predicate(item)` is True
    """
    return [element for element in testlist if function(element)]


def length(list):
    """
    given a list, return the total number of items within it
    """
    return sum(1 for _ in list)


def map(function, maplist):
    """
    given a function and a list, return the list of the results of applying
    `function(item)` on all items
    """
    return [function(element) for element in maplist]


def foldl(function, foldlist, initial):
    """
    given a function, a list, and initial accumulator, fold (reduce) each
    item into the accumulator from the left
    """
    for element in foldlist:
        initial = function(initial,element)
    return initial


def foldr(function, foldlist, initial):
    """
    given a function, a list, and an initial accumulator, fold (reduce) each
    item into the accumulator from the right
    """
    for element in foldlist[::-1]:
        initial = function(initial,element)
    return initial


def reverse(rlist):
    """
    given a list, return a list with all the original items, but in reversed
    order
    """
    return rlist[::-1]
