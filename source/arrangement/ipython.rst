========
IPython
========

通常のインタラクティブシェルを起動するコマンド ::

   $ python

の代わりに, 拡張されたインタラクティブシェル IPython を起動するコマンド ::

   $ ipython

を実行してください. 次のような出力が出ればOKです. ::

   Python 3.4.3 |Anaconda 2.2.0 (x86_64)| (default, Mar  6 2015, 12:07:41)
   Type "copyright", "credits" or "license" for more information.

   IPython 3.1.0 -- An enhanced Interactive Python.
   Anaconda is brought to you by Continuum Analytics.
   Please check out: http://continuum.io/thanks and https://binstar.org
   ?         -> Introduction and overview of IPython's features.
   %quickref -> Quick reference.
   help      -> Python's own help system.
   object?   -> Details about 'object', use 'object??' for extra details.

   In [1]:


通常のインタラクティブシェルの入力待ち >>> の代わりに In [1] と書かれています.

.. ipython::

   In [1]: x = 10  # 変数 x に 10 を「代入」する

   In [2]: x ** 2  # 変数 x と 2 を掛ける

Pythonインタプリタは ``#`` から行末までを読み飛ばします. このノートではコードの解説をするために付加しますが,
読者が付ける必要は (必ずしも) ありません.

% が先頭についている命令は IPython のマジックコマンドと呼ばれる特殊コマンドです
次の3つは説明不要でしょう

.. ipython::

   In [3]: %pwd

   In [4]: %cd /Users/kenjisato/Documents/workspace

   In [5]: %ls

``%cat`` はテキストファイルの中身を表示します. ``%pycat`` はPythonスクリプトをシンタックスハイライトして表示します.

.. ipython::

   In [6]: %cat hello.py

   In [7]: %pycat hello.py

``%run`` でスクリプトを実行します. 実行時のオプションが沢山あるので公式ドキュメントを参照してください.
https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-run

.. ipython::

   In [8]: %run hello

関数などのオブジェクト名の最後に ``?`` をつけてリターンを押すことでドキュメントを表示します.

.. ipython::

   In [8]: range?

IPythonシェル内で定義されている変数を一覧するためには, ``%whos`` を使います.

.. ipython::

   In [5]: y = -1

   In [6]: s = "important text"

   In [8]: x_tmp = 0

   @verbatim
   In [9]: %whos
   Variable   Type    Data/Info
   ----------------------------
   s          str     important text
   x          int     10
   x_tmp      int     0
   y          int     -1


同じ文字列から始まる変数や関数が複数あるときは, 途中まで入力して TABキーを押すと候補が現れます.

.. ipython::

   @verbatim
   In [10]: x<TAB>
   %xdel   %xmode  x       x_tmp


他にも日常的に使うコマンドがたくさんありますので, 必要に応じて説明していきます.