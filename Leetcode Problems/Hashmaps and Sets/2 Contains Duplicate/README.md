<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/contains-duplicate/description/" target="_blank" rel="noreferrer">217. Contains Duplicate</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> The element 1 occurs at the indices 0 and 3.
</pre>

<br/>


Example 2
<pre><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span>
<strong>Output:</strong> <span class="example-io">false</span>
<strong>Explanation:</strong></pre>

<br/>

Constraints:
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(n)` |

- Use a set to keep track of elements we've seen
- For each num in nums:
  - If num is in the set already, return true
  - Otherwise add num to the set
- Return false

<br/>

## **Code**

Python
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
```
<br/>

C++
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (int num : nums) {
            // if num is found in the set
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }

        return false;
    }
};
```
<br/>

Java
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }

        return false;
    }
}
```
<br/>

JavaScript
```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const seen = new Set();

    for (const num of nums) {
        if (seen.has(num)) {
            return true;
        }
        seen.add(num);
    }

    return false;
};
```
<br/>
