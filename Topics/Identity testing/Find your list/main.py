def find_my_list(lists, my_list):

    for idx, lst in enumerate(lists):
        if my_list is lst:
            return idx

    return None
