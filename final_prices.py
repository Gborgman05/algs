# O(n^2) time, O(n) space
# tried stack, but that didn't do any better than brute force
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        final = [0] * len(prices)
        filled = 0
        for i in range(len(prices)):
            price = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] <= price:
                    price = price - prices[j]
                    break
            final[i] = price
        return final
            
        #     if not stack:
        #         stack.append(price)
        #     else:
        #         while stack and stack[-1] >= price:
        #             i = len(stack) + filled
        #             final[i] = stack.pop() - price
        #             filled += 1
        #         stack.append(price)
        # return final