# -*- coding: utf-8 -*-
import pprint
import difflib
import unicodedata


def main():

    # サンプル
    correct_word = 'サーバ'
    words = ['サーバー', 'サーバ', 'ｻｰﾊﾞｰ', 'ｻｰﾊﾞ', 'ドッカー']

    # 単語の類似率を算出
    create_words_probabilities(correct_word, words)


def create_words_probabilities(correct_word, words):
    """
    正しい単語から、類似している単語なのか確率を算出
    ## difflib.SequenceMatcher
    -> https://docs.python.org/ja/3/library/difflib.html#sequencematcher-objects
    @return list
    """

    print(f'正となる単語: {correct_word}')

    # 単語を正規化
    fixed_words = {str(word):unicodedata.normalize('NFKC', word) for word in words}
    # 類似確率を求める
    probabilities = [difflib.SequenceMatcher(None, correct_word, word).ratio() for word in fixed_words.values()]

    keys = list(fixed_words.keys())
    result = list(zip(keys, probabilities))
    pprint.pprint(result)
    
    return result


if __name__ == "__main__":
    main()


