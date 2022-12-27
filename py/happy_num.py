class Solution:

    def isHappy(self, n: int) -> bool:
        def calculate_sum_of_dig_squared(n: int):
            if n % 10 == n:
                return n ** 2
            return calculate_sum_of_dig_squared((n - (n % 10)) / 10) + (n % 10) ** 2 
        list_of_dig = []
        current_num = n
        while True:
            current_num = calculate_sum_of_dig_squared(current_num)
            if current_num == 1:
                return True
            if current_num in list_of_dig:
                return False
            else:
                list_of_dig.append(current_num)