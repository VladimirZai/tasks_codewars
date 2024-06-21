class Dictionary:
    def __init__(self, words):
        self.words = words

    def levenshtein_distance(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,
                                   dp[i][j - 1] + 1,
                                   dp[i - 1][j - 1] + 1)
        return dp[len1][len2]

    def find_most_similar(self, term):
        min_distance = float('inf')
        most_similar_word = None

        for word in self.words:
            distance = self.levenshtein_distance(term, word)
            if distance < min_distance:
                min_distance = distance
                most_similar_word = word

        return most_similar_word


fruits = Dictionary(['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana'])
print(fruits.find_most_similar('strawbery'))
print(fruits.find_most_similar('berry'))
print(fruits.find_most_similar('aple'))
print(fruits.find_most_similar('slkds'))
