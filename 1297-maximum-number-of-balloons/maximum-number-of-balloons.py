class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       
        my_dict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        # Loop through each character in the input text
        for char in text:
           if char in my_dict:

                my_dict[char] +=1

        # Perform floor division on specific keys
        my_dict['l'] //= 2
        my_dict['o'] //= 2

        # Return the minimum value among the counts
        return min(my_dict.values())
