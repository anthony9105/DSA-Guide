<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/valid-sudoku/" target="_blank" rel="noreferrer">36. Valid Sudoku</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Medium-F5A623" alt="Difficulty: Medium"/>
</p>

<p>Determine if a&nbsp;<code>9 x 9</code> Sudoku board&nbsp;is valid.&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:</p>
<ol>
	<li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.</li>
	<li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
	<li>Each of the nine&nbsp;<code>3 x 3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
</ol>
<p><strong>Note:</strong></p>
<ul>
	<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
	<li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.</li>
</ul>

</br>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height: 250px; width: 250px;">
<pre><strong>Input:</strong> board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> true
</pre>


</br>

Example 2
<pre><strong>Input:</strong> board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being modified to <strong>8</strong>. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
</pre>


</br>

Constraints:
<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> is a digit <code>1-9</code> or <code>'.'</code>.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(1)` | `O(1)` |

<sub>O(1) since there is a fixed (constant) amount used.  IF the board size is changing then it is O(n<sup>2</sup>).</sub><br>
<sub>**Time:** 9 rows × 9 columns = O(81) = O(1).</sub><br>
<sub>**Space:** 81 slots (9 rows) + 81 slots (9 columns) + 81 slots (9 boxes) = O(243) = O(1).</sub>

</br>

- { TODO: explain approach, step by step }

<br/>

## **Code**

Python
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create lists of sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num != '.':
                    box_index = (i // 3) * 3 + (j // 3)

                    if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                        return False
                    
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
        return True
```
<br/>

C++
```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        vector<unordered_set<char>> boxes(9);

        for (int i=0; i < 9; i++) {
            for (int j=0; j < 9; j++) {
                char num = board[i][j];
                if (num == '.') continue;

                // calculating the index of the box that the cell is in
                // ex: rows 0-2 and columns 0-2 correspond to box 0
                int boxIndex = (i / 3) * 3 + (j / 3);

                // if num already exists in the corresponding row, column, or box return false
                if (rows[i].count(num) || cols[j].count(num) || boxes[boxIndex].count(num)) {
                    return false;
                }

                // add num to the respective sets
                rows[i].insert(num);
                cols[j].insert(num);
                boxes[boxIndex].insert(num);
            }
        }
        return true;
    }
};
```
<br/>

Java
```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] boxes = new HashSet[9];

        for (int i=0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for (int i=0; i < 9; i++) {
            for (int j=0; j < 9; j++) {
                char num = board[i][j];

                if (num == '.') continue;

                int boxIndex = (i / 3) * 3 + (j / 3);

                if (rows[i].contains(num) || cols[j].contains(num) || boxes[boxIndex].contains(num)) {
                    return false;
                }

                rows[i].add(num);
                cols[j].add(num);
                boxes[boxIndex].add(num);
            }
        }
        return true;
    }
}
```
<br/>

JavaScript
```javascript
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    let rows = Array.from({ length: 9 }, () => new Set());
    let cols = Array.from({ length: 9 }, () => new Set());
    let boxes = Array.from({ length: 9 }, () => new Set());

    for (let i=0; i < 9; i++) {
        for (let j=0; j < 9; j++) {
            const num = board[i][j];

            if (num === '.') continue;

            const boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);

            if (rows[i].has(num) || cols[j].has(num) || boxes[boxIndex].has(num)) {
                return false;
            }

            rows[i].add(num);
            cols[j].add(num);
            boxes[boxIndex].add(num);
        }
    }
    return true;
};
```
<br/>

C#
```csharp
public class Solution {
    public bool IsValidSudoku(char[][] board) {
        HashSet<char>[] rows = new HashSet<char>[9];
        HashSet<char>[] cols = new HashSet<char>[9];
        HashSet<char>[] boxes = new HashSet<char>[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<char>();
            cols[i] = new HashSet<char>();
            boxes[i] = new HashSet<char>();
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char num = board[i][j];

                if (num == '.') continue;

                int boxIndex = (i / 3) * 3 + (j / 3);
                if (rows[i].Contains(num) || cols[j].Contains(num) || boxes[boxIndex].Contains(num)) {
                    return false;
                }

                rows[i].Add(num);
                cols[j].Add(num);
                boxes[boxIndex].Add(num);
            }
        }

        return true;
    }
}
```

