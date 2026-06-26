<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/spiral-matrix/description/" target="_blank" rel="noreferrer">54. Spiral Matrix</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Medium-F5A623" alt="Difficulty: Medium"/>
</p>

<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;">
<pre><strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<br/>

Example 2

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;">
<pre><strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

Constraints:
<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n * m)` | `O(n)` |

<sub>Where `m` is the number of rows in `matrix` and `n` is the number of columns (length of each inner list, such as `matrix[0]`).</sub>

- Define 4 boundaries: `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.
- Iterate until the length of `order` reaches the same size as `matrix` (until `order` is complete):
  - **Left to right:** 
    - Iterate from the `left` to the `right` at just the `top` boundary, appending each element to `order`.  
    - When done, `top` boundary is moved down by 1 (increase `top` by 1).
  - **Top to bottom:** 
    - Iterate from the `top` to the `bottom` at just the `right` boundary, appending each element to `order`.  
    - When done, `right` boundary is moved left by 1 (decrease `right` by 1).
  - **If there is still rows left (`if top <= bottom`):**
    - **Right to left:** 
      - Iterate from the `right` to the `left` at just the `bottom` boundary, appending each element to `order`.  
      - When done, `bottom` boundary is moved up by 1 (decrease `bottom` by 1).
  - **If there is still columns left (`if left <= right`):**
    - **Bottom to top:** 
      - Iterate from the `bottom` to the `top` at just the `left` boundary, appending each element to `order`.  
      - When done, `left` boundary is moved right by 1 (increase `left` by 1).
- Return `order`.

<br/>

## **Code**

Python
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []

        if len(matrix) is 0:
            return order
        
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m-1
        left = 0
        right = n-1

        while len(order) < m*n:
            for j in range(left, right + 1):
                order.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                order.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    order.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    order.append(matrix[i][left])
                left += 1

        return order
```
<br/>

C++
```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> order;

        if (matrix.empty()) return order;

        int m = matrix.size();      // rows
        int n = matrix[0].size();   // columns

        // representations of the current boundaries of the matrix
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;

        // while the size of order is not the size of the m*n dimensions
        // of the matrix
        while (order.size() != m*n) {
            // traverse from left to right and update top
            for (int j = left; j <= right; j++) {
                order.push_back(matrix[top][j]);
            }
            top++;

            // traverse from top to bottom and update right
            for (int i = top; i <= bottom; i++) {
                order.push_back(matrix[i][right]);
            }
            right--;

            // traverse from right to left (if applicable)
            // and update bottom
            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    order.push_back(matrix[bottom][j]);
                }
                bottom--;
            }

            // traverse from bottom to top (if applicable)
            // and update left 
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    order.push_back(matrix[i][left]);
                }
                left++;
            }
        }

        return order;
    }
};
```
<br/>

