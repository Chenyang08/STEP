宿題その1

問題：

    サンプルプログラムを変更して、「*」「/」に対応せよ

    例： 3.0 + 4 * 2 − 1 / 5

    細かい仕様は適宜定義してよい

    サンプルプログラム: https://github.com/xharaken/step2015/blob/master/calculator_modularize_2.py

    取り組むときのポイント：

    モジュール化を意識する

    デバッグするときは「デバッグの鉄則」を意識する

ポイント：どうやって「*」「/」と「+」「−」の優先度を扱うか？

     式を2段階で評価すればよい：

     1回目の評価で「*」「/」を処理

     3.0 + 4 * 2 − 1 / 5 ⇒ 3.0 + 8 − 0.2

     2回目の評価で「+」「−」を処理
     
     3.0 + 8 − 0.2 ⇒ 3.6

--------------------------------------------

宿題その2

    書いたプログラムが正しく動いていることを確認するためのテストを追加せよ

    できるだけ網羅的に

    1

    1 + 2

    1.0 + 2

    1.0 + 2.0

    ...

---------------------------------

宿題その3

  さらに括弧に対応せよ

  例： (3.0 + 4 * (2 − 1)) / 5

IDEA:

For the equation which has bracket, we need to extract the content in the bracket, and consider the order of calculating. 

We need to calculate the innermost bracket, thus we need to find the innermost bracket at first. 

For example, 5*(10/(2+3))+4*5, the rightmost left-bracket “(” should be the innermost bracket. 

However,   5*(10/(2+3))+4*(5+2), the rightmost right-bracket “)” is not the innermost one. And it might let the equation not in order.

So, we can find the leftmost right-bracket 4*(5+2)+5*(10/(2+3)), even if there are two bracket not in nest structure, we can calculate the equation in order.

We can implement it by using split() and raplit().
