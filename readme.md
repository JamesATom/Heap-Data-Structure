# Heap Implementation in Python

This repository contains a Python implementation of a Heap data structure that can function as either a Min-heap or a Max-heap.

## Overview

A Heap is a complete binary tree data structure that satisfies the heap property. This implementation provides:
- Support for both Min-heap and Max-heap
- Core heap operations (insert, remove, peek)
- Helper methods for maintaining heap property

## Features

- **Flexible Heap Type**: Create either a Min-heap or Max-heap using a boolean parameter
- **Core Operations**:
  - `insert`: Add a new element to the heap (O(log n))
  - `remove`: Remove and return the root element (O(log n))
  - `peek`: View the root element without removing it (O(1))
- **Helper Methods**:
  - `parent_index`: Get parent node index
  - `left_child_index`: Get left child node index
  - `right_child_index`: Get right child node index
  - `heapify_up`: Maintain heap property after insertion
  - `heapify_down`: Maintain heap property after removal

## Usage

```python
# Create a Max-heap
heap = Heap(is_min_heap=False)

# Insert elements
heap.insert(32)
heap.insert(35)
heap.insert(3)
heap.insert(23)

# Remove root element (returns the maximum value in Max-heap)
max_value = heap.remove()

# Peek at root element without removing it
root_value = heap.peek()
```

## Implementation Details

The heap is implemented using a Python list with the following properties:
- For any element at index `i`:
  - Parent is at index `(i-1)//2`
  - Left child is at index `2*i + 1`
  - Right child is at index `2*i + 2`

Time Complexities:
- Insert: O(log n)
- Remove: O(log n)
- Peek: O(1)
- Space Complexity: O(n)

## Example

```python
heap = Heap(is_min_heap=False)  # Create a Max-heap
heap.insert(32)
heap.insert(35)
heap.insert(3)
heap.insert(23)
heap.insert(27)
heap.insert(15)

# Elements will be removed in descending order (Max-heap)
while heap.heap:
    print(heap.remove())
```

## Note

This implementation uses a zero-based array to store the heap elements and includes complete error handling for edge cases such as empty heaps. The heap automatically resizes as elements are added or removed.