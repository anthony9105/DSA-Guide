<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/summary-ranges/description/" target="_blank" rel="noreferrer">228. Summary Ranges</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>You are given a <strong>sorted unique</strong> integer array <code>nums</code>.</p>
<p>A <strong>range</strong> <code>[a,b]</code> is the set of all integers from <code>a</code> to <code>b</code> (inclusive).</p>
<p>Return <em>the <strong>smallest sorted</strong> list of ranges that <strong>cover all the numbers in the array exactly</strong></em>. That is, each element of <code>nums</code> is covered by exactly one of the ranges, and there is no integer <code>x</code> such that <code>x</code> is in one of the ranges but not in <code>nums</code>.</p>
<p>Each range <code>[a,b]</code> in the list should be output as:</p>
<ul>
	<li><code>"a-&gt;b"</code> if <code>a != b</code></li>
	<li><code>"a"</code> if <code>a == b</code></li>
</ul>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> nums = [0,1,2,4,5,7]
<strong>Output:</strong> ["0-&gt;2","4-&gt;5","7"]
<strong>Explanation:</strong> The ranges are:
[0,2] --&gt; "0-&gt;2"
[4,5] --&gt; "4-&gt;5"
[7,7] --&gt; "7"
</pre>

Example 2
<pre><strong>Input:</strong> nums = [0,2,3,4,6,8,9]
<strong>Output:</strong> ["0","2-&gt;4","6","8-&gt;9"]
<strong>Explanation:</strong> The ranges are:
[0,0] --&gt; "0"
[2,4] --&gt; "2-&gt;4"
[6,6] --&gt; "6"
[8,9] --&gt; "8-&gt;9"
</pre>

Constraints:
<ul>
	<li><code>0 &lt;= nums.length &lt;= 20</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>All the values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(n)` |

- Initialize `start` as the starting value of the first range, `nums[0]`.
- Also initialize `end`, and an empty `ranges` list.
- Iterate for each `num` in `nums` (starting from the second element):
  - If the current `num` is +1 of the previous (`end`):
    - Then we know the current range is not complete, so extend it (`end = num`).
  - Otherwise:
    - Add/append the completed range to `ranges` and reset it -> `start = num` and `end = num`. 
- Add/append whatever range is left at the end to `ranges`.
- Return `ranges`. 

<br/>

## **Code**

Python
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start = nums[0]
        end = nums[0]
        ranges = []

        def add_range(start, end):
            if start == end:
                return str(end)
            else:
                return f"{start}->{end}"
        
        # for each num in nums (starting from 2nd element)
        for num in nums[1:]:
            # if currnt value is +1 of the previous
            if num == end + 1:
                # extend current range
                end = num
            else:
                # add the previous range and reset
                ranges.append(add_range(start, end))
                start = num
                end = num

        # add the last range
        ranges.append(add_range(start, end))

        return ranges
```
<br/>

C++
```cpp
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        // return empty vector if nums is empty
        if (nums.empty()) return {};

        // the start value of the current range
        int start = nums[0];

        // the final summary ranges
        vector<string> ranges;

        // lambda helper function
        auto addRange = [&](int start, int end) {
            // if the start and end of the range are the same, the range 
            // consists of a single number, so just add the one number to ranges
            if (start == end) {
                ranges.push_back(to_string(start));
            }
            // if the start and end are different add to ranges in the format of
            // start->end
            else {
                ranges.push_back(to_string(start) + "->" + to_string(end));
            }
        };

        // loop through nums starting at the 2nd element
        for (int i=1; i < nums.size(); i++) {
            // if the current value isn't +1 of the previous
            if (nums[i] != nums[i-1] + 1) {
                // the range is complete, so use addRange
                addRange(start, nums[i-1]);

                // start a new range
                start = nums[i];
            }
        }

        // add the last range
        addRange(start, nums.back());

        return ranges;
    }
};
```
<br/>


JavaScript
```javascript
var summaryRanges = function(nums) {
    if (nums.length === 0) return [];

    var start = nums[0];
    var ranges = [];

    // loop through nums with an extra iteration for the last range,
    // starting from the 2nd element
    for (var i = 1; i <= nums.length; i++) {
        // if at the end of the array OR the current value is NOT +1 of the previous
        if (i === nums.length || nums[i] !== nums[i - 1] + 1) {
            // if the start and end of the range are the same, the range 
            // consists of a single number, so just add the one number to ranges 
            if (start === nums[i - 1]) {
                ranges.push(`${start}`);
            }
            // if the start and end are different add to ranges in the format of
            // start->end
            else {
                ranges.push(`${start}->${nums[i - 1]}`);
            }

            // update start to the current number
            start = nums[i];
        }
    }

    return ranges;
};
```

<br/>
