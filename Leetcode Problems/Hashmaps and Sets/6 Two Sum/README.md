<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/two-sum/" target="_blank" rel="noreferrer">1. Two Sum</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Medium-F5A623" alt="Difficulty: Medium"/>
</p>

<p>You are given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>
<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>
<p>You can return the answer in any order.</p>


<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

> [!NOTE]Example 1
> <p><strong>Input:</strong> <code>nums = [2,7,11,15], target = 9</code></p>
> <p><strong>Output:</strong> <code>[0,1]</code></p>
> <p><strong>Explanation:</strong></p>
> <p>The sum of <code>nums[0]</code> and <code>nums[1]</code> is <code>2 + 7 = 9</code>, which equals the target. Therefore, the indices <code>[0, 1]</code> are returned.</p>

</br>

> [!TIP]Example 2
> <p><strong>Input:</strong> <code>nums = [3,2,4], target = 6</code></p>
> <p><strong>Output:</strong> <code>[1,2]</code></p>
> <p><strong>Explanation:</strong></p>
> <p>The sum of <code>nums[1]</code> and <code>nums[2]</code> is <code>2 + 4 = 6</code>, which equals the target. Therefore, the indices <code>[1, 2]</code> are returned.</p>

</br>

> [!NOTE]Example 3
> <p><strong>Input:</strong> <code>nums = [3,3], target = 6</code></p>
> <p><strong>Output:</strong> <code>[0,1]</code></p>
> <p><strong>Explanation:</strong></p>
> <p>The sum of <code>nums[0]</code> and <code>nums[1]</code> is <code>3 + 3 = 6</code>, which equals the target. Therefore, the indices <code>[0, 1]</code> are returned.</p>

</br>

Constraints:
<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(n)` |

- Use hashmap, `visited`, to track the numbers that have been visited (keys will be the numbers, values will be their index).
- Loop through `nums`:
  - Calculate the remaining value needed with the current `num`, (`target - num`).
  - If this remaining value is found in `visited`, return that index and the current one as the result.
  - Otherwise add `num` and the corresponding index to `visited`.

<br/>

## **Code**

Python
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            remaining = target - num

            if remaining in visited:
                return [i, visited[remaining]]

            visited[num] = i
```
<br/>

C++
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> visited;

        for (int i=0; i < nums.size(); i++) {
            int remaining = target - nums[i];

            if (visited.find(remaining) != visited.end()) {
                return {i, visited.find(remaining)->second};
            }
            // visited.insert({nums[i], i});
            visited[nums[i]] = i;
        }

        throw invalid_argument("No twoSum solution");
    }
};
```
<br/>

Java
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> visited = new HashMap<>();

        for (int i=0; i < nums.length; i++) {
            int remaining = target - nums[i];

            if (visited.containsKey(remaining)) {
                return new int[] {i, visited.get(remaining)};
            }
            visited.put(nums[i], i);
        }

        throw new IllegalArgumentException("No two sum solution");
    }
}
```
<br/>

JavaScript
```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const visited = new Map();

    for (let i=0; i < nums.length; i++) {
        const remaining = target - nums[i];

        if (visited.has(remaining)) {
            return [i, visited.get(remaining)];
        }
        
        visited.set(nums[i], i);
    } 

    throw new Error("No twoSum solution");
};
```
<br/>

C#
```csharp
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> visited = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            int remaining = target - nums[i];

            if (visited.ContainsKey(remaining)) {
                return [visited[remaining], i];
            }

            visited[nums[i]] = i;
        }

        throw new InvalidOperationException("No TwoSum solution");
    }
}
```

