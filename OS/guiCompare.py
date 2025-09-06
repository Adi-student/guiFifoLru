import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from collections import deque
import time

class PageReplacementGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Page Replacement Algorithm Comparison Tool")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Test data
        self.demo_ref_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
        self.demo_frames = 3
        self.current_ref_string = self.demo_ref_string.copy()
        self.current_frames = self.demo_frames
        
        self.create_main_window()
        
    def create_main_window(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.root.title("Page Replacement Algorithm Comparison Tool")
        
        # Title
        title_label = tk.Label(self.root, text="Page Replacement Algorithm Comparison Tool", 
                              font=("Arial", 20, "bold"), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=20)
        
        # Test case info frame
        info_frame = tk.LabelFrame(self.root, text="Current Test Case", font=("Arial", 12, "bold"), 
                                  bg='#f0f0f0', fg='#333', padx=10, pady=10)
        info_frame.pack(pady=10, padx=20, fill='x')
        
        test_info = f"TEST: Demo - Original Test Case\nReference String: {self.current_ref_string}\nNumber of Frames: {self.current_frames}"
        tk.Label(info_frame, text=test_info, font=("Arial", 10), bg='#f0f0f0', 
                justify='left').pack(anchor='w')
        
        # Input frame
        input_frame = tk.LabelFrame(self.root, text="Customize Test Case", font=("Arial", 12, "bold"), 
                                   bg='#f0f0f0', fg='#333', padx=10, pady=10)
        input_frame.pack(pady=10, padx=20, fill='x')
        
        # Reference string input
        tk.Label(input_frame, text="Reference String (comma-separated):", 
                bg='#f0f0f0', font=("Arial", 10)).grid(row=0, column=0, sticky='w', pady=5)
        self.ref_string_entry = tk.Entry(input_frame, width=50, font=("Arial", 10))
        self.ref_string_entry.insert(0, ",".join(map(str, self.current_ref_string)))
        self.ref_string_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Frames input
        tk.Label(input_frame, text="Number of Frames:", 
                bg='#f0f0f0', font=("Arial", 10)).grid(row=1, column=0, sticky='w', pady=5)
        self.frames_entry = tk.Entry(input_frame, width=10, font=("Arial", 10))
        self.frames_entry.insert(0, str(self.current_frames))
        self.frames_entry.grid(row=1, column=1, sticky='w', pady=5, padx=10)
        
        # Update button
        update_btn = tk.Button(input_frame, text="Update Test Case", 
                              command=self.update_test_case, bg='#4CAF50', fg='white',
                              font=("Arial", 10, "bold"), padx=20)
        update_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg='#f0f0f0')
        buttons_frame.pack(pady=30)
        
        # Create buttons
        btn_style = {"font": ("Arial", 12, "bold"), "width": 20, "height": 2, "relief": "raised", "bd": 3}
        
        fifo_btn = tk.Button(buttons_frame, text="FIFO Simulation", 
                            command=self.open_fifo_window, bg='#2196F3', fg='white', **btn_style)
        fifo_btn.grid(row=0, column=0, padx=10, pady=10)
        
        lru_btn = tk.Button(buttons_frame, text="LRU Simulation", 
                           command=self.open_lru_window, bg='#FF9800', fg='white', **btn_style)
        lru_btn.grid(row=0, column=1, padx=10, pady=10)
        
        compare_btn = tk.Button(buttons_frame, text="Comparison Results", 
                               command=self.open_comparison_window, bg='#9C27B0', fg='white', **btn_style)
        compare_btn.grid(row=1, column=0, padx=10, pady=10)
        
        analysis_btn = tk.Button(buttons_frame, text="Comprehensive Analysis", 
                                command=self.open_analysis_window, bg='#F44336', fg='white', **btn_style)
        analysis_btn.grid(row=1, column=1, padx=10, pady=10)
        
        # Exit button
        exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit, 
                            bg='#607D8B', fg='white', font=("Arial", 12, "bold"), 
                            width=15, height=1)
        exit_btn.pack(pady=20)
        
    def update_test_case(self):
        try:
            ref_str_text = self.ref_string_entry.get().strip()
            self.current_ref_string = [int(x.strip()) for x in ref_str_text.split(',')]
            self.current_frames = int(self.frames_entry.get().strip())
            messagebox.showinfo("Success", "Test case updated successfully!")
            self.create_main_window()  # Refresh the main window
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")
            
    def fifo_page_replacement(self, reference_string, frames):
        memory = deque(maxlen=frames)
        page_faults = 0
        hits = 0
        detailed_log = []
        
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
        
        total_references = len(reference_string)
        hit_ratio = (hits / total_references) * 100 if total_references > 0 else 0
        
        return page_faults, hit_ratio, detailed_log
    
    def lru_page_replacement(self, reference_string, frames):
        memory = []
        page_faults = 0
        hits = 0
        detailed_log = []
        
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
            else:
                page_faults += 1
                old_page = None
                if len(memory) == frames:
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
        
        total_references = len(reference_string)
        hit_ratio = (hits / total_references) * 100 if total_references > 0 else 0
        
        return page_faults, hit_ratio, detailed_log
    
    def create_test_info_header(self, parent):
        info_frame = tk.LabelFrame(parent, text="Current Test Case", font=("Arial", 10, "bold"), 
                                  bg='#f8f8f8', fg='#333', padx=10, pady=5)
        info_frame.pack(pady=5, padx=10, fill='x')
        
        test_info = f"TEST: Demo - Original Test Case\nReference String: {self.current_ref_string}\nNumber of Frames: {self.current_frames}"
        tk.Label(info_frame, text=test_info, font=("Arial", 9), bg='#f8f8f8', 
                justify='left').pack(anchor='w')
        
        return info_frame
    
    def open_fifo_window(self):
        fifo_window = tk.Toplevel(self.root)
        fifo_window.title("FIFO Page Replacement Simulation")
        fifo_window.geometry("900x700")
        fifo_window.configure(bg='#f0f0f0')
        
        # Test info header
        self.create_test_info_header(fifo_window)
        
        # Title
        title_label = tk.Label(fifo_window, text="FIFO Page Replacement Simulation", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2196F3')
        title_label.pack(pady=10)
        
        # Run simulation
        page_faults, hit_ratio, detailed_log = self.fifo_page_replacement(
            self.current_ref_string, self.current_frames)
        
        # Results frame
        results_frame = tk.LabelFrame(fifo_window, text="Results", font=("Arial", 12, "bold"), 
                                     bg='#f0f0f0', fg='#333', padx=10, pady=10)
        results_frame.pack(pady=10, padx=20, fill='x')
        
        results_text = f"Total Page Faults: {page_faults}\nHit Ratio: {hit_ratio:.2f}%\nTotal References: {len(self.current_ref_string)}"
        tk.Label(results_frame, text=results_text, font=("Arial", 11), bg='#f0f0f0', 
                justify='left').pack(anchor='w')
        
        # Detailed log
        log_frame = tk.LabelFrame(fifo_window, text="Detailed Simulation Log", 
                                 font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333')
        log_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Create treeview for log
        columns = ('Step', 'Page', 'Action', 'Frames', 'Replaced')
        tree = ttk.Treeview(log_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        
        # Populate treeview
        for entry in detailed_log:
            replaced = entry['replaced'] if entry['replaced'] else '-'
            tree.insert('', tk.END, values=(
                entry['step'], entry['page'], entry['action'], 
                str(entry['frames']), replaced
            ))
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(log_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Back button
        back_btn = tk.Button(fifo_window, text="Back to Main", 
                            command=fifo_window.destroy, bg='#607D8B', fg='white',
                            font=("Arial", 10, "bold"))
        back_btn.pack(pady=10)
    
    def open_lru_window(self):
        lru_window = tk.Toplevel(self.root)
        lru_window.title("LRU Page Replacement Simulation")
        lru_window.geometry("900x700")
        lru_window.configure(bg='#f0f0f0')
        
        # Test info header
        self.create_test_info_header(lru_window)
        
        # Title
        title_label = tk.Label(lru_window, text="LRU Page Replacement Simulation", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#FF9800')
        title_label.pack(pady=10)
        
        # Run simulation
        page_faults, hit_ratio, detailed_log = self.lru_page_replacement(
            self.current_ref_string, self.current_frames)
        
        # Results frame
        results_frame = tk.LabelFrame(lru_window, text="Results", font=("Arial", 12, "bold"), 
                                     bg='#f0f0f0', fg='#333', padx=10, pady=10)
        results_frame.pack(pady=10, padx=20, fill='x')
        
        results_text = f"Total Page Faults: {page_faults}\nHit Ratio: {hit_ratio:.2f}%\nTotal References: {len(self.current_ref_string)}"
        tk.Label(results_frame, text=results_text, font=("Arial", 11), bg='#f0f0f0', 
                justify='left').pack(anchor='w')
        
        # Detailed log
        log_frame = tk.LabelFrame(lru_window, text="Detailed Simulation Log", 
                                 font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333')
        log_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Create treeview for log
        columns = ('Step', 'Page', 'Action', 'Frames', 'Replaced')
        tree = ttk.Treeview(log_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        
        # Populate treeview
        for entry in detailed_log:
            replaced = entry['replaced'] if entry['replaced'] else '-'
            tree.insert('', tk.END, values=(
                entry['step'], entry['page'], entry['action'], 
                str(entry['frames']), replaced
            ))
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(log_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Back button
        back_btn = tk.Button(lru_window, text="Back to Main", 
                            command=lru_window.destroy, bg='#607D8B', fg='white',
                            font=("Arial", 10, "bold"))
        back_btn.pack(pady=10)
    
    def open_comparison_window(self):
        comp_window = tk.Toplevel(self.root)
        comp_window.title("FIFO vs LRU Comparison")
        comp_window.geometry("1200x700")
        comp_window.configure(bg='#f0f0f0')
        
        # Test info header
        self.create_test_info_header(comp_window)
        
        # Title
        title_label = tk.Label(comp_window, text="FIFO vs LRU Comparison Results", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#9C27B0')
        title_label.pack(pady=10)
        
        # Run both algorithms
        start_time = time.time()
        fifo_faults, fifo_hit_ratio, fifo_log = self.fifo_page_replacement(
            self.current_ref_string, self.current_frames)
        fifo_time = time.time() - start_time
        
        start_time = time.time()
        lru_faults, lru_hit_ratio, lru_log = self.lru_page_replacement(
            self.current_ref_string, self.current_frames)
        lru_time = time.time() - start_time
        
        # Create main content frame with two columns
        main_frame = tk.Frame(comp_window, bg='#f0f0f0')
        main_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Left column for results and analysis
        left_frame = tk.Frame(main_frame, bg='#f0f0f0')
        left_frame.pack(side='left', fill='both', expand=False, padx=(0, 10))
        
        # Right column for side-by-side comparison
        right_frame = tk.Frame(main_frame, bg='#f0f0f0')
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Results frame (in left column)
        results_frame = tk.LabelFrame(left_frame, text="Comparison Results", 
                                     font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333')
        results_frame.pack(pady=5, fill='x')
        
        # Create comparison table
        comparison_text = f"""FIFO Algorithm:
  • Page Faults: {fifo_faults}
  • Hit Ratio: {fifo_hit_ratio:.2f}%
  • Execution Time: {fifo_time:.6f} seconds

LRU Algorithm:
  • Page Faults: {lru_faults}
  • Hit Ratio: {lru_hit_ratio:.2f}%
  • Execution Time: {lru_time:.6f} seconds"""
        
        tk.Label(results_frame, text=comparison_text, font=("Arial", 10), 
                bg='#f0f0f0', justify='left').pack(anchor='w', padx=10, pady=10)
        
        # Analysis frame (in left column)
        analysis_frame = tk.LabelFrame(left_frame, text="Performance Analysis", 
                                      font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333')
        analysis_frame.pack(pady=5, fill='x')
        
        # Determine winner
        if fifo_faults < lru_faults:
            winner = "FIFO"
            difference = lru_faults - fifo_faults
            color = '#2196F3'
        elif lru_faults < fifo_faults:
            winner = "LRU"
            difference = fifo_faults - lru_faults
            color = '#FF9800'
        else:
            winner = "TIE"
            difference = 0
            color = '#4CAF50'
        
        if winner == "TIE":
            analysis_text = "Both algorithms performed equally well!\n\nWhy equal performance?\n"
            # Analyze why they're equal
            if self.current_frames >= len(set(self.current_ref_string)):
                analysis_text += "• Enough frames for all unique pages\n• No page replacement needed"
            elif self.current_frames == 1:
                analysis_text += "• Only 1 frame available\n• Both algorithms behave identically"
            elif self.current_frames == 2:
                analysis_text += "• With 2 frames, patterns may not\n  reveal algorithm differences"
            else:
                analysis_text += "• Reference pattern doesn't favor\n  either algorithm significantly"
        else:
            improvement = (difference / max(fifo_faults, lru_faults)) * 100
            analysis_text = f"Winner: {winner}\nBy {difference} fewer page faults\nPerformance improvement: {improvement:.2f}%\n\n"
            
            # Explain why there's a difference
            if winner == "LRU":
                analysis_text += "LRU wins because:\n• It considers recency of use\n• Better for patterns with locality"
            else:
                analysis_text += "FIFO wins because:\n• Simple replacement strategy works\n• Less overhead in this case"
        
        # Add frame analysis
        unique_pages = len(set(self.current_ref_string))
        analysis_text += f"\n\nFrame Analysis:\n• Unique pages: {unique_pages}\n• Available frames: {self.current_frames}"
        
        if self.current_frames >= unique_pages:
            analysis_text += "\n• No replacement needed after initial loading"
        elif self.current_frames == 1:
            analysis_text += "\n• Algorithms behave identically with 1 frame"
        else:
            analysis_text += f"\n• Page replacement will occur\n• Algorithms may differ with {self.current_frames} frames"
        
        analysis_label = tk.Label(analysis_frame, text=analysis_text, font=("Arial", 9), 
                                 bg='#f0f0f0', fg=color, justify='left')
        analysis_label.pack(pady=10, anchor='w', padx=10)
        
        # Detailed comparison table (in right column)
        detail_frame = tk.LabelFrame(right_frame, text="Side-by-Side Comparison", 
                                    font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333')
        detail_frame.pack(fill='both', expand=True)
        
        # Create comparison treeview
        columns = ('Step', 'Page', 'FIFO Action', 'FIFO Frames', 'LRU Action', 'LRU Frames')
        tree = ttk.Treeview(detail_frame, columns=columns, show='headings', height=20)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=90, anchor='center')
        
        # Populate comparison
        for i in range(len(fifo_log)):
            tree.insert('', tk.END, values=(
                fifo_log[i]['step'], fifo_log[i]['page'],
                fifo_log[i]['action'], str(fifo_log[i]['frames']),
                lru_log[i]['action'], str(lru_log[i]['frames'])
            ))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Back button
        back_btn = tk.Button(comp_window, text="Back to Main", 
                            command=comp_window.destroy, bg='#607D8B', fg='white',
                            font=("Arial", 10, "bold"))
        back_btn.pack(pady=10)
    
    def open_analysis_window(self):
        analysis_window = tk.Toplevel(self.root)
        analysis_window.title("Comprehensive Analysis")
        analysis_window.geometry("1000x700")
        analysis_window.configure(bg='#f0f0f0')
        
        # Test info header
        self.create_test_info_header(analysis_window)
        
        # Title
        title_label = tk.Label(analysis_window, text="Comprehensive Algorithm Analysis", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#F44336')
        title_label.pack(pady=10)
        
        # Run comprehensive analysis
        test_scenarios = [
            {
                'name': 'Current Test Case',
                'reference_string': self.current_ref_string,
                'frames': [self.current_frames]
            },
            {
                'name': 'Sequential Access',
                'reference_string': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
                'frames': [3, 4, 5]
            },
            {
                'name': 'Repeated Pattern',
                'reference_string': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
                'frames': [2, 3, 4]
            },
            {
                'name': 'Random Access',
                'reference_string': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4],
                'frames': [3, 4, 5]
            }
        ]
        
        # Results frame with scrolled text
        results_frame = tk.LabelFrame(analysis_window, text="Analysis Results", 
                                     font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333')
        results_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        text_widget = scrolledtext.ScrolledText(results_frame, width=100, height=25, 
                                               font=("Courier", 10), bg='white')
        text_widget.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Run analysis and display results
        all_results = []
        
        text_widget.insert(tk.END, "COMPREHENSIVE PAGE REPLACEMENT ALGORITHM ANALYSIS\n")
        text_widget.insert(tk.END, "=" * 80 + "\n\n")
        
        for scenario in test_scenarios:
            for frame_size in scenario['frames']:
                # Run both algorithms
                fifo_faults, fifo_hit_ratio, _ = self.fifo_page_replacement(
                    scenario['reference_string'], frame_size)
                lru_faults, lru_hit_ratio, _ = self.lru_page_replacement(
                    scenario['reference_string'], frame_size)
                
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
                
                result = {
                    'test_name': f"{scenario['name']} - {frame_size} frames",
                    'fifo_faults': fifo_faults,
                    'fifo_hit_ratio': fifo_hit_ratio,
                    'lru_faults': lru_faults,
                    'lru_hit_ratio': lru_hit_ratio,
                    'winner': winner,
                    'difference': difference
                }
                all_results.append(result)
                
                # Display individual test result
                text_widget.insert(tk.END, f"TEST: {result['test_name']}\n")
                text_widget.insert(tk.END, f"Reference String: {scenario['reference_string']}\n")
                text_widget.insert(tk.END, f"Frames: {frame_size}\n")
                text_widget.insert(tk.END, f"FIFO - Faults: {fifo_faults}, Hit Ratio: {fifo_hit_ratio:.2f}%\n")
                text_widget.insert(tk.END, f"LRU  - Faults: {lru_faults}, Hit Ratio: {lru_hit_ratio:.2f}%\n")
                text_widget.insert(tk.END, f"Winner: {winner}")
                if difference > 0:
                    text_widget.insert(tk.END, f" (by {difference} faults)")
                text_widget.insert(tk.END, "\n" + "-" * 60 + "\n\n")
        
        # Summary analysis
        text_widget.insert(tk.END, "\nSUMMARY ANALYSIS\n")
        text_widget.insert(tk.END, "=" * 50 + "\n")
        
        fifo_wins = sum(1 for r in all_results if r['winner'] == 'FIFO')
        lru_wins = sum(1 for r in all_results if r['winner'] == 'LRU')
        ties = sum(1 for r in all_results if r['winner'] == 'TIE')
        
        text_widget.insert(tk.END, f"Total Tests: {len(all_results)}\n")
        text_widget.insert(tk.END, f"FIFO Wins: {fifo_wins}\n")
        text_widget.insert(tk.END, f"LRU Wins: {lru_wins}\n")
        text_widget.insert(tk.END, f"Ties: {ties}\n\n")
        
        # Average performance
        avg_fifo_faults = sum(r['fifo_faults'] for r in all_results) / len(all_results)
        avg_lru_faults = sum(r['lru_faults'] for r in all_results) / len(all_results)
        avg_fifo_hit_ratio = sum(r['fifo_hit_ratio'] for r in all_results) / len(all_results)
        avg_lru_hit_ratio = sum(r['lru_hit_ratio'] for r in all_results) / len(all_results)
        
        text_widget.insert(tk.END, "Average Performance:\n")
        text_widget.insert(tk.END, f"FIFO - Avg Faults: {avg_fifo_faults:.2f}, Avg Hit Ratio: {avg_fifo_hit_ratio:.2f}%\n")
        text_widget.insert(tk.END, f"LRU  - Avg Faults: {avg_lru_faults:.2f}, Avg Hit Ratio: {avg_lru_hit_ratio:.2f}%\n")
        
        # Back button
        back_btn = tk.Button(analysis_window, text="Back to Main", 
                            command=analysis_window.destroy, bg='#607D8B', fg='white',
                            font=("Arial", 10, "bold"))
        back_btn.pack(pady=10)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PageReplacementGUI()
    app.run()
