#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# polygon.py
#

import math    # for math.sqrt()

class Polygon(object):
    # コンストラクタ 一辺の長さを登録する
    def __init__(self, side):
        self.side = side

    # 周囲長を返す
    def get_perimeter(self):
        print('Not implemented')
        return 0

    # 面積を返す
    def get_area(self):
        print('Not implemented')
        return 0

# 以下、Polygonを継承してget_perimeter, get_areaをもつ
# サブクラス、Triangle, Squareを作りなさい

# Triangleのクラス定義




# Squareのクラス定義



# 上で定義したクラスを使うメインプログラム
if __name__ == '__main__':
    polygons = [Triangle(3.0), Triangle(4.5), Square(2.5)]
    for s in polygons:
        print(f'Type: {type(s)},  Perimeter: {s.get_perimeter()}, Area: {s.get_area()}')
