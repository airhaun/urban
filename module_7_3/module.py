class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        with open('test_file.txt', 'r', encoding='utf-8') as file:
            for name_file in self.file_names:
                content = file.read().lower()
                content = content.translate(str.maketrans('.', ',', '!'))
                words = content.split()
                all_words[name_file] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                position = words.index(word.lower())
                result[file_name] = position + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT'))