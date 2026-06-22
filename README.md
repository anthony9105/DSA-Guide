<h1 align="center" style="font-size: 40px">Anthony's Data Structures and Algorithm's Guide</h1>

<p align="center">
  Created by <strong>Anthony Liscio</strong><br/>
  <a href="https://github.com/anthony9105">@anthony9105 on GitHub</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-blue" style="margin-right: 25px;" alt="Python"/>
  <img src="https://img.shields.io/badge/C++-lightblue" style="margin-right: 25px;" alt="C++"/>
  <img src="https://img.shields.io/badge/Java-red" style="margin-right: 25px;" alt="Java"/>
  <img src="https://img.shields.io/badge/TypeScript-purple" style="margin-right: 25px;" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/C%23-239120" style="margin-right: 25px;" alt="C#"/>
  <img src="https://img.shields.io/github/license/anthony9105/DSA-Guide?color=%23FFD700" alt="License" style="margin-right: 25px;"/>
  <img src="https://img.shields.io/badge/Maintainer-Anthony-green" alt="Maintainer"/>
</p>

## Contents
- [**Data Structures \& When To Use Them**](#data-structures--when-to-use-them)
  - [**Arrays/Lists**](#arrayslists)
  - [**Linked-Lists**](#linked-lists)
    - [**Pointers**](#pointers)
  - [**Hash-Maps**](#hash-maps)
  - [**Hash-Sets**](#hash-sets)
  - [**Stacks**](#stacks)
  - [**Queues**](#queues)
  - [**Trees**](#trees)
  - [**Graphs**](#graphs)
  - [**Heaps**](#heaps)
- [**Leetcode Problems and Solutions**](./Leetcode%20Problems/README.md)
- [**Key Algorithms**](./algorithms.md)

<br/>
<br/>

# **Data Structures & When To Use Them**

## **Arrays/Lists**
A collection of elements stored in **contiguous memory**, accessible by index.  
> <sub>*Contiguous memory:* elements stored back-to-back with no gaps (e.g. `arr[0]` at address `1000`,
> `arr[1]` at `1004`, `arr[2]` at `1008`). This is what makes index-based reads `O(1)` and insert/delete
> at an index `O(n)`.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Fast reads | Slow inserts and deletes (except at the end) |

| Read | Insert (at index) | Insert (at end) | Delete (at index) | Delete (at end) |
|------|--------|--------  |----             |----               |
|`O(1)`|`O(n)`  |`O(1)` amortized |`O(n)`|`O(1)`|  

<br/>

**When to use:** When you need fast random access by index and don't need to frequently add/remove elements from the middle/front (e.g. lookup tables, fixed-size data, or building up a result by only appending).

<details>
<summary>Python</summary>

```python
arr: list[int] = [1, 2, 3, 4, 5]

# Read - O(1)
val: int = arr[2] # 3

# Insert at end - O(1) amortized
arr.append(99) # [1, 2, 3, 4, 5, 99]

# Insert at index - O(n), shifts elements after index
arr.insert(2, 97) # [1, 2, 97, 3, 4, 5, 99]

# Delete at end - O(1)
arr.pop() # [1, 2, 97, 3, 4, 5]

# Delete at index - O(n), shifts elements after index
arr.pop(2) # [1, 2, 3, 4, 5]
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

vector<int> arr = {1, 2, 3, 4, 5};

int val = arr[2]; // 3

arr.push_back(99); // {1, 2, 3, 4, 5, 99}
// or arr.emplace_back(99);

arr.insert(arr.begin() + 2, 97); // {1, 2, 97, 3, 4, 5, 99}

arr.pop_back(); // {1, 2, 97, 3, 4, 5}

arr.erase(arr.begin() + 2); // {1, 2, 3, 4, 5}
```
</details>

<details>
<summary>Java</summary>

```java
import java.util.ArrayList;

ArrayList arr = new ArrayList<>(List.of(1, 2, 3, 4, 5));

int val = arr.get(2); // 3

arr.add(99); // [1, 2, 3, 4, 5, 99]

arr.add(2, 97); // [1, 2, 97, 3, 4, 5, 99]

arr.remove(arr.size() - 1); // [1, 2, 97, 3, 4, 5]

arr.remove(2); // [1, 2, 3, 4, 5]
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
const arr: number[] = [1, 2, 3, 4, 5];

const val: number = arr[2]; // 3

arr.push(99); // [1, 2, 3, 4, 5, 99]

arr.splice(2, 0, 97); // [1, 2, 97, 3, 4, 5, 99]

arr.pop(); // [1, 2, 97, 3, 4, 5]

arr.splice(2, 1); // [1, 2, 3, 4, 5]
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

List arr = new List { 1, 2, 3, 4, 5 };

int val = arr[2]; // 3

arr.Add(99); // [1, 2, 3, 4, 5, 99]

arr.Insert(2, 97); // [1, 2, 97, 3, 4, 5, 99]

arr.RemoveAt(arr.Count - 1); // [1, 2, 97, 3, 4, 5]

arr.RemoveAt(2); // [1, 2, 3, 4, 5]
```

</details>

<br/>

> <sub>**Note:** `std::vector` (C++) and `ArrayList` (Java) are dynamic arrays — they handle 
> resizing for you, which is why this is more used in practice. Fixed-size raw 
> arrays (`int arr[]`, Java `int[]`) exist too, but resizing them manually requires 
> allocating new memory and copying everything over, which is *why* insert/delete is O(n).</sub>

<br/>
<br/>

## **Linked-Lists**
A chain of nodes, where each node holds a value and a [pointer](#pointers) to the next node in the sequence. <sub>(Also a pointer to the previous node if its a doubly linked list).</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Fast inserts and deletes (only at a known position) | Slow reads |

| Read (by index) | Insert (at head) | Insert (at end) | Delete (at head) | Delete (at end) |
|------|--------|--------  |----             |----               |
|`O(n)`|`O(1)`  |`O(n)`* |`O(1)`|`O(n)`*|

<br/>

<sub>* Requires traversing from the head to find the position — unless a `tail` pointer is maintained, which makes insert at end `O(1)`. Delete at end stays `O(n)` even with a `tail` pointer, since a singly linked list can't go backward to find the second-to-last node.</sub>

<details>
<summary>Python</summary>

```python
from typing import Optional
class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[Node] = None

# Build list: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Read - O(n), must walk from head.
# So worst case it goes through the whole n-size
# linked list to reach the node we want
def get(head: Node, index: int) -> int:
    curr = head
    for _ in range(index):
        curr = curr.next
    return curr.val

val: int = get(head, 2) # 3

# Insert - O(1), once you have a reference to the node
new_node = Node(99)
new_node.next = head.next.next
head.next.next = new_node  # 1 -> 2 -> 99 -> 3

# Delete - O(1), once you have a reference to the previous node
head.next.next = head.next.next.next  # 1 -> 2 -> 3
```

</details>

<details>
<summary>C++</summary>

```cpp
struct Node {
    int val;
    Node* next;
    Node(int v) : val(v), next(nullptr) {}
};

// Build list: 1 -> 2 -> 3
Node* head = new Node(1);
head->next = new Node(2);
head->next->next = new Node(3);

// Read - O(n), must walk from head
int get(Node* head, int index) {
    Node* curr = head;
    for (int i = 0; i < index; ++i) {
        curr = curr->next;
    }
    return curr->val;
}

int val = get(head, 2); // 3

// Insert - O(1), once you have a reference to the node
Node* newNode = new Node(99);
newNode->next = head->next->next;
head->next->next = newNode;  // 1 -> 2 -> 99 -> 3

// Delete - O(1), once you have a reference to the previous node
Node* toDelete = head->next->next->next;
head->next->next->next = head->next->next->next->next;
delete toDelete;  // 1 -> 2 -> 3
```

</details>

<details>
<summary>Java</summary>

```java
class Node {
    int val;
    Node next;
    Node(int v) {
        val = v;
        next = null;
    }
}

// Build list: 1 -> 2 -> 3
Node head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);

// Read - O(n), must walk from head
int get(Node head, int index) {
    Node curr = head;
    for (int i = 0; i < index; i++) {
        curr = curr.next;
    }
    return curr.val;
}

int val = get(head, 2); // 3

// Insert - O(1), once you have a reference to the node
Node newNode = new Node(99);
newNode.next = head.next.next;
head.next.next = newNode;  // 1 -> 2 -> 99 -> 3

// Delete - O(1), once you have a reference to the previous node
head.next.next = head.next.next.next;  // 1 -> 2 -> 3
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
class Node {
    val: number;
    next: Node | null;
    constructor(val: number) {
        this.val = val;
        this.next = null;
    }
}

// Build list: 1 -> 2 -> 3
const head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);

// Read - O(n), must walk from head
function get(head: Node, index: number): number {
    let curr: Node = head;
    for (let i = 0; i < index; i++) {
        curr = curr.next!;
    }
    return curr.val;
}

const val: number = get(head, 2); // 3

// Insert - O(1), once you have a reference to the node
const newNode = new Node(99);
newNode.next = head.next!.next;
head.next!.next = newNode;  // 1 -> 2 -> 99 -> 3

// Delete - O(1), once you have a reference to the previous node
head.next!.next = head.next!.next!.next;  // 1 -> 2 -> 3
```

</details>

<details>
<summary>C#</summary>

```csharp
class Node {
    public int Val;
    public Node Next;
    public Node(int val) {
        Val = val;
        Next = null;
    }
}

// Build list: 1 -> 2 -> 3
Node head = new Node(1);
head.Next = new Node(2);
head.Next.Next = new Node(3);

// Read - O(n), must walk from head
int Get(Node head, int index) {
    Node curr = head;
    for (int i = 0; i < index; i++) {
        curr = curr.Next;
    }
    return curr.Val;
}

int val = Get(head, 2); // 3

// Insert - O(1), once you have a reference to the node
Node newNode = new Node(99);
newNode.Next = head.Next.Next;
head.Next.Next = newNode;  // 1 -> 2 -> 99 -> 3

// Delete - O(1), once you have a reference to the previous node
head.Next.Next = head.Next.Next.Next;  // 1 -> 2 -> 3
```

</details>

<br/>

**When to use:** When you need frequent inserts/deletes (especially at the head/middle) and don't need random access by index (e.g. implementing queues, stacks, or LRU caches).

<br/>


**Common problems where this is useful:**
- <sub>`Reverse Linked List` — using three pointers (prev, curr, next) to flip the direction of each link</sub>
- <sub>`Linked List Cycle` — detecting a cycle with the fast/slow pointer technique</sub>
- <sub>`Middle of the Linked List` — finding the midpoint in one pass using fast/slow pointers</sub>
- <sub>`Merge Two Sorted Lists` — merging using a dummy node to simplify edge cases</sub>
- <sub>`Remove Nth Node From End of List` — using two pointers offset by n to find the target node in one pass</sub>
- <sub>`Palindrome Linked List` — combining the fast/slow midpoint trick with in-place reversal</sub>
- <sub>`LRU Cache` — combining a doubly linked list with a hash map for O(1) get/put</sub>


> <sub>**Note: Singly vs Doubly Linked Lists**</sub>
>
> <sub>The examples above are a **singly** linked list — each node only stores a pointer to the **next** node, so you can only traverse forward.</sub>
>
> <sub>A **doubly** linked list adds a second pointer, **prev**, so each node also knows its predecessor. This costs a bit of extra memory per node, but lets you:</sub>
> - <sub>Traverse backward</sub>
> - <sub>Delete a node in `O(1)` *without* needing a separate reference to the previous node (since the node already points to it)</sub>
>
> <sub>C++'s `std::list` and Python's `collections.deque` are both implemented as doubly linked lists under the hood.</sub>


<br/>

### **Pointers**
A variable that stores the **memory address** of another variable, rather than the value itself.

```cpp
int x = 4;
int *pX = &x;
```
|Variable | Address | Value |
|-----|------|-----|
| x | 0x1000 | 4 |
| pX | 0x1004 | 0x1000 (address of variable x) |

<br/>

*Integer named x is set to 4:*
```cpp
int x = 4;
```

<br/>

When `*` is next to a type it makes a pointer of that type.  With this x can be accessed by reference.
*Integer pointer named pX is set to the address of x:*
```cpp
int *pX = &x;
// OR
int* pX = &x;
```

<br/>

When `*` is on its own it's a dereferencer.
*Integer named y is set to the thing pointed to by pX:*
```cpp
int y = *pX;
```

<br/>

**Null pointers**

A pointer set to `nullptr` points to nothing.  Dereferencing it is undefined behavior and a common source of crashes. This is exactly why linked list code so often checks `if (node != nullptr)` before accessing `node->val`.

In a linked list specifically, the **last node's `next` pointer is always `nullptr`**, that indicates that traversal has reached the end of the list.

```cpp
int* pX = nullptr;
```

<br/>

**Dangling pointers**

Calling `delete` on a pointer frees the memory it points to, but doesn't erase the pointer variable itself, it still holds the old address. Using it afterward (a "dangling pointer") is undefined behavior.

```cpp
int* pX = new int(4);
delete pX;
// pX is now dangling — using *pX here is undefined behavior
```
To avoid this, set the pointer to `nullptr` immediately after deleting it. Dereferencing a `nullptr` will still crash, but it crashes loudly and immediately instead of silently reading/writing to memory that something else may have already reused.

```cpp
int* pX = new int(4);
delete pX;
pX = nullptr;  // pX is no longer dangling
```

<br/>


**When to use:** Whenever you need to reference or modify data without copying it, or link separate pieces of memory together (e.g. linked list/tree nodes, passing large objects to functions without copying them, or dynamic memory allocation).

> <sub>**Note:** Python doesn't expose raw pointers or memory addresses the way C++ does — every 
> variable in Python is already a reference to an object under the hood, but you can't 
> dereference it, do pointer arithmetic, or get a dangling reference the way you can in C++. 
> This is also why Python doesn't need `nullptr` checks the same way — the equivalent is checking 
> `if node is None`.</sub>


<br/>
<br/>

## **Hash-Maps**
A collection of key-value pairs, where each key maps to a value via a **hash function** that converts the key into an index into an internal array (the "buckets"). <sub>This is what makes lookups `O(1)` on average.  Instead of searching, the key's hash tells you almost exactly where to look.</sub>

> <sub>Also known as `hash tables`, `dictionaries`, `maps`.
> If multiple keys hash to the same bucket (a **collision**), they end up chained together in that bucket — turning lookups in that bucket back into a linear search. This is why worst-case time is `O(n)`, even though it's rare in practice with a good hash function.</sub>

<br/>


| ✅Pros | ❌Cons |
|------|------|
| Fast reads/searching/insert/delete (average case) | No ordering (in most implementations) |
| | Worst-case `O(n)` if many collisions occur (but this is rare) |
| | Extra memory overhead vs. an array |

| Read | Insert | Delete |
|------|--------|--------|
|`O(1)` avg<br>`O(n)` worst|`O(1)` avg<br>`O(n)` worst|`O(1)` avg<br>`O(n)` worst|

<br/>

<details>
<summary>Python</summary>

```python
d: dict[str, int] = {"a": 1, "b": 2}

# Read - O(1) average
val = d["a"]

# Insert - O(1) average
d["c"] = 3

# Delete - O(1) average
del d["a"]

# Check if a key exists - O(1) average
if "b" in d:
    print("found")

# Get with a default value (avoids a KeyError if missing)
val = d.get("z", -1)  # -1, since "z" isn't in the dict

# Iterate over keys and values
for key, value in d.items():
    print(key, value)
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <unordered_map>
using namespace std;

unordered_map<string, int> m = {{"a", 1}, {"b", 2}};

// Read - O(1) average
int val = m["a"];

// Insert - O(1) average
m["c"] = 3;

// Delete - O(1) average
m.erase("a");

// Check if a key exists - O(1) average
if (m.find("b") != m.end()) {
    // found
}
// OR (C++20)
if (m.contains("b")) {
    // found
}

// Get with a default value (avoids inserting a new entry if missing)
int val2 = m.count("z") ? m["z"] : -1;  // -1, since "z" isn't in the map

// Iterate over keys and values
for (const auto& [key, value] : m) {
    // use key, value
}
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.HashMap;

HashMap<String, Integer> m = new HashMap<>();
m.put("a", 1);
m.put("b", 2);

// Read - O(1) average
int val = m.get("a");

// Insert - O(1) average
m.put("c", 3);

// Delete - O(1) average
m.remove("a");

// Check if a key exists - O(1) average
if (m.containsKey("b")) {
    // found
}

// Get with a default value (avoids null if missing)
int val2 = m.getOrDefault("z", -1);  // -1, since "z" isn't in the map

// Iterate over keys and values
for (Map.Entry<String, Integer> entry : m.entrySet()) {
    String key = entry.getKey();
    int value = entry.getValue();
}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
const m: Map<string, number> = new Map([["a", 1], ["b", 2]]);

// Read - O(1) average
const val: number | undefined = m.get("a");

// Insert - O(1) average
m.set("c", 3);

// Delete - O(1) average
m.delete("a");

// Check if a key exists - O(1) average
if (m.has("b")) {
    // found
}

// Get with a default value (avoids undefined if missing)
const val2: number = m.get("z") ?? -1;  // -1, since "z" isn't in the map

// Iterate over keys and values
for (const [key, value] of m) {
    // use key, value
}
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

Dictionary<string, int> m = new Dictionary<string, int> {
    { "a", 1 },
    { "b", 2 }
};

// Read - O(1) average
int val = m["a"];

// Insert - O(1) average
m["c"] = 3;

// Delete - O(1) average
m.Remove("a");

// Check if a key exists - O(1) average
if (m.ContainsKey("b")) {
    // found
}

// Get with a default value (avoids an exception if missing)
int val2 = m.TryGetValue("z", out int found) ? found : -1;  // -1, since "z" isn't in the map

// Iterate over keys and values
foreach (KeyValuePair<string, int> entry in m) {
    string key = entry.Key;
    int value = entry.Value;
}
```

</details>


<br/>

**When to use:** When you need fast lookups by key and don't care about ordering (e.g. counting frequencies, caching, deduplication, or grouping data).

<br/>


**Common problems where this is useful:**
- <sub>`Two Sum` — checking if a complement value has been seen before, in one pass</sub>
- <sub>`Group Anagrams` — grouping strings by a canonical key (e.g. sorted letters)</sub>
- <sub>`Valid Anagram / Contains Duplicate` — counting character/element frequencies</sub>
- <sub>`Longest Substring Without Repeating Characters` — tracking the last seen index of each character</sub>
- <sub>`Subarray Sum Equals K` — storing running (prefix) sums to check for a target difference in O(1)</sub>
- <sub>`LRU Cache` — combining a hash map with a doubly linked list for O(1) get/put</sub>
- <sub>`Top K Frequent Elements` — counting frequencies, then bucketing/sorting by count</sub>


<br/>
<br/>

## **Hash-Sets**
A collection of **unique** values, with no associated key — built on the same hashing mechanism as a hash map, but storing only the value itself (used purely to track membership). <sub>This is what makes lookups `O(1)` on average, the value's hash tells you almost exactly where to look, the same way it does in a hash map.</sub>

> <sub>Also known as `sets`.
> Functionally, a hash set behaves like a hash map where every key maps to nothing (or a dummy value) — same collision/bucket mechanism, same `O(n)` worst case if many values hash to the same bucket.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Fast membership checks/insert/delete (average case) | No ordering (in most implementations) |
| Automatically removes duplicates | Worst-case `O(n)` if many collisions occur (but this is rare) |
| | Can't store duplicate values, or associate a value with extra data |

| Contains | Insert | Delete |
|------|--------|--------|
|`O(1)` avg<br>`O(n)` worst|`O(1)` avg<br>`O(n)` worst|`O(1)` avg<br>`O(n)` worst|

<br/>

<details>
<summary>Python</summary>

```python
s: set[int] = {1, 2, 3}

# Contains - O(1) average
found = 2 in s

# Insert - O(1) average
s.add(4)

# Delete - O(1) average
s.remove(1)

# Union, intersection, difference
a = {1, 2, 3}
b = {2, 3, 4}
union = a | b         # {1, 2, 3, 4}
intersection = a & b  # {2, 3}
difference = a - b    # {1}

# Iterate over values
for val in s:
    print(val)
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <unordered_set>
using namespace std;

unordered_set<int> s = {1, 2, 3};

// Contains - O(1) average
bool found = s.find(2) != s.end();
// OR (C++20)
bool found2 = s.contains(2);

// Insert - O(1) average
s.insert(4);

// Delete - O(1) average
s.erase(1);

// Iterate over values
for (int val : s) {
    // use val
}
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.HashSet;

HashSet<Integer> s = new HashSet<>();
s.add(1);
s.add(2);
s.add(3);

// Contains - O(1) average
boolean found = s.contains(2);

// Insert - O(1) average
s.add(4);

// Delete - O(1) average
s.remove(1);

// Iterate over values
for (int val : s) {
    // use val
}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
const s: Set<number> = new Set([1, 2, 3]);

// Contains - O(1) average
const found: boolean = s.has(2);

// Insert - O(1) average
s.add(4);

// Delete - O(1) average
s.delete(1);

// Iterate over values
for (const val of s) {
    // use val
}
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

HashSet<int> s = new HashSet<int> { 1, 2, 3 };

// Contains - O(1) average
bool found = s.Contains(2);

// Insert - O(1) average
s.Add(4);

// Delete - O(1) average
s.Remove(1);

// Iterate over values
foreach (int val in s) {
    // use val
}
```

</details>

<br/>

**When to use:** When you only care whether something exists, not what it's associated with (e.g. deduplication, fast membership checks, or tracking visited/seen items).

<br/>

**Common problems where this is useful:**
- <sub>`Contains Duplicate` — checking if any value has already been seen</sub>
- <sub>`Longest Consecutive Sequence` — O(1) lookups to check if the next/previous number exists</sub>
- <sub>`Single Number` — using set operations to isolate non-duplicate values</sub>
- <sub>`Intersection of Two Arrays` — using set intersection to find shared elements</sub>
- <sub>`Linked List Cycle` — tracking visited nodes when not using the fast/slow pointer trick</sub>
- <sub>`Word Break` — tracking which substrings are valid dictionary words</sub>

<br/>
<br/>

## **Stacks**
A collection of elements where access is restricted to one end — the **top**. Items are added and removed in **LIFO** order (Last In, First Out), like a stack of plates: you can only take from the top, and the last plate you put on is the first one you take off. It's the underlying mechanism behind **DFS (Depth-First Search)** on trees and graphs, whether using an explicit stack, or recursion (recursive call stack). <sub>Most implementations are built on top of a dynamic array or linked list, so the underlying complexity is inherited from whichever one is used.</sub>

> <sub>The call stack your code runs on (function calls, recursion) is a real-world example of this — each function call is "pushed" on entry and "popped" on return, which is also why deep recursion can cause a stack overflow.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Fast push/pop from the top | No random access — can't read/modify the middle without removing everything above it |
| Simple to implement | Only the top element is ever accessible |

| Push | Pop | Peek |
|------|-----|------|
|`O(1)`|`O(1)`|`O(1)`|

<br/>

<details>
<summary>Python</summary>

```python
stack: list[int] = []

# Push - O(1)
stack.append(1)
stack.append(2)
stack.append(3)

# Pop - O(1)
top = stack.pop()  # 3, stack is now [1, 2]

# Peek - O(1)
top = stack[-1]  # 2

# Check if empty
is_empty = len(stack) == 0
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <stack>
using namespace std;

stack<int> s;

// Push - O(1)
s.push(1);
s.push(2);
s.push(3);

// Pop - O(1)
int top = s.top();
s.pop();  // removes 3, stack is now {1, 2}

// Peek - O(1)
int top2 = s.top();  // 2

// Check if empty
bool isEmpty = s.empty();
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.Deque;
import java.util.ArrayDeque;

Deque<Integer> stack = new ArrayDeque<>();

// Push - O(1)
stack.push(1);
stack.push(2);
stack.push(3);

// Pop - O(1)
int top = stack.pop();  // 3, stack is now [1, 2]

// Peek - O(1)
int top2 = stack.peek();  // 2

// Check if empty
boolean isEmpty = stack.isEmpty();
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
const stack: number[] = [];

// Push - O(1)
stack.push(1);
stack.push(2);
stack.push(3);

// Pop - O(1)
const top: number | undefined = stack.pop();  // 3, stack is now [1, 2]

// Peek - O(1)
const top2: number = stack[stack.length - 1];  // 2

// Check if empty
const isEmpty: boolean = stack.length === 0;
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

Stack<int> stack = new Stack<int>();

// Push - O(1)
stack.Push(1);
stack.Push(2);
stack.Push(3);

// Pop - O(1)
int top = stack.Pop();  // 3, stack is now [1, 2]

// Peek - O(1)
int top2 = stack.Peek();  // 2

// Check if empty
bool isEmpty = stack.Count == 0;
```

</details>

<br/>

**When to use:** When you need to process or undo things in reverse order of how they were added (e.g. matching/validating pairs, backtracking, or tracking the most recent unresolved item).

<br/>

**Common problems where this is useful:**
- <sub>`Valid Parentheses` — pushing open brackets, popping and matching on close brackets</sub>
- <sub>`Min Stack` — designing a stack that also tracks the minimum value in O(1)</sub>
- <sub>`Evaluate Reverse Polish Notation` — pushing operands, popping two at a time to apply each operator</sub>
- <sub>`Daily Temperatures` — using a stack to track indices while finding the next greater element</sub>
- <sub>`Largest Rectangle in Histogram` — using a stack to track increasing bar heights</sub>
- <sub>`Basic Calculator` — using a stack to handle nested parentheses in an expression</sub>
- <sub>`Number of Islands` / `Clone Graph` — DFS traversal using an explicit stack (or recursion) to explore as deep as possible before backtracking</sub>

<br/>
<br/>

## **Queues**
A collection of elements where access is restricted to **both ends** — items are added at the **back** and removed from the **front**. Items are processed in **FIFO** order (First In, First Out), like a line at a store: whoever joined first gets served first. <sub>Most implementations are built on top of a doubly linked list or a circular buffer, since both ends need fast access.</sub>

> <sub>It's the underlying mechanism behind **BFS (Breadth-First Search)** on trees and graphs — each level is fully processed before moving to the next, which is exactly FIFO behavior. (Compare this to Stacks, which power DFS instead.)</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Fast push/pop from each end | No random access, can't read/modify the middle without removing everything in front of it |
| Maintains insertion order naturally | A plain array-based queue is `O(n)` to dequeue, unless implemented carefully |

| Enqueue | Dequeue | Peek |
|------|-----|------|
|`O(1)`|`O(1)`|`O(1)`|

<br/>

<sub>* `O(1)` here assumes a proper queue implementation (doubly linked list or circular buffer). Using a plain array/list and removing from the front (`pop(0)` in Python, `shift()` in JS) is `O(n)`, since every remaining element has to shift over.</sub>

<details>
<summary>Python</summary>

```python
from collections import deque

q: deque[int] = deque()

# Enqueue - O(1)
q.append(1)
q.append(2)
q.append(3)

# Dequeue - O(1)
front = q.popleft()  # 1, queue is now [2, 3]

# Peek - O(1)
front2 = q[0]  # 2

# Check if empty
is_empty = len(q) == 0
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <queue>
using namespace std;

queue<int> q;

// Enqueue - O(1)
q.push(1);
q.push(2);
q.push(3);

// Dequeue - O(1)
int front = q.front();
q.pop();  // removes 1, queue is now {2, 3}

// Peek - O(1)
int front2 = q.front();  // 2

// Check if empty
bool isEmpty = q.empty();
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.Queue;
import java.util.LinkedList;

Queue<Integer> q = new LinkedList<>();

// Enqueue - O(1)
q.offer(1);
q.offer(2);
q.offer(3);

// Dequeue - O(1)
int front = q.poll();  // 1, queue is now [2, 3]

// Peek - O(1)
int front2 = q.peek();  // 2

// Check if empty
boolean isEmpty = q.isEmpty();
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
// TypeScript has no built-in queue - an array works, but shift() is O(n)
// Shown here for simplicity; use a proper Deque class for true O(1) behavior
const q: number[] = [];

// Enqueue - O(1)
q.push(1);
q.push(2);
q.push(3);

// Dequeue - O(n), since every remaining element shifts over
const front: number | undefined = q.shift();  // 1, queue is now [2, 3]

// Peek - O(1)
const front2: number = q[0];  // 2

// Check if empty
const isEmpty: boolean = q.length === 0;
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

Queue<int> q = new Queue<int>();

// Enqueue - O(1)
q.Enqueue(1);
q.Enqueue(2);
q.Enqueue(3);

// Dequeue - O(1)
int front = q.Dequeue();  // 1, queue is now [2, 3]

// Peek - O(1)
int front2 = q.Peek();  // 2

// Check if empty
bool isEmpty = q.Count == 0;
```

</details>

<br/>

**When to use:** When you need to process things in the order they arrived (e.g. BFS traversal, task scheduling, buffering data between producers/consumers).

<br/>

**Common problems where this is useful:**
- <sub>`Binary Tree Level Order Traversal` — BFS using a queue to process one level at a time</sub>
- <sub>`Rotting Oranges` — multi-source BFS to find the time for a state to spread</sub>
- <sub>`Number of Islands` (BFS variant) — using a queue instead of a stack/recursion to explore each island</sub>
- <sub>`Course Schedule` — BFS-based topological sort (Kahn's algorithm) using a queue of zero-indegree nodes</sub>
- <sub>`Sliding Window Maximum` — a monotonic deque to track the max in O(1) per window</sub>
- <sub>`Design Circular Queue` — implementing fixed-size queue behavior directly</sub>

<br/>
<br/>

## **Trees**
A hierarchical structure of nodes, where each node holds a value and pointers to its **children**. The topmost node is the **root**, and nodes with no children are **leaves**. <sub>A tree is essentially a linked list that branches — instead of one `next` pointer, each node can have multiple child pointers.</sub>

> <sub>A **binary tree** restricts each node to at most 2 children (`left` and `right`), a common variant. A **binary search tree (BST)** adds an ordering rule: everything in the left subtree is smaller than the node, everything in the right subtree is larger — which is what makes search `O(log n)` on a balanced tree.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Fast search/insert/delete on a balanced BST | Performance degrades to `O(n)` if the tree becomes unbalanced (e.g. a "skewed" tree) |
| Naturally represents hierarchical data | More complex to implement than arrays or linked lists |

| Search | Insert | Delete |
|------|-----|------|
|`O(log n)` balanced<br>`O(n)` worst|`O(log n)` balanced<br>`O(n)` worst|`O(log n)` balanced<br>`O(n)` worst|

<br/>

<sub>* These complexities apply to a **binary search tree**. A balanced tree (e.g. AVL, Red-Black) keeps height at `O(log n)`; an unbalanced tree (e.g. one built by inserting sorted data in order) can degrade to a single chain, making it effectively a linked list — `O(n)`.</sub>

<details>
<summary>Python</summary>

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

# Build tree:
#       5
#      / \
#     3   8
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)

# Search (BST) - O(log n) balanced, O(n) worst
def search(node: Optional[TreeNode], target: int) -> bool:
    if node is None:
        return False
    if node.val == target:
        return True
    if target < node.val:
        return search(node.left, target)
    return search(node.right, target)

found = search(root, 8)  # True

# Insert (BST) - O(log n) balanced, O(n) worst
def insert(node: Optional[TreeNode], val: int) -> TreeNode:
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

root = insert(root, 4)  # 4 becomes 3's right child

# Traversal - O(n), visits every node
def inorder(node: Optional[TreeNode]) -> list[int]:
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

values = inorder(root)  # [3, 4, 5, 8]
```

</details>

<details>
<summary>C++</summary>

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Build tree:
//       5
//      / \
//     3   8
TreeNode* root = new TreeNode(5);
root->left = new TreeNode(3);
root->right = new TreeNode(8);

// Search (BST) - O(log n) balanced, O(n) worst
bool search(TreeNode* node, int target) {
    if (node == nullptr) return false;
    if (node->val == target) return true;
    if (target < node->val) return search(node->left, target);
    return search(node->right, target);
}

bool found = search(root, 8); // true

// Insert (BST) - O(log n) balanced, O(n) worst
TreeNode* insert(TreeNode* node, int val) {
    if (node == nullptr) return new TreeNode(val);
    if (val < node->val) node->left = insert(node->left, val);
    else node->right = insert(node->right, val);
    return node;
}

root = insert(root, 4); // 4 becomes 3's right child

// Traversal - O(n), visits every node
void inorder(TreeNode* node, vector<int>& result) {
    if (node == nullptr) return;
    inorder(node->left, result);
    result.push_back(node->val);
    inorder(node->right, result);
}
```

</details>

<details>
<summary>Java</summary>

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int v) {
        val = v;
        left = null;
        right = null;
    }
}

// Build tree:
//       5
//      / \
//     3   8
TreeNode root = new TreeNode(5);
root.left = new TreeNode(3);
root.right = new TreeNode(8);

// Search (BST) - O(log n) balanced, O(n) worst
boolean search(TreeNode node, int target) {
    if (node == null) return false;
    if (node.val == target) return true;
    if (target < node.val) return search(node.left, target);
    return search(node.right, target);
}

boolean found = search(root, 8); // true

// Insert (BST) - O(log n) balanced, O(n) worst
TreeNode insert(TreeNode node, int val) {
    if (node == null) return new TreeNode(val);
    if (val < node.val) node.left = insert(node.left, val);
    else node.right = insert(node.right, val);
    return node;
}

root = insert(root, 4); // 4 becomes 3's right child

// Traversal - O(n), visits every node
void inorder(TreeNode node, List<Integer> result) {
    if (node == null) return;
    inorder(node.left, result);
    result.add(node.val);
    inorder(node.right, result);
}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val: number) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

// Build tree:
//       5
//      / \
//     3   8
const root = new TreeNode(5);
root.left = new TreeNode(3);
root.right = new TreeNode(8);

// Search (BST) - O(log n) balanced, O(n) worst
function search(node: TreeNode | null, target: number): boolean {
    if (node === null) return false;
    if (node.val === target) return true;
    if (target < node.val) return search(node.left, target);
    return search(node.right, target);
}

const found: boolean = search(root, 8); // true

// Insert (BST) - O(log n) balanced, O(n) worst
function insert(node: TreeNode | null, val: number): TreeNode {
    if (node === null) return new TreeNode(val);
    if (val < node.val) node.left = insert(node.left, val);
    else node.right = insert(node.right, val);
    return node;
}

// Traversal - O(n), visits every node
function inorder(node: TreeNode | null, result: number[]): void {
    if (node === null) return;
    inorder(node.left, result);
    result.push(node.val);
    inorder(node.right, result);
}
```

</details>

<details>
<summary>C#</summary>

```csharp
class TreeNode {
    public int Val;
    public TreeNode Left;
    public TreeNode Right;
    public TreeNode(int val) {
        Val = val;
        Left = null;
        Right = null;
    }
}

// Build tree:
//       5
//      / \
//     3   8
TreeNode root = new TreeNode(5);
root.Left = new TreeNode(3);
root.Right = new TreeNode(8);

// Search (BST) - O(log n) balanced, O(n) worst
bool Search(TreeNode node, int target) {
    if (node == null) return false;
    if (node.Val == target) return true;
    if (target < node.Val) return Search(node.Left, target);
    return Search(node.Right, target);
}

bool found = Search(root, 8); // true

// Insert (BST) - O(log n) balanced, O(n) worst
TreeNode Insert(TreeNode node, int val) {
    if (node == null) return new TreeNode(val);
    if (val < node.Val) node.Left = Insert(node.Left, val);
    else node.Right = Insert(node.Right, val);
    return node;
}

// Traversal - O(n), visits every node
void Inorder(TreeNode node, List<int> result) {
    if (node == null) return;
    Inorder(node.Left, result);
    result.Add(node.Val);
    Inorder(node.Right, result);
}
```

</details>

<br/>

**When to use:** When your data is naturally hierarchical, or you need fast search/insert/delete while keeping data sorted (e.g. file systems, autocomplete/tries, decision trees, or any sorted dataset with frequent updates).

<br/>

**Common problems where this is useful:**
- <sub>`Maximum Depth of Binary Tree` — basic recursive DFS to compute height</sub>
- <sub>`Validate Binary Search Tree` — DFS while tracking valid min/max bounds per node</sub>
- <sub>`Lowest Common Ancestor of a BST` — using BST ordering to navigate toward both targets</sub>
- <sub>`Binary Tree Level Order Traversal` — BFS using a queue, one level at a time</sub>
- <sub>`Kth Smallest Element in a BST` — inorder traversal exploits BST ordering to visit nodes in sorted order</sub>
- <sub>`Serialize and Deserialize Binary Tree` — preorder traversal to encode/decode tree structure</sub>

> <sub>**Note: Balanced vs Unbalanced**</sub>
>
> <sub>A tree's height directly determines its complexity — `O(log n)` operations rely on the tree being roughly balanced (height ≈ log₂(n)). Inserting already-sorted data into a plain BST with no rebalancing produces a worst-case **skewed tree** (effectively a linked list), degrading every operation to `O(n)`.</sub>
>
> <sub>Self-balancing trees (AVL, Red-Black) automatically rebalance on insert/delete to guarantee `O(log n)` — this is what `std::map` (C++), `TreeMap` (Java), and similar sorted containers use internally.</sub>

<br/>
<br/>

## **Graphs**
A collection of **nodes (vertices)** connected by **edges**. Unlike a tree, a graph has no strict hierarchy — any node can connect to any other node, cycles are allowed, and there's no single "root." <sub>A tree is actually a special case of a graph — one with no cycles, and exactly one path between any two nodes.</sub>

> <sub>Edges can be **directed** (one-way, like a follower relationship) or **undirected** (two-way, like a friendship), and **weighted** (edges have a cost, like distance) or **unweighted**.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Models real-world relationships naturally (networks, maps, dependencies) | More complex to traverse and reason about than trees |
| Flexible — supports cycles, multiple paths, disconnected components | Many algorithms (shortest path, cycle detection) are non-trivial/complicated |

| Representation | Space | Edge Lookup |
|------|-----|------|
|Adjacency List|`O(V + E)`|`O(degree)`|
|Adjacency Matrix|`O(V²)`|`O(1)`|

<br/>

<sub>*V = number of vertices, E = number of edges. An **adjacency list** (a hash map/array of lists) is more space-efficient for sparse graphs (few edges); an **adjacency matrix** (a 2D array/grid) gives instant edge lookups but wastes memory on sparse graphs. Most LeetCode graph problems use an adjacency list.</sub>

<details>
<summary>Python</summary>

```python
from collections import defaultdict, deque
from typing import Optional

# Adjacency list representation
graph: dict[int, list[int]] = defaultdict(list)
graph[1].append(2)
graph[1].append(3)
graph[2].append(4)

# BFS - O(V + E)
def bfs(start: int) -> list[int]:
    visited = set()
    visited.add(start)
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# DFS - O(V + E)
def dfs(start: int, visited: Optional[set[int]] = None, order: list[int] = None) -> list[int]:
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited, order)
    return order
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

// Adjacency list representation
unordered_map<int, vector<int>> graph;
graph[1].push_back(2);
graph[1].push_back(3);
graph[2].push_back(4);

// BFS - O(V + E)
vector<int> bfs(int start) {
    unordered_set<int> visited = {start};
    queue<int> q;
    q.push(start);
    vector<int> order;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order.push_back(node);
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
    return order;
}

// DFS - O(V + E)
void dfs(int node, unordered_set<int>& visited, vector<int>& order) {
    visited.insert(node);
    order.push_back(node);
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, visited, order);
        }
    }
}
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.*;

// Adjacency list representation
Map<Integer, List<Integer>> graph = new HashMap<>();
graph.computeIfAbsent(1, k -> new ArrayList<>()).add(2);
graph.computeIfAbsent(1, k -> new ArrayList<>()).add(3);
graph.computeIfAbsent(2, k -> new ArrayList<>()).add(4);

// BFS - O(V + E)
List<Integer> bfs(int start) {
    Set<Integer> visited = new HashSet<>(List.of(start));
    Queue<Integer> queue = new LinkedList<>(List.of(start));
    List<Integer> order = new ArrayList<>();

    while (!queue.isEmpty()) {
        int node = queue.poll();
        order.add(node);
        for (int neighbor : graph.getOrDefault(node, List.of())) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.offer(neighbor);
            }
        }
    }
    return order;
}

// DFS - O(V + E)
void dfs(int node, Set<Integer> visited, List<Integer> order) {
    visited.add(node);
    order.add(node);
    for (int neighbor : graph.getOrDefault(node, List.of())) {
        if (!visited.contains(neighbor)) {
            dfs(neighbor, visited, order);
        }
    }
}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
// Adjacency list representation
const graph: Map<number, number[]> = new Map();
graph.set(1, [2, 3]);
graph.set(2, [4]);

// BFS - O(V + E)
function bfs(start: number): number[] {
    const visited = new Set<number>([start]);
    const queue: number[] = [start];
    const order: number[] = [];

    while (queue.length > 0) {
        const node = queue.shift()!;
        order.push(node);
        for (const neighbor of graph.get(node) ?? []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    return order;
}

// DFS - O(V + E)
function dfs(node: number, visited: Set<number> = new Set(), order: number[] = []): number[] {
    visited.add(node);
    order.push(node);
    for (const neighbor of graph.get(node) ?? []) {
        if (!visited.has(neighbor)) {
            dfs(neighbor, visited, order);
        }
    }
    return order;
}
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

// Adjacency list representation
Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();
graph[1] = new List<int> { 2, 3 };
graph[2] = new List<int> { 4 };

// BFS - O(V + E)
List<int> Bfs(int start) {
    HashSet<int> visited = new HashSet<int> { start };
    Queue<int> queue = new Queue<int>();
    queue.Enqueue(start);
    List<int> order = new List<int>();

    while (queue.Count > 0) {
        int node = queue.Dequeue();
        order.Add(node);
        foreach (int neighbor in graph.GetValueOrDefault(node, new List<int>())) {
            if (!visited.Contains(neighbor)) {
                visited.Add(neighbor);
                queue.Enqueue(neighbor);
            }
        }
    }
    return order;
}

// DFS - O(V + E)
void Dfs(int node, HashSet<int> visited, List<int> order) {
    visited.Add(node);
    order.Add(node);
    foreach (int neighbor in graph.GetValueOrDefault(node, new List<int>())) {
        if (!visited.Contains(neighbor)) {
            Dfs(neighbor, visited, order);
        }
    }
}
```

</details>

<br/>

**When to use:** When your data represents relationships/connections rather than a strict hierarchy (e.g. social networks, maps/routing, dependency resolution, or any "is connected to" relationship).

<br/>

**Common problems where this is useful:**
- <sub>`Number of Islands` — DFS/BFS to count connected components in a grid</sub>
- <sub>`Course Schedule` — cycle detection / topological sort on a directed graph</sub>
- <sub>`Clone Graph` — DFS/BFS while mapping original nodes to their clones</sub>
- <sub>`Pacific Atlantic Water Flow` — multi-source DFS/BFS from each border</sub>
- <sub>`Network Delay Time` — Dijkstra's algorithm for shortest path on a weighted graph</sub>
- <sub>`Graph Valid Tree` — checking a graph has exactly V-1 edges and no cycles</sub>

> <sub>**Note: Cycle Detection**</sub>
>
> <sub>Unlike trees, graphs can contain cycles — so traversal code must track **visited** nodes, or it will loop forever. This is the single most common bug in graph problems: forgetting to mark a node visited before (not after) recursing into it.</sub>

<br/>
<br/>


## **Heaps**
A tree-based structure that keeps the **smallest** (min-heap) or **largest** (max-heap) element always accessible at the root in `O(1)`, while still supporting efficient insert/remove. <sub>Despite being a tree conceptually, heaps are almost always implemented as a plain array — a node at index `i` has children at `2i+1` and `2i+2`, so no pointers are needed.</sub>

> <sub>Also known as a **priority queue** — a heap is the typical underlying implementation, since it always gives you fast access to the highest-priority (smallest/largest) item.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Always-fast access to the min/max element | No fast access to any other element — finding an arbitrary value is `O(n)` |
| Faster insert than keeping a fully sorted array | Not fully sorted — only the root is guaranteed to be min/max |

| Get Min/Max | Insert | Remove Min/Max |
|------|-----|------|
|`O(1)`|`O(log n)`|`O(log n)`|

<br/>

<sub>* Insert/remove are `O(log n)` because the heap only needs to "bubble" the element up or down one path to restore the heap property — it doesn't need to re-sort everything.</sub>

<details>
<summary>Python</summary>

```python
import heapq

# Python's heapq is a min-heap by default
heap: list[int] = []

# Insert - O(log n)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

# Get min - O(1)
smallest = heap[0]  # 1

# Remove min - O(log n)
smallest = heapq.heappop(heap)  # 1, heap now contains [3, 5]

# Max-heap trick: negate values on insert/pop
max_heap: list[int] = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
largest = -heapq.heappop(max_heap)  # 5
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <queue>
using namespace std;

// Min-heap requires greater<int> comparator (max-heap is the default)
priority_queue<int, vector<int>, greater<int>> minHeap;

// Insert - O(log n)
minHeap.push(5);
minHeap.push(1);
minHeap.push(3);

// Get min - O(1)
int smallest = minHeap.top(); // 1

// Remove min - O(log n)
minHeap.pop(); // heap now contains {3, 5}

// Max-heap (the default)
priority_queue<int> maxHeap;
maxHeap.push(5);
maxHeap.push(1);
int largest = maxHeap.top(); // 5
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.PriorityQueue;
import java.util.Collections;

// PriorityQueue is a min-heap by default
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Insert - O(log n)
minHeap.offer(5);
minHeap.offer(1);
minHeap.offer(3);

// Get min - O(1)
int smallest = minHeap.peek(); // 1

// Remove min - O(log n)
smallest = minHeap.poll(); // 1, heap now contains [3, 5]

// Max-heap, using a reverse comparator
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
maxHeap.offer(5);
maxHeap.offer(1);
int largest = maxHeap.peek(); // 5
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
// TypeScript has no built-in heap — shown conceptually using a sorted insert
// In practice, use a library (e.g. "heap-js" / "@datastructures-js/priority-queue")
class MinHeap {
    private heap: number[] = [];

    push(val: number): void { // O(log n)
        this.heap.push(val);
        this.heap.sort((a, b) => a - b); // simplified, not true O(log n) without a real heap impl
    }

    peek(): number { // O(1)
        return this.heap[0];
    }

    pop(): number | undefined { // O(log n) with a real heap
        return this.heap.shift();
    }
}

const minHeap = new MinHeap();
minHeap.push(5);
minHeap.push(1);
minHeap.push(3);
const smallest: number = minHeap.peek(); // 1
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

// PriorityQueue<TElement, TPriority> is a min-heap by default (.NET 6+)
PriorityQueue<int, int> minHeap = new PriorityQueue<int, int>();

// Insert - O(log n)
minHeap.Enqueue(5, 5);
minHeap.Enqueue(1, 1);
minHeap.Enqueue(3, 3);

// Get min - O(1) via Peek
int smallest = minHeap.Peek(); // 1

// Remove min - O(log n)
smallest = minHeap.Dequeue(); // 1, heap now contains 3, 5
```

</details>

<br/>

**When to use:** When you repeatedly need the smallest/largest element from a changing collection (e.g. priority scheduling, finding the kth largest/smallest element, or merging sorted data).

<br/>

**Common problems where this is useful:**
- <sub>`Kth Largest Element in an Array` — maintaining a min-heap of size k</sub>
- <sub>`Top K Frequent Elements` — counting frequencies, then using a heap to extract the top k</sub>
- <sub>`Merge K Sorted Lists` — a min-heap to always pick the smallest head among k lists</sub>
- <sub>`Find Median from Data Stream` — two heaps (one min, one max) to track the middle efficiently</sub>
- <sub>`Task Scheduler` — a max-heap to always schedule the most frequent remaining task</sub>
- <sub>`K Closest Points to Origin` — a max-heap of size k to track the k closest points</sub>

> <sub>**Note: Heap vs Sorted Array**</sub>
>
> <sub>A fully sorted array gives `O(1)` access to the min *and* max, but insert is `O(n)` (must shift to maintain order). A heap trades away full sorting — it only guarantees the root is min/max — in exchange for `O(log n)` insert. If you need fast repeated access to just one end (not both, and not full ordering), a heap is the better fit.</sub>

<br/>
<br/>