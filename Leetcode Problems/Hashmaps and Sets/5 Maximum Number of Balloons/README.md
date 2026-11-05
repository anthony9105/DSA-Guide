<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/maximum-number-of-balloons/" target="_blank" rel="noreferrer">1189. Maximum Number of Balloons</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Given a string <code>text</code>, you want to use the characters of <code>text</code> to form as many instances of the word <strong>"balloon"</strong> as possible.</p>
<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;"></strong></p>
<pre><strong>Input:</strong> text = "nlaebolko"
<strong>Output:</strong> 1
</pre>

</br>

Example 2
<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;"></strong></p>
<pre><strong>Input:</strong> text = "loonbalxballpoon"
<strong>Output:</strong> 2
</pre>

</br>

Example 3
<pre><strong>Input:</strong> text = "leetcode"
<strong>Output:</strong> 0
</pre>

</br>

Constraints:
<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code> consists of lower case English letters only.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(1)` |

- Use a hashmap to store the characters of `text`, and the frequencies.
- Return the maximum value of the `charCount` of each of the relevant keys: `b`, `a`, `l` (divided by 2, since 2 are needed for each balloon), `o` (divided by 2), and `n`.

<br/>

## **Code**

Python
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # char_count = {t: text.count(t) for t in 'balloon'}
        # char_count['l'] //= 2
        # char_count['o'] //= 2
        # return min(char_count.values())
        char_count = Counter(text)
        
        return min(
            char_count['b'],
            char_count['a'],
            char_count['l'] // 2,
            char_count['o'] // 2,   
            char_count['n']
        )
```
<br/>

C++
```cpp
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> charCount;
        
        for (char ch : text) {
            charCount[ch]++;
        }

        return min({
            charCount['b'],
            charCount['a'],
            charCount['l'] / 2, // since 'l' occurs twice in balloon
            charCount['o'] / 2, // since 'o' occurs twice in balloon
            charCount['n']
        });
    }
};
```
<br/>

Java
```java
class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character, Integer> charCount = new HashMap<>();

        for (char ch : text.toCharArray()) {
            charCount.put(ch, charCount.getOrDefault(ch, 0) + 1);
        }

        // get the counts for the characters needed to form "balloon"
        int countB = charCount.getOrDefault('b', 0);
        int countA = charCount.getOrDefault('a', 0);
        int countL = charCount.getOrDefault('l', 0) / 2;  // Need 2 'l's
        int countO = charCount.getOrDefault('o', 0) / 2;  // Need 2 'o's
        int countN = charCount.getOrDefault('n', 0);

        return Math.min( Math.min(countB, countA), Math.min( Math.min(countL, countO), countN ) );
    }
}
```
<br/>

JavaScript
```javascript
/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    const charCount = {};

    for (const ch of text) {
        charCount[ch] = (charCount[ch] || 0) + 1;
    }

    return Math.min(
        charCount['b'] || 0,
        charCount['a'] || 0,
        Math.floor(charCount['l'] / 2) || 0,
        Math.floor(charCount['o'] / 2) || 0,
        charCount['n'] || 0,
    );
};
```
<br/>