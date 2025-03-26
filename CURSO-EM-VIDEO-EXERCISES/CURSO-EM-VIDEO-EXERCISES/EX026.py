#BIG O NOTATION

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        attempt = list[mid]
        
        if attempt == item:
            return mid
        elif attempt > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None
