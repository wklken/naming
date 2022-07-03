# -*- coding: utf-8 -*-
import nltk

from re import finditer
from itertools import groupby


"""
  >>> import nltk
  >>> nltk.download('averaged_perceptron_tagger')
"""


def _camel_case_split(identifier):
    matches = finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", identifier)
    return [m.group(0) for m in matches]


def read_words(file_path):
    words = set()
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
            words.add(line)
    return sorted(list(words))


def process_k8s_specific_words(words):
    version_keys = [
        "V1",
        "v1",
        "V1beta",
        "v1beta",
        "V1beta1",
        "V1beta2",
        "V1alpha1",
        "V1Beta1",
        "V1Beta2",
        "V1Alpha1",
        "V2",
        "v2",
        "v2beta",
        "V2beta",
        "V2beta1",
        "V2beta2",
        "V2alpha1",
        "V2Beta1",
        "V2Beta2",
        "V2Alpha1",
        "V3",
    ]

    k8s_specificed_words = {"crd", "cri", "kube", "kubelet"}

    filtered_words = set()
    for key in words:
        if key.lower() in k8s_specificed_words:
            continue

        for v in version_keys:
            key = key.replace(v, "")
        filtered_words.add(key)

    return sorted(list(filtered_words))


def split_into_words(words):
    s = set()
    for word in words:
        parts = _camel_case_split(word)

        for p in parts:
            # remove "" "a" "us"
            if len(p) <= 2:
                continue
            if any(map(str.isdigit, p)):
                continue
            if all(map(str.isupper, p)):
                continue

            s.add(p.lower())

    s = sorted(list(s))
    return s


def _gen_adj_words(word, words):
    adj_words = set()
    if word[-1] == "e" and word + "d" in words:
        adj_words.add(word + "d")

    if word[-1] == "p" and word + "ped" in words:
        adj_words.add(word + "ped")
    if word[-1] == "l" and word + "led" in words:
        adj_words.add(word + "led")
    if word[-1] == "r" and word + "red" in words:
        adj_words.add(word + "red")
    if word[-1] == "n" and word + "ned" in words:
        adj_words.add(word + "ned")

    if word + "ed" in words:
        adj_words.add(word + "ed")

    if word[-1] == "p" and word + "ping" in words:
        adj_words.add(word + "ping")
    if word[-1] == "g" and word + "ging" in words:
        adj_words.add(word + "ging")
    if word[-1] == "t" and word + "ting" in words:
        adj_words.add(word + "ting")

    if word[-1] == "e" and word[:-1] + "ing" in words:
        adj_words.add(word[:-1] + "ing")

    if word + "ing" in words:
        adj_words.add(word + "ing")

    if word[-1] == "e" and word[:-1] + "able" in words:
        adj_words.add(word[:-1] + "able")
    if word[-1] == "t" and word + "table" in words:
        adj_words.add(word + "table")

    if word + "able" in words:
        adj_words.add(word + "able")

    return adj_words


def nltk_noun(words):
    noun = set()
    others = set()

    tagged = nltk.pos_tag(words, tagset="universal")
    for (word, tag) in tagged:
        if tag in ("NOUN", "PRON", "ADV"):
            noun.add(word)
        else:
            others.add(word)
    return sorted(list(noun)), sorted(list(others))


def pprint_list_to_markdown(title, data):
    print("##", title, len(data))
    print()
    print("| Word | Related |")
    print("|------|---------|")

    grouped = [list(g) for k, g in groupby(data, key=lambda x: x[0])]
    for li in grouped:
        if li:
            prefix = li[0][0]
            related = ", ".join(li)
            print("| %s | %s |" % (prefix.upper(), related))
    print()


if __name__ == "__main__":
    file_path = "./k8s_struct_naming.txt"
    # print("read file:", file_path)

    words = read_words(file_path)
    # print("got words:", len(words))

    filtered_words = process_k8s_specific_words(words)
    # print("got filtered words:", len(filtered_words))

    splitted_words = split_into_words(filtered_words)

    filtered_words = process_k8s_specific_words(splitted_words)
    # print("got filtered words2:", len(filtered_words))

    noun, others = nltk_noun(splitted_words)
    pprint_list_to_markdown("Noun in struct name", noun)
    pprint_list_to_markdown("Others in struct name", others)
