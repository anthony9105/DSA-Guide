<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/valid-anagram/" target="_blank" rel="noreferrer">242. Valid Anagram</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_mq_" data-state="closed" class="" fdprocessedid="eph7ws">anagram</button></span> of <code>s</code>, and <code>false</code> otherwise.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> <span class="example-io">s = "anagram", t = "nagaram"</span>
<strong>Output:</strong> <span class="example-io">true</span>
</pre>

Example 2
<pre><strong>Input:</strong> <span class="example-io">s = "rat", t = "car"</span>
<strong>Output:</strong> <span class="example-io">false</span>
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(m + n)` | `O(1)` |

- If `s` and `t` are not the same size/length, return false since it would be impossible for them to be anagrams.
- Use a hashmap to store the characters and the frequencies of `s` (or `t` instead).
- Loop through each character in `t` (or `s` instead):
  - If the character is not in the hashmap, or its frequency is 0, return false.
  - Decrease the frequency of that character in the hashmap by 1.
- Return true.

<br/>

## **Code**

Python
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
```
<br/>

C++
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> charCount;

        for (char ch: s) {
            charCount[ch]++;
        }

        for (char ch: t) {
            if (charCount.find(ch) == charCount.end() || charCount[ch] == 0) {
                return false;
            }
            charCount[ch]--;
        }

        return true;
    }
};
```
<br/>

Java
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> charCount = new HashMap<>();

        for (char ch : s.toCharArray()) {
            charCount.put(ch, charCount.getOrDefault(ch, 0) + 1);
        } 

        for (char ch : t.toCharArray()) {
            if (!charCount.containsKey(ch) || charCount.get(ch) == 0) {
                return false;
            }
            charCount.put(ch, charCount.get(ch) - 1);
        }

        return true;
    }
}
```
<br/>

JavaScript
```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    charCount = {};

    for (const ch of s) {
        charCount[ch] = (charCount[ch] || 0) + 1;
    }

    for (const ch of t) {
        // if ch is not in charCount or count is 0
        if (!charCount[ch]) {
            return false;
        }
        charCount[ch]--;
    }

    return true;
};
```
<br/>
