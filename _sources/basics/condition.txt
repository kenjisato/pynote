==========
条件分岐
==========

if-else
------------

特定の式が真であるか偽であるかを判定し, 異なるコードを実行したいとしましょう.

例えば, ``income``, ``tax_rate`` を整数型の変数として,

- ``income`` の値が 1,000,000 未満であれば ``tax_rate = 0.0``
- ``income`` の値が それ以上のときは ``tax_rate = 0.1``

というように, 所得に応じた税率を設定したいようなケースです. 次のように書きます.

::

   if income < 10 ** 6:
       tax_rate = 0.0
   else:
       tax_rate = 0.1


このコードがやろうとしていることは, なんとなく読み取っていただけると思います.
``if`` の終わりから ``:`` (コロン) まで間に条件を書きます. 条件が真であれば直後の行が実行され, 偽であれば,
``else:`` に続く行が実行されます.

実際に, 動かしてみましょう. 上のコードをコピーして, IPython シェルにペーストします. ペーストをするときには,
IPython マジックコマンド ``%paste`` を使います.


.. ipython::

   In [2]: income = 10 ** 7

   @verbatim
   In [3]: %paste
   if income < 10 ** 6:
       tax_rate = 0.0
   else:
       tax_rate = 0.1

   ## -- End pasted text --

   @suppress
   In [4]: tax_rate = 0.1

   In [4]: tax_rate
   Out[4]: 0.1


条件判定後に実行される行は, 1行だけである必要はありません. 次のような書き方も可能ですし, もっと行を増やすこともできます.

::

   if income < 10 ** 6:
       tax_rate = 0.0
       subsidy = 10000
   else:
       tax_rate = 0.1
       subsidy = 0


このコードも, コピー → ``%paste`` で動きを確認しておいてください.

すでに, 気づいている人もいるかもしれませんが, ``if`` から ``else`` の間に書かれている
コードはインデントされています. 他のプログラミング言語の経験のある人は, 「コードを読みやすくするためにこのようにしている」と考える
かもしれません. しかしそれは正しくありません. Python では, コロンで終わる行の次の行から, インデントレベルが戻るまでのコードを
塊 (ブロック) として扱います.

したがって, 次のようなコードはエラーになります. コピー → ``%paste`` で確認してみましょう.

::

   if 0 < 1:
   print('0 is smaller than 1')


.. ipython::
   :verbatim:

   In [5]: %paste
   if 0 < 1:
   print('0 is smaller than 1')

   ## -- End pasted text --
     File "<ipython-input-5-e3464c16c2e0>", line 2
       print('0 is smaller than 1')
           ^
   IndentationError: expected an indented block


このインデントはスペース4つにするのが標準です. ``if`` 節の中のブロック, ``else`` 節の中のブロックで使われるインデントを紹介しました.
Python ではいたるところでインデントが現れます. 基本ルールは同じなので, 混乱することはないでしょう.

タブをスペース4つに展開してくれるテキストエディタが必要な理由が分かっていただけたと思います.


if-elif-else
------------

もっと沢山の場合分けをしたくなることもあります.

- ``income`` の値が 1,000,000 未満であれば ``tax_rate = 0.0``
- ``income`` の値が 1,000,000 以上,  5,000,000 未満であれば ``tax_rate = 0.1``
- ``income`` の値が 5,000,000 以上, 10,000,000 未満であれば ``tax_rate = 0.2``
- 10,000,000 以上のときは ``tax_rate = 0.3``

というコードは, 次のように書けます.

::

   if income < 10 ** 6:
       tax_rate = 0.0
   elif income < 5 * 10 ** 6:
       tax_rate = 0.1
   elif income < 10 ** 7:
       tax_rate = 0.2
   else:
       tax_rate = 0.3


``elif`` は else if を表すキーワードです.


条件判定の例
-------------------

条件判定に使う式・変数の値があらかじめ決まっているのであれば, ``if-elif-else`` には何の意味もありません.
どんな値が入るかが分からないような状況を作って実験してみましょう. 1つの例を挙げますので, 他にどのような使い道があるか考えてみてください.


ユーザーからの入力を判定する
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

テキストエディタで次のファイルを作ってください. ファイル名は ``condition_input.py`` とします.

::

   # condition_input.py

   raw_input = input('Enter income: ')  # 1, 2
   income = int(raw_input)  # 3

   if income < 10 ** 6:
       tax_rate = 0.0
   elif income < 5 * 10 ** 6:
       tax_rate = 0.1
   elif income < 10 ** 7:
       tax_rate = 0.2
   else:
       tax_rate = 0.3

   print('tax rate is', tax_rate)



1. ``input()`` はユーザーに入力を求める組み込み関数です. 入力してリターンキー (エンターキー) を叩くと, 入力内容が文字列として出力されます.
2. ``raw_input`` 変数は ``input()`` の出力文字列を参照しています.
3. ``int()`` は文字列を整数に変換する組み込み関数で, これによって ``raw_input`` から整数変数 ``income`` を作ることができました.

IPython シェルで次の挙動を確認してください.

.. ipython::

   @verbatim
   In [19]: %run condition_input
   Enter income: 100000000
   tax rate is 0.3


ここではキーボード入力を条件判定しましたが, データを読み込んで値ごとに違う振る舞いをさせるようなことも考えられます.


ランダムネス
^^^^^^^^^^^^^^^^^^^^^^^^^^^

入力値がランダムに決まる場合にも条件判定が役に立ちます.

::

   # condition_random.py

   import random  # 1

   dice1 = random.randrange(1, 7)  # 2
   dice2 = random.randrange(1, 7)
   total = dice1 + dice2  # 3

   if total % 2:  # 4
       print('Even: total is', total)
   else:
       print('Odd: total is', total)


1. ``random`` モジュールは擬似乱数を生成する関数群を提供している
2. ``random.randrange(1,7)`` は1以上, 7未満の整数をランダムに生成
3. 2回振ったサイコロの目の合計を計算
4. 目の合計が奇数か偶数かを判定する

このコードを実行してみましょう.

.. ipython::
   :verbatim:

   In [54]: %run condition_random.py
   Even: total is 5

   In [55]: %run condition_random.py
   Even: total is 3

   In [56]: %run condition_random.py
   Odd: total is 6

   In [57]: %run condition_random.py
   Odd: total is 6

   In [58]: %run condition_random.py
   Even: total is 9

   In [59]: %run condition_random.py
   Even: total is 5