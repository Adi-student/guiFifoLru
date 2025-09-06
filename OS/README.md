# Page Replacement Algorithm Comparison Tool

A comprehensive GUI-based educational tool for comparing FIFO (First In, First Out) and LRU (Least Recently Used) page replacement algorithms in operating systems. This tool provides interactive simulations, detailed analysis, and visual comparisons to help understand the performance characteristics of different page replacement strategies.

## 🚀 Features

### Core Functionality
- **FIFO Algorithm Simulation**: Step-by-step visualization of First In, First Out page replacement
- **LRU Algorithm Simulation**: Detailed LRU (Least Recently Used) algorithm execution
- **Side-by-Side Comparison**: Direct performance comparison between algorithms
- **Comprehensive Analysis**: Multi-scenario testing with statistical analysis
- **Interactive GUI**: User-friendly Tkinter-based interface

### Key Capabilities
- ✅ **Real-time Simulation**: Watch algorithms execute step-by-step
- ✅ **Performance Metrics**: Page faults, hit ratios, and execution times
- ✅ **Custom Test Cases**: Input your own reference strings and frame counts
- ✅ **Multiple Test Scenarios**: Pre-built test cases for different access patterns
- ✅ **Detailed Logging**: Complete execution traces with frame states
- ✅ **Statistical Analysis**: Win/loss ratios and average performance metrics

## 📋 Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [User Interface Guide](#user-interface-guide)
4. [Algorithm Details](#algorithm-details)
5. [Test Scenarios](#test-scenarios)
6. [Understanding Results](#understanding-results)
7. [Educational Use](#educational-use)
8. [Technical Implementation](#technical-implementation)
9. [Contributing](#contributing)

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)
- Standard Python libraries: `collections`, `time`

### Setup Instructions

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd page-replacement-tool
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

3. **Run the Application**
   ```bash
   python guiCompare.py
   ```

### File Structure
```
page-replacement-tool/
├── guiCompare.py          # Main GUI application
├── fifoSimul.py           # Original FIFO implementation
├── lruSimul.py            # Original LRU implementation
├── fifolruCompare.py      # Console comparison tool
└── README.md              # This documentation
```

## 🎯 Quick Start

1. **Launch the Application**
   ```bash
   python guiCompare.py
   ```

2. **Default Test Case**
   - Reference String: `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]`
   - Number of Frames: `3`

3. **Basic Usage**
   - Click "FIFO Simulation" to see FIFO algorithm in action
   - Click "LRU Simulation" to see LRU algorithm execution
   - Click "Comparison Results" for side-by-side analysis
   - Click "Comprehensive Analysis" for multi-scenario testing

## 🖥️ User Interface Guide

### Main Window
![Main Window Features]
- **Current Test Case Display**: Shows active reference string and frame count
- **Customize Test Case**: Input fields for custom reference strings and frames
- **Algorithm Buttons**: Access to different simulation modes
- **Update Test Case**: Apply custom inputs to all simulations

### FIFO Simulation Window
- **Test Case Header**: Current test parameters
- **Results Summary**: Total page faults, hit ratio, and references
- **Detailed Log Table**: Step-by-step execution with columns:
  - Step: Reference sequence number
  - Page: Current page being accessed
  - Action: "Page Fault" or "Hit"
  - Frames: Current state of memory frames
  - Replaced: Page that was replaced (if any)

### LRU Simulation Window
- **Similar Layout**: Same structure as FIFO with LRU-specific results
- **Color-coded Interface**: Orange theme for easy distinction
- **LRU-specific Logic**: Shows recency-based replacement decisions

### Comparison Results Window
- **Two-Column Layout**: 
  - Left: Comparison results and performance analysis
  - Right: Side-by-side execution comparison
- **Performance Metrics**: Direct comparison of both algorithms
- **Winner Determination**: Automatic identification of better performer
- **Detailed Analysis**: Explanation of why algorithms differ

### Comprehensive Analysis Window
- **Multiple Test Scenarios**: Automated testing across different patterns
- **Scrollable Results**: Complete analysis of all test cases
- **Summary Statistics**: Overall performance comparison
- **Pattern Analysis**: Results for different access patterns

## 🔍 Algorithm Details

### FIFO (First In, First Out)
```python
def fifo_page_replacement(reference_string, frames):
    # Uses deque with maxlen for automatic oldest page removal
    # Simple: Always replace the page that arrived first
    # Time Complexity: O(1) per reference
    # Space Complexity: O(frames)
```

**Characteristics:**
- ✅ Simple implementation
- ✅ Predictable behavior
- ❌ Doesn't consider page usage patterns
- ❌ Can suffer from Belady's anomaly

### LRU (Least Recently Used)
```python
def lru_page_replacement(reference_string, frames):
    # Maintains order of page usage
    # Always replaces the page not used for the longest time
    # Time Complexity: O(frames) per reference
    # Space Complexity: O(frames)
```

**Characteristics:**
- ✅ Considers temporal locality
- ✅ Generally better performance
- ❌ More complex implementation
- ❌ Higher overhead for tracking usage

## 📊 Test Scenarios

### Built-in Test Cases

1. **Demo - Original Test Case**
   - Reference: `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]`
   - Purpose: Standard comparison with mixed access pattern
   - Expected: LRU typically performs better with 3 frames

2. **Sequential Access Pattern**
   - Reference: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]`
   - Purpose: Tests behavior with sequential page access
   - Expected: Both algorithms struggle, FIFO may perform similarly

3. **Repeated Pattern**
   - Reference: `[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]`
   - Purpose: Tests algorithms with high locality
   - Expected: LRU should significantly outperform FIFO

4. **Random Access Pattern**
   - Reference: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]`
   - Purpose: Tests with unpredictable access patterns
   - Expected: Variable results depending on frame count

## 📈 Understanding Results

### Key Metrics

#### Page Faults
- **Definition**: Number of times a requested page is not in memory
- **Lower is Better**: Fewer page faults indicate better performance
- **Impact**: Each page fault requires expensive disk I/O operations

#### Hit Ratio
- **Formula**: `(Total References - Page Faults) / Total References × 100`
- **Higher is Better**: More hits mean better memory utilization
- **Typical Range**: 60-95% depending on algorithm and pattern

#### Execution Time
- **Purpose**: Measures algorithm overhead
- **Note**: In real systems, page fault cost dominates algorithm overhead

### Performance Analysis

#### When FIFO Performs Better
- Very small frame counts (1-2 frames)
- Random access patterns with no locality
- When simplicity and low overhead are priorities

#### When LRU Performs Better
- Moderate frame counts (3-6 frames)
- Access patterns with temporal locality
- Applications with working set behavior

#### When Both Perform Equally
- **Sufficient Memory**: When frames ≥ unique pages
- **Single Frame**: Both algorithms behave identically
- **Specific Patterns**: Some reference strings don't favor either approach

### Frame Count Effects

```
Frame Count Analysis:
├── 1 Frame: Both algorithms identical (every access is a fault after first load)
├── 2-3 Frames: Algorithms typically differ, LRU often better
├── 4-6 Frames: Performance gap may narrow
└── 8+ Frames: Often identical (sufficient memory for all unique pages)
```

## 🎓 Educational Use

### Learning Objectives
1. **Algorithm Understanding**: Visualize how page replacement works
2. **Performance Comparison**: See real differences between strategies
3. **Memory Management**: Understand impact of frame allocation
4. **System Design**: Learn trade-offs in algorithm selection

### Classroom Activities
1. **Prediction Exercise**: Have students predict which algorithm will perform better
2. **Custom Test Cases**: Create reference strings that favor specific algorithms
3. **Frame Size Analysis**: Explore how memory size affects performance
4. **Real-world Simulation**: Use patterns from actual applications

### Study Questions
1. Why do both algorithms perform the same with sufficient frames?
2. What reference patterns favor LRU over FIFO?
3. How does the working set size affect algorithm choice?
4. What are the trade-offs between simplicity and performance?

## ⚙️ Technical Implementation

### Architecture Overview
```
PageReplacementGUI (Main Class)
├── GUI Components (Tkinter)
├── Algorithm Implementations
│   ├── fifo_page_replacement()
│   └── lru_page_replacement()
├── Analysis Functions
│   ├── run_comparison()
│   └── comprehensive_analysis()
└── Utility Functions
    ├── create_test_info_header()
    └── update_test_case()
```

### Key Data Structures
- **FIFO**: `collections.deque(maxlen=frames)` for automatic FIFO behavior
- **LRU**: `list` with manual reordering for recency tracking
- **Logging**: Dictionaries storing step-by-step execution details

### GUI Framework
- **Tkinter**: Standard Python GUI library
- **ttk.Treeview**: For tabular data display
- **ScrolledText**: For comprehensive analysis results
- **Custom Layouts**: Responsive frames and professional styling

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Submit a pull request with detailed description

### Contribution Guidelines
- Follow PEP 8 Python style guidelines
- Add docstrings for new functions
- Test GUI functionality across different screen sizes
- Include test cases for new algorithms or features

### Future Enhancements
- [ ] Additional algorithms (Optimal, Clock, Second Chance)
- [ ] Export results to CSV/PDF
- [ ] Animated visualizations
- [ ] Performance benchmarking with larger datasets
- [ ] Save/load custom test scenarios
- [ ] Command-line interface option

## 📞 Support

### Common Issues

**Q: Application won't start**
- Ensure Python 3.6+ is installed
- Verify Tkinter is available: `python -c "import tkinter"`

**Q: Custom input not working**
- Use comma-separated integers for reference string
- Ensure frame count is a positive integer
- Click "Update Test Case" after making changes

**Q: Why do results seem identical sometimes?**
- With sufficient frames, no replacement occurs
- With 1 frame, both algorithms behave the same
- Some reference patterns don't reveal algorithm differences

### Getting Help
- Check the console for error messages
- Verify input format matches examples
- Review test case requirements in the GUI

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and distribute for academic and learning applications.

---

**Author**: Adrian  
**Course**: Operating Systems  
**Purpose**: Educational tool for understanding page replacement algorithms  
**Last Updated**: September 2025

---

*This tool is designed to help students and educators understand the practical differences between page replacement algorithms through interactive visualization and comprehensive analysis.*