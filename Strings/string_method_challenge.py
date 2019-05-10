def remove2(str_lst: list, sub: str) -> tuple:
    """Write a function that accepts a list of strings and another string that removes that string from the list
without list iteration or list methods (aka only string methods).
It should return a tuple with the updated string, number of deletions, and the indexes of the deleted values."""
    text = "".join(str_lst)
    deletions = text.count(sub)

    icount = 0
    last_occurence = -1
    ilist = []

    while icount < deletions:
        last_occurence = text.find(sub, last_occurence + 1)
        ilist.append(last_occurence)
        icount += 1

    updated = text.replace(sub, "")

    return(updated, deletions, ilist)

my_list = ["b", "a", "b", "b", "a", "a", "b", "a", "b"]
print(remove2(my_list, "b"))

        
        
