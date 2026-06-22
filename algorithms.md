<h1 align="center" style="font-size: 40px">Key Algorithms</h1>

## Contents
- [Searching/Traversal](#searchingtraversal)
  - [**Binary Search**](#binary-search)
  - [**DFS (Depth-First Search)**](#dfs-depth-first-search)
  - [**BFS (Breadth-First Search)**](#bfs-breadth-first-search)
- [Sorting](#sorting) 
  - [Bubble Sort (Bad)](#bubble-sort-bad) 
  - [Insertion Sort](#insertion-sort)
  - [**Merge Sort**](#merge-sort)
  - [**Quick Sort**](#quick-sort)
  - [**Heap Sort**](#heap-sort)


<br/>

# Searching/Traversal
## **Binary Search**
A search algorithm that finds a target in a **sorted** collection by repeatedly halving the search space.  Compare the middle element, then discard the half that can't contain the target. This is what makes it extremely fast: `O(log n)`.</sub>

> <sub>Binary search **requires the data to be sorted** first, if it isn't, you'd need to sort it (`O(n log n)`) before binary search becomes worthwhile, or use a linear search instead.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| *Extremely fast* `O(logn)`, much faster than linear search on large datasets | Only works on sorted data |
| | Requires random access (works on arrays, not linked lists) |


| Search |
|------|
|`O(logn)`|

<br/>


<details>
<summary>Python</summary>

```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found

nums = [1, 3, 5, 7, 9, 11]
index = binary_search(nums, 7)  # 3
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

int binarySearch(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;

    while (left <= right) {
        const int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        } 
        else if (nums[mid] < target) {
            left = mid + 1;
        } 
        else {
            right = mid - 1;
        }
    }

    return -1; // not found
}

vector<int> nums = {1, 3, 5, 7, 9, 11};
int index = binarySearch(nums, 7); // 3
```

</details>

<details>
<summary>Java</summary>

```java
int binarySearch(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1; // not found
}

int[] nums = {1, 3, 5, 7, 9, 11};
int index = binarySearch(nums, 7); // 3
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function binarySearch(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);

        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1; // not found
}

const nums: number[] = [1, 3, 5, 7, 9, 11];
const index: number = binarySearch(nums, 7); // 3
```

</details>

<details>
<summary>C#</summary>

```csharp
int BinarySearch(int[] nums, int target) {
    int left = 0, right = nums.Length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1; // not found
}

int[] nums = { 1, 3, 5, 7, 9, 11 };
int index = BinarySearch(nums, 7); // 3
```

</details>

<br/>

**When to use:** When you need to search a sorted collection efficiently, or when the problem can be reframed as "find the smallest/largest value where some condition becomes true" (binary search on the answer).

<br/>

**Common problems where this is useful:**
- <sub>`Search in Rotated Sorted Array` — binary search adapted to a sorted-but-rotated array</sx>
- <sub>`Find First and Last Position of Element in Sorted Array` — binary search twice, for the left and right boundary</sub>
- <sub>`Find Minimum in Rotated Sorted Array` — binary search to find the rotation point</sub>
- <sub>`Median of Two Sorted Arrays` — binary search on the partition point between two arrays</sub>
- <sub>`Koko Eating Bananas` — binary search on the answer (the eating speed), not the array itself</sub>

> <sub>**Note: `left + (right - left) / 2` vs `(left + right) / 2`**</sub>
>
> <sub>Both calculate the midpoint, but `(left + right) / 2` can overflow in languages with fixed-size integers (C++, Java, C#) if `left` and `right` are both close to the max integer value. `left + (right - left) / 2` avoids this, since the intermediate sum never exceeds `right`. Python doesn't have this issue (integers are arbitrary precision), but it's a good habit to carry across languages.</sub>

<br/>
<br/>

## **DFS (Depth-First Search)**
A traversal algorithm that explores as **deep as possible** down one path before backtracking — visiting a neighbor, then that neighbor's neighbor, and so on, only stepping back once a path is exhausted. <sub>This is exactly **LIFO** behavior, which is why DFS is implemented with a [stack](./README.md#stacks) — either explicitly, or implicitly via recursion (the call stack).</sub>

> <sub>Works on both [trees](./README.md#trees) and [graphs](./README.md#graphs). On a graph, **visited tracking is required** to avoid infinite loops if a cycle exists — trees don't need this, since there's only one path to each node.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Uses less memory than BFS on wide graphs/trees | Doesn't guarantee the shortest path |
| Simple to implement recursively | Deep recursion can cause a stack overflow on very deep structures |

| Traversal |
|------|
|`O(V + E)`|

<br/>

<sub>* V = vertices (nodes), E = edges. On a tree specifically, this simplifies to `O(n)`, since E = n - 1.</sub>

<details>
<summary>Python</summary>

```python
# Recursive DFS (implicit stack via the call stack)
def dfs(graph: dict[int, list[int]], node: int, visited: set[int] = None) -> list[int]:
    if visited is None:
        visited = set()
    visited.add(node)
    order = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            order += dfs(graph, neighbor, visited)
    return order

# Iterative DFS (explicit stack)
def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = {start}
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// Recursive DFS (implicit stack via the call stack)
void dfs(unordered_map<int, vector<int>>& graph, int node, unordered_set<int>& visited, vector<int>& order) {
    visited.insert(node);
    order.push_back(node);
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(graph, neighbor, visited, order);
        }
    }
}

// Iterative DFS (explicit stack)
vector<int> dfsIterative(unordered_map<int, vector<int>>& graph, int start) {
    unordered_set<int> visited = {start};
    vector<int> stack = {start};
    vector<int> order;

    while (!stack.empty()) {
        int node = stack.back();
        stack.pop_back();
        order.push_back(node);
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                stack.push_back(neighbor);
            }
        }
    }
    return order;
}
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.*;

// Recursive DFS (implicit stack via the call stack)
void dfs(Map<Integer, List<Integer>> graph, int node, Set<Integer> visited, List<Integer> order) {
    visited.add(node);
    order.add(node);
    for (int neighbor : graph.getOrDefault(node, List.of())) {
        if (!visited.contains(neighbor)) {
            dfs(graph, neighbor, visited, order);
        }
    }
}

// Iterative DFS (explicit stack)
List<Integer> dfsIterative(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>(List.of(start));
    Deque<Integer> stack = new ArrayDeque<>(List.of(start));
    List<Integer> order = new ArrayList<>();

    while (!stack.isEmpty()) {
        int node = stack.pop();
        order.add(node);
        for (int neighbor : graph.getOrDefault(node, List.of())) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                stack.push(neighbor);
            }
        }
    }
    return order;
}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
// Recursive DFS (implicit stack via the call stack)
function dfs(graph: Map<number, number[]>, node: number, visited: Set<number> = new Set(), order: number[] = []): number[] {
    visited.add(node);
    order.push(node);
    for (const neighbor of graph.get(node) ?? []) {
        if (!visited.has(neighbor)) {
            dfs(graph, neighbor, visited, order);
        }
    }
    return order;
}

// Iterative DFS (explicit stack)
function dfsIterative(graph: Map<number, number[]>, start: number): number[] {
    const visited = new Set<number>([start]);
    const stack: number[] = [start];
    const order: number[] = [];

    while (stack.length > 0) {
        const node = stack.pop()!;
        order.push(node);
        for (const neighbor of graph.get(node) ?? []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                stack.push(neighbor);
            }
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

// Recursive DFS (implicit stack via the call stack)
void Dfs(Dictionary<int, List<int>> graph, int node, HashSet<int> visited, List<int> order) {
    visited.Add(node);
    order.Add(node);
    foreach (int neighbor in graph.GetValueOrDefault(node, new List<int>())) {
        if (!visited.Contains(neighbor)) {
            Dfs(graph, neighbor, visited, order);
        }
    }
}

// Iterative DFS (explicit stack)
List<int> DfsIterative(Dictionary<int, List<int>> graph, int start) {
    HashSet<int> visited = new HashSet<int> { start };
    Stack<int> stack = new Stack<int>();
    stack.Push(start);
    List<int> order = new List<int>();

    while (stack.Count > 0) {
        int node = stack.Pop();
        order.Add(node);
        foreach (int neighbor in graph.GetValueOrDefault(node, new List<int>())) {
            if (!visited.Contains(neighbor)) {
                visited.Add(neighbor);
                stack.Push(neighbor);
            }
        }
    }
    return order;
}
```

</details>

<br/>

**When to use:** When you need to explore every possible path (backtracking), check connectivity, or the problem doesn't require the *shortest* path — just *a* complete path (e.g. maze solving, cycle detection, topological sort).

<br/>

**Common problems where this is useful:**
- <sub>`Number of Islands` — DFS to mark and count each connected group of land cells</sub>
- <sub>`Path Sum` — DFS down a tree, tracking the running sum along each path</sub>
- <sub>`Combination Sum` / `Permutations` — DFS-based backtracking to explore all valid combinations</sub>
- <sub>`Course Schedule` — DFS-based cycle detection on a directed graph</sub>
- <sub>`Word Search` — DFS from each grid cell, backtracking when a path doesn't pan out</sub>
- <sub>`Clone Graph` — DFS while mapping original nodes to their clones</sub>

<br/>
<br/>


## **BFS (Breadth-First Search)**
A traversal algorithm that explores **level by level** — visiting all of a node's immediate neighbors before moving on to their neighbors. <sub>This is exactly **FIFO** behavior, which is why BFS is implemented with a [queue](./README.md#queues).</sub>

> <sub>Works on both [trees](./README.md#trees) and [graphs](./README.md#graphs). Unlike DFS, BFS guarantees the **shortest path** in an unweighted graph — since it explores in order of distance from the start, the first time it reaches a target is guaranteed to be via the shortest route.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Guarantees the shortest path (unweighted graphs) | Uses more memory than DFS on wide graphs/trees (stores a full level at once) |
| No risk of stack overflow (no deep recursion) | Slightly more setup than DFS (requires a queue + visited tracking) |

| Traversal |
|------|
|`O(V + E)`|

<br/>

<sub>* V = vertices (nodes), E = edges. On a tree specifically, this simplifies to `O(n)`, since E = n - 1.</sub>

<details>
<summary>Python</summary>

```python
from collections import deque

def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = {start}
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
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>
using namespace std;

vector<int> bfs(unordered_map<int, vector<int>>& graph, int start) {
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
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.*;

List<Integer> bfs(Map<Integer, List<Integer>> graph, int start) {
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
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function bfs(graph: Map<number, number[]>, start: number): number[] {
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
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;

List<int> Bfs(Dictionary<int, List<int>> graph, int start) {
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
```

</details>

<br/>

**When to use:** When you need the *shortest* path in an unweighted graph, or need to process data level by level (e.g. shortest path, level-order traversal, finding the minimum number of steps).

<br/>

**Common problems where this is useful:**
- <sub>`Binary Tree Level Order Traversal` — processing one tree level at a time</sub>
- <sub>`Rotting Oranges` — multi-source BFS to find the time for a state to spread</sub>
- <sub>`Word Ladder` — BFS to find the shortest transformation sequence between words</sub>
- <sub>`Shortest Path in Binary Matrix` — BFS to guarantee the minimum number of steps</sub>
- <sub>`01 Matrix` — multi-source BFS from all zero cells simultaneously</sub>
- <sub>`Course Schedule` (BFS variant) — topological sort using Kahn's algorithm with a queue</sub>

> <sub>**Note: DFS vs BFS — which to pick**</sub>
>
> <sub>If the problem asks for the **shortest path/fewest steps** in an unweighted graph, use BFS — DFS can't guarantee this. If you need to explore **every possible path** (backtracking, combinations) or just check connectivity, DFS is usually simpler and uses less memory.</sub>

<br/>
<br/>

# Sorting

| Algorithm | Best | Average | Worst | Space | Stable | Linked List Friendly | Viable In Practice |
|-----------|------|---------|-------|-------|--------|----------------------|-----------|
| [Bubble Sort](#bubble-sort-bad) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | ✅ | ❌ |
| [Insertion Sort](#insertion-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | ✅ | ✅ <sub>(only on very small or nearly-sorted data)</sub> |
| [Merge Sort](#merge-sort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)`* | Yes | ✅ | ✅ |
| [Quick Sort](#quick-sort) | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(log n)` | No | ❌ | ✅ |
| [Heap Sort](#heap-sort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | No | ❌ | ✅ <sub>(when space is limited)</sub> |

<sub>* `O(1)` extra space when merge sorting a linked list directly (relinking nodes), vs. `O(n)` on an array (requires temporary arrays).</sub>

## **Bubble Sort (Bad)**
A sorting algorithm that repeatedly steps through the list, **swapping adjacent elements** if they're in the wrong order — each pass "bubbles" the largest unsorted element to its correct position at the end. <sub>Named for how larger elements rise to the top of the list with each pass, like bubbles in water.</sub>

> <sub>Mostly used for teaching sorting concepts, it's pretty much never the right choice in practice due to its poor time complexity.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Very simple to understand and implement | `O(n²)` — way too slow |
| In-place (no extra memory needed) | Almost never used in practice over faster alternatives |
| Stable (preserves the relative order of equal elements) | |

| Best Case | Average Case | Worst Case | Space |
|------|------|------|------|
|`O(n)`|`O(n²)`|`O(n²)`|`O(1)`|

<br/>

<sub>* Best case (`O(n)`) occurs when the list is already sorted, if an early-exit check is included (stop once a full pass makes no swaps).</sub>

<details>
<summary>Python</summary>

```python
def bubble_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break  # already sorted, exit early
    return nums

nums = [5, 1, 4, 2, 8]
sorted_nums = bubble_sort(nums)  # [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

void bubbleSort(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                swap(nums[j], nums[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted, exit early
    }
}

vector<int> nums = {5, 1, 4, 2, 8};
bubbleSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>Java</summary>

```java
void bubbleSort(int[] nums) {
    int n = nums.length;
    for (int i = 0; i < n; i++) {
        boolean swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                int temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted, exit early
    }
}

int[] nums = {5, 1, 4, 2, 8};
bubbleSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function bubbleSort(nums: number[]): number[] {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted, exit early
    }
    return nums;
}

const nums: number[] = [5, 1, 4, 2, 8];
const sortedNums: number[] = bubbleSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C#</summary>

```csharp
void BubbleSort(int[] nums) {
    int n = nums.Length;
    for (int i = 0; i < n; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                (nums[j], nums[j + 1]) = (nums[j + 1], nums[j]);
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted, exit early
    }
}

int[] nums = { 5, 1, 4, 2, 8 };
BubbleSort(nums); // { 1, 2, 4, 5, 8 }
```

</details>

<br/>

**When to use:** Rarely in practice — mostly useful for understanding sorting fundamentals, or in situations where simplicity matters more than performance on very small datasets.

<br/>

**Common problems where this is useful:**
- <sub>Rarely asked directly — but understanding it builds intuition for swap-based logic used in problems like `Sort Colors` (Dutch National Flag)</sub>

<br/>
<br/>

## **Insertion Sort**
A sorting algorithm that builds the sorted list **one element at a time** — taking each element and inserting it into its correct position among the already-sorted elements before it. <sub>Similar to how you might sort a hand of playing cards — picking up one card at a time and inserting it into the right spot among the cards already in your hand.</sub>

> <sub>Efficient for small or **nearly-sorted** datasets — its best case is `O(n)` when the data is already sorted, since each element only needs to shift a tiny amount (or not at all).</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Very fast on small or nearly-sorted data | `O(n²)` worst case — slow on large, unsorted datasets |
| In-place (no extra memory needed) | Still slower than Merge/Quick Sort on large random data |
| Stable (preserves the relative order of equal elements) | |

| Best Case | Average Case | Worst Case | Space |
|------|------|------|------|
|`O(n)`|`O(n²)`|`O(n²)`|`O(1)`|

<br/>

<sub>* Best case (`O(n)`) occurs when the list is already sorted — each new element only needs one comparison to confirm it's already in place.</sub>

<details>
<summary>Python</summary>

```python
def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

nums = [5, 1, 4, 2, 8]
sorted_nums = insertion_sort(nums)  # [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

void insertionSort(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        int key = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
}

vector<int> nums = {5, 1, 4, 2, 8};
insertionSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>Java</summary>

```java
void insertionSort(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
        int key = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
}

int[] nums = {5, 1, 4, 2, 8};
insertionSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function insertionSort(nums: number[]): number[] {
    for (let i = 1; i < nums.length; i++) {
        const key = nums[i];
        let j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
    return nums;
}

const nums: number[] = [5, 1, 4, 2, 8];
const sortedNums: number[] = insertionSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C#</summary>

```csharp
void InsertionSort(int[] nums) {
    for (int i = 1; i < nums.Length; i++) {
        int key = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
}

int[] nums = { 5, 1, 4, 2, 8 };
InsertionSort(nums); // { 1, 2, 4, 5, 8 }
```

</details>

<br/>

**When to use:** When the dataset is small, or already mostly sorted (e.g. inserting new elements into an already-sorted list one at a time).

<br/>

**Common problems where this is useful:**
- <sub>`Insertion Sort List` — applying the same logic directly to a linked list instead of an array</sub>
- <sub>`Sort an Almost Sorted Array` (general technique) — exploits insertion sort's strong best-case performance on nearly-sorted data</sub>

<br/>
<br/>


## **Merge Sort**
A **divide-and-conquer** sorting algorithm that splits the list in half repeatedly until each piece has one element, then merges those pieces back together in sorted order. <sub>The "merge" step is the key operation — combining two already-sorted lists into one sorted list is `O(n)`, and that's what's repeated at every level of the split.</sub>

> <sub>Guarantees `O(n log n)` in every case (best, average, and worst) — unlike Quick Sort, its performance doesn't depend on the input data's arrangement.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Consistently `O(n log n)`, even in the worst case | Requires `O(n)` extra space, it's not *in-place* |
| Stable (preserves the relative order of equal elements) | Slightly slower in practice than Quick Sort on average, due to the extra memory allocation |
| Works well on linked lists (no random access needed) | |

| Best Case | Average Case | Worst Case | Space |
|------|------|------|------|
|`O(n log n)`|`O(n log n)`|`O(n log n)`|`O(n)`|

<br/>

<sub>* The `O(n)` space comes from needing temporary arrays to hold each half during the merge step. An in-place variant exists but is significantly more complex and rarely used.</sub>

<details>
<summary>Python</summary>

```python
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [5, 1, 4, 2, 8]
sorted_nums = merge_sort(nums)  # [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

vector<int> merge(vector<int>& left, vector<int>& right) {
    vector<int> result;
    int i = 0, j = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) result.push_back(left[i++]);
        else result.push_back(right[j++]);
    }
    while (i < left.size()) result.push_back(left[i++]);
    while (j < right.size()) result.push_back(right[j++]);
    return result;
}

vector<int> mergeSort(vector<int> nums) {
    if (nums.size() <= 1) return nums;

    int mid = nums.size() / 2;
    vector<int> left(nums.begin(), nums.begin() + mid);
    vector<int> right(nums.begin() + mid, nums.end());

    left = mergeSort(left);
    right = mergeSort(right);

    return merge(left, right);
}

vector<int> nums = {5, 1, 4, 2, 8};
vector<int> sortedNums = mergeSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>Java</summary>

```java
import java.util.*;

List<Integer> merge(List<Integer> left, List<Integer> right) {
    List<Integer> result = new ArrayList<>();
    int i = 0, j = 0;
    while (i < left.size() && j < right.size()) {
        if (left.get(i) <= right.get(j)) result.add(left.get(i++));
        else result.add(right.get(j++));
    }
    result.addAll(left.subList(i, left.size()));
    result.addAll(right.subList(j, right.size()));
    return result;
}

List<Integer> mergeSort(List<Integer> nums) {
    if (nums.size() <= 1) return nums;

    int mid = nums.size() / 2;
    List<Integer> left = mergeSort(nums.subList(0, mid));
    List<Integer> right = mergeSort(nums.subList(mid, nums.size()));

    return merge(left, right);
}

List<Integer> nums = Arrays.asList(5, 1, 4, 2, 8);
List<Integer> sortedNums = mergeSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function merge(left: number[], right: number[]): number[] {
    const result: number[] = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) result.push(left[i++]);
        else result.push(right[j++]);
    }
    return [...result, ...left.slice(i), ...right.slice(j)];
}

function mergeSort(nums: number[]): number[] {
    if (nums.length <= 1) return nums;

    const mid = Math.floor(nums.length / 2);
    const left = mergeSort(nums.slice(0, mid));
    const right = mergeSort(nums.slice(mid));

    return merge(left, right);
}

const nums: number[] = [5, 1, 4, 2, 8];
const sortedNums: number[] = mergeSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C#</summary>

```csharp
using System.Collections.Generic;
using System.Linq;

List<int> Merge(List<int> left, List<int> right) {
    List<int> result = new List<int>();
    int i = 0, j = 0;
    while (i < left.Count && j < right.Count) {
        if (left[i] <= right[j]) result.Add(left[i++]);
        else result.Add(right[j++]);
    }
    result.AddRange(left.Skip(i));
    result.AddRange(right.Skip(j));
    return result;
}

List<int> MergeSort(List<int> nums) {
    if (nums.Count <= 1) return nums;

    int mid = nums.Count / 2;
    List<int> left = MergeSort(nums.Take(mid).ToList());
    List<int> right = MergeSort(nums.Skip(mid).ToList());

    return Merge(left, right);
}

List<int> nums = new List<int> { 5, 1, 4, 2, 8 };
List<int> sortedNums = MergeSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<br/>

**When to use:** When you need guaranteed `O(n log n)` performance regardless of input arrangement, stability matters, or you're sorting a linked list (no random access required).

<br/>

**Common problems where this is useful:**
- <sub>`Sort List` — merge sort applied directly to a linked list</sub>
- <sub>`Merge K Sorted Lists` — repeatedly applying the merge step across multiple lists</sub>
- <sub>`Count of Smaller Numbers After Self` — a modified merge sort that counts inversions during the merge step</sub>
- <sub>`Reverse Pairs` — similar inversion-counting trick during the merge step</sub>

<br/>
<br/>


## **Quick Sort**
A **divide-and-conquer** sorting algorithm that picks a **pivot** element, partitions the list so everything smaller is on one side and everything larger is on the other, then recursively sorts each side. <sub>Unlike Merge Sort, the "combining" work happens *before* the recursion (during partitioning), not after — once both sides are sorted, the whole list is already sorted.</sub>

> <sub>The same **partitioning** logic powers **Quickselect** — a related technique for finding the kth smallest/largest element without fully sorting, in `O(n)` average time.</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| `O(n log n)` average, and usually faster in practice than Merge Sort | `O(n²)` worst case (e.g. already-sorted data with a poor pivot choice) |
| In-place (no extra memory needed, aside from recursion stack) | Not stable (can reorder equal elements) |
| | Depends on picking a good pivot |

| Best Case | Average Case | Worst Case | Space |
|------|------|------|------|
|`O(n log n)`|`O(n log n)`|`O(n²)`|`O(log n)`|

<br/>

<sub>* Worst case occurs when the pivot is consistently the smallest or largest element (e.g. always picking the first/last element on already-sorted data). Choosing a random or median pivot avoids this in practice. Space is `O(log n)` for the recursion stack on a balanced split.</sub>

<details>
<summary>Python</summary>

```python
def quick_sort(nums: list[int], low: int = 0, high: int = None) -> list[int]:
    if high is None:
        high = len(nums) - 1

    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

    return nums

def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

nums = [5, 1, 4, 2, 8]
sorted_nums = quick_sort(nums)  # [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

int partition(vector<int>& nums, int low, int high) {
    int pivot = nums[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (nums[j] <= pivot) {
            i++;
            swap(nums[i], nums[j]);
        }
    }
    swap(nums[i + 1], nums[high]);
    return i + 1;
}

void quickSort(vector<int>& nums, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(nums, low, high);
        quickSort(nums, low, pivotIndex - 1);
        quickSort(nums, pivotIndex + 1, high);
    }
}

vector<int> nums = {5, 1, 4, 2, 8};
quickSort(nums, 0, nums.size() - 1); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>Java</summary>

```java
int partition(int[] nums, int low, int high) {
    int pivot = nums[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (nums[j] <= pivot) {
            i++;
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    int temp = nums[i + 1];
    nums[i + 1] = nums[high];
    nums[high] = temp;
    return i + 1;
}

void quickSort(int[] nums, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(nums, low, high);
        quickSort(nums, low, pivotIndex - 1);
        quickSort(nums, pivotIndex + 1, high);
    }
}

int[] nums = {5, 1, 4, 2, 8};
quickSort(nums, 0, nums.length - 1); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function partition(nums: number[], low: number, high: number): number {
    const pivot = nums[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
        if (nums[j] <= pivot) {
            i++;
            [nums[i], nums[j]] = [nums[j], nums[i]];
        }
    }
    [nums[i + 1], nums[high]] = [nums[high], nums[i + 1]];
    return i + 1;
}

function quickSort(nums: number[], low: number = 0, high: number = nums.length - 1): number[] {
    if (low < high) {
        const pivotIndex = partition(nums, low, high);
        quickSort(nums, low, pivotIndex - 1);
        quickSort(nums, pivotIndex + 1, high);
    }
    return nums;
}

const nums: number[] = [5, 1, 4, 2, 8];
const sortedNums: number[] = quickSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C#</summary>

```csharp
int Partition(int[] nums, int low, int high) {
    int pivot = nums[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (nums[j] <= pivot) {
            i++;
            (nums[i], nums[j]) = (nums[j], nums[i]);
        }
    }
    (nums[i + 1], nums[high]) = (nums[high], nums[i + 1]);
    return i + 1;
}

void QuickSort(int[] nums, int low, int high) {
    if (low < high) {
        int pivotIndex = Partition(nums, low, high);
        QuickSort(nums, low, pivotIndex - 1);
        QuickSort(nums, pivotIndex + 1, high);
    }
}

int[] nums = { 5, 1, 4, 2, 8 };
QuickSort(nums, 0, nums.Length - 1); // { 1, 2, 4, 5, 8 }
```

</details>

<br/>

**When to use:** When you need fast average-case sorting in-place, and worst-case performance isn't a major concern (or can be mitigated with a good pivot strategy, like choosing randomly).

<br/>

**Common problems where this is useful:**
- <sub>`Kth Largest Element in an Array` — Quickselect, the partitioning logic from Quick Sort applied without full sorting</sub>
- <sub>`Sort Colors` — a 3-way partition variant (Dutch National Flag problem)</sub>
- <sub>`Sort an Array` — direct application of Quick Sort as a general-purpose sort</sub>

<br/>
<br/>


## **Heap Sort**
A sorting algorithm that first builds a **[max-heap](./README.md#heaps)** from the data, then repeatedly removes the maximum element and places it at the end of the array — shrinking the heap by one each time. <sub>This directly reuses the heap's `O(log n)` remove-max operation, repeated n times.</sub>

> <sub>Unlike Quick Sort and Merge Sort, Heap Sort guarantees `O(n log n)` **and** is in-place — but it's typically slower in practice than Quick Sort due to weaker cache locality (heap operations jump around the array more than Quick Sort's sequential partitioning).</sub>

<br/>

| ✅Pros | ❌Cons |
|------|------|
| Guarantees `O(n log n)` in every case | Not stable (can reorder equal elements) |
| In-place (no extra memory needed) | Slower in practice than Quick Sort due to weaker cache locality |

| Best Case | Average Case | Worst Case | Space |
|------|------|------|------|
|`O(n log n)`|`O(n log n)`|`O(n log n)`|`O(1)`|

<br/>

<sub>* Building the initial heap is `O(n)`, and each of the n removals is `O(log n)` — giving the overall `O(n log n)`.</sub>

<details>
<summary>Python</summary>

```python
def heapify(nums: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def heap_sort(nums: list[int]) -> list[int]:
    n = len(nums)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Repeatedly remove the max, placing it at the end
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

    return nums

nums = [5, 1, 4, 2, 8]
sorted_nums = heap_sort(nums)  # [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C++</summary>

```cpp
#include <vector>
using namespace std;

void heapify(vector<int>& nums, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && nums[left] > nums[largest]) largest = left;
    if (right < n && nums[right] > nums[largest]) largest = right;

    if (largest != i) {
        swap(nums[i], nums[largest]);
        heapify(nums, n, largest);
    }
}

void heapSort(vector<int>& nums) {
    int n = nums.size();

    for (int i = n / 2 - 1; i >= 0; i--) heapify(nums, n, i);

    for (int i = n - 1; i > 0; i--) {
        swap(nums[0], nums[i]);
        heapify(nums, i, 0);
    }
}

vector<int> nums = {5, 1, 4, 2, 8};
heapSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>Java</summary>

```java
void heapify(int[] nums, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && nums[left] > nums[largest]) largest = left;
    if (right < n && nums[right] > nums[largest]) largest = right;

    if (largest != i) {
        int temp = nums[i];
        nums[i] = nums[largest];
        nums[largest] = temp;
        heapify(nums, n, largest);
    }
}

void heapSort(int[] nums) {
    int n = nums.length;

    for (int i = n / 2 - 1; i >= 0; i--) heapify(nums, n, i);

    for (int i = n - 1; i > 0; i--) {
        int temp = nums[0];
        nums[0] = nums[i];
        nums[i] = temp;
        heapify(nums, i, 0);
    }
}

int[] nums = {5, 1, 4, 2, 8};
heapSort(nums); // {1, 2, 4, 5, 8}
```

</details>

<details>
<summary>TypeScript</summary>

```typescript
function heapify(nums: number[], n: number, i: number): void {
    let largest = i;
    const left = 2 * i + 1;
    const right = 2 * i + 2;

    if (left < n && nums[left] > nums[largest]) largest = left;
    if (right < n && nums[right] > nums[largest]) largest = right;

    if (largest !== i) {
        [nums[i], nums[largest]] = [nums[largest], nums[i]];
        heapify(nums, n, largest);
    }
}

function heapSort(nums: number[]): number[] {
    const n = nums.length;

    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) heapify(nums, n, i);

    for (let i = n - 1; i > 0; i--) {
        [nums[0], nums[i]] = [nums[i], nums[0]];
        heapify(nums, i, 0);
    }

    return nums;
}

const nums: number[] = [5, 1, 4, 2, 8];
const sortedNums: number[] = heapSort(nums); // [1, 2, 4, 5, 8]
```

</details>

<details>
<summary>C#</summary>

```csharp
void Heapify(int[] nums, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && nums[left] > nums[largest]) largest = left;
    if (right < n && nums[right] > nums[largest]) largest = right;

    if (largest != i) {
        (nums[i], nums[largest]) = (nums[largest], nums[i]);
        Heapify(nums, n, largest);
    }
}

void HeapSort(int[] nums) {
    int n = nums.Length;

    for (int i = n / 2 - 1; i >= 0; i--) Heapify(nums, n, i);

    for (int i = n - 1; i > 0; i--) {
        (nums[0], nums[i]) = (nums[i], nums[0]);
        Heapify(nums, i, 0);
    }
}

int[] nums = { 5, 1, 4, 2, 8 };
HeapSort(nums); // { 1, 2, 4, 5, 8 }
```

</details>

<br/>

**When to use:** When you need guaranteed `O(n log n)` performance **and** in-place sorting (no extra memory) — a middle ground between Merge Sort's stability/extra memory and Quick Sort's average-case speed/worst-case risk.

<br/>

**Common problems where this is useful:**
- <sub>`Sort an Array` — direct application of Heap Sort as a general-purpose sort</sub>
- <sub>`Kth Largest Element in an Array` — conceptually related, since both rely on the heap's max-extraction property</sub>

<br/>
<br/>