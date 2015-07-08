====================
関数定義 (その2)
====================

スコープ
--------------

変数は定義される位置によって, スコープと呼ばれる有効範囲が異なります.
関数は独自のスコープを作り, 関数内部で定義される変数を関数の外側で使うことはできないようになっています.

次の振る舞いを確認してください.

.. ipython::

   In [4]: y = 'hello'

   In [5]: z = 100

   In [6]: def f(x):
      ...:     y = 2
      ...:     z = -1
      ...:     return x*2 + z
      ...:

   In [7]: f(1)
   Out[7]: 1

   In [8]: y
   Out[8]: 'hello'

   In [9]: z
   Out[9]: 100


.. image:: /_static/scope/pythontutor.png
   :scale: 50%
   :alt: stackframe

関数の内部で定義されていた変数は, 関数の内部でのみ有効です.
一方, 関数の外側で定義された変数を使うことは可能です. ただし, 意図しない結果を招く恐れがあるので,
このようなコードを書く必然性がなければ避ける方が懸命でしょう.

.. ipython::

   In [3]: g = 10

   In [4]: def f(x):
      ...:     return g * x
      ...:

   In [5]: f(10)
   Out[5]: 100

   In [6]: g = 20  # 一見 f とは関係がないような変更

   In [7]: f(10)   # しかし, f の挙動を変えてしまっている
   Out[7]: 200

次のように書くほうが安全です.

.. ipython::

   In [8]: def f(x, g):
      ...:     return g * x
      ...:

   In [9]: f(10, g=10)
   Out[9]: 100

   In [10]: f(10, g=20)
   Out[10]: 200

あるいは, 次のように書くのもよいかもしれません.

.. ipython::

   In [12]: def fg(g):
      ....:     def _f(x):
      ....:         return g * x
      ....:     return _f
      ....:

   In [13]: f = fg(10)

   In [14]: f(10)
   Out[14]: 100

   In [15]: f = fg(20)  # 明示的な変更

   In [16]: f(10)
   Out[16]: 200



キーワード引数, デフォルト引数
---------------------------------------------

キーワード引数
^^^^^^^^^^^^^^^^^^^^^^^^

すでに上で例を出しましたが, 関数呼び出しの際に ``func_name(仮引数名=実引数)`` の形で
引数を渡すことができます. 次の関数を例にとって説明しましょう.

.. ipython::

   In [23]: def hello(name, title):
      ....:     print('Hello,', title, name, '!')
      ....:

以下の呼び出し方法が認められています.

.. ipython::

   In [24]: hello('Brown', 'Ms.')  # 位置指定引数
   Hello, Ms. Brown !

   In [25]: hello(name='Brown', title='Mr.')  # キーワード引数
   Hello, Ms. Brown !

   In [26]: hello(title='Mr.', name='Brown')  # キーワード引数は順序交換可
   Hello, Ms. Brown !

   In [27]: hello('Brown', title='Mr.')  #  2個目だけキーワードというのも可
   Hello, Ms. Brown !

しかし, 以下のような呼び出しは認められていません.


.. ipython::
   :okexcept:

   In [28]: hello('Mr.', name='Brown')  # 1
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-28-45cbf09d2eb9> in <module>()
   ----> 1 hello('Mr.', name='Brown')

   TypeError: hello() got multiple values for argument 'name'

   In [29]: hello(title='Mr.', 'Brown')  #2
     File "<ipython-input-29-cba1c2130c59>", line 1
       hello(title='Mr.', 'Brown')
                               ^
   SyntaxError: non-keyword arg after keyword arg


1. 位置指定引数は前から順に評価される. ``'President'`` は ``name`` 変数に代入されているので,
   ``name`` キーワード引数があると2度代入しようとして ``TypeError`` になる.
2. 位置指定引数より前にキーワード指定引数を書くことはできない. これは文法エラー (``SyntaxError``)

これらのエラーはエラーメッセージをきちんと読めば対応できるでしょう.


keyword-only argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python 3.x では, 次のように関数を定義することができます.

.. ipython::

   In [42]: def my_print(s, *, reverse):
      ....:     if reverse:
      ....:         print(s[::-1])
      ....:     else:
      ....:         print(s)
      ....:

``*`` よりあとに書かれた仮引数は, キーワード引数としてのみ渡すことができます
(keyword-only argument).

.. ipython::

   In [43]: my_print('abc', reverse=True)
   cba

   In [44]: my_print('abc', reverse=False)
   abc

これは, 次のような呼び出しを禁止するために使われます. (``True`` が意味するものが何かが
わかりにくいとコードの可読性が下がってしまうのです)

.. ipython::
   :okexcept:

   In [45]: my_print('error', True)
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-45-dc202b040992> in <module>()
   ----> 1 my_print('error', True)

   TypeError: my_print() takes 1 positional argument but 2 were given


デフォルト引数
^^^^^^^^^^^^^^^^^^^^^^^^^^^

関数にはデフォルト値を指定することができます.

.. ipython::

   In [46]: def salute(name, title, msg='Hello'):
      ....:     print(msg + ',', title, name + '!')
      ....:

   In [47]: salute('Brown', 'Mr.')
   Hello, Mr. Brown!

   In [48]: salute('Brown', 'Mr.', 'Good morning')
   Good morning, Mr. Brown!


デフォルト値として ``None`` がよく使われます. 特定の引数が設定されているときと
そうでないときで関数の振る舞いを変えたい場合に使います.


