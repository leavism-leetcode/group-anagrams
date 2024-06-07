# Copy/paste template from LeetCode below
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # <charCount, list of anagrams>

        for word in strs:
            count = [
                0
            ] * 26  # creates an array of 26 zeroes, one for each lowercase letter

            for character in word:
                # ord() gets ASCII of character
                # ord("b") - ord("a") = 98 - 97 = 1
                # We'll use this value to get the position of character in count
                # "b" is position 1 in count, incrementing it means "b" has appeared in word
                count[ord(character) - ord("a")] += 1

            # Append the count list for each word into result hashmap, with:
            # <count that represents each unique set of characters as a tuple, list of words that match that set of characters>
            # Appending the count list as a tuple because Python won't allow lists as keys
            result[tuple(count)].append(word)

        return result.values()


# After copy/pasting the template from LeetCode, uncomment the following to start testing.
# solution = Solution()
