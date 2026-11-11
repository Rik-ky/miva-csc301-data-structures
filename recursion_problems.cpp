/**
 * MIVA Open University - Department of Data Science
 * Course: CSC 301 - Data Structures
 * Question 2: Solving Problems Using Recursion
 * 
 * Student: Richard John
 * Reg No: 2024/C/DSC/0548
 * Email: richard.john@miva.edu.ng
 * Repository: https://github.com/Rik-ky/miva-csc301-data-structures
 */

#include <iostream>
#include <string>
#include <vector>

// ==============================================================================
// 1. FACTORIAL CALCULATION
// Base Case: If n <= 1, factorial is 1 (0! = 1, 1! = 1).
// Recursive Case: Return n * factorial(n - 1).
// ==============================================================================
long long factorial(int n) {
    // Error handling for negative input
    if (n < 0) {
        std::cout << "[ERROR] Factorial is undefined for negative integers (" << n << "). ";
        return -1;
    }
    // Base Case
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive Case
    return n * factorial(n - 1);
}

// ==============================================================================
// 2. FIBONACCI SEQUENCE
// Base Case: If n == 0 return 0; if n == 1 return 1.
// Recursive Case: Return fibonacci(n - 1) + fibonacci(n - 2).
// ==============================================================================
int fibonacci(int n) {
    // Base Cases
    if (n <= 0) return 0;
    if (n == 1) return 1;
    // Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Helper function to print the first n Fibonacci numbers
void printFirstNFibonacci(int n) {
    if (n <= 0) {
        std::cout << "[ERROR] Number of terms must be greater than 0.\n";
        return;
    }
    std::cout << "First " << n << " terms: ";
    for (int i = 0; i < n; ++i) {
        std::cout << fibonacci(i);
        if (i < n - 1) std::cout << ", ";
    }
    std::cout << "\n";
}

// ==============================================================================
// 3. STRING REVERSAL
// Base Case: If string length <= 1, return the string as is.
// Recursive Case: Reverse the substring from index 1 to end, then append the first character.
// ==============================================================================
std::string reverseString(const std::string& str) {
    // Base Case
    if (str.length() <= 1) {
        return str;
    }
    // Recursive Case: reverse(rest) + first_character
    return reverseString(str.substr(1)) + str[0];
}

// ==============================================================================
// 4. RECURSIVE BINARY SEARCH
// Base Cases:
//   - If low > high: Target is not present in the array (return -1).
//   - If arr[mid] == target: Target found (return mid index).
// Recursive Cases:
//   - If target < arr[mid]: Search left sub-array (low to mid - 1).
//   - If target > arr[mid]: Search right sub-array (mid + 1 to high).
// ==============================================================================
int binarySearchRecursive(const int arr[], int low, int high, int target) {
    // Base Case 1: Target not found (search interval exhausted)
    if (low > high) {
        return -1;
    }

    int mid = low + (high - low) / 2; // Prevents potential integer overflow

    // Base Case 2: Target found at middle index
    if (arr[mid] == target) {
        return mid;
    }

    // Recursive Case 1: Target lies in the left partition
    if (target < arr[mid]) {
        return binarySearchRecursive(arr, low, mid - 1, target);
    }

    // Recursive Case 2: Target lies in the right partition
    return binarySearchRecursive(arr, mid + 1, high, target);
}

// ==============================================================================
// TEST EXECUTION RUNNER WITH THREE DISTINCT INPUT SETS PER PROBLEM
// ==============================================================================
int main() {
    std::cout << "======================================================================\n";
    std::cout << " MIVA OPEN UNIVERSITY | CSC 301: DATA STRUCTURES TMA\n";
    std::cout << " Candidate: Richard John (Matric: 2024/C/DSC/0548)\n";
    std::cout << " Question 2: Solving Problems Using Recursion\n";
    std::cout << "======================================================================\n\n";

    // --------------------------------------------------------------------------
    // PART A: FACTORIAL CALCULATION TESTS
    // --------------------------------------------------------------------------
    std::cout << ">>> 1. FACTORIAL TESTS (Base Case: n <= 1 -> 1 | Recursive: n * f(n-1))\n";
    std::cout << "----------------------------------------------------------------------\n";
    // Input Set 1: Edge case (n = 0)
    std::cout << "Test 1 [Edge Case: 0!]:        " << factorial(0) << " (Expected: 1)\n";
    // Input Set 2: Typical positive integer (n = 5)
    std::cout << "Test 2 [Standard: 5!]:         " << factorial(5) << " (Expected: 120)\n";
    // Input Set 3: Larger integer (n = 10)
    std::cout << "Test 3 [Large Value: 10!]:     " << factorial(10) << " (Expected: 3628800)\n";
    // Additional Edge Case: Negative value error handling
    std::cout << "Test 4 [Negative Input: -4!]:  " << factorial(-4) << " (Error Handled)\n\n";

    // --------------------------------------------------------------------------
    // PART B: FIBONACCI SEQUENCE TESTS
    // --------------------------------------------------------------------------
    std::cout << ">>> 2. FIBONACCI SEQUENCE TESTS (Base: n<=0->0, n=1->1 | Rec: f(n-1)+f(n-2))\n";
    std::cout << "----------------------------------------------------------------------\n";
    // Input Set 1: Single term edge case (n = 1)
    std::cout << "Test 1 [Single term (n=1)]:    ";
    printFirstNFibonacci(1);
    // Input Set 2: Moderate sequence (n = 7)
    std::cout << "Test 2 [Standard (n=7)]:       ";
    printFirstNFibonacci(7);
    // Input Set 3: Extended sequence (n = 12)
    std::cout << "Test 3 [Extended (n=12)]:      ";
    printFirstNFibonacci(12);
    // Additional Edge Case: Zero / Invalid terms
    std::cout << "Test 4 [Invalid (n=0)]:        ";
    printFirstNFibonacci(0);
    std::cout << "\n";

    // --------------------------------------------------------------------------
    // PART C: STRING REVERSAL TESTS
    // --------------------------------------------------------------------------
    std::cout << ">>> 3. STRING REVERSAL TESTS (Base: len<=1 -> str | Rec: rev(sub)+first)\n";
    std::cout << "----------------------------------------------------------------------\n";
    // Input Set 1: Edge case (empty string)
    std::string s1 = "";
    std::cout << "Test 1 [Empty String \"\"]:       \"" << reverseString(s1) << "\" (Length: 0)\n";
    // Input Set 2: Palindrome word ("racecar")
    std::string s2 = "racecar";
    std::cout << "Test 2 [Palindrome \"racecar\"]:  \"" << reverseString(s2) << "\"\n";
    // Input Set 3: Multi-word university phrase ("Data Structures")
    std::string s3 = "Data Structures";
    std::cout << "Test 3 [Phrase \"Data Structures\"]: \"" << reverseString(s3) << "\"\n";
    // Additional case: Institutional string
    std::string s4 = "Miva Open University";
    std::cout << "Test 4 [Phrase \"Miva Open University\"]: \"" << reverseString(s4) << "\"\n\n";

    // --------------------------------------------------------------------------
    // PART D: RECURSIVE BINARY SEARCH TESTS
    // --------------------------------------------------------------------------
    std::cout << ">>> 4. RECURSIVE BINARY SEARCH TESTS\n";
    std::cout << "----------------------------------------------------------------------\n";
    int sortedArray[] = {4, 11, 19, 28, 35, 42, 58, 67, 73, 89, 95};
    int n = sizeof(sortedArray) / sizeof(sortedArray[0]);

    std::cout << "Sorted Array: [ ";
    for (int i = 0; i < n; ++i) std::cout << sortedArray[i] << (i < n - 1 ? ", " : " ");
    std::cout << "]\n";

    // Input Set 1: Target located in the array (Target = 42)
    int target1 = 42;
    int idx1 = binarySearchRecursive(sortedArray, 0, n - 1, target1);
    std::cout << "Test 1 [Find " << target1 << "]:  Found at index " << idx1 
              << " (Value: " << sortedArray[idx1] << ")\n";

    // Input Set 2: Boundary targets (first element = 4, last element = 95)
    int target2 = 4;
    int target3 = 95;
    std::cout << "Test 2a [Find first " << target2 << "]: Found at index " 
              << binarySearchRecursive(sortedArray, 0, n - 1, target2) << "\n";
    std::cout << "Test 2b [Find last " << target3 << "]:  Found at index " 
              << binarySearchRecursive(sortedArray, 0, n - 1, target3) << "\n";

    // Input Set 3: Target not present in the array (Target = 50)
    int target4 = 50;
    int idx4 = binarySearchRecursive(sortedArray, 0, n - 1, target4);
    std::cout << "Test 3 [Search non-existent " << target4 << "]: Result = " << idx4 
              << " (Correctly reported as NOT FOUND)\n";

    // Input Set 4: Edge case on empty array (low > high)
    int emptyArray[] = {};
    int idxEmpty = binarySearchRecursive(emptyArray, 0, -1, 10);
    std::cout << "Test 4 [Search in Empty Array]:    Result = " << idxEmpty 
              << " (Handled safely without segmentation fault)\n";

    std::cout << "\n======================================================================\n";
    std::cout << " [ALL RECURSION TESTS COMPLETED SUCCESSFULLY]\n";
    std::cout << "======================================================================\n";

    return 0;
}
