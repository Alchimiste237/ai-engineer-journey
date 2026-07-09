"""product_except_self.py

Exercise: Write a function product_except_self(lst) that returns a new list where
each element is the product of all other elements WITHOUT using division.

Typical constraint/insight:
- If you tried to use division, you'd need to handle zeros carefully.
- The intended O(n) solution uses prefix products and suffix products.

Approach (O(n) without division):
1) Prefix products:
   prefix[i] = product of lst[0..i-1] (elements before i)
2) Suffix products:
   suffix[i] = product of lst[i+1..end] (elements after i)
3) Result:
   result[i] = prefix[i] * suffix[i]

We can do it with O(1) extra space beyond the output by:
- storing prefix products in the output array
- multiplying by a running suffix product from the right.

Complexity:
- Time:  O(n)
- Space: O(1) extra (not counting output), O(n) if you explicitly build prefix/suffix arrays.
"""

from __future__ import annotations

from typing import List


def product_except_self(lst: List[int]) -> List[int]:
    """Return array where result[i] is the product of all elements except lst[i]."""

    n = len(lst)
    if n == 0:
        return []

    # res[i] will first store prefix products (product of elements before i).
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= lst[i]

    # Now multiply each res[i] by the suffix product (product of elements after i).
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= lst[i]

    return res


if __name__ == "__main__":
    data = [1, 2, 3, 4]
    print(product_except_self(data))  # Expected: [24, 12, 8, 6]

    data_with_zero = [1, 2, 0, 4]
    print(product_except_self(data_with_zero))  # Expected: [0, 0, 8, 0]

