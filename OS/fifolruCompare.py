from collections import deque
import time

def fifo_page_replacement(reference_string, frames, verbose=False):
    memory = deque(maxlen=frames)
    page_faults = 0
    hits = 0
    detailed_log = []
    
    if verbose:
        print(f"\n--- FIFO Simulation (Frames: {frames}) ---")
    
    for i, page in enumerate(reference_string):
        if page not in memory:
            page_faults += 1
            old_page = None
            if len(memory) == frames:
                old_page = memory[0]
            memory.append(page)
            
            log_entry = {
                'step': i + 1,
                'page': page,
                'action': 'Page Fault',
                'frames': list(memory),
                'replaced': old_page
            }
            detailed_log.append(log_entry)
            
            if verbose:
                if old_page:
                    print(f"Step {i+1}: Page fault: {page} (replaced {old_page}) -> Frames: {list(memory)}")
                else:
                    print(f"Step {i+1}: Page fault: {page} -> Frames: {list(memory)}")
        else:
            hits += 1
            log_entry = {
                'step': i + 1,
                'page': page,
                'action': 'Hit',
                'frames': list(memory),
                'replaced': None
            }
            detailed_log.append(log_entry)
            
            if verbose:
                print(f"Step {i+1}: Hit: {page} -> Frames: {list(memory)}")
    
    total_references = len(reference_string)
    hit_ratio = (hits / total_references) * 100 if total_references > 0 else 0
    
    return page_faults, hit_ratio, detailed_log

def lru_page_replacement(reference_string, frames, verbose=False):
    memory = []
    page_faults = 0
    hits = 0
    detailed_log = []
    
    if verbose:
        print(f"\n--- LRU Simulation (Frames: {frames}) ---")
    
    for i, page in enumerate(reference_string):
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
            
            log_entry = {
                'step': i + 1,
                'page': page,
                'action': 'Hit',
                'frames': memory.copy(),
                'replaced': None
            }
            detailed_log.append(log_entry)
            
            if verbose:
                print(f"Step {i+1}: Hit: {page} -> Frames: {memory}")
        else:
            page_faults += 1
            old_page = None
            if len(memory) == frames:
                # Page out the least recently used (first element)
                old_page = memory.pop(0)
            memory.append(page)
            
            log_entry = {
                'step': i + 1,
                'page': page,
                'action': 'Page Fault',
                'frames': memory.copy(),
                'replaced': old_page
            }
            detailed_log.append(log_entry)
            
            if verbose:
                if old_page:
                    print(f"Step {i+1}: Page fault: {page} (replaced {old_page}) -> Frames: {memory}")
                else:
                    print(f"Step {i+1}: Page fault: {page} -> Frames: {memory}")
    
    total_references = len(reference_string)
    hit_ratio = (hits / total_references) * 100 if total_references > 0 else 0
    
    return page_faults, hit_ratio, detailed_log

def run_comparison_test(reference_string, frames, test_name, verbose=False):
    """
    Run both algorithms on the same test case and compare results
    """
    print(f"\n{'='*60}")
    print(f"TEST: {test_name}")
    print(f"Reference String: {reference_string}")
    print(f"Number of Frames: {frames}")
    print(f"{'='*60}")
    
    # Run FIFO
    start_time = time.time()
    fifo_faults, fifo_hit_ratio, fifo_log = fifo_page_replacement(reference_string, frames, verbose)
    fifo_time = time.time() - start_time
    
    # Run LRU
    start_time = time.time()
    lru_faults, lru_hit_ratio, lru_log = lru_page_replacement(reference_string, frames, verbose)
    lru_time = time.time() - start_time
    
    # Display results
    print(f"\n--- COMPARISON RESULTS ---")
    print(f"FIFO Algorithm:")
    print(f"  - Page Faults: {fifo_faults}")
    print(f"  - Hit Ratio: {fifo_hit_ratio:.2f}%")
    print(f"  - Execution Time: {fifo_time:.6f} seconds")
    
    print(f"\nLRU Algorithm:")
    print(f"  - Page Faults: {lru_faults}")
    print(f"  - Hit Ratio: {lru_hit_ratio:.2f}%")
    print(f"  - Execution Time: {lru_time:.6f} seconds")
    
    # Determine winner
    if fifo_faults < lru_faults:
        winner = "FIFO"
        difference = lru_faults - fifo_faults
    elif lru_faults < fifo_faults:
        winner = "LRU"
        difference = fifo_faults - lru_faults
    else:
        winner = "TIE"
        difference = 0
    
    print(f"\n--- ANALYSIS ---")
    if winner == "TIE":
        print("Both algorithms performed equally well!")
    else:
        print(f"Winner: {winner} (by {difference} fewer page faults)")
        improvement = (difference / max(fifo_faults, lru_faults)) * 100
        print(f"Performance improvement: {improvement:.2f}%")
    
    return {
        'test_name': test_name,
        'reference_string': reference_string,
        'frames': frames,
        'fifo_faults': fifo_faults,
        'fifo_hit_ratio': fifo_hit_ratio,
        'fifo_time': fifo_time,
        'lru_faults': lru_faults,
        'lru_hit_ratio': lru_hit_ratio,
        'lru_time': lru_time,
        'winner': winner,
        'difference': difference
    }

def run_comprehensive_analysis():
    """
    Run multiple test scenarios and provide comprehensive analysis
    """
    print("COMPREHENSIVE PAGE REPLACEMENT ALGORITHM COMPARISON")
    print("=" * 80)
    
    # Test scenarios
    test_scenarios = [
        {
            'name': 'Basic Test Case',
            'reference_string': [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1],
            'frames': [3, 4, 5]
        },
        {
            'name': 'Sequential Access Pattern',
            'reference_string': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
            'frames': [3, 4, 5]
        },
        {
            'name': 'Repeated Pattern',
            'reference_string': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
            'frames': [2, 3, 4]
        },
        {
            'name': 'Random Access Pattern',
            'reference_string': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4],
            'frames': [3, 4, 5]
        },
        {
            'name': 'Locality of Reference',
            'reference_string': [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 4, 4, 2, 2, 5, 5, 5],
            'frames': [3, 4]
        }
    ]
    
    all_results = []
    
    for scenario in test_scenarios:
        for frame_size in scenario['frames']:
            result = run_comparison_test(
                scenario['reference_string'], 
                frame_size, 
                f"{scenario['name']} - {frame_size} frames",
                verbose=False
            )
            all_results.append(result)
    
    # Summary analysis
    print(f"\n{'='*80}")
    print("SUMMARY ANALYSIS")
    print(f"{'='*80}")
    
    fifo_wins = sum(1 for r in all_results if r['winner'] == 'FIFO')
    lru_wins = sum(1 for r in all_results if r['winner'] == 'LRU')
    ties = sum(1 for r in all_results if r['winner'] == 'TIE')
    
    print(f"Total Tests Run: {len(all_results)}")
    print(f"FIFO Wins: {fifo_wins}")
    print(f"LRU Wins: {lru_wins}")
    print(f"Ties: {ties}")
    
    # Average performance
    avg_fifo_faults = sum(r['fifo_faults'] for r in all_results) / len(all_results)
    avg_lru_faults = sum(r['lru_faults'] for r in all_results) / len(all_results)
    avg_fifo_hit_ratio = sum(r['fifo_hit_ratio'] for r in all_results) / len(all_results)
    avg_lru_hit_ratio = sum(r['lru_hit_ratio'] for r in all_results) / len(all_results)
    
    print(f"\nAverage Performance:")
    print(f"FIFO - Avg Page Faults: {avg_fifo_faults:.2f}, Avg Hit Ratio: {avg_fifo_hit_ratio:.2f}%")
    print(f"LRU  - Avg Page Faults: {avg_lru_faults:.2f}, Avg Hit Ratio: {avg_lru_hit_ratio:.2f}%")
    
    # Best and worst cases
    best_fifo = min(all_results, key=lambda x: x['fifo_faults'])
    best_lru = min(all_results, key=lambda x: x['lru_faults'])
    worst_fifo = max(all_results, key=lambda x: x['fifo_faults'])
    worst_lru = max(all_results, key=lambda x: x['lru_faults'])
    
    print(f"\nBest Performance:")
    print(f"FIFO Best: {best_fifo['test_name']} - {best_fifo['fifo_faults']} faults")
    print(f"LRU Best:  {best_lru['test_name']} - {best_lru['lru_faults']} faults")
    
    print(f"\nWorst Performance:")
    print(f"FIFO Worst: {worst_fifo['test_name']} - {worst_fifo['fifo_faults']} faults")
    print(f"LRU Worst:  {worst_lru['test_name']} - {worst_lru['lru_faults']} faults")
    
    return all_results

def interactive_test():
    """
    Allow user to input custom test cases
    """
    print("\n" + "="*60)
    print("INTERACTIVE TESTING MODE")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Test with custom reference string")
        print("2. Test with predefined scenarios")
        print("3. Run comprehensive analysis")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            try:
                ref_str_input = input("Enter reference string (comma-separated): ")
                reference_string = [int(x.strip()) for x in ref_str_input.split(',')]
                frames = int(input("Enter number of frames: "))
                verbose = input("Show detailed steps? (y/n): ").lower().startswith('y')
                
                result = run_comparison_test(reference_string, frames, "Custom Test", verbose)
                
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == '2':
            # Quick predefined test
            test_cases = [
                ([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5], 3),
                ([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1], 4),
                ([1, 2, 3, 1, 4, 2, 5, 1, 2, 3, 4, 5], 3)
            ]
            
            for i, (ref_str, frames) in enumerate(test_cases, 1):
                run_comparison_test(ref_str, frames, f"Predefined Test {i}", verbose=False)
                
        elif choice == '3':
            run_comprehensive_analysis()
            
        elif choice == '4':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    # Run a quick demonstration
    print("PAGE REPLACEMENT ALGORITHM COMPARISON TOOL")
    print("=" * 80)
    
    # Demo with the original test case
    demo_ref_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    run_comparison_test(demo_ref_string, 3, "Demo - Original Test Case", verbose=True)
    
    # Ask user what they want to do next
    print("\n" + "="*60)
    choice = input("Would you like to run more tests? (y/n): ").lower()
    if choice.startswith('y'):
        interactive_test()
    else:
        print("Run the script again to perform more comparisons!")
