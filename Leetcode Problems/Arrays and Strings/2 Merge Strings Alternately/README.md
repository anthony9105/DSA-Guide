<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <a href="https://leetcode.com/problems/merge-strings-alternately/description/"><h1 align="center" style="font-size: 35px">1768. Merge Strings Alternately</h1></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>
<p>Return <em>the merged string.</em></p>


<details>
<summary>Examples and Constraints</summary>
<br/>
Example 1
<pre><strong>Input:</strong> word1 = "abc", word2 = "pqr"
<strong>Output:</strong> "apbqcr"
<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

Example 2
<pre><strong>Input:</strong> word1 = "ab", word2 = "pqrs"
<strong>Output:</strong> "apbqrs"
<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(1)` |


- Iterate while `i` < `word1 length` and `j` < `word2 length`:
  - Append the character of `word1` at index `i` to the end of `merged_word` and then increment `i`
  - Append the character of `word2` at index `j` to the end of `merged_word` and then increment `j`
- If `word1` and `word2` are not the same length one of them will still have remaining characters.
- Iterate while `i` < `word1 length`:
  - Append the character of word1 at index `i` to the end of `merged_word` and then increment `i`.
- Repeat this process but for `word2` with `j`.
- Finally, return `merged_word`.

</br>

## **Code**

Python
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged_word += word1[i]
            merged_word += word2[j]

            i += 1
            j += 1

        while i < len(word1):
            merged_word += word1[i]
            i += 1
        while j < len(word2):
            merged_word += word2[j]
            j += 1
        
        return merged_word
```
<br/>

C++
```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string mergedWord = "";
        int i = 0, j = 0;

        // loop through adding the characters one by one
        // until the end of one (or both) of the words
        while (i < word1.size() && j < word2.size()) {
            mergedWord += word1[i++];
            mergedWord += word2[j++];
        }

        // if theres any remaining characters add them
        // (happens to one of the words if their lengths
        // are different)
        while (i < word1.size()) {
            mergedWord += word1[i++];
        }
        while (j < word2.size()) {
            mergedWord += word2[j++];
        }

        return mergedWord;
    }
};
```