def lru_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    
    print("\n--- LRU Simulation ---")
    for page in reference_string:
        if page in memory:
            # Move the page to the end (most recently used)
            memory.remove(page)
            memory.append(page)
            print(f"Hit: {page} -> Current frames: {memory}")
        else:
            page_faults += 1
            if len(memory) == frames:
                # Page out the least recently used (first element)
                memory.pop(0)
            memory.append(page)
            print(f"Page fault: {page} -> Current frames: {memory}")
            
    return page_faults

# Test case
ref_str_lru = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frames_lru = 3
faults_lru = lru_page_replacement(ref_str_lru, frames_lru)
print(f"\nTotal page faults with LRU: {faults_lru}")