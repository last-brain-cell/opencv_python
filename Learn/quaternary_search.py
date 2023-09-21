def quaternary_search(arr, query):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid1 = lo + (hi - lo) // 4
        mid2 = lo + 2 * (hi - lo) // 4
        mid3 = lo + 3 * (hi - lo) // 4

        if arr[mid1] == query:
            return mid1
        elif arr[mid2] == query:
            return mid2
        elif arr[mid3] == query:
            return mid3
        elif arr[mid1] > query:
            hi = mid1 - 1
        elif arr[mid3] < query:
            lo = mid3 + 1
        else:
            lo = mid2 + 1
            hi = mid3 - 1

    return -1