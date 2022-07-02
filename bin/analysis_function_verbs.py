# -*- coding: utf-8 -*-


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
def synonym(words):
    pass


# 反义词
def antonym(words):
    antonym_dict = {}
    an_prefixes = ["un", "an", "im", "ir", "il", "in", "dis"]
    an_suffixes = ["less"]
    for word in words:
        for an_prefix in an_prefixes:
            an_word = an_prefix + word
            if an_word in words:
                antonym_dict[word] = an_word

        for an_suffix in an_suffixes:
            an_word = word + an_suffix
            if an_word in words:
                antonym_dict[word] = an_word

    wrong_list = ["it", "to", "put", "port", "ports", "prove"]
    for word in wrong_list:
        del antonym_dict[word]
    return antonym_dict


def verb_and_its_adj(words):
    verb_ads_dict = {}
    for word in words:
        if word[-1] == "e" and word + "d" in words:
            verb_ads_dict[word] = word + "d"

        if word[-1] == "p" and word + "pped" in words:
            verb_ads_dict[word] = word + "pped"

    wrong_list = ["see"]
    for word in wrong_list:
        del verb_ads_dict[word]

    return verb_ads_dict


if __name__ == "__main__":
    file_path = "./function_names.txt"
    print("read file:", file_path)

    words = read_words(file_path)
    print("got words:", len(words))

    antonym_dict = antonym(words)
    print("got antonym:", len(antonym_dict), antonym_dict)

    verb_ads_dict = verb_and_its_adj(words)
    print("got verb_and_its_adj:", len(verb_ads_dict), verb_ads_dict)
