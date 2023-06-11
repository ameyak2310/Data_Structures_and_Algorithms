def myquicksort(lst):
    if len(lst) == 1:
        sorted_list = list
    else:
        pivot = lst[0]
        small = []; same = []; big = []
        
        for item in lst:
            if item < pivot:
                small.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                big.append(item)
                
        sorted_list = small + same + big
        
    return sorted_list

myquicksort([1,1,2,3,3,5,66,999,1000])
        
        