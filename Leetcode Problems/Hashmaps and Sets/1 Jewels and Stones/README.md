<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/jewels-and-stones/" target="_blank" rel="noreferrer">771. Jewels and Stones</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>You're given strings <code>jewels</code> representing the types of stones that are jewels, and <code>stones</code> representing the stones you have. Each character in <code>stones</code> is a type of stone you have. You want to know how many of the stones you have are also jewels.</p>

<p>Letters are case sensitive, so <code>"a"</code> is considered a different type of stone from <code>"A"</code>.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> jewels = "aA", stones = "aAAbbbb"
<strong>Output:</strong> 3
</pre>

Example 2
<pre><strong>Input:</strong> jewels = "z", stones = "ZZ"
<strong>Output:</strong> 0
</pre>

Constraints:
<ul>
	<li><code>1 &lt;=&nbsp;jewels.length, stones.length &lt;= 50</code></li>
	<li><code>jewels</code> and <code>stones</code> consist of only English letters.</li>
	<li>All the characters of&nbsp;<code>jewels</code> are <strong>unique</strong>.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(j + s)` <br/> <sub>simply `O(n)`</sub> | `O(j)` <br/> <sub>simply `O(n)`</sub> |

<sub>Where `j` is the length of `jewels`, and `s` is the length of `stones`.</sub>

- Create a set, `jewel_set`, with all the characters in `jewels`.
- Initialize `count` to 0.
- Iterate through each character `stone` in `stones`:
  - If `stone` is in `jewel_set`:
    - Increment `count` by 1.
- Return `count`.

<br/>

## **Code**

Python
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)

        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1
        
        return count
```
<br/>

C++
```cpp
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_set<char> jewelSet(jewels.begin(), jewels.end());

        int count = 0;
        for (char stone : stones) {
            if (jewelSet.find(stone) != jewelSet.end()) {
                count++;
            }
        }

        return count; 
    }
};
```
<br/>

Java
```java
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashSet<Character> jewelSet = new HashSet<>();

        for (char jewel : jewels.toCharArray()) {
            jewelSet.add(jewel);
        }

        int count = 0;
        for (char stone : stones.toCharArray()) {
            if (jewelSet.contains(stone)) {
                count++;
            }
        }

        return count;
    }
}
```
<br/>

JavaScript
```javascript
var numJewelsInStones = function(jewels, stones) {
    const jewelSet = new Set(jewels);
    let count = 0;

    for (const stone of stones) {
        if (jewelSet.has(stone)) {
            count++;
        }
    }

    return count;
};
```
<br/>
