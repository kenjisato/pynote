==================================
Windows のコマンド操作
==================================


キーボードのWindowsキーとRキーを同時に押してください. 「ファイル名を指定して実行」のダイアログが現れるので, 「powershell」と入力して
エンター（リターン）キーを押すか, OK をクリックしてください.

.. image:: /_static/windows_shell/winR.png
   :scale: 50%
   :alt: ファイル名を指定して実行

実行すると次のような画面が立ち上がります. Windows PowerShell というアプリケーションです.

.. image:: /_static/windows_shell/wshell-01.png
   :scale: 30%
   :alt: Windows PowerShell

ls
^^

以下では, シェル (Windows であれば Windows PowerShell) でコマンド入力するということを指示するときには, 次の記法を用います. 上の
スクリーンショットと見比べてください. ``PS C:\Users\Kenji >`` と書かれている部分はユーザー名や作業中のディレクトリによって変わるので,
この部分を ``$`` で置き換えます.  ::

   $ ls

シェルに 「 ls 」とだけ入力してエンター（リターン）を押した結果, 次のような出力が表示されます.

.. image:: /_static/windows_shell/wshell-02.png
   :scale: 30%
   :alt: ls の結果

コマンドに加えて, コマンドの出力を表示するときは, 画面キャプチャの代わりに次のように書くことにします. ::

   $ ls

       ディレクトリ: C:\Users\Kenji


   Mode                LastWriteTime     Length Name
   ----                -------------     ------ ----
   d----        2015/06/20     15:31            .continuum
   d----        2015/06/20     15:31            Anaconda3
   d-r--        2015/05/26     14:07            Contacts
   d-r--        2015/05/26     14:07            Desktop
   d-r--        2015/06/20     15:39            Documents
   d-r--        2014/06/16     14:52            Downloads
   d-r--        2015/05/26     14:07            Favorites
   d-r--        2015/05/26     14:07            Links
   d-r--        2015/05/26     14:07            Music
   da---        2015/06/20     14:48            OneDrive
   d-r--        2014/06/16     14:53            OneDrive.old
   d-r--        2015/05/26     14:07            Pictures
   d-r--        2015/05/26     14:07            Saved Games
   d-r--        2015/05/26     14:07            Searches
   d-r--        2014/06/16     14:52            Videos


「 ls 」コマンドは, シェルが現在基準点としている作業ディレクトリ (カレントディレクトリ) の中身をリストするためのコマンドです.

他にもいくつか大切なコマンドがあるので覚えてください.


pwd
^^^

現在の作業ディレクトリ（カレントディレクトリ）へのパスを表示するコマンド 「 pwd 」::

   $ pwd

   Path
   ----
   C:\Users\Kenji

シェルを実行しているときには「自分がどのディレクトリで作業しているか？」ということを意識しておくとよいでしょう.


cd
^^

作業ディレクトリを移動するコマンド 「 cd 」. カレントディレクトリ内にある Documents に移動します. 入力途中で (例えば Doc だけ入力して)
TABキーを押すと候補が表示されます. ::

   $ cd Documents
   $ pwd

   Path
   ----
   C:\Users\Kenji\Documents

同じコマンドですが, 親ディレクトリ (カレントディレクトリを含んでいるディレクトリ) に移動するには次のようにします.::

   $ cd ..
   $ pwd

   Path
   ----
   C:\Users\Kenji

「 C:\ 」から始まる完全なパス(絶対パス) を指定して移動することもできます. ::

   $ cd C:\Users\Kenji\Documents


mkdir
^^^^^

カレントディレクトリに子ディレクトリを追加するには, 「 mkdir 」コマンドを使います. workspace という名前のディレクトリを作ってみましょう.::

   $ mkdir workspace

       ディレクトリ: C:\Users\Kenji\Documents


   Mode                LastWriteTime     Length Name
   ----                -------------     ------ ----
   d----        2015/06/20     16:50            workspace



Pythonインタラクティブシェル
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

これからの作業はすべて, 今新しく作ったディレクトリの中で行うことにしましょう. Python のインタラクティブセッションを開始しましょう. ::

   $ cd workspace
   $ python

次のような表示が出れば成功です::


   Python 3.4.3 |Anaconda 2.2.0 (64-bit)| (default, Mar  6 2015, 12:06:10) [MSC v.1600 64 bit (AMD64)]
   on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

いま実行されているのはPython のインタラクティブシェルというアプリケーションです. 「 >>> 」と書かれているののは, シェルが入力待ち状態に
なっているという意味です. Windows PowerShell のシェルコマンドは, 「 $ command_name 」 で表しました. 「Python のシェルに入力して
ください」ということを 「 >>> 」を付けて表します. シェルの出力については先ほどと同様に扱います. すなわち, >>> を書いている行は読者が
入力することを想定していて, >>> を書いてない行はそのコマンドが実行の結果です::

   >>> import this
   The Zen of Python, by Tim Peters

   Beautiful is better than ugly.
   Explicit is better than implicit.
   Simple is better than complex.
   Complex is better than complicated.
   Flat is better than nested.
   Sparse is better than dense.
   Readability counts.
   Special cases aren't special enough to break the rules.
   Although practicality beats purity.
   Errors should never pass silently.
   Unless explicitly silenced.
   In the face of ambiguity, refuse the temptation to guess.
   There should be one-- and preferably only one --obvious way to do i
   Although that way may not be obvious at first unless you're Dutch.
   Now is better than never.
   Although never is often better than *right* now.
   If the implementation is hard to explain, it's a bad idea.
   If the implementation is easy to explain, it may be a good idea.
   Namespaces are one honking great idea -- let's do more of those!

シェルを終了するときは::

   >>> exit()

を実行します.

Hello, world!
^^^^^^^^^^^^^^^

Sublime Text 3 はコマンドラインから呼び出すことができます. 環境変数に「C:\\Program Files\\Sublime Text 3」を追加して::

   $ subl hello.py

と入力してください. Sublime Text 3 が起動して同名のファイルを開きます (なければ作成されます).

Sublime Text 3 を使っていないくても結構ですが, いずれにせよシェルのカレントディレクトリと同じ場所に「 hello.py 」ファイルを次の内容で
作成してください.::

   # hello.py
   print('Hello, world!')

それから, Windows PowerShell で次のコマンドを実行して出力を確認してください.::

   $ python hello.py
   Hello, world!

「 hello.py 」のように命令を書き連ねたファイルをスクリプトファイルと呼びます. 計算や作図の手続きをスクリプトファイル
（たとえば「script.py」という名前にしたとしましょう）に書きシェルで::

   $ python script.py

を実行して結果を出力する, というのがプログラムの作成から実行の基本的な流れになります.
