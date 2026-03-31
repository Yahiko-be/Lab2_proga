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


def main():
    try:
        raw_input = "Програмування це цікаво я йду до дому"
        processor = TextProcessor(raw_input)

        print("Початковий текст:")
        print(processor.get_string())

        sorted_text = processor.sort_words_by_vowels()

        print("\nТекст після сортування слів за кількістю голосних:")
        print(sorted_text)

    except Exception as e:
        print(f"Виникла помилка під час виконання: {e}")


if __name__ == "__main__":
    main()