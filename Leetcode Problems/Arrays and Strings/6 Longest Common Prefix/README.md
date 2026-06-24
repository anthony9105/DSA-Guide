<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/longest-common-prefix/description/" target="_blank" rel="noreferrer">14. Longest Common Prefix</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>
<p>If there is no common prefix, return an empty string <code>""</code>.</p>


<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

Example 2
<pre><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n * m)` | `O(1)` |

<sub>Where `m` is the number of strings/words in `strs` and `n` is the length of the shortest string.</sub>

<br/>

- Initialize `shortest_str_len` to infinity (or max int).
- Iterate through each `word` in `strs`:
  - Update `shortest_str_len` with the shortest `word`'s length.
- Initialize `char_index` to 0.
- Iterate while `char_index` < `shortest_str_len`:
  - Iterate for each index of `strs` (starting with the second index (1)):
    - If the current characters don't match (we have reached an end to the substring):
      - Return the substring of `strs[0]` from the beginning to whatever was previously reached (`char_index`).
    - Increment `char_index` by 1.
- Return the substring `strs[0][:charIndex]` (index 0 to `char_index`).

<br/>

## **Code**

Python
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) is 0:
            return ""

        shortest_str_len = float('inf')

        for word in strs:
            shortest_str_len = min(shortest_str_len, len(word))
        
        char_index = 0
        while char_index < shortest_str_len:
            curr_char = strs[0][char_index]

            for str_index in range(1, len(strs)):
                if strs[str_index][char_index] != curr_char:
                    return strs[0][:char_index]
            
            char_index += 1
        
        return strs[0][:char_index]
```
<br/>

C++
```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        int shortestStrLen = INT_MAX;

        // get the shortest string in the list
        for (const string& str: strs) {
            shortestStrLen = min(shortestStrLen, static_cast<int>(str.size()));
        }

        int charIndex = 0;
        // while the character index is less than the shortest string 
		// in the list
        while (charIndex < shortestStrLen) {
            // current character to compare to
            char currentChar = strs[0][charIndex];

            // for each string in the list
            for (int strIndex=1; strIndex < strs.size(); strIndex++) {
                // if the characters are not equal
                if (strs[strIndex][charIndex] != currentChar) {
                    return strs[0].substr(0, charIndex);
                }
            }
            charIndex++;
        }
        return strs[0].substr(0, charIndex);
    }
};
```
<br/>

Java
```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        int shortestStrLen = Integer.MAX_VALUE;

        for (String str: strs) {
            shortestStrLen = Math.min(shortestStrLen, str.length());
        }

        int charIndex = 0;
        while (charIndex < shortestStrLen) {
            char currentChar = strs[0].charAt(charIndex);
            for (int strIndex = 0; strIndex < strs.length; strIndex++) {
                if (currentChar != strs[strIndex].charAt(charIndex)) {
                    return strs[0].substring(0, charIndex);
                }
            }
            charIndex++;
        }
        return strs[0].substring(0, charIndex);
    }
}
```
<br/>

TypeScript
```typescript
function longestCommonPrefix(strs: string[]): string {
    if (strs.length === 0) return "";

    var shortestStrLen: number = Infinity;

    for (const word of strs) {
        shortestStrLen = (word.length < shortestStrLen) ? word.length : shortestStrLen;
    }

    var charIndex: number = 0;
    while (charIndex < shortestStrLen) {
        const currChar: string = strs[0][charIndex];

        for (var strIndex:number = 0; strIndex < strs.length; strIndex++) {
            if (strs[strIndex][charIndex] != currChar) {
                return strs[0].substring(0, charIndex);
            }
        }

        charIndex++;
    }

    return strs[0].substring(0, charIndex);
};
```
<br/>