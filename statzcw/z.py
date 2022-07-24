"""
    Test python module. This will be deleted when re-packaging the below functions.
    Functions will live in similarly named files within statscw package,
        under different name to avoid shodowing outer scope.
    Made by jjheffernan on week 4 of Zip Code Wilmington
"""

avg_val = 0


def count(funlist: list) -> float:
    return len(funlist)
    # pass # escape pass


def mean(funlist: list) -> float:
    global avg_val
    average = sum(funlist)/len(funlist)
    avg_val = int(average)
    return average
    pass  # escape pass


def mode(funlist: list) -> float:
    # this might need lots of if statements
    # min(), len(),
    temp_set = set(funlist)
    return max(temp_set, key=funlist.count)
    pass  # escape pass


def median(funlist: list) -> float:
    funlist.sort()
    if len(funlist) % 2 !=0:
        return funlist[int((len(funlist)/2)-1)]
    else:
        return funlist[int((len(funlist)-1)/2)]

    pass


def variance(funlist: list) -> float:

    pass


def stddev(funlist: list) -> float:
    pass


def stderr(funlist: list) -> float:
    pass


def corr(listx: list, listy: list) -> float:
    pass
