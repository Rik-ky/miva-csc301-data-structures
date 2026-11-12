import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# ==============================================================================
# NUMBERED CANVAS: EXACT MIVA HEADER BANNER + FOOTER
# ==============================================================================
class MivaNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(MivaNumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(MivaNumberedCanvas, self).showPage()
        super(MivaNumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        w, h = A4
        
        # 1. Top Header Banner
        banner_img = '/Users/rik/.gemini/antigravity/scratch/miva_csc301_lab/miva_exact_top_banner.png'
        banner_h = 68.05
        if os.path.exists(banner_img):
            self.drawImage(banner_img, 0, h - banner_h, width=w, height=banner_h, mask='auto')
        
        # 2. Header Text
        self.setFont("Helvetica-Bold", 14.5)
        self.setFillColor(colors.white)
        self.drawString(38, h - 31, "Tutor-Marked  Assessment")
        
        self.setFont("Helvetica", 10.5)
        self.setFillColor(colors.HexColor("#dbeafe"))
        self.drawString(38, h - 47, "CSC 301 - Data Structures")

        # 3. Footer Line & Copyright
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(38, 28, w - 38, 28)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(38, 16, "© Copyright 2024 MIVA Open University All Rights Reserved")
        
        # Page Number
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(w - 38, 16, page_str)
        
        self.restoreState()


def generate_csc301_report():
    pdf_path = "/Users/rik/.gemini/antigravity/scratch/miva_csc301_lab/MIVA_CSC301_TMA_Richard_John_2024_C_DSC_0548.pdf"
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=38,
        rightMargin=38,
        topMargin=76,
        bottomMargin=38
    )

    styles = getSampleStyleSheet()

    # Typography Styles
    title_h1 = ParagraphStyle(
        'ExactH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#09304f"),
        spaceBefore=8,
        spaceAfter=6,
        keepWithNext=True
    )

    title_h2 = ParagraphStyle(
        'ExactH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#09304f"),
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True
    )

    body = ParagraphStyle(
        'ExactBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=7
    )

    bullet_p = ParagraphStyle(
        'ExactBullet',
        parent=body,
        leftIndent=16,
        bulletIndent=6,
        spaceAfter=6
    )

    code_p = ParagraphStyle(
        'ExactCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.0,
        leading=8.7,
        textColor=colors.HexColor("#0f172a")
    )

    output_p = ParagraphStyle(
        'ExactOutput',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.8,
        leading=8.3,
        textColor=colors.HexColor("#0f172a")
    )

    tbl_header = ParagraphStyle(
        'TblH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.white,
        alignment=1
    )

    tbl_cell = ParagraphStyle(
        'TblC',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.0,
        leading=12.5,
        textColor=colors.HexColor("#1e293b")
    )

    story = []

    # ==============================================================================
    # PAGE 1: STUDENT DETAILS, GITHUB REPOSITORY & QUESTION 1 OVERVIEW & MEMORY MGMT
    # ==============================================================================
    student_info_data = [
        [
            Paragraph("<b>Candidate Name:</b>", body), Paragraph("Richard John", body),
            Paragraph("<b>Reg / Matric No:</b>", body), Paragraph("<b>2024/C/DSC/0548</b>", body)
        ],
        [
            Paragraph("<b>Department:</b>", body), Paragraph("Data Science", body),
            Paragraph("<b>Institutional Email:</b>", body), Paragraph("richard.john@miva.edu.ng", body)
        ]
    ]
    t_student = Table(student_info_data, colWidths=[1.5*72, 1.7*72, 1.6*72, 2.4*72])
    t_student.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_student)
    story.append(Spacer(1, 8))

    git_html = (
        "<b>Source Code & Verification Repository:</b> "
        "<font color='#1d4ed8'><u>https://github.com/Rik-ky/miva-csc301-data-structures</u></font>"
    )
    t_git = Table([[Paragraph(git_html, body)]], colWidths=[7.2 * 72])
    t_git.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#eff6ff")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#93c5fd")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_git)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Question 1: Implementing a Custom Singly Linked List", title_h1))
    
    q1_desc = (
        "<b>Objective & Implementation Scope:</b> A robust, object-oriented C++ program was designed to implement "
        "a custom singly linked list from first principles. The implementation features modular methods to add nodes at the beginning, "
        "middle (by 1-based index), and end of the list, delete nodes by value or by position, display all nodes, "
        "and enforce comprehensive error handling for edge conditions including deletions on empty lists and out-of-bounds positions."
    )
    story.append(Paragraph(q1_desc, body))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Memory Management Analysis:", title_h2))

    memory_explanation = (
        "In a C++ singly linked list, memory is dynamically partitioned between the heap and the call stack. "
        "When an insertion is invoked, the <code>new</code> operator dynamically allocates a <code>Node</code> structure "
        "on the free store (heap), reserving memory for its integer data payload and a pointer to the next node (<code>Node* next</code>). "
        "The stack maintains only lightweight references, primarily the <code>head</code> pointer and transient traversal variables. "
        "Unlike contiguous arrays, linked list nodes reside at non-contiguous heap addresses, interconnected solely by forward pointers. "
        "During deletion, target nodes are unlinked by updating the preceding node's <code>next</code> pointer, and their heap memory is "
        "explicitly freed using <code>delete</code> to prevent memory leaks and dangling pointers. "
        "Finally, the class destructor iterates through all remaining nodes, deallocating each sequentially in O(n) time to ensure "
        "complete resource reclamation."
    )
    story.append(Paragraph(memory_explanation, body))

    story.append(PageBreak())

    # ==============================================================================
    # PAGE 2: QUESTION 1 C++ SOURCE CODE (PART 1 - STRUCT & INSERTIONS)
    # ==============================================================================
    story.append(Paragraph("Question 1: C++ Implementation (Node Struct & Insertions)", title_h1))
    story.append(Paragraph("The listing below presents the node structure and insertion routines at the beginning, end, and middle of the linked list:", body))
    story.append(Spacer(1, 4))

    q1_code_p1 = """// ==============================================================================
// Question 1: Custom Singly Linked List (Node Definition & Insertions)
// Course: CSC 301 - Data Structures | Miva Open University
// Candidate: Richard John (2024/C/DSC/0548) | richard.john@miva.edu.ng
// ==============================================================================
#include <iostream>

struct Node {
    int data;       // Node integer payload
    Node* next;     // Forward pointer to subsequent node
    Node(int value) : data(value), next(nullptr) {}
};

class SinglyLinkedList {
private:
    Node* head;     // Pointer to the first node
    int size;       // Number of active nodes

public:
    SinglyLinkedList() : head(nullptr), size(0) {}
    ~SinglyLinkedList() { clear(); }

    bool isEmpty() const { return head == nullptr; }
    int getSize() const { return size; }

    // 1. Add a node to the beginning of the list
    void insertAtBeginning(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
        size++;
        std::cout << "[SUCCESS] Inserted " << value << " at the beginning.\\n";
    }

    // 2. Add a node to the end of the list
    void insertAtEnd(int value) {
        Node* newNode = new Node(value);
        if (isEmpty()) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next != nullptr) current = current->next;
            current->next = newNode;
        }
        size++;
        std::cout << "[SUCCESS] Inserted " << value << " at the end.\\n";
    }

    // 3. Add a node at a specific position (1-based index)
    void insertAtPosition(int value, int position) {
        if (position < 1 || position > size + 1) {
            std::cout << "[ERROR] Invalid position " << position 
                      << ". Valid range is 1 to " << (size + 1) << ".\\n";
            return;
        }
        if (position == 1) {
            insertAtBeginning(value);
            return;
        }
        Node* newNode = new Node(value);
        Node* current = head;
        for (int i = 1; i < position - 1; ++i) current = current->next;
        newNode->next = current->next;
        current->next = newNode;
        size++;
        std::cout << "[SUCCESS] Inserted " << value << " at position " << position << ".\\n";
    }
"""
    code_t1 = Table([[Preformatted(q1_code_p1, code_p)]], colWidths=[7.2 * 72])
    code_t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(code_t1)
    story.append(PageBreak())

    # ==============================================================================
    # PAGE 3: QUESTION 1 C++ SOURCE CODE (PART 2 - DELETIONS & TRAVERSAL)
    # ==============================================================================
    story.append(Paragraph("Question 1: C++ Implementation (Deletions & Traversal)", title_h1))
    story.append(Paragraph("The listing below implements node deletions by value and position, defensive error handling, traversal display, and heap deallocation:", body))
    story.append(Spacer(1, 4))

    q1_code_p2 = """    // 4. Delete a node by value with defensive error handling
    bool deleteByValue(int value) {
        if (isEmpty()) {
            std::cout << "[ERROR] Cannot delete from an empty list.\\n";
            return false;
        }
        if (head->data == value) {
            Node* temp = head; head = head->next; delete temp; size--;
            std::cout << "[SUCCESS] Deleted node with value " << value << " (head node).\\n";
            return true;
        }
        Node* current = head;
        while (current->next != nullptr && current->next->data != value) current = current->next;
        if (current->next == nullptr) {
            std::cout << "[ERROR] Value " << value << " not found in the list.\\n";
            return false;
        }
        Node* nodeToDelete = current->next;
        current->next = nodeToDelete->next;
        delete nodeToDelete;
        size--;
        std::cout << "[SUCCESS] Deleted node with value " << value << ".\\n";
        return true;
    }

    // 5. Delete a node by position (1-based index)
    bool deleteByPosition(int position) {
        if (isEmpty()) {
            std::cout << "[ERROR] Cannot delete from an empty list.\\n";
            return false;
        }
        if (position < 1 || position > size) {
            std::cout << "[ERROR] Invalid position " << position << ". Valid range is 1 to " << size << ".\\n";
            return false;
        }
        if (position == 1) {
            Node* temp = head; head = head->next; int val = temp->data; delete temp; size--;
            std::cout << "[SUCCESS] Deleted node at position 1 (value: " << val << ").\\n";
            return true;
        }
        Node* current = head;
        for (int i = 1; i < position - 1; ++i) current = current->next;
        Node* nodeToDelete = current->next;
        int val = nodeToDelete->data;
        current->next = nodeToDelete->next;
        delete nodeToDelete;
        size--;
        std::cout << "[SUCCESS] Deleted node at position " << position << " (value: " << val << ").\\n";
        return true;
    }

    // 6. Display all nodes in the list
    void display() const {
        if (isEmpty()) { std::cout << "List: [ EMPTY ] (Size: 0)\\n"; return; }
        std::cout << "List: [ ";
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data;
            if (current->next != nullptr) std::cout << " -> ";
            current = current->next;
        }
        std::cout << " -> NULL ] (Size: " << size << ")\\n";
    }

    // Deallocate all nodes on the heap
    void clear() {
        Node* current = head;
        while (current != nullptr) {
            Node* temp = current; current = current->next; delete temp;
        }
        head = nullptr; size = 0;
    }
};
"""
    code_t2 = Table([[Preformatted(q1_code_p2, code_p)]], colWidths=[7.2 * 72])
    code_t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(code_t2)
    story.append(PageBreak())

    # ==============================================================================
    # PAGE 4: QUESTION 1 VERIFIED EXECUTION OUTPUTS (3 TEST DATASETS)
    # ==============================================================================
    story.append(Paragraph("Question 1 Verified Execution Outputs", title_h1))
    story.append(Paragraph("The program was tested with three distinct datasets: (1) Standard operations, (2) Edge cases and error handling, and (3) Practical student ID batch processing:", body))
    story.append(Spacer(1, 4))

    with open('/Users/rik/.gemini/antigravity/scratch/miva_csc301_lab/q1_output.txt', 'r') as f:
        q1_terminal_output = f.read().strip()

    t_out1 = Table([[Preformatted(q1_terminal_output, output_p)]], colWidths=[7.2 * 72])
    t_out1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_out1)
    story.append(PageBreak())

    # ==============================================================================
    # PAGE 5: QUESTION 2 OVERVIEW, RECURSION TABLE & COMPARATIVE SUMMARY
    # ==============================================================================
    story.append(Paragraph("Question 2: Solving Problems Using Recursion", title_h1))
    
    q2_intro = (
        "<b>Objective & Recursive Implementations:</b> A modular C++ program was implemented to solve four classic algorithmic "
        "problems using recursion: (1) Factorial calculation, (2) Fibonacci sequence generation, (3) In-place/substring String Reversal, "
        "and (4) Recursive Binary Search on sorted arrays. Each function defines rigorous base and recursive cases."
    )
    story.append(Paragraph(q2_intro, body))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Base Case and Recursive Case Analysis:", title_h2))

    cases_data = [
        [Paragraph("Function", tbl_header), Paragraph("Base Case", tbl_header), Paragraph("Recursive Case", tbl_header), Paragraph("Time / Space Complexity", tbl_header)],
        [Paragraph("Factorial", tbl_cell), Paragraph("<code>n &lt;= 1</code>: returns 1", tbl_cell), Paragraph("<code>n * factorial(n - 1)</code>", tbl_cell), Paragraph("Time: O(n)<br/>Space: O(n) stack", tbl_cell)],
        [Paragraph("Fibonacci", tbl_cell), Paragraph("<code>n &lt;= 0</code>: 0<br/><code>n == 1</code>: 1", tbl_cell), Paragraph("<code>fib(n - 1) + fib(n - 2)</code>", tbl_cell), Paragraph("Time: O(2<sup>n</sup>)<br/>Space: O(n) stack", tbl_cell)],
        [Paragraph("String Reversal", tbl_cell), Paragraph("<code>str.length() &lt;= 1</code>:<br/>return str", tbl_cell), Paragraph("<code>reverse(str.substr(1)) + str[0]</code>", tbl_cell), Paragraph("Time: O(n<sup>2</sup>) (substr)<br/>Space: O(n) stack", tbl_cell)],
        [Paragraph("Binary Search", tbl_cell), Paragraph("<code>low &gt; high</code>: -1<br/><code>arr[mid] == key</code>: mid", tbl_cell), Paragraph("<code>key &lt; arr[mid]</code>: left<br/><code>key &gt; arr[mid]</code>: right", tbl_cell), Paragraph("Time: O(log n)<br/>Space: O(log n) stack", tbl_cell)],
    ]
    t_cases = Table(cases_data, colWidths=[1.3*72, 1.8*72, 2.3*72, 1.8*72])
    t_cases.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#09304f")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_cases)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Recursion vs. Iteration Comparative Summary:", title_h2))

    recursion_summary = (
        "Recursion and iteration are fundamental computational approaches for repetitive problem solving. "
        "In recursion, a function calls itself to resolve progressively smaller sub-problems until reaching a terminating base case. "
        "Each recursive invocation pushes an activation record onto the call stack, allocating memory for parameters, local variables, "
        "and return addresses. Consequently, recursion incurs O(n) auxiliary stack space, runtime function-call overhead, "
        "and vulnerability to stack overflow if recursion depth is unbounded. "
        "Conversely, iteration relies on looping constructs managed by loop variables residing in constant stack space (O(1) memory), "
        "providing superior execution speed and cache locality. "
        "However, recursion is strongly preferred in problems with self-similar, branching, or divide-and-conquer structures where "
        "iterative equivalents require complex manual stack management. "
        "Primary scenarios favoring recursion include hierarchical data structures (binary tree traversals, trie operations), "
        "graph depth-first search (DFS), divide-and-conquer paradigms (Merge Sort, Quick Sort, Binary Search), "
        "and backtracking algorithms (N-Queens, maze traversal), where recursive formulations deliver unmatched mathematical clarity and maintainability."
    )
    story.append(Paragraph(recursion_summary, body))

    story.append(PageBreak())

    # ==============================================================================
    # PAGE 6: QUESTION 2 C++ SOURCE CODE (PART 1 - FACTORIAL, FIBONACCI, STRING)
    # ==============================================================================
    story.append(Paragraph("Question 2: C++ Implementation (Factorial, Fibonacci, String)", title_h1))
    story.append(Paragraph("The listing below implements the recursive functions for factorial calculation, Fibonacci sequence generation, and string reversal:", body))
    story.append(Spacer(1, 4))

    q2_code_p1 = """// ==============================================================================
// Question 2: Solving Problems Using Recursion (Part 1)
// Course: CSC 301 - Data Structures | Miva Open University
// Candidate: Richard John (2024/C/DSC/0548) | richard.john@miva.edu.ng
// ==============================================================================
#include <iostream>
#include <string>

// 1. FACTORIAL CALCULATION
// Base Case: n <= 1 returns 1 (handles 0! = 1, 1! = 1)
// Recursive Case: n * factorial(n - 1)
long long factorial(int n) {
    if (n < 0) {
        std::cout << "[ERROR] Factorial is undefined for negative integers (" << n << "). ";
        return -1;
    }
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// 2. FIBONACCI SEQUENCE
// Base Case: n <= 0 returns 0; n == 1 returns 1
// Recursive Case: fibonacci(n - 1) + fibonacci(n - 2)
int fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

void printFirstNFibonacci(int n) {
    if (n <= 0) {
        std::cout << "[ERROR] Number of terms must be greater than 0.\\n";
        return;
    }
    std::cout << "First " << n << " terms: ";
    for (int i = 0; i < n; ++i) {
        std::cout << fibonacci(i);
        if (i < n - 1) std::cout << ", ";
    }
    std::cout << "\\n";
}

// 3. STRING REVERSAL
// Base Case: String length <= 1 returns string as is
// Recursive Case: reverse(rest of string) + first character
std::string reverseString(const std::string& str) {
    if (str.length() <= 1) {
        return str;
    }
    return reverseString(str.substr(1)) + str[0];
}
"""
    code_t3 = Table([[Preformatted(q2_code_p1, code_p)]], colWidths=[7.2 * 72])
    code_t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(code_t3)
    story.append(PageBreak())

    # ==============================================================================
    # PAGE 7: QUESTION 2 C++ SOURCE CODE (PART 2 - BINARY SEARCH & TEST HARNESS)
    # ==============================================================================
    story.append(Paragraph("Question 2: C++ Implementation (Binary Search & Runner)", title_h1))
    story.append(Paragraph("The listing below implements recursive binary search with mid-overflow prevention and the multi-input test harness:", body))
    story.append(Spacer(1, 4))

    q2_code_p2 = """// 4. RECURSIVE BINARY SEARCH
// Base Cases: low > high (not found: -1) | arr[mid] == target (found: mid)
// Recursive Cases: target < arr[mid] (search left) | target > arr[mid] (search right)
int binarySearchRecursive(const int arr[], int low, int high, int target) {
    if (low > high) {
        return -1; // Base case: element not present
    }
    int mid = low + (high - low) / 2; // Prevents overflow
    if (arr[mid] == target) {
        return mid; // Base case: target located
    }
    if (target < arr[mid]) {
        return binarySearchRecursive(arr, low, mid - 1, target);
    }
    return binarySearchRecursive(arr, mid + 1, high, target);
}

int main() {
    // Part A: Factorial Tests
    std::cout << ">>> 1. FACTORIAL TESTS\\n";
    std::cout << "Test 1 [0!]:        " << factorial(0) << " (Expected: 1)\\n";
    std::cout << "Test 2 [5!]:        " << factorial(5) << " (Expected: 120)\\n";
    std::cout << "Test 3 [10!]:       " << factorial(10) << " (Expected: 3628800)\\n";
    std::cout << "Test 4 [-4!]:       " << factorial(-4) << " (Handled)\\n\\n";

    // Part B: Fibonacci Tests
    std::cout << ">>> 2. FIBONACCI TESTS\\n";
    std::cout << "Test 1 [n=1]:  "; printFirstNFibonacci(1);
    std::cout << "Test 2 [n=7]:  "; printFirstNFibonacci(7);
    std::cout << "Test 3 [n=12]: "; printFirstNFibonacci(12);
    std::cout << "Test 4 [n=0]:  "; printFirstNFibonacci(0);
    std::cout << "\\n";

    // Part C: String Reversal Tests
    std::cout << ">>> 3. STRING REVERSAL TESTS\\n";
    std::cout << "Test 1 [\\\"\\\"]:       \\\"" << reverseString("") << "\\\"\\n";
    std::cout << "Test 2 [\\\"racecar\\\"]:  \\\"" << reverseString("racecar") << "\\\"\\n";
    std::cout << "Test 3 [\\\"Data Structures\\\"]: \\\"" << reverseString("Data Structures") << "\\\"\\n\\n";

    // Part D: Binary Search Tests
    std::cout << ">>> 4. BINARY SEARCH TESTS\\n";
    int sortedArray[] = {4, 11, 19, 28, 35, 42, 58, 67, 73, 89, 95};
    int n = sizeof(sortedArray) / sizeof(sortedArray[0]);
    std::cout << "Test 1 [Find 42]:  Index " << binarySearchRecursive(sortedArray, 0, n - 1, 42) << "\\n";
    std::cout << "Test 2 [Find 4]:   Index " << binarySearchRecursive(sortedArray, 0, n - 1, 4) << "\\n";
    std::cout << "Test 3 [Find 50]:  Result " << binarySearchRecursive(sortedArray, 0, n - 1, 50) << " (Not found)\\n";
    int emptyArray[] = {};
    std::cout << "Test 4 [Empty]:    Result " << binarySearchRecursive(emptyArray, 0, -1, 10) << " (Safe)\\n";
    return 0;
}
"""
    code_t4 = Table([[Preformatted(q2_code_p2, code_p)]], colWidths=[7.2 * 72])
    code_t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(code_t4)
    story.append(PageBreak())

    # ==============================================================================
    # PAGE 8: QUESTION 2 VERIFIED EXECUTION OUTPUTS & EDGE CASE LOGS
    # ==============================================================================
    story.append(Paragraph("Question 2 Verified Execution Outputs", title_h1))
    story.append(Paragraph("The terminal capture below validates all four recursive problems across standard inputs and boundary edge cases (0!, negative inputs, empty strings, and empty array binary searches):", body))
    story.append(Spacer(1, 4))

    with open('/Users/rik/.gemini/antigravity/scratch/miva_csc301_lab/q2_output.txt', 'r') as f:
        q2_terminal_output = f.read().strip()

    t_out2 = Table([[Preformatted(q2_terminal_output, output_p)]], colWidths=[7.2 * 72])
    t_out2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_out2)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Submission Conclusion:</b> All requirements for CSC 301 have been implemented with verified numerical "
        "and logical precision. Complete source code and output logs are published in the GitHub repository: "
        "<font color='#1d4ed8'><u>https://github.com/Rik-ky/miva-csc301-data-structures</u></font>.",
        body
    ))

    doc.build(story, canvasmaker=MivaNumberedCanvas)
    print(f"CSC 301 Assessment Report successfully compiled at: {pdf_path}")


if __name__ == '__main__':
    generate_csc301_report()
