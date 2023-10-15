# def create_an_empty_list():
#     return None

def create_an_empty_list():
    return []

# def create_a_list():
#     return None


def create_a_list():
    # Create a new list with four elements
    new_list = [1, 'apple', True, 3.14]
    return new_list


# def add_element_to_end_of_list(l, element):
#     return None

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l


# def add_element_to_start_of_list(l, element):
#     return None

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l


# def remove_element_from_end_of_list(l):
#     return None

def remove_element_from_end_of_list(l):
    if len(l) > 0:
        removed_element = l.pop()
        return l  # Return the modified list
    else:
        # Handle the case when the list is empty
        return None


# def remove_element_from_start_of_list(l):
#     return None

def remove_element_from_start_of_list(l):
    if len(l) > 0:
        del l[0]
        return l  # Return the modified list
    else:
        # Handle the case when the list is empty
        return None


# def retrieve_first_element_from_list(l):
#     return None

def retrieve_first_element_from_list(l):
    if len(l) > 0:
        return l[0]  # Return the first element of the list
    else:
        # Handle the case when the list is empty
        return None


# def retrieve_element_from_index(l, index):
#     return None

def retrieve_element_from_index(l, index):
    if 0 <= index < len(l):
        return l[index]  # Return the element at the specified index
    else:
        # Handle the case when the index is out of range
        return None


# def retrieve_last_element_from_list(l):
#     return None

def retrieve_last_element_from_list(l):
    if len(l) > 0:
        return l[-1]  # Return the last element of the list
    else:
        # Handle the case when the list is empty
        return None
