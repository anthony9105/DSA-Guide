<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/roman-to-integer/" target="_blank" rel="noreferrer">13. Roman to Integer</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>
<pre><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two ones added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given a roman numeral, convert it to an integer.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>
Example 1
<pre><strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.
</pre>

Example 2
<pre><strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V= 5, III = 3.
</pre>

Example 3
<pre><strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= s.length &lt;= 15</code></li>
	<li><code>s</code> contains only&nbsp;the characters <code>('I', 'V', 'X', 'L', 'C', 'D', 'M')</code>.</li>
	<li>It is <strong>guaranteed</strong>&nbsp;that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(1)` |


- Use a [hashmap](../../../README.md#hash-maps) to store the 7 symbols and their corresponding values.
- Initialize a variable `sum` to 0.
- Iterate through each character in `s` by index:
  - Check whether subtraction should apply: the current character must be `I`, `X`, or `C`, **and** the next character's value must be exactly 5× or 10× the current character's value (e.g. `IV`, `IX`, `XL`, `XC`, `CD`, `CM`).
  - If subtraction applies, subtract the current character's value from `sum`; otherwise, add it.
- Finally, return `sum`.

</br>

## **Code**

Python
```python
class Solution:
    def useSubtraction(self, mapped_vals, s, i):
        if s[i] not in {'I', 'X', 'C'}:
            return False

        if i >= len(s) - 1:
            return False

        currVal = mapped_vals[s[i]]
        nextVal = mapped_vals[s[i+1]]

        if currVal >= nextVal:
            return False
        
        return nextVal == currVal * 5 or nextVal == currVal * 10


    def romanToInt(self, s: str) -> int:
        sum = 0

        mapped_vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i, character in enumerate(s):
            if self.useSubtraction(mapped_vals, s, i):
                sum -= mapped_vals[s[i]]
            else:
                sum += mapped_vals[s[i]]

        return sum
```
<br/>

C++
```cpp
class Solution {
public:
    bool useSubtraction(unordered_map<char, int> &mappedVals, string &s, int i) {
        // subtraction can only happen if the current character is 'I', 'X', or 'C'
        if (s[i] != 'I' && s[i] != 'X' && s[i] != 'C') return false;
        if (i >= (int)s.size() - 1) return false;

        int currVal = mappedVals[s[i]];
        int nextVal = mappedVals[s[i+1]];

        // check if the next value is greater than currVal AND the next value is a valid 
        // factor of the current value (5 or 10)
        return currVal < nextVal && (nextVal == currVal * 5 || nextVal == currVal * 10);
    }


    int romanToInt(string s) {
        int sum = 0;

        unordered_map<char, int> mappedVals = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}, 
        };

        // for each character in the given string
        for (int i=0; i < s.size(); i++) {
            // use subtraction if the specific conditions are met
            if (useSubtraction(mappedVals, s, i)) {
                sum -= mappedVals[s[i]];
            }
            else {
                sum += mappedVals[s[i]];
            }
        }

        return sum;
    }
};
```