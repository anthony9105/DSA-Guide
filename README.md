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
- [**Leetcode Problems and Solutions**](./Leetcode%20Problems/README.md)

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

<sub>* Requires traversing from the head to find the position — unless a `tail` pointer is maintained, which makes insert at end `O(1)`. Delete at end stays `O(n)` even with a `tail` pointer, since a singly linked list can't go backward to find the second-to-last node.<sub>

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

<sub>

**Common problems where this is useful:**
- `Reverse Linked List` — using three pointers (prev, curr, next) to flip the direction of each link
- `Linked List Cycle` — detecting a cycle with the fast/slow pointer technique
- `Middle of the Linked List` — finding the midpoint in one pass using fast/slow pointers
- `Merge Two Sorted Lists` — merging using a dummy node to simplify edge cases
- `Remove Nth Node From End of List` — using two pointers offset by n to find the target node in one pass
- `Palindrome Linked List` — combining the fast/slow midpoint trick with in-place reversal
- `LRU Cache` — combining a doubly linked list with a hash map for O(1) get/put

</sub>


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

<sub>

**Common problems where this is useful:**
- `Two Sum` — checking if a complement value has been seen before, in one pass
- `Group Anagrams` — grouping strings by a canonical key (e.g. sorted letters)
- `Valid Anagram / Contains Duplicate` — counting character/element frequencies
- `Longest Substring Without Repeating Characters` — tracking the last seen index of each character
- `Subarray Sum Equals K` — storing running (prefix) sums to check for a target difference in O(1)
- `LRU Cache` — combining a hash map with a doubly linked list for O(1) get/put
- `Top K Frequent Elements` — counting frequencies, then bucketing/sorting by count

</sub>

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

<sub>

**Common problems where this is useful:**
- `Contains Duplicate` — checking if any value has already been seen
- `Longest Consecutive Sequence` — O(1) lookups to check if the next/previous number exists
- `Single Number` — using set operations to isolate non-duplicate values
- `Intersection of Two Arrays` — using set intersection to find shared elements
- `Linked List Cycle` — tracking visited nodes when not using the fast/slow pointer trick
- `Word Break` — tracking which substrings are valid dictionary words

</sub>

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

<sub>

**Common problems where this is useful:**
- `Valid Parentheses` — pushing open brackets, popping and matching on close brackets
- `Min Stack` — designing a stack that also tracks the minimum value in O(1)
- `Evaluate Reverse Polish Notation` — pushing operands, popping two at a time to apply each operator
- `Daily Temperatures` — using a stack to track indices while finding the next greater element
- `Largest Rectangle in Histogram` — using a stack to track increasing bar heights
- `Basic Calculator` — using a stack to handle nested parentheses in an expression
- `Number of Islands` / `Clone Graph` — DFS traversal using an explicit stack (or recursion) to explore as deep as possible before backtracking

</sub>

<br/>
<br/>