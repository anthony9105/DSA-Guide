<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/is-subsequence/description/" target="_blank" rel="noreferrer">392. Is Subsequence</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>subsequence</strong> of </em><code>t</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>"ace"</code> is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code> while <code>"aec"</code> is not).</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre>

Example 2
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>

Constraints:
<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(1)` |

- Use an index variable `j` for string `s`.
- Iterate through each character in `t` by index:
  - If the current characters match, increase `j`.
  - If all the elements in `s` are reached (if `j` equals the length of `s`), return `true` since that means `s` is a subsequence of `t`.
- If this point is reached it means `s` is *NOT* a subsequence of `t`, so return `false`. 

<br/>

## **Code**

Python
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        if len(s) is 0:
            return True
        
        for letter in t:
            if letter == s[j]:
                j += 1
            
            if j == len(s):
                return True
            
        return False
```
<br/>

C++
```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        // index for s
        int j=0;

        // if s is empty ""
        if (s.size() == 0) {
            return true;
        }

        // for loop to go through each index of t
        for (int i=0; i < t.size(); i++) {
            // if the characters match, increase j
            if (s[j] == t[i]) {
                j++;
            }

            // if j gets through all the elements in s
            // return true
            if (j == s.size()) {
                return true;
            } 
        }

        return false;
    }
};
```
<br/>

Java
```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        int j=0;

        if (s.length() == 0) return true;

        for (char ch: t.toCharArray()) {
            if (ch == s.charAt(j)) {
                j++;
            }

            if (j == s.length()) return true;
        }

        return false;
    }
}
```
<br/>

TypeScript
```typescript
function isSubsequence(s: string, t: string): boolean {
    var j: number = 0;

    if (s.length === 0) return true;

    for (const ch of t as string) {
        if (ch === s[j]) j++;

        if (j === s.length) return true;
    }

    return false;
};
```
<br/>

C#
```csharp
public class Solution {
    public bool IsSubsequence(string s, string t) {
        int j = 0;

        if (s.Length == 0) {
            return true;
        }

        foreach (char letter in t) {
            if (letter == s[j]) {
                j++;
            }

            if (j == s.Length) {
                return true;
            }
        }

        return false;
    }
}
```

