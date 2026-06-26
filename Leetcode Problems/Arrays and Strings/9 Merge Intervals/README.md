<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/merge-intervals/description/" target="_blank" rel="noreferrer">56. Merge Intervals</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Medium-F5A623" alt="Difficulty: Medium"/>
</p>

<p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>


<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
</pre>

Example 2
<pre><strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

Example 3
<pre><strong>Input:</strong> intervals = [[4,7],[1,4]]
<strong>Output:</strong> [[1,7]]
<strong>Explanation:</strong> Intervals [1,4] and [4,7] are considered overlapping.
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(nlogn)` | `O(n)` |

- Sort the intervals by the first element (start) values in ascending order.  (`nlogn`).
- Initialize a `list[list[int]]` with `intervals[0]`.
- For each `interval` in `intervals` (can skip the first interval as its already in):
  - If the "end" part of last interval in `output` is $\ge$ the "start" value of `interval`:
    - Update it with the maximum value between itself and the "end" value of the current `interval`, to "merge" these intervals.
  - Otherwise:
    - Append `interval` to `output` snce it belongs as a completely new interval.
- Return `output`.

<br/>

## **Code**

Python
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by the first element in 
		# each List[int] (interval)
        intervals.sort(key = lambda interval: interval[0])

        # start output with the first interval
        output = [intervals[0]]

        for interval in intervals:
            # if the 'end' of the last interval in output, is 
            # greater than/equal to the 'start' of the current
            # interval (if there is overlap), then update the 
            # 'end' of the interval in output
            if output[-1][1] >= interval[0]:
                output[-1][1] = max(output[-1][1], interval[1])
            # if there's no overlap, add a new interval to output
            else:
                output.append(interval)
        
        return output
```
<br/>

C++
```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> output;

        if (intervals.empty()) return output;

        // sort intervals by start time
        sort(intervals.begin(), intervals.end());

        // have output start with the first interval
        output.push_back(intervals[0]);

        // for each index of intervals (starting from the 2nd element)
        for (int i = 1; i < intervals.size(); i++) {
            // if the 2nd number of the last interval in output is
            // greater than or equal to the current interval, merge them
            if (output.back()[1] >= intervals[i][0]) {
                output.back()[1] = max(output.back()[1], intervals[i][1]);
            }
            // just add the interval normally if there's no overlap
            else {
                output.push_back(intervals[i]);
            }
        }

        return output;
    }
};
```
<br/>


JavaScript
```javascript
var merge = function(intervals) {
    // sort by the first element of each interval (ascending)
    intervals.sort((a, b) => a[0] - b[0]);

    output = [intervals[0]];

    for (const interval of intervals) {
        if (output.at(-1)[1] >= interval[0]) {
            output.at(-1)[1] = Math.max(output.at(-1)[1], interval[1]);
        }
        else {
            output.push(interval);
        }
    }

    return output;
};
```
<br/>
