from collections import deque

def fifo_page_replacement(reference_string, frame_size):
    memory = deque(maxlen=frame_size)
    page_faults = 0

    for page in reference_string:
        if page not in memory:
            if len(memory) == frame_size:
                memory.popleft()
            memory.append(page)
            page_faults += 1
        print(f"Memory: {list(memory)}")

    return page_faults

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
frame_size = 3
page_faults = fifo_page_replacement(reference_string, frame_size)
print(f"Total page faults: {page_faults}")

