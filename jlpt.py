# encoding:utf-8

import random
import argparse
import time


_gojuon = [
    ('a', 'あ', 'ア'),
    ('i', 'い', 'イ'),
    ('u', 'う', 'ウ'),
    ('e', 'え', 'エ'),
    ('o', 'お', 'オ'),

    ('ka', 'か', 'カ'),
    ('ki', 'き', 'キ'),
    ('ku', 'く', 'ク'),
    ('ke', 'け', 'ケ'),
    ('ko', 'こ', 'コ'),

    ('sa', 'さ', 'サ'),
    ('si(shi)', 'し', 'シ'),
    ('su', 'す', 'ス'),
    ('se', 'せ', 'セ'),
    ('so', 'そ', 'ソ'),

    ('ta', 'た', 'タ'),
    ('ti(chi)', 'ち', 'チ'),
    ('tu(tsu)', 'つ', 'ツ'),
    ('te', 'て', 'テ'),
    ('to', 'と', 'ト'),

    ('na', 'な', 'ナ'),
    ('ni', 'に', 'ニ'),
    ('nu', 'ぬ', 'ヌ'),
    ('ne', 'ね', 'ネ'),
    ('no', 'の', 'ノ'),

    ('ha', 'は', 'ハ'),
    ('hi', 'ひ', 'ヒ'),
    ('hu(fu)', 'ふ', 'フ'),
    ('he', 'へ', 'ヘ'),
    ('ho', 'ほ', 'ホ'),

    ('ma', 'ま', 'マ'),
    ('mi', 'み', 'ミ'),
    ('mu', 'む', 'ム'),
    ('me', 'め', 'メ'),
    ('mo', 'も', 'モ'),

    ('ya', 'や', 'ヤ'),
    ('yu', 'ゆ', 'ユ'),
    # ('ye(e)', '𛀁', 'エ'),
    ('yo', 'よ', 'ヨ'),

    ('ra', 'ら', 'ラ'),
    ('ri', 'り', 'リ'),
    ('ru', 'る', 'ル'),
    ('re', 'れ', 'レ'),
    ('ro', 'ろ', 'ロ'),

    ('wa', 'わ', 'ワ'),
    # ('wi(i)', 'ゐ', 'ヰ'),
    # ('we(e)', 'ゑ', 'ヱ'),
    ('wo(o)', 'を', 'ヲ'),
]


_yoon = [
    ('kya', 'きゃ', 'キャ'),
    ('kyu', 'きゅ', 'キュ'),
    ('kyo', 'きょ', 'キョ'),

    ('sya(sha)', 'しゃ', 'シャ'),
    ('syu(shu)', 'しゅ', 'シュ'),
    ('syo(sho)', 'しょ', 'ショ'),

    ('tya(cha)', 'ちゃ', 'チャ'),
    ('tyu(chu)', 'ちゅ', 'チュ'),
    ('tyo(cho)', 'ちょ', 'チョ'),

    ('nya', 'にゃ', 'ニャ'),
    ('nyu', 'にゅ', 'ニュ'),
    ('nyo', 'にょ', 'ニョ'),

    ('hya', 'ひゃ', 'ヒャ'),
    ('hyu', 'ひゅ', 'ヒュ'),
    ('hyo', 'ひょ', 'ヒョ'),

    ('mya', 'みゃ', 'ミャ'),
    ('myu', 'みゅ', 'ミュ'),
    ('myo', 'みょ', 'ミョ'),

    ('rya', 'りゃ', 'リャ'),
    ('ryu', 'りゅ', 'リュ'),
    ('ryo', 'りょ', 'リョ'),
]


_dakuten = [
    ('ga', 'が', 'ガ'),
    ('gi', 'ぎ', 'ギ'),
    ('gu', 'ぐ', 'グ'),
    ('ge', 'げ', 'ゲ'),
    ('go', 'ご', 'ゴ'),

    ('za', 'ざ', 'ザ'),
    ('zi(ji)', 'じ', 'ジ'),
    ('zu', 'ず', 'ズ'),
    ('ze', 'ぜ', 'ゼ'),
    ('zo', 'ぞ', 'ゾ'),

    ('da', 'だ', 'ダ'),
    ('di(ji)', 'ぢ', 'ヂ'),
    ('du(zu)', 'づ', 'ヅ'),
    ('de', 'で', 'デ'),
    ('do', 'ど', 'ド'),

    ('ba', 'ば', 'バ'),
    ('bi', 'び', 'ビ'),
    ('bu', 'ぶ', 'ブ'),
    ('be', 'べ', 'ベ'),
    ('bo', 'ぼ', 'ボ'),
]


_yoon_dakuten = [
    ('gya', 'ぎゃ', 'ギャ'),
    ('gyu', 'ぎゅ', 'ギュ'),
    ('gyo', 'ぎょ', 'ギョ'),

    ('zya(ja)', 'じゃ', 'ジャ'),
    ('zyu(ju)', 'じゅ', 'ジュ'),
    ('zyo(jo)', 'じょ', 'ジョ'),

    ('dya(ja)', 'ぢゃ', 'ヂャ'),
    ('dyu(ju)', 'ぢゅ', 'ヂュ'),
    ('dyo(jo)', 'ぢょ', 'ヂョ'),

    ('bya', 'びゃ', 'ビャ'),
    ('byu', 'びゅ', 'ビュ'),
    ('byo', 'びょ', 'ビョ'),
]


_handakuten = [
    ('pa', 'ぱ', 'パ'),
    ('pi', 'ぴ', 'ピ'),
    ('pu', 'ぷ', 'プ'),
    ('pe', 'ぺ', 'ペ'),
    ('po', 'ぽ', 'ポ'),
]


_yoon_handakuten = [
    ('pya', 'ぴゃ', 'ピャ'),
    ('pyu', 'ぴゅ', 'ピュ'),
    ('pyo', 'ぴょ', 'ピョ'),
]


_nasal = [
    ('n', 'ん', 'ン'),
]


class JLPT():
    def __init__(self):
        pass

    def random(self, groups=[], count=0):
        collect = []
        for g in groups:
            collect += random.sample(g, len(g))

        if count == 0 or len(collect) < count:
            count = len(collect)

        sample = random.sample(collect, count)
        return sample

    def display(self, sample, index):
        _ = input('Press Enter to continue:')
        width = 10
        time_cost = {}
        for one in sample:
            hint = one[index]
            begin = time.time()
            _ = input(hint+'')
            end = time.time()
            print(''.join([f'{i: <{width}}' for i in one]))
            elapsed = round(end - begin, 1)
            time_cost[one] = elapsed
            print(f'{elapsed}s')
            print()

        total_time = sum(time_cost.values())
        rank = [(str(v),) + k for k, v in sorted(time_cost.items(),
                                                 key=lambda i: i[1], reverse=True)]
        print(f'Total time:{total_time}s')
        top_n = 10
        if len(rank) < top_n:
            top_n = len(rank)
        for i in range(top_n):
            print(''.join([f'{i: <{width}}' for i in rank[i]]))

    def run(self, key, scope, count):
        index = 0
        if key == 'romaji':
            index = 0
        elif key == 'hiragana':
            index = 1
        elif key == 'katakana':
            index = 2
        else:
            pass

        groups = []
        for i in scope:
            if i == 'gojuon':
                groups.append(_gojuon)
            elif i == 'yoon':
                groups.append(_yoon)
            elif i == 'dakuten':
                groups.append(_dakuten)
            elif i == 'yoon_dakuten':
                groups.append(_yoon_dakuten)
            elif i == 'handakuten':
                groups.append(_handakuten)
            elif i == 'yoon_handakuten':
                groups.append(_yoon_handakuten)
            elif i == 'nasal':
                groups.append(_nasal)
            else:
                pass
        sample = self.random(groups, count)
        self.display(sample, index)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', type=str, default='romaji',
                        choices=['romaji', 'hiragana', 'katakana'], required=False)
    parser.add_argument('-g', '--group', nargs='+', default=['gojuon'],
                        choices=['gojuon', 'yoon', 'dakuten',
                                 'handakuten', 'yoon_dakuten', 'yoon_handakuten'],
                        required=False)
    parser.add_argument('-c', '--count', type=int,
                        default=50, help=r'count', required=False)
    args = parser.parse_args()

    jlpt = JLPT()
    jlpt.run(args.key, args.group, args.count)
