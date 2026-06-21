<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <a href="https://leetcode.com/problems/find-closest-number-to-zero/description/"><h1 align="center" style="font-size: 35px">2239. Find Number Closest to Zero</h1></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

Given an integer array `nums` of size `n`, return *the number with the value **closest** to* `0` *in* `nums`. If there are multiple answers, return *the number with the **largest** value.*

<details>
<summary>Examples and Constraints</summary>
<br/>
Example 1
<pre><strong>Input:</strong> nums = [-4,-2,1,4,8]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
</pre>

Example 2
<pre><strong>Input:</strong> nums = [2,-1,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</details>


## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(1)` |

- Set `closest` to the first number in the list.
- Iterate through each number `x` in the list `nums`:
  - If `x`'s absolute value is less than `closest` **OR** if both absolute values are the same *but* `x` is greater than the current `closest`:
    - Update `closest` to `x`, <sub>since a closer number (or a tie with a larger value) has been found.</sub>  
- Finally, return `closest`.

## **Code**

Python
```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for x in nums:
            if (abs(x) < abs(closest) or
                abs(x) == abs(closest) and x > closest):
                closest = x
            
        return closest
```

C++
```cpp
class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int closestNum = nums[0];

        for (int x : nums) {
            if (abs(x) < abs(closestNum) ||
                abs(x) == abs(closestNum) && x > closestNum) {
                closestNum = x;
            }
        }

        return closestNum;
    }
};
```