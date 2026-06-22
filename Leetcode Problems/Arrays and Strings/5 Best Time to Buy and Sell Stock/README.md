<p align="center">
  <img src="../../LC_logo.png" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank" rel="noreferrer">121. Best Time to Buy and Sell Stock</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy"/>
</p>

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

Example 2
<pre><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

Constraints:
<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O(n)` | `O(1)` |

- Initialize `min_price` to infinity (or max int), and `max_profit` to 0.
- Iterate through each `price` in `prices`:
  - If the current `price` is less than `min_price`:
    - Set `min_price = price`.
  - Calculate what the `profit` would be using the current `price` as the sell price and `min_price` as the buy price.
  - If this calculated `profit` is greater than `max_profit`:
    - Set `max_profit = profit`.
- Return `max_profit`. 

<br/>

## **Code**

Python
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit
```
<br/>

C++
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // set minPrice to the max int value and
        // maxProfit to 0
        int minPrice = INT_MAX;
        int maxProfit = 0;

        // for each price in the list
        for (int price : prices) {
            // if the current price is less than minPrice,
            // update minPrice to be the current price
            if (price < minPrice) minPrice = price;

            // get the profit of the current price (sell price)
            // minus the minPrice (the buy price)
            int profit = price - minPrice;

            // if the current profit is greater than maxProfit,
            // update the maxProfit to be the current profit
            if (profit > maxProfit) maxProfit = profit;
        }

        return maxProfit;
    }
};
```
<br/>

TypeScript
```typescript
function maxProfit(prices: number[]): number {
    var minPrice: number = Infinity;
    var maxProfit: number = 0;

    for (const price of prices) {
        if (price < minPrice) minPrice = price;

        const profit: number = price - minPrice;

        if (profit > maxProfit) maxProfit = profit;
    }

    return maxProfit;
};
```
<br/>