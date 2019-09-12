# -*- coding: utf-8 -*-
import random


def main():

    get_probability()


def get_probability():

    num_diamonds = 0  # ダイヤだった回数
    total = 0  # 3枚がダイヤだった回数

    for i in range(10):
        for j in range(100000):
            # カードを用意
            cards = ['♦'] * 13 + ['♥'] * 13 + ['☘'] * 13 + ['♠'] * 13

            # よく混ぜます。
            random.shuffle(cards)

            # ここから一枚引いて箱に入れます。
            box = cards.pop(random.randint(0, len(cards) - 1))

            # 残りのカードをよく切ります。
            random.shuffle(cards)

            # さらに3枚引きます。
            card1 = cards.pop(random.randint(0, len(cards) - 1))
            card2 = cards.pop(random.randint(0, len(cards) - 1))
            card3 = cards.pop(random.randint(0, len(cards) - 1))

            # 3枚のカードがすべてダイヤのときでboxの中のカードがダイヤだったら
            # num_diamondsをダイヤじゃなかったらnum_not_daiamondsを一つカウントします。
            if card1 == card2 == card3 == '♦':
                if box == '♦':
                    num_diamonds += 1
                total += 1

        # 結果を表示します。
        print('{0}/{1} ({2}))'.format(num_diamonds, total, float(num_diamonds) / total * 100))


if __name__ == "__main__":
    main()



