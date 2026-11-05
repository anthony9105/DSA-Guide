<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/ransom-note/description/" target="_blank" rel="noreferrer">383. Ransom Note</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre>

Example 2
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre>

Example 3
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(m + n)` | `O(m)` |

<sub>Where `m` is the length of `magazine` and `n` is the length of `ransomNote`.</sub>

- Fill a hashmap with the magazine characters and their frequencies.
- For each character in `ransomNote`:
  - If the frequency (value) of the key is > 0:
    - Decrease the frequency by 1.
  - Otherwise: return false.
- Return true.

<br/>

## **Code**

Python
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)

        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch] -= 1
            else:
                return False
        
        return True
```
<br/>

C++
```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> hashmap;

        for (char ch : magazine) {
            hashmap[ch]++;
        }

        for (char ch : ransomNote) {
            if (hashmap[ch] > 0) {
                hashmap[ch]--;
            }
            else {
                return false;
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
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> hashmap = new HashMap<>();

        for (char ch : magazine.toCharArray()) {
            // getOrDefault(Object key, V defaultValue)
            hashmap.put(ch, hashmap.getOrDefault(ch, 0) + 1);
        }

        for (char ch : ransomNote.toCharArray()) {
            if (hashmap.getOrDefault(ch, 0) > 0) {
                hashmap.put(ch, hashmap.get(ch) - 1);
            }
            else {
                return false;
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
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    hashmap = {};

    for (const ch of magazine) {
        hashmap[ch] = (hashmap[ch] || 0) + 1;
    }

    for (const ch of ransomNote) {
        if (hashmap[ch] > 0) {
            hashmap[ch]--;
        }
        else {
            return false;
        }
    }

    return true;
};
```
<br/>