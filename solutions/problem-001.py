class Solution:
	def solve(self, numbers: list, target: int):
		for number in numbers:
			difference = target - number

			if difference in numbers:
				return True

		return False
		

solution = Solution()

# There are no integers in the list. Therefore it is impossible to produce the target integer and the function should return False.
assert solution.solve([], 17) == False


# There is a pair of integers that will produce the target integer, 17, which are integers 10 and 7. Therefore, the function should return True.
assert solution.solve([10, 15, 3, 7], 17) == True


# There are no pairs of integers that will produce the target integer, 17. Therefore, the function should return False.
assert solution.solve([10, 15, 3, 4], 17) == False


# There is a pair of integers that will produce the target inteher, 1, which are integers 3 and -2. Therefore, the function should return True.
assert solution.solve([2, 5, 3, -2], 1)