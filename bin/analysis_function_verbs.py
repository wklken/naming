# -*- coding: utf-8 -*-

from collections import defaultdict

from nltk.corpus import wordnet

# install https://github.com/nltk/nltk
# pip install nltk
# >>> import nltk
# >>> nltk.download()
# >>> nltk.download('omw-1.4')


def read_words(file_path):
    words = {}
    with open(file_path) as f:
        for line in f:
            # do strip
            line = line.strip(" 0123456789\n")
            # ignore single
            if len(line) <= 1:
                continue
            # ignore all digital
            if line.isdigit():
                continue
            words[line] = True
    return words


# synonym 近义词
def synonym_from_nltk(words):
    synonym_nltk_dict = defaultdict(list)

    s = _remove_duplicated_words(words)
    for word in words:
        if word not in s:
            continue

        an_from_nltk = set()
        for synset in wordnet.synsets(word):
            for synlemma in synset.lemmas():
                an_from_nltk.add(synlemma.name())
        if an_from_nltk:
            an_set = set()
            for w in an_from_nltk:
                w = w.lower()
                if len(w) <= 1:
                    continue
                if w == word.lower():
                    continue

                an_set.add(w)

            if an_set:
                synonym_nltk_dict[word].extend(list(an_set))

    return synonym_nltk_dict


# 反义词
def antonym_from_rule(words):
    antonym_dict = defaultdict(list)
    an_prefixes = ["un", "an", "im", "ir", "il", "in", "dis"]
    an_suffixes = ["less"]
    for word in words:
        for an_prefix in an_prefixes:
            an_word = an_prefix + word
            if an_word in words:
                antonym_dict[word].append(an_word)
                continue

        for an_suffix in an_suffixes:
            an_word = word + an_suffix
            if an_word in words:
                antonym_dict[word].append(an_word)
                continue

    wrong_list = ["it", "to", "put", "port", "ports", "prove"]
    for word in wrong_list:
        del antonym_dict[word]
    return antonym_dict


def _remove_duplicated_words(words):
    s = set()
    s.update(words.keys())
    for word in words:
        if word + "s" in s:
            s.remove(word + "s")
        if word + "es" in s:
            s.remove(word + "es")
        if word + "ed" in s:
            s.remove(word + "ed")
        if word + "ing" in s:
            s.remove(word + "ing")
    return s


def antonym_from_nltk(words):
    antonym_nltk_dict = defaultdict(list)

    s = _remove_duplicated_words(words)
    for word in words:
        if word not in s:
            continue

        an_from_nltk = set()
        for synset in wordnet.synsets(word):
            for synlemma in synset.lemmas():
                an_from_nltk.update([a.name() for a in synlemma.antonyms()])
        if an_from_nltk:
            antonym_nltk_dict[word].extend(list(an_from_nltk))
    return antonym_nltk_dict


def verb_and_its_adj_from_rule(words):
    verb_ads_dict = defaultdict(list)
    for word in words:
        if word[-1] == "e" and word + "d" in words:
            verb_ads_dict[word].append(word + "d")

        if word[-1] == "p" and word + "ped" in words:
            verb_ads_dict[word].append(word + "ped")
        if word[-1] == "l" and word + "led" in words:
            verb_ads_dict[word].append(word + "led")
        if word[-1] == "r" and word + "red" in words:
            verb_ads_dict[word].append(word + "red")
        if word[-1] == "n" and word + "ned" in words:
            verb_ads_dict[word].append(word + "ned")

        if word + "ed" in words:
            verb_ads_dict[word].append(word + "ed")

        if word[-1] == "p" and word + "ping" in words:
            verb_ads_dict[word].append(word + "ping")
        if word[-1] == "g" and word + "ging" in words:
            verb_ads_dict[word].append(word + "ging")
        if word[-1] == "t" and word + "ting" in words:
            verb_ads_dict[word].append(word + "ting")

        if word[-1] == "e" and word[:-1] + "ing" in words:
            verb_ads_dict[word].append(word[:-1] + "ing")

        if word + "ing" in words:
            verb_ads_dict[word].append(word + "ing")

        if word[-1] == "e" and word[:-1] + "able" in words:
            verb_ads_dict[word].append(word[:-1] + "able")
        if word[-1] == "t" and word + "table" in words:
            verb_ads_dict[word].append(word + "table")

        if word + "able" in words:
            verb_ads_dict[word].append(word + "able")

    wrong_list = ["see"]
    for word in wrong_list:
        del verb_ads_dict[word]

    return verb_ads_dict


def pprint_defaultdict_to_markdown(title, data):
    print("##", title, len(data))
    print()
    print("| Word | Related |")
    print("|------|---------|")
    for key, value in data.items():
        print("| %s | %s |" % (key, ", ".join(value)))
    print()


if __name__ == "__main__":
    file_path = "./function_names.txt"
    # print("read file:", file_path)

    words = read_words(file_path)
    # print("got words:", len(words))

    antonym_dict = antonym_from_rule(words)
    pprint_defaultdict_to_markdown("Antonym(by rules)", antonym_dict)
    # print("got antonym:", len(antonym_dict), antonym_dict)

    verb_ads_dict = verb_and_its_adj_from_rule(words)
    pprint_defaultdict_to_markdown("Verb And It's Adj(by rules)", verb_ads_dict)
    # print("got verb_and_its_adj:", len(verb_ads_dict), verb_ads_dict)

    antonym_nltk_dict = antonym_from_nltk(words)
    pprint_defaultdict_to_markdown("Antonym(by nltk)", antonym_nltk_dict)
    # print("got antonym_nltk_dict:", len(antonym_nltk_dict), antonym_nltk_dict)

    synonym_nltk_dict = synonym_from_nltk(words)
    pprint_defaultdict_to_markdown("Synonym(by nltk)", synonym_nltk_dict)
    # print("got synonym_nltk_dict:", len(synonym_nltk_dict), synonym_nltk_dict)
