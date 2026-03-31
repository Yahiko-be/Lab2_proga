import unittest
import re


class TextProcessor:
    def __init__(self, initial_text):
        self.data = list(initial_text)

    def get_string(self):
        return "".join(self.data)

    def sort_words_by_vowels(self):
        text = self.get_string()
        words = re.findall(r'\b\w+\b', text)
        non_words = re.split(r'\b\w+\b', text)

        def count_vowels(word):
            vowels = "aeiouyAEIOUYаеєиіїоуюяАЕЄИІЇОУЮЯ"
            return sum(1 for char in word if char in vowels)

        words.sort(key=count_vowels)

        result = []
        for i in range(len(words)):
            result.append(non_words[i])
            result.append(words[i])
        result.append(non_words[-1])

        self.data = list("".join(result))
        return self.get_string()


class TestTextProcessor(unittest.TestCase):
    def test_vowel_sorting_basic(self):
        input_text = "Кіт іде додому"
        processor = TextProcessor(input_text)
        result = processor.sort_words_by_vowels()
        self.assertEqual(result, "Кіт іде додому")

    def test_vowel_sorting_different_counts(self):
        input_text = "Яблуко є смачне"
        processor = TextProcessor(input_text)
        result = processor.sort_words_by_vowels()
        self.assertEqual(result, "є смачне Яблуко")

    def test_empty_string(self):
        processor = TextProcessor("")
        result = processor.sort_words_by_vowels()
        self.assertEqual(result, "")

    def test_punctuation_preservation(self):
        input_text = "Привіт, світ!"
        processor = TextProcessor(input_text)
        result = processor.sort_words_by_vowels()
        self.assertEqual(result, "світ, Привіт!")


if __name__ == "__main__":
    unittest.main()