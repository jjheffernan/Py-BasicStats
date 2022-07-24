"""
    Test python module. This will be deleted when re-packaging the below functions.
    Functions will live in similarly named files within statscw package,
        under different name to avoid shodowing outer scope.
    Made by jjheffernan on week 4 of Zip Code Wilmington
"""
import math

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

    # pass


def variance(funlist: list) -> float:
    temp_mean = mean(funlist)
    result = sum((i-temp_mean)**2 for i in funlist) / len(funlist)
    return result
    # pass


def stddev(funlist: list) -> float:
    return variance(funlist) ** (1/2)
    # pass


def stderr(funlist: list) -> float:
    # need to build out
    return stddev(funlist) / math.sqrt(count(funlist))
    pass


def covariance(a: list, b: list) -> float:
    temp_sum = 0

    # x_mean = math.fsum(a) / len(a)
    # y_mean = math.fsum(b) / len(b)
    for i in range(0, count(a)):
        temp_sum += ((a[i] - mean(a)) * (b[i] - mean(b)))
    cov = temp_sum / (count(a) - 1)
    return cov
    # pass


def corr(listx: list, listy: list) -> float:
    return covariance(listx, listy) / stddev(listx) * stddev(listy)
    # pass
