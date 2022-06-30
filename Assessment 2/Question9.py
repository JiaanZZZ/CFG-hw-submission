def two_sum(arr1,target_sum):
    arr_set=set({})
    for x in arr1:
        if target_sum-x in arr_set:
            return [x,target_sum-x]
        arr_set.add(x)
    return []

