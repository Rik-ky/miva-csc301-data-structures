# CSC 301: Data Structures - Tutor-Marked Assessment

**Institution:** Miva Open University  
**Department:** Data Science  
**Course Code:** CSC 301  
**Candidate Name:** Richard John  
**Matriculation Number:** 2024/C/DSC/0548  
**Institutional Email:** richard.john@miva.edu.ng  

---

## Project Overview

This repository contains the complete C++ implementations, test harnesses, and execution logs for the CSC 301 (Data Structures) Tutor-Marked Assessment.

### Question 1: Implementing a Custom Singly Linked List
A custom object-oriented singly linked list implemented in C++ without external container libraries:
- **Node Structure:** Integer payload and raw forward pointer (`Node* next`).
- **Insertion Operations:**
  - `insertAtBeginning(int value)`: `O(1)` prepend operation.
  - `insertAtEnd(int value)`: `O(n)` append operation.
  - `insertAtPosition(int value, int position)`: 1-based index insertion with boundary checks.
- **Deletion Operations:**
  - `deleteByValue(int value)`: Searches and deletes target node, handling head, intermediate, and non-existent values.
  - `deleteByPosition(int position)`: Deletes node at 1-based index with boundary validation.
- **Traversal & Inspection:**
  - `display()`: Formatted traversal displaying all node values and current size.
  - `isEmpty()`, `getSize()`.
- **Memory Management:** Dynamic allocation via `new`, explicit deallocation via `delete`, and automatic heap reclamation in the destructor `~SinglyLinkedList()`.
- **Test Datasets:**
  1. Standard sequential insertions and deletions.
  2. Edge cases and defensive error handling (empty list deletion, out-of-bounds index, non-existent value).
  3. Practical batch processing simulating student ID records.

### Question 2: Solving Problems Using Recursion
Four classic computational problems implemented using recursion in C++:
1. **Factorial Calculation:** Recursive implementation (`n!`) with base case `n <= 1` returning `1`, negative input validation, and 64-bit integer support.
2. **Fibonacci Sequence:** Recursive generation of the first `n` terms with base cases `n <= 0 -> 0` and `n == 1 -> 1`.
3. **String Reversal:** Recursive string reversal using substring decomposition with base case `length <= 1`.
4. **Recursive Binary Search:** Divide-and-conquer search on sorted arrays featuring overflow-safe midpoint calculation (`low + (high - low) / 2`) and base cases for element found and subarray exhaustion.
- **Test Cases:** Evaluated against 3+ distinct inputs per function plus boundary edge cases (`0!`, negative inputs, empty strings, palindromes, search on empty arrays, missing elements).

---

## Directory Structure

```text
├── custom_linked_list.cpp                         # C++ source code for Question 1
├── recursion_problems.cpp                         # C++ source code for Question 2
├── q1_output.txt                                  # Verified execution log for Question 1
├── q2_output.txt                                  # Verified execution log for Question 2
├── generate_report.py                             # Automated PDF assessment generator
├── miva_exact_top_banner.png                      # Miva assessment header template asset
├── MIVA_CSC301_TMA_Richard_John_2024_C_DSC_0548.pdf # Final compiled 8-page submission document
├── .gitignore                                     # Git build and binary artifact exclusions
└── README.md                                      # Documentation and build instructions
```

---

## Compilation & Execution

Both programs use standard C++17 and compile with any standard C++ compiler (`clang++` or `g++`).

### Question 1: Singly Linked List
```bash
# Compile
clang++ -std=c++17 -Wall -Wextra custom_linked_list.cpp -o custom_linked_list

# Execute
./custom_linked_list
```

### Question 2: Recursion Algorithms
```bash
# Compile
clang++ -std=c++17 -Wall -Wextra recursion_problems.cpp -o recursion_problems

# Execute
./recursion_problems
```

### Rebuilding the PDF Assessment Report
```bash
# Ensure Python 3.10+ and reportlab are installed
pip install reportlab pypdf

# Generate PDF
python3 generate_report.py
```
The script builds `MIVA_CSC301_TMA_Richard_John_2024_C_DSC_0548.pdf` matching the official Miva assessment document format.

---

## License & Academic Integrity

This coursework is an individual submission prepared by Richard John (Matric: 2024/C/DSC/0548) for CSC 301 at Miva Open University.
