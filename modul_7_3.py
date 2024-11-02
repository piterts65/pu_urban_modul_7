
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as f:
                file = f.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(sym, '')
                all_words[name] = file.split()
        return all_words

    def find(self, word):
        place = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                place[value] = key.index(word.lower()) + 1
            return place

    def count(self, word):
        count_ = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            count_[value] = words_count
        return count_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('Щго')) # 4 слова teXT в тексте всего