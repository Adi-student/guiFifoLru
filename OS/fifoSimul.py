from collections import deque

def fifo_page_replacement(reference_string, frames):
    memory = deque(maxlen=frames)
    page_faults = 0
    
    print("\n--- FIFO Simulation ---")
    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) == frames:
                # Page out the oldest page
                memory.popleft()
            memory.append(page)
            print(f"Page fault: {page} -> Current frames: {list(memory)}")
        else:
            print(f"Hit: {page} -> Current frames: {list(memory)}")
            
    return page_faults

# Test case
ref_str_fifo = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frames_fifo = 3
faults_fifo = fifo_page_replacement(ref_str_fifo, frames_fifo)
print(f"\nTotal page faults with FIFO: {faults_fifo}")