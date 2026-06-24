<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/product-of-array-except-self/description/" target="_blank" rel="noreferrer">238. Product of Array Except Self</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Medium-F5A623" alt="Difficulty: Medium"/>
</p>

<p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>



<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre>

Example 2
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>

Constraints:
<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The input is generated such that <code>answer[i]</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(n)` |

The trick is that for each position, you need the `(product of everything to the left)` x the `(product of everything to the right)`.

For example if `nums = [1, 2, 3, 4]`:
- For 1, answer = 2 × 3 × 4 = `24`
- For 2, answer = 1 × 3 × 4 = `12`
- For 3, answer = 1 × 2 × 4 = `8`
- For 4, answer = 1 × 2 × 3 = `6`

| i | nums[i] | product except self |
| - | ------- | ------------------- |
| 0 | 1       | 2 × 3 × 4 = `24`    |
| 1 | 2       | 1 × 3 × 4 = `12`    |
| 2 | 3       | 1 × 2 × 4 = `8`     |
| 3 | 4       | 1 × 2 × 3 = `6`     |


<br/>

-------------

Instead of multiplying all numbers except the current one every time (which would be `O(n²)`), we compute the left and right products separately:

| i | nums[i] | | left product  |
| :-: |:--: |:---------: | -------------: |
| 0 | 1 | [ `1`, &nbsp;2, &nbsp;3, &nbsp;4 ]       | <sub>(nothing on the left)</sub> `1`  |
| 1 | 2 | [ <u>1</u>, &nbsp;`2`, &nbsp;3, &nbsp;4 ]        | `1`             |
| 2 | 3 | [ <u>1, &nbsp;2</u>, &nbsp;`3`, &nbsp;4 ]        | 1 × 2 = `2`     |
| 3 | 4 | [ <u>1, &nbsp;2, &nbsp;3</u>, &nbsp;`4` ]        | 1 × 2 × 3 = `6` |


`Left products` = `[1, 1, 2, 6]`

-------

<br/>

| i | nums[i] | | right product  |
| :-: |:---: |:---------: | --------------: |
| 0 | 1 | [ &nbsp;`1`, &nbsp;<u>2, &nbsp;3, &nbsp;4</u> ]       | 2 × 3 × 4 = `24` |
| 1 | 2 | [ &nbsp;1, &nbsp;`2`, &nbsp;<u>3, &nbsp;4</u> ]       | 3 × 4 = `12`    |
| 2 | 3 | [ &nbsp;1, &nbsp;2, &nbsp;`3`, &nbsp;<u>4</u> ]       | `4`          |
| 3 | 4 | [ &nbsp;1, &nbsp;2, &nbsp;3, &nbsp;`4` ]       | <sub>(nothing on the right)</sub> `1`  |


`Right products` = `[24, 12, 4, 1]`

Finally: **`answer`** = `[1 x 24, 1 x 12, 2 x 4, 6 x 1]` = **`[24, 12, 8, 6]`**

<br/>
<br/>

Process:
- Initialize a `left` and `right` product to 1 to start.
- First get the `left` products array and store it in `answer`, by iterating through each `num` in `nums`:
  - Keep in mind that the first element here will always be 1 since there will be nothing to its left.
  - Simplify the calculation for the `left` product as itself multiplied current `num`.
- Now in the same way get the `right` products but to save time this can also be combined with the final step of multiplying corresponding the `left` and `right` product elements by each other to get the final answer.
- Return `answer`.

<br/>

## **Code**

Python
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        answer = []
        left = 1
        right = 1

        for num in nums:
            answer.append(left)
            left *= num
        
        for i in reversed(range(N)):
            answer[i] *= right
            right *= nums[i]
        
        return answer
```
<br/>

C++
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // nums size
        const int N = nums.size();

        vector<int> answer(N);
        int leftProduct = 1;
        int rightProduct = 1;

        // calculate left products and add them as the
        // elements in answer
        for (int i=0; i < N; i++) {
            answer[i] = leftProduct;
            leftProduct *= nums[i];
        }

        // calculate right products and multiply
        // them by the corresponding left products
        // which are in answer.
        // (Goes from right to left)
        for (int j=N-1; j >= 0; j--) {
            answer[j] *= rightProduct;
            rightProduct *= nums[j];
        }

        return answer;
    }
};
```
<br/>

Java
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        final int N = nums.length;

        int[] answer = new int[N];
        int left = 1;
        int right = 1;

        for (int i = 0; i < N; i++) {
            answer[i] = left;
            left *= nums[i];
        }

        for (int i = N-1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }

        return answer;
    }
}
```
<br/>

JavaScript
```javascript
var productExceptSelf = function(nums) {
    const N = nums.length;

    var answer = []
    var left = 1;
    var right = 1;

    for (const num of nums) {
        answer.push(left);
        left *= num;
    }

    for (var i= N-1; i >= 0; i--) {
        answer[i] *= right;
        right *= nums[i];
    }

    return answer;
};
```
<br/>

