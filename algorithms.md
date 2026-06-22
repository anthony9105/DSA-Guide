<h1 align="center" style="font-size: 40px">Key Algorithms</h1>

## Contents
- [**Binary Search**](#binary-search)


<br/>

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