=================
関数定義 (その1)
=================

:doc:`arithmetic` で ``math.log()``, ``math.log10()``, ``math.exp()`` などの関数を使いました. これらの関数は標準ライブラリ
で定義されているものです. この節では, 自前の関数を定義する方法を学びます.


基本構文
------------

基本の構文は次の通りです. ::

   def function_name(param1, param2, ...):
       # do something here
       return output

例えば, ::

   def my_double(x):  # 1, 2
       return 2 * x  # 3

のように書きます. 例のごとく コピー → ``%paste`` で IPython シェルに渡し, 動作を確認してみてください.

.. ipython::

   @verbatim
   In [60]: %paste
   def my_double(x):
       return 2 * x

   ## -- End pasted text --

   @suppress
   In [60]: def my_double(x): return 2 * x

   In [61]: my_double(10)  # 4
   Out[61]: 20

   In [62]: my_double(-2.0)  # 5
   Out[62]: -4.0

   In [63]: my_double(1-3j)  # 5
   Out[63]: (2-6j)

   In [65]: my_double("abc")  # 5
   Out[65]: 'abcabc'


1. ``my_double`` は関数の名前です
2. ``def my_double(x):`` の行で, 仮引数 (パラメータ) ``x`` を宣言しています. これで, ``my_double`` は引数を1つだけ取る関数になります.
3. ``return`` 文が関数によって値が出力されます.
4. 仮引数 ``x`` を 10 として関数が実行されます. ``return`` 文は 2 * 10 を出力します.
5. この関数は ``2 * x`` さえ正しく定義されていれば実行できます. ただし, 常に意味があるとは限りません.


仮引数を2つ以上取る場合も同様に定義します.

.. ipython::

   In [68]: def my_add(x, y): return x + y  # 簡単な関数なら1行で定義してよい

   In [69]: my_add(10, 2)
   Out[69]: 12

   In [70]: my_add(-1.0, 3.8)
   Out[70]: 2.8

   In [71]: my_add('abc', 'def')
   Out[71]: 'abcdef'


引数を1つも取らない関数も定義できます.

.. ipython::

   In [71]: import random

   In [77]: def random_print(): print('The number is', random.random())

   In [78]: random_print()
   The number is 0.1416135489112309


関数作成の目的
-------------------------

関数を作る目的は, 繰り返し実行するコード片をまとめて再利用しやすくしたり, プログラムのロジックを明確にすることにあります.

例えば, 次のコードと,

::

   # Code-1

   raw_input = input('Enter income: ')
   income = int(raw_input)  # 3

   if income < 10 ** 6:
      tax_rate = 0.0
   elif income < 5 * 10 ** 6:
      tax_rate = 0.1
   elif income < 10 ** 7:
      tax_rate = 0.2
   else:
       tax_rate = 0.3

   after_tax_income = income * (1 - tax_rate)
   print('After tax income is', after_tax_income)


次のコードを比べてみてください.


::

   # Code-2

   def input_integer(msg):
       raw_input = input(msg + ': ')
       return int(raw_input)

   def tax_rate(income):
       if income < 10 ** 6:
           tax_rate = 0.0
       elif income < 5 * 10 ** 6:
           tax_rate = 0.1
       elif income < 10 ** 7:
           tax_rate = 0.2
       else:
           tax_rate = 0.3
       return tax_rate

   income = input_integer('Enter income')
   after_tax_income = income * (1.0 - tax_rate(income))
   print('after tax income is', after_tax_income)


Code-1 と比較して Code-2 の方が行数が長くなっています. Code-1 はコードを上から順に読めばよいのに対して,
Code-2 では関数定義に戻らないと何をしているのかが分かりません.

それでは Code-2 を使う利点は何でしょうか?

1つには, Code-1 では ``raw_input`` という中間生成物が残り続けるのに対して,
Code-2 では ``input_integer()`` 関数の呼び出し時に生成され関数が値を返すと消滅します.
このような変数を **ローカル変数** と呼びます (:doc:`userdefined_func2` 参照).
プログラムが二度と使わない名前で溢れてしまうことに比べると,
とても上品な振る舞いです.

次に, ``tax_rate()`` 関数は, 税率計算に必要なロジックを抽出したものであることに注目してください. 仮引数 ``income`` の値が
いくらなのかは事前には分かりませんが, どんな値が入ろうとも適切に処理しようとします. 一方 Code-1 の税率計算部分は, 見た目はまったく
同じなのですが, 事前に ``income`` の値が定まっているという点で異なっています.
データとロジックを分離するというのは一般的に言ってよい方針であり, プログラムの規模が大きくなるとこの方針は威力を発揮します.

次のコード片

::

   after_tax_income = income * (1.0 - tax_rate(income))


に注目してください. ここで, 税引き後所得 ``after_tax_income`` は ``tax_rate(income)`` によって算出された税率をもとに計算されていますが,

+ ``tax_rate()`` を **使うプログラマー** は ``tax_rate()`` の実装方法を意識する必要はありません
+ ``tax_rate()`` を **作るプログラマー** はどのように使われるかを意識する必要がありません

2人の間で共有しなければいけない理解は「収入を入力すると税率が出力される」という仕様のみです.
計算手続きの論理的な塊を関数としてまとめて実装の詳細を関数定義に隠蔽することで, プログラムのロジックが整理されて可読性を高め,
保守や拡張が容易になります. これは
「 `抽象化 <https://ja.wikipedia.org/wiki/抽象化_(計算機科学)#.E6.A7.8B.E9.80.A0.E5.8C.96.E3.83.97.E3.83.AD.E3.82.B0.E3.83.A9.E3.83.9F.E3.83.B3.E3.82.B0>`_ 」
と呼ばれるもっと大きな概念の一部ですが, 重要な点なので意識しておくとよいでしょう.

ちなみに, この ``tax_rate()`` は税率のしきい値と限界税率の設定を関数内部に埋め込んでいます (ハードコードされている).
税率変更を見越して長期的に使いたいコードであれば, Code-2 のような書き方は望ましくないでしょう.
一時的に必要なだけのアドホックなコードを書いているのであれば, 税率を変更できる余地があっても使い道がないでしょう.
設計の目的に応じて適切な実装を選択することが大切です.


参考: Online Python Tutor
--------------------------------

`Online Python Tutor <http://www.pythontutor.com>`_ はコードの実行過程をヴィジュアル化してくれるウェブサービスです.
変数が作られるタイミング, 条件分岐, 関数呼び出しの動作を理解するのに大きな助けになってくれると思います. ぜひ活用してください.

Code-1 と Code-2 について `Online Python Tutor <http://www.pythontutor.com>`_ の出力を掲載しておきます. 実際に動かしてみてください.

Code-1
^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div style="margin: 10px auto">
       <iframe width="800" height="700" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=raw_input+%3D+input('Enter+income%3A+'%29%0Aincome+%3D+int(raw_input%29++%23+3%0A%0Aif+income+%3C+10+**+6%3A%0A++++tax_rate+%3D+0.0%0Aelif+income+%3C+5+*+10+**+6%3A%0A++++tax_rate+%3D+0.1%0Aelif+income+%3C+10+**+7%3A%0A++++tax_rate+%3D+0.2%0Aelse%3A%0A++++tax_rate+%3D+0.3%0A%0Aafter_tax_income+%3D+income+*+(1+-+tax_rate%29%0Aprint('After+tax+income+is',+after_tax_income%29&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=350&codeDivHeight=400"> </iframe>
   </div>


Code-2
^^^^^^^^^^^^^^^^^

.. raw:: html

   <div style="margin: 10px auto">
      <iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=def+input_integer(msg%29%3A%0A++++raw_input+%3D+input(msg+%2B+'%3A+'%29%0A++++return+int(raw_input%29%0A%0Adef+tax_rate(income%29%3A%0A++++if+income+%3C+10+**+6%3A%0A++++++++tax_rate+%3D+0.0%0A++++elif+income+%3C+5+*+10+**+6%3A%0A++++++++tax_rate+%3D+0.1%0A++++elif+income+%3C+10+**+7%3A%0A++++++++tax_rate+%3D+0.2%0A++++else%3A%0A++++++++tax_rate+%3D+0.3%0A++++return+tax_rate%0A%0Aincome+%3D+input_integer('Enter+income'%29%0Aafter_tax_income+%3D+income+*+(1.0+-+tax_rate(income%29%29%0Aprint('after+tax+income+is',+after_tax_income%29&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%2210000000%22%5D&curInstr=16&codeDivWidth=350&codeDivHeight=400"> </iframe>
   </div>





