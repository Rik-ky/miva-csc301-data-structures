/**
 * MIVA Open University - Department of Data Science
 * Course: CSC 301 - Data Structures
 * Question 1: Implementation of a Custom Singly Linked List
 * 
 * Student: Richard John
 * Reg No: 2024/C/DSC/0548
 * Email: richard.john@miva.edu.ng
 * Repository: https://github.com/Rik-ky/miva-csc301-data-structures
 */

#include <iostream>

// Definition of a single node in the singly linked list
struct Node {
    int data;       // Data payload
    Node* next;     // Pointer to the next node in the sequence

    // Constructor to initialise a new node with data and null pointer
    Node(int value) : data(value), next(nullptr) {}
};

// SinglyLinkedList class encapsulating list operations and memory management
class SinglyLinkedList {
private:
    Node* head;     // Pointer to the first node in the list
    int size;       // Number of active nodes in the list

public:
    // Constructor initializes an empty list
    SinglyLinkedList() : head(nullptr), size(0) {}

    // Destructor to deallocate all nodes on the heap to prevent memory leaks
    ~SinglyLinkedList() {
        clear();
    }

    // Helper method to check if the list is empty
    bool isEmpty() const {
        return head == nullptr;
    }

    // Returns current number of nodes
    int getSize() const {
        return size;
    }

    // Deallocate all nodes in the list
    void clear() {
        Node* current = head;
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;    // Free heap memory for this node
        }
        head = nullptr;
        size = 0;
    }

    // 1. Add a node to the beginning of the list
    void insertAtBeginning(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
        size++;
        std::cout << "[SUCCESS] Inserted " << value << " at the beginning.\n";
    }

    // 2. Add a node to the end of the list
    void insertAtEnd(int value) {
        Node* newNode = new Node(value);
        if (isEmpty()) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = newNode;
        }
        size++;
        std::cout << "[SUCCESS] Inserted " << value << " at the end.\n";
    }

    // 3. Add a node at a specific position (1-based index)
    void insertAtPosition(int value, int position) {
        // Validation check for invalid positions
        if (position < 1 || position > size + 1) {
            std::cout << "[ERROR] Invalid position " << position 
                      << ". Valid range is 1 to " << (size + 1) << ".\n";
            return;
        }

        // Inserting at the beginning
        if (position == 1) {
            insertAtBeginning(value);
            return;
        }

        // Inserting in the middle or end
        Node* newNode = new Node(value);
        Node* current = head;
        for (int i = 1; i < position - 1; ++i) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
        size++;
        std::cout << "[SUCCESS] Inserted " << value << " at position " << position << ".\n";
    }

    // 4. Delete a node by its value
    bool deleteByValue(int value) {
        // Error handling for empty list
        if (isEmpty()) {
            std::cout << "[ERROR] Cannot delete from an empty list.\n";
            return false;
        }

        // Case 1: Target value is at the head node
        if (head->data == value) {
            Node* temp = head;
            head = head->next;
            delete temp;
            size--;
            std::cout << "[SUCCESS] Deleted node with value " << value << " (head node).\n";
            return true;
        }

        // Case 2: Target value is in subsequent nodes
        Node* current = head;
        while (current->next != nullptr && current->next->data != value) {
            current = current->next;
        }

        // Target value was not found in the list
        if (current->next == nullptr) {
            std::cout << "[ERROR] Value " << value << " not found in the list.\n";
            return false;
        }

        Node* nodeToDelete = current->next;
        current->next = nodeToDelete->next;
        delete nodeToDelete;
        size--;
        std::cout << "[SUCCESS] Deleted node with value " << value << ".\n";
        return true;
    }

    // 5. Delete a node by its 1-based position
    bool deleteByPosition(int position) {
        // Error handling: empty list check
        if (isEmpty()) {
            std::cout << "[ERROR] Cannot delete from an empty list.\n";
            return false;
        }

        // Error handling: position range check
        if (position < 1 || position > size) {
            std::cout << "[ERROR] Invalid position " << position 
                      << ". Valid range is 1 to " << size << ".\n";
            return false;
        }

        // Case 1: Deleting head node
        if (position == 1) {
            Node* temp = head;
            head = head->next;
            int deletedVal = temp->data;
            delete temp;
            size--;
            std::cout << "[SUCCESS] Deleted node at position 1 (value: " << deletedVal << ").\n";
            return true;
        }

        // Case 2: Deleting middle or tail node
        Node* current = head;
        for (int i = 1; i < position - 1; ++i) {
            current = current->next;
        }

        Node* nodeToDelete = current->next;
        int deletedVal = nodeToDelete->data;
        current->next = nodeToDelete->next;
        delete nodeToDelete;
        size--;
        std::cout << "[SUCCESS] Deleted node at position " << position 
                  << " (value: " << deletedVal << ").\n";
        return true;
    }

    // 6. Display all nodes currently in the linked list
    void display() const {
        if (isEmpty()) {
            std::cout << "List: [ EMPTY ] (Size: 0)\n";
            return;
        }

        std::cout << "List: [ ";
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data;
            if (current->next != nullptr) {
                std::cout << " -> ";
            }
            current = current->next;
        }
        std::cout << " -> NULL ] (Size: " << size << ")\n";
    }
};

// ==============================================================================
// TEST EXECUTION RUNNER WITH 3 DISTINCT DATASETS
// ==============================================================================
int main() {
    std::cout << "======================================================================\n";
    std::cout << " MIVA OPEN UNIVERSITY | CSC 301: DATA STRUCTURES TMA\n";
    std::cout << " Candidate: Richard John (Matric: 2024/C/DSC/0548)\n";
    std::cout << " Question 1: Custom Singly Linked List Verification\n";
    std::cout << "======================================================================\n\n";

    SinglyLinkedList list;

    // --------------------------------------------------------------------------
    // TEST SET 1: General Operations (Beginning, Middle, End, and Deletions)
    // --------------------------------------------------------------------------
    std::cout << ">>> TEST SET 1: Standard Insertions and Deletions\n";
    std::cout << "----------------------------------------------------------------------\n";
    list.display();

    // Adding nodes to end, beginning, and middle
    list.insertAtBeginning(30);
    list.insertAtBeginning(10);
    list.insertAtEnd(50);
    list.display();

    // Insert into middle (position 2)
    list.insertAtPosition(20, 2);
    list.display();

    // Insert into middle (position 4)
    list.insertAtPosition(40, 4);
    list.display();

    // Deleting nodes by value and position
    std::cout << "\n-- Performing Deletions on Test Set 1 --\n";
    list.deleteByValue(30);       // Delete middle value
    list.display();

    list.deleteByPosition(1);     // Delete head position
    list.display();

    list.deleteByPosition(3);     // Delete tail position
    list.display();

    // --------------------------------------------------------------------------
    // TEST SET 2: Edge Cases & Error Handling Robustness
    // --------------------------------------------------------------------------
    std::cout << "\n>>> TEST SET 2: Edge Cases and Defensive Error Handling\n";
    std::cout << "----------------------------------------------------------------------\n";
    list.clear();
    std::cout << "[INFO] List cleared for edge case validation.\n";
    list.display();

    // Test error: deleting from empty list
    std::cout << "\nAttempting deletion on empty list:\n";
    list.deleteByValue(99);
    list.deleteByPosition(1);

    // Test error: inserting at invalid out-of-bounds positions
    std::cout << "\nAttempting out-of-bounds insertions:\n";
    list.insertAtPosition(100, 0);     // Invalid index 0
    list.insertAtPosition(200, 5);     // Out of range for empty list

    // Single element list behavior
    std::cout << "\nOperating on a single-element list:\n";
    list.insertAtBeginning(77);
    list.display();

    // Delete non-existent value
    list.deleteByValue(999);

    // Successfully delete the only element
    list.deleteByPosition(1);
    list.display();

    // --------------------------------------------------------------------------
    // TEST SET 3: Sequential Student ID Records & Batch Processing
    // --------------------------------------------------------------------------
    std::cout << "\n>>> TEST SET 3: Practical Batch Processing (Student ID Records)\n";
    std::cout << "----------------------------------------------------------------------\n";
    int student_ids[] = {101, 102, 104, 105};
    for (int id : student_ids) {
        list.insertAtEnd(id);
    }
    list.display();

    // Insert missing record 103 at position 3
    std::cout << "\nInserting missing student ID 103 at position 3:\n";
    list.insertAtPosition(103, 3);
    list.display();

    // Insert priority transfer student at beginning
    std::cout << "\nInserting transfer student ID 100 at beginning:\n";
    list.insertAtBeginning(100);
    list.display();

    // Remove withdrawn student 104 by value
    std::cout << "\nRemoving withdrawn student ID 104 by value:\n";
    list.deleteByValue(104);
    list.display();

    // Final clean up and verification
    std::cout << "\nClearing all remaining records:\n";
    list.clear();
    list.display();

    std::cout << "\n[ALL TESTS COMPLETED SUCCESSFULLY]\n";
    return 0;
}
