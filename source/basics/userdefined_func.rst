==============
関数定義
==============

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
5. この関数は 2 * x さえ正しく定義されていれば実行できます. ただし, 常に意味があるとは限りません.


仮引数を2つ以上取る場合も同様に定義します.

.. ipython::

   In [68]: def my_add(x, y): return x + y  # 簡単な関数なら1行で定義してよい

   In [69]: my_add(10, 2)
   Out[69]: 12

   In [70]: my_add(-1.0, 3.8)
   Out[70]: 2.8

   In [71]: my_add('abc', 'def')
   Out[71]: 'abcdef'


スコープ
------------

関数を作る目的は, 繰り返し実行するコード片をまとめて再利用しやすくするところにあります.