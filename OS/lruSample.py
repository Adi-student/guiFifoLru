from collections import OrderedDict

def lru_page_replacement(reference_string, frame_size):
    memory = OrderedDict()
    page_faults = 0

    for page in reference_string:
        if page not in memory:
            if len(memory) == frame_size:
                memory.popitem(last=False)
            memory[page] = None
            page_faults += 1
        else:
            memory.move_to_end(page)
        print(f"Memory: {list(memory.keys())}")

    return page_faults

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
frame_size = 3
page_faults = lru_page_replacement(reference_string, frame_size)
print(f"Total page faults: {page_faults}")
