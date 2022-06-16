class Solution:
	def first_approach(self, numbers: list):
		"""
		Find the product of the entire array and divide this by
		the number in the array that will be exluded. The quotient
		is appended to a new list.
		"""
		product = 1

		product_list = []


		for number in numbers:
			product *= number
		

		for number in numbers:
			product_list.append(int(product / number))


		return product_list


	def second_approach(self, numbers: list):
		"""
		Loop through the original list of numbers. In each loop,
		create a copy of the original array excluding the number
		the loop is currently in. Find the product of the newly
		created list and append the answer to a new list.
		"""

		product_list = []


		for index in range(len(numbers)):
			product = 1

			_numbers = numbers[:]

			_numbers.pop(index)


			for x in range(len(_numbers)):
				product *= _numbers[x]

			product_list.append(product)


		return product_list


solution = Solution()


# Test Code


assert solution.first_approach([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
print("Test for first approach with input of [1, 2, 3, 4, 5] passed!")


assert solution.second_approach([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
print("Test for second approach with input of [1, 2, 3, 4, 5] passed!")


assert solution.first_approach([3, 2, 1]) == [2, 3, 6]
print("Test for first approach with input of [3, 2, 1] passed!")


assert solution.second_approach([3, 2, 1]) == [2, 3 ,6]
print("Test for second approach with input of [3, 2, 1] passed!")


assert solution.first_approach([5, 10, 15, 20]) == [3000, 1500, 1000, 750]
print("Test for first approach with input of [5, 10, 15, 20] passed!")


assert solution.second_approach([5, 10, 15, 20]) == [3000, 1500, 1000, 750]
print("Test for second approach with input of [5, 10, 15, 20] passed!")