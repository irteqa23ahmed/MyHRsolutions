def poisonousPlants(p):
    curr = p[0]
    curr_count = 0
    max_val = 0
    temp = -1
    for i in range(1, len(p)):
        if p[i] > curr:
            if temp==-1 or temp >= p[i]-curr:
                curr_count += 1
            elif curr_count != 1:
                curr = temp + curr
                if max_val < curr_count:
                    max_val = curr_count
                curr_count = 1
            temp = p[i]-curr
        else:
            curr = p[i]
            if max_val < curr_count:
                max_val = curr_count
            curr_count = 0
            temp = -1
    if max_val < curr_count:
        max_val = curr_count
    return max_val
