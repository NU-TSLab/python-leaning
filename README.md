# Python 練習用

各章の問題を解いてください。回答がわからない場合は、問題の下の解説を読みもう一度問題を解いてみてください。

# 目次
* Python 練習用
* 目次
* 問題
    * 1.Pythonについて
    * 2.環境構築
    * 3.基本的な文法
    * 4.変数とデータ型、演算子
    * 5.制御文(条件分岐、繰り返し)
    * 6.データ形式(リスト、辞書、リスト内包形式)
    * 7.関数、クラス
    * 8.ファイル操作
    * 9.モジュール
    * 10.発展問題

# 問題
## 1. Pythonについて

### 問1
Pythonとはどんな動物か？

<details><summary>解説</summary>

Python言語の製作者グイド・ヴァン・ロッサムが
「Monty Python's Flying Circus（空飛ぶモンティ・パイソン）」
で知られるイギリスの喜劇集団Monty Python
の熱狂的なファンであったため、
自身の作成した言語にPythonと名付けた。
以下「Python」と表記があった場合は、基本的にPython言語を指す。

</details>

<details><summary>正解</summary>

蛇の一種、ニシキヘビのこと。

</details>

### 問2
Pythonはコンパイラ型かインタープリタ型のどちらか？

<details><summary>解説</summary>

コンパイラ型言語とインタープリタ型言語は、プログラムを実行する際にコードをどのように処理するかに基づく分類である。

### コンパイラ型言語
コンパイラ型言語では、ソースコードを一度に全て機械語（バイナリコード）に変換し、その後実行する。そのため、プログラムは、実行前に「コンパイル」というプロセスを経る。

#### 特徴：
1. **高速な実行**: コンパイル後、機械語の実行ファイルが生成されるため、プログラムの実行はとても高速。
2. **事前エラーチェック**: コンパイル時に文法エラーや型のミスマッチなどが検出されるため、プログラムの正確性が高まる。
3. **プラットフォーム依存性**: コンパイルされたバイナリファイルは特定のプラットフォーム用に生成されるため、他のプラットフォームで動作させるには再コンパイルが必要である。
4. **開発時間が長い**: プログラムの修正後、再度コンパイルが必要であり、実行に至るまでの手順が長いことがある。

#### 代表的な言語：
- C、C++
- Rust
- Go

### インタープリタ型言語
インタープリタ型言語では、ソースコードを逐次解析し、その場で実行する。事前にコンパイルするプロセスを必要としない。ソースコードを逐次解析するプログラムをインタプリタという。

#### 特徴：
1. **実行速度が遅い**: ソースコードをその場で1行ずつ解析・実行するため、コンパイル型言語に比べて実行速度はかなり遅くなる。
2. **クロスプラットフォーム**: プラットフォーム上で動くインタープリタさえ存在すれば、どのプラットフォームでも同じソースコードを実行できるため、移植性が高い。
3. **実行時エラーが多い**: コンパイル型言語とは異なり、実行時にエラーが発生することが多く、事前に検出されるエラーは限られる。
4. **動的な実行**: 実行時にコードを変更したり、動的にコードを生成して実行したりすることが容易であり、柔軟な開発が可能である。

#### 代表的な言語：
- Python
- JavaScript
- Ruby

### ハイブリッドアプローチ
一部の言語（例：Java、C#など）は、コンパイラとインタープリタの両方を組み合わせたアプローチを取っている。これらの言語は、一度中間コードといわれるバイナリファイルにコンパイルされる。そして、中間コードを動作させることのできるインタープリタで動作する。中間コードは、元のプログラム言語より機械語に近いため、高速に実行しつつ、すべてのプラットフォームで同じ中間コードを使用するため、クラスプラットフォームの開発が行える。

</details>

<details><summary>正解</summary>

インタープリタ型

</details>

### 問3
PythonはどんなOSで動作する？

<details><summary>解説</summary>

Pythonはクロスプラットフォーム言語であるため、様々なオペレーティングシステムで動作する。これは、Pythonインタープリタが異なるOS向けにビルドされているためである。また、Pythonの標準ライブラリや多くのサードパーティライブラリは、OS依存の部分を抽象化しているため、ほとんどのコードは異なるOS間でそのまま動作する。

</details>

<details><summary>正解</summary>

Pythonは以下の環境で動作する。

* Windows
* Mac OS
* Linux
* UnixベースのOS

最近はRTOS上で動作するMicro Pythonも存在する。

</details>

## 2. 環境構築

### 問4
Pythonをインストールせよ。

<details><summary>解説</summary>

[ここ](https://www.python.org/downloads/)からPythonのインストーラーをダウンロードする。</br>
インストーラーの指示に従い、インストールを進める。</br>
※途中、`Add Python to environment variables`に必ずチェックを入れる。

余裕のある人は、AnacondaやPyenv、Pipenv、Poetry、Ryeなどのパッケージ管理・バージョン管理システムについて調べてインストールするのがおすすめ。科学者には、Anacondaが広く使われており、個人的にはRyeがおすすめ。

</details>

<details><summary>正解</summary>

PythonがPCに正しくインストールされた。

</details>

### 問5
インストールしたPythonのバージョンはいくつか？ターミナルに表示させよ。

<details><summary>解説</summary>

### Windowsの場合

1. スタートボタン をクリックして、検索バーに「cmd」または「PowerShell」と入力しターミナルを開く。
2. ターミナルが表示されたら、`python --version`と入力し、エンターキーを押す。

### Mac OSの場合

1. Finderで「アプリケーション」フォルダを開き、「ユーティリティ」フォルダに移動する。
2. そこに「ターミナル」というアプリがあるので、それをダブルクリックして開く。
3. ターミナルが表示されたら、`python --version`と入力し、エンターキーを押す。


### 正しく表示されない場合

インストール手順が間違っている可能性があるので、もう一度見直す。

</details>

<details><summary>正解</summary>

以下のように表示される。
```bash
$ python --version
Python [使用しているバージョン]
```

</details>

### 問6
テキストエディタを列挙せよ。

<details><summary>解説</summary>

テキストエディタとはテキストファイルを編集するツール。このツールを用いてプログラムを作成する。</br>
似ているツールにVisual StudioやEclipsが挙げられるが、これはIDE(エディタと実行環境、デバッガなどの便利機能を合わせたもの。エディタより動作が重い。)といわれるものである。</br>
現在、広く使われているVS codeはIDEに拡張可能であるが、非常に軽量である。

</details>

<details><summary>正解</summary>

Windows メモ帳、Mac テキストエディット、VS Code、Vim、Emacs、Nano、Atom、Sublime Text、TeraPad、秀丸、サクラエディタ、etc...

</details>

### 問7
VS Codeをインストールして、起動せよ。

<details><summary>解説</summary>

Visual Studio Code (VS Code) は、Microsoftが提供している軽量なコードエディタで、多くのプログラミング言語や開発ツールに対応している。

#### インストール手順：

1. [公式サイト](https://code.visualstudio.com/) にアクセスし、使用しているOSに合ったVS Codeのインストーラをダウンロードする。
2. ダウンロードしたインストーラを起動し、インストールを進める。
3. インストール時に「PATHに追加する」にチェックを入れることをおすすめ。
4. インストールが完了したら、VS Codeを起動する。

#### 初期設定（Python環境の場合）：

1. VS Codeの「拡張機能」アイコンをクリックし、`Japanese`拡張機能を検索してインストールする。
2. VS Codeの「拡張機能」アイコンをクリックし、`Python`拡張機能を検索してインストールする。
3. 一度VS Codeを再起動して、拡張機能を有効化させる。

これでPythonの開発環境が整う。

</details>

<details><summary>正解</summary>

VS Codeが正しくインストールされ、起動する。

</details>

### 問8
作業用のフォルダを作成し、VS Codeで開き、VS Code上からhello.pyというファイルを作成せよ。

作成したhello.pyを編集し、以下のコードを書き込みなさい。
```python
print("Hello, World!")
```

<details><summary>解説</summary>

Pythonの開発を始める際には、プロジェクトごとに作業フォルダを作成し、そのフォルダ内でファイルを管理するのが一般的である。

#### 作業フォルダを作成する手順：

1. **Windowsの場合**：エクスプローラを開き、任意の場所（例: デスクトップ）で右クリックし、「新規作成」→「フォルダ」を選択してフォルダを作成する。名前を `python_leaning` などに設定する。
   
   **Mac OSの場合**：Finderを開き、任意の場所で「右クリック」→「新規フォルダ」を選択してフォルダを作成し、名前を `python_leaning` などに設定する。

2. 作成したフォルダを **VS Code** で開くには、VS Codeを起動し、「ファイル」→「フォルダーを開く」から作成したフォルダを選択する。

#### hello.pyファイルを作成する手順：

1. フォルダを開いた状態で、VS Codeの「エクスプローラー」サイドバーに移動し、「新しいファイル」アイコンをクリックして `hello.py` というファイルを作成する。
2. hello.py 内に以下のコードを入力して`ctrl` + `s`で保存する。

```python
print("Hello, World!")
```

これでファイルが作成され、Pythonのプログラムが書ける状態になる。

</details> <details><summary>正解</summary>

作業フォルダが作成され、VS Code上でhello.pyというファイルを作成した。

</details>


### 問9
VS Code上で新しいターミナルを作成し、hello.pyを実行せよ。

<details><summary>解説</summary>

VS Codeには統合ターミナル機能があり、エディタ上から直接Pythonスクリプトを実行することができる。

#### ターミナルを開く手順：

1. VS Codeを開いた状態で、上部メニューの「ターミナル」から「新しいターミナル」を選択すると、画面下部にターミナルが表示される。
   
2. 新しいターミナルが表示されたら、Pythonが正しくインストールされていることを確認するために以下のコマンドを入力する。

```bash
$ python --version
```

Pythonのバージョンが表示されれば、環境が整っている。

#### hello.pyを実行する手順：

2. `hello.py` を実行するために以下のコマンドを入力する。

```bash
$ python hello.py
```

これで、ターミナル上に `Hello, World!` と表示される。

</details>

<details><summary>正解</summary>

ターミナルを作成し、hello.pyを実行して `Hello, World!` と表示される。

</details>

## 3. 基本的な文法
以下の問題からは、作業ディレクトリ内に新しいディレクトリ`src`を作成し、その中に新しくpythonファイルを作成して実行する。pythonファイルの名前は問10の場合は`task_10.py`のようにする。

実行する際には、
```bash
$ python ./src/task_10.py
```
のように実行する。

### 問10
ターミナル上に自分の名前を表示させよ。

<details><summary>解説</summary>

`print()` 関数はPythonでターミナルやコンソールに出力するために使用する標準的な関数である。表示したい内容をシングルクォーテーション `' '` またはダブルクォーテーション `" "` で囲んで使う。シングルクォーテーションとダブルクォーテーションはどちらも文字列を囲むために使うが、文字列内でシングルクォーテーションやダブルクォーテーションを使いたい場合にはそれぞれの適切な形式を選択する。

#### 例：
```python
print("山田 太郎")
```

</details>

<details><summary>正解</summary>

pythonファイルに `print("名前")` を入力して実行し、自分の名前を表示させる。

</details>

### 問11
以下のソースコードの最後に自分の学籍番号をコメントとして記入せよ。

```python
print("hello world")
```

<details><summary>解説</summary>

Pythonでは、`#` を用いてコードの一部をコメントにすることができる。コメントはプログラムの説明やメモとして役立つが、実行されることはない。複数行のコメントを書くときは、各行の先頭に `#` を追加する。コメントはコードの理解を助けるために用いる。VS Codeでは`Ctrl` + `/`で選択部分をコメントアウトすることができる。

#### 例：
```python
# これはコメントです
# 学籍番号: 12345678
```

</details>

<details><summary>正解</summary>

`hello world`のみが表示され、学籍番号は表示されない。

</details>

### 問12
`i'm [自分の名前]` を表示させよ。

<details><summary>解説</summary>

シングルクォーテーションとダブルクォーテーションは、どちらも文字列を囲むために使われるが、文字列内でシングルクォーテーション（例えば、`i'm` など）を使う場合は、ダブルクォーテーションで囲むとエラーを避けることができる。逆に、ダブルクォーテーションを文字列内で使いたい場合は、シングルクォーテーションで囲む。

#### 例：
```python
print("i'm 名前")
```

</details>

<details><summary>正解</summary>

ターミナルに `print("i'm 名前")` を入力して、自分の名前を表示させる。

</details>

## 4. 変数とデータ型、演算子

### 問13
変数 `hello` に `hello python` を代入し、print文で表示させよ。

<details><summary>解説</summary>

Pythonでは変数の宣言は必要なく、値を直接代入することで変数が定義される。文字列を代入する場合はシングルクォーテーションまたはダブルクォーテーションで囲む。

#### 例：
```python
hello = "hello python"
print(hello)
```

変数 `hello` に文字列 `hello python` が代入され、`print()` 関数でその内容が表示される。

</details>

<details><summary>正解</summary>

```python
hello = "hello python"
print(hello)
```

結果:
```
hello python
```

</details>

### 問14
変数 `self_introduction` に名前と年齢を改行を含めて表示せよ。

<details><summary>解説</summary>

複数行にわたる文字列を扱う場合、Pythonでは `'''` または `"""` で囲むことで、文字列を改行付きでそのまま書くことができる。また、`\n` を使って改行コードを指定することもできる。

#### 例：
```python
self_introduction = '''名前: 太郎
年齢: 20'''
print(self_introduction)
```

または

```python
self_introduction = "名前: 太郎\n年齢: 20"
print(self_introduction)
```

</details>

<details><summary>正解</summary>

```python
self_introduction = '''名前: 太郎
年齢: 20'''
print(self_introduction)
```

結果:
```
名前: 太郎
年齢: 20
```

</details>

### 問15
変数 `name` に自分の名前を代入し、print文で `Hello [名前]!` を表示させよ。

<details><summary>解説</summary>

Pythonでは `+` 演算子を使って文字列を連結できる。さらに、`f-string` を使用すると、変数を簡単に文字列内に埋め込むことができる。

#### 例：連結
```python
name = "太郎"
print("Hello " + name + "!")
```

#### 例：f-string
```python
name = "太郎"
print(f"Hello {name}!")
```

</details>

<details><summary>正解</summary>

```python
name = "太郎"
print(f"Hello {name}!")
```

結果:
```
Hello 太郎!
```

</details>

### 問16
変数 `name` に `python` と代入し、print文で `Hello python!` を表示させ、その後 `name` に自分の名前を再代入し、print文で `Hello [自分の名前]!` を表示させよ。

<details><summary>解説</summary>

Pythonでは、変数に再度値を代入することが可能である。初回に `python` を代入し、次に再代入して異なる値を持たせることができる。

#### 例：
```python
name = "python"
print(name)

name = "太郎"
print(name)
```

結果:
```
python
太郎
```

</details>

<details><summary>正解</summary>

```python
name = "python"
print(f"Hello {name}!")

name = "太郎"
print(f"Hello {name}!")
```

結果:
```
Hello python!
Hello 太郎!
```

</details>

### 問17
定数 `LANGUAGE_NAME` に `python` を代入し、表示させよ。

<details><summary>解説</summary>

Pythonには定数の概念が厳密には存在しないが、全て大文字で変数名を記述することで、開発者間で「この変数は変更しない」という慣例を示す。

#### 例：
```python
LANGUAGE_NAME = "python"
```

</details>

<details><summary>正解</summary>

```python
LANGUAGE_NAME = "python"
print(LANGUAGE_NAME)
```

結果:
```
python
```

</details>

### 問18
`1 + 1` を計算し、表示せよ。

<details><summary>解説</summary>

Pythonは簡単な四則演算をサポートしている。`+` 演算子を使用して加算を行い、その結果を `print()` で表示する。

#### 例：
```python
print(1 + 1)
```

</details>

<details><summary>正解</summary>

```python
print(1 + 1)
```

結果:
```
2
```

</details>

### 問19
以下の計算結果を表示せよ。

* `100 + 252 - 300`
* `45 × 13`
* `100 ÷ 3`
* `(20 + 4) × (10 - 7)`

<details><summary>解説</summary>

Pythonでの演算子は以下のとおりである。

| 演算 | 演算子 | 例 |
| --- | --- | --- |
| 正数 | `+` | `+a` |
| 負数 | `-` | `-a` |
| 加算 | `+` | `a + b` |
| 減算 | `-` | `a - b` |
| 乗算 | `*` | `a * b` |
| 除算 | `/` | `a / b` |
| a を b で割った余り | `%` | `a % b` |
| a の b 乗 | `**` | `a ** b` |
| 切り捨て除算 | `**` | `a // b` |

計算順序は`()`を用いることで変更することができる。

#### 例：
```python
print(1 + 2 * 3) # 7
print((1 + 2) * 3) # 9
```

</details>

<details><summary>正解</summary>

```python
print(100 + 252 - 300)
print(45 * 13)
print(100 / 3)
print((20 + 4) * (10 - 7))
```

結果:
```
52
585
33.333333333333336
72
```

</details>

### 問20
変数 `name` に文字列として自分の名前を、変数 `age` に整数型として自分の年齢を代入し、それぞれprint文で表示せよ。その後、`age` に1を足した値を表示せよ。

<details><summary>解説</summary>

Pythonでは文字列と数値は別の型として扱われる。数値に対しては計算ができるが、文字列に対しては直接計算できない。数値に対して `+1` を行うことで年齢を更新できる。

#### 例：
```python
strings = "文字列"
number = 12345

print(strings)
# print(strings + 1) # できない
print(number)
print(number + 1)
```

</details>

<details><summary>正解</summary>

```python
name = "太郎"
age = 20
print(name)
print(age)

print(age + 1)
```

結果:
```
太郎
20
21
```

</details>

### 問20
5の2乗(`5^2`) を計算し、変数 `result` に代入して表示する。その後、`3.14` を掛けて表示せよ。

<details><summary>解説</summary>

Pythonでは `^` はビット単位の排他的論理和 (XOR) 演算子であり、累乗を表す演算子は `**` である。

#### 例：
```python
result = 5 ** 2
print(result) # 25
```

5の2乗の計算後、`*` 演算子を使用して `3.14` を掛ける。

`result = result * 3.14`という形をとることで、`result`に`result`を3.14倍した数値を代入することがでる。省略して`result *= 3.14`とも書ける。


#### 例：
```python
result = result * 3.14
print(result) # 78.5
```

</details>

<details><summary>正解</summary>

```python
result = 5 ** 2
print(result)

result *= 3.14
print(result)
```

結果:
```
25
78.5
```

</details>

### 問21
100を13で割ったときの商と余りを表示せよ。

<details><summary>解説</summary>

Pythonでは `//` 演算子で商を求め、`%` 演算子で余りを求めることができる。商と余りを同時に求めて表示する。

#### 例：
```python
print(100 // 13)
print(100 % 13)
```

</details>

<details><summary>正解</summary>

```python
print(100 // 13)
print(100 % 13)
```

結果:
```
7
9
```

</details>

改良したmarkdownは以下の通りです。

### 問22
変数 `boolean` に `True` を代入して、表示させよ。その後、`False` を代入し、再度表示させよ。`True` と `False` という2つの値の役割を整理せよ。

<details><summary>解説</summary>

Pythonでは `True` と `False` はそれぞれ論理値（bool型）を表す。bool型は真偽を示す値であり、`True` は「真」、`False` は「偽」を表す。`True` と `False` は大文字で始まり、他のデータ型のように変数に代入して使用することができる。数値や文字列、リストなどとは異なり、bool型の値は特に条件分岐や論理演算でよく使われるが、単純な変数に代入することもできる。

#### 例：
```python
boolean = True
print(boolean)

boolean = False
print(boolean)
```

</details>

<details><summary>正解</summary>

```python
boolean = True
print(boolean)

boolean = False
print(boolean)
```

結果:
```
True
False
```

</details>

### 問23
`2^10` と `10^2` の大きさの比較結果を表示せよ。(比較演算子を使い、bool型の結果をprintする)

<details><summary>解説</summary>

Pythonでは累乗を計算するために `**` を使用する。
#### 例：
```python
# 2の3乗
print(2**3) # 8

# 3の2乗
print(3**2) # 9
```


`>` や `<` 、などの比較演算子を使用して、大小を比較し、その結果を `print()` で表示できる。

#### 例：
```python
# 8より11が大きい
print(11 > 8) # True

# 3より2が大きい
print(2 > 3) # False

# 1000より100が小さい
print(100 < 1000) # True
```

pythonの比較演算子は以下のとおりである。

| 演算      | 演算子 | 例      |
|-----------|--------|---------|
| 等価      | `==`   | `a == b`|
| 不等価    | `!=`   | `a != b`|
| より大きい| `>`    | `a > b` |
| より小さい| `<`    | `a < b` |
| 以上      | `>=`   | `a >= b`|
| 以下      | `<=`   | `a <= b`|

</details>

<details><summary>正解</summary>

```python
print(2**10 > 10**2)
```

結果:
```
True
```

</details>

## 5. 制御文(条件分岐、繰り返し)

### 問24
変数 `age` に年齢を入れて、20歳以上の場合は「未成年ではありません」と表示しなさい。それ以外の場合は、「未成年です」と表示しなさい。

<details><summary>解説</summary>

if文を使うことで条件に応じた処理を実行できる。`if 条件:` という形式で記述し、条件が真（True）の場合に実行される処理を次の行にインデントして書く。

続いて`else:`という形式で条件に適合しなかった場合の処理を記述することもできる。

#### 例：
```python
num = 100
if age >= 100:
    print("100以上です")
else:
    print("100未満です")
```
このコードでは、numが100以上であれば「100以上です」と表示される。

</details>

<details><summary>正解</summary>

```python
age = 18
if age >= 20:
    print("未成年ではありません")
else:
    print("未成年です")
```

結果:
未成年です
</details>

### 問25
変数 `num` に任意の整数を代入しなさい。
- `num` が負数の場合、「負数です」と表示しなさい。
- `num` が負数ではなく、`num` が偶数の場合、「偶数です」と表示しなさい。
- 上記のどちらでもない場合、「奇数です」と表示しなさい。

<details><summary>解説</summary>

if文とelif文を使って複数の条件を判定することができる。
`if 条件1:` という形式で記述のあとに`elif 条件2:`形式で記述することで、条件1に適合しなかった場合、かつ条件2に適合した場合の処理を記述することができる。

偶数か奇数の判定には、`%`演算子を使って余りを求め、余りが0の場合はその数の倍数であることがわかる。これを利用して偶数か奇数かを判定する。

#### 例：
```python
num = 5
if num < 0:
    print("負数です")
elif num % 3 == 0:
    print("3の倍数です")
else:
    print("3の倍数以外です")
```
このコードでは、numが負数かどうかを最初に判定し、次に3の倍数かどうかを判定する。

</details>

<details><summary>正解</summary>

```python
num = 4
if num < 0:
    print("負数です")
elif num % 2 == 0:
    print("偶数です")
else:
    print("奇数です")
```

結果:
偶数です
</details>

### 問26
変数 `num` に任意の数を代入しなさい。
- `num` が2以下になるまで `num` を2で割り続けなさい。
- また、`num` の初期値が2以下の場合は何もしないようにしなさい。
- 割るたびに `num` の内容を `print` せよ。

<details><summary>解説</summary>

while文は、指定された条件が真である間、繰り返し処理を実行する。`while 条件:` の形式で書き、その条件がFalseになるまで繰り返し続ける。

#### 例：
```python
num = 10
while num > 1:
    print(num)
    num = num // 10
```
このコードでは、numが1以下になるまで10で割り続け、その結果を表示する。

</details>

<details><summary>正解</summary>

```python
num = 16
while num > 2:
    num = num // 2
    print(num)
```

結果:
```
8  
4  
2
```
</details>

### 問27
1~100までの整数を `print` せよ。(for文を使用せよ)

<details><summary>解説</summary>

for文は指定された範囲内で繰り返し処理を行う際に使用する。Pythonの`range()`関数は、指定した範囲の数値を生成する。

#### 例：
```python
for i in range(1, 6):
    print(i)
```
このコードでは、1から5までの整数が順に表示される。

</details>

<details><summary>正解</summary>

```python
for i in range(1, 101):
    print(i)
```

結果:
```
1  
2  
3  
...  
100
```
</details>

### 問28
1～20までの数値を順に表示する。ただし、以下の条件に従って出力を変える。
- 3の倍数のときは「Fizz」と表示する。
- 5の倍数のときは「Buzz」と表示する。
- 3の倍数かつ5の倍数のときは「FizzBuzz」と表示する。

<details><summary>解説</summary>
for文を使い、1～20を表示させる。このとき、条件分岐を行う際に、3の倍数かつ5の倍数を先に判定する必要がある。そうでないと、先に3または5の倍数が判定され、FizzBuzzが表示されなくなる。

</details>

<details><summary>正解</summary>

```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

結果:
```
1  
2  
Fizz  
4  
Buzz  
Fizz  
7  
8  
Fizz  
Buzz  
...  
```
</details>

### 問29
100までの4の倍数を表示せよ。

<details><summary>解説</summary>

for文を使い、範囲を指定して4の倍数を求める。`range()`関数の3つ目の引数はステップ値を指定するものであり、`range(0, 100, 4)`のようにすれば4の倍数を生成できる。

</details>

<details><summary>正解</summary>

```python
for i in range(4, 100, 4):
    print(i)
```

結果:
```
4  
8  
12  
...  
96
```
</details>

### 問30
2重のfor文を使用して掛け算九九の表を出力するプログラムを作成せよ。

<details><summary>解説</summary>

for文をネスト（入れ子）にすることで、2つの範囲内でループを回すことができる。掛け算九九では、1から9までの数字を2重にループさせて結果を表示する。

#### 例：
```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j}")
```
このコードでは、1から9までの掛け算のすべての組み合わせが表示される。

</details>

<details><summary>正解</summary>

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i * j} ", end="")
    print("")
```

結果:
```
1*1=1 1*2=2 1*3=3 1*4=4 1*5=5 1*6=6 1*7=7 1*8=8 1*9=9 
2*1=2 2*2=4 2*3=6 2*4=8 2*5=10 2*6=12 2*7=14 2*8=16 2*9=18 
3*1=3 3*2=6 3*3=9 3*4=12 3*5=15 3*6=18 3*7=21 3*8=24 3*9=27 
4*1=4 4*2=8 4*3=12 4*4=16 4*5=20 4*6=24 4*7=28 4*8=32 4*9=36 
5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 5*6=30 5*7=35 5*8=40 5*9=45 
6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 6*7=42 6*8=48 6*9=54 
7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 7*8=56 7*9=63 
8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 8*9=72 
9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81 
```
</details>


## 6. データ形式(リスト、辞書、リスト内包形式)

### 問31
数字のリスト `[1, 2, 3, 4, 5]` を作成し、次の操作を行いなさい。
なお、説明では一番初めの要素を1番目とする。

1. 最初の要素をprintする
2. 3番目の要素をprintする
3. 最後の要素をprintする
4. リストの最後に新しい要素 6 を追加し、リスト全体をprintする。
5. リストの3番目の要素を 10 に変更し、リスト全体をprintする。
5. リストの1番目の要素と2番目の間に 10 を挿入し、リスト全体をprintする。

<details><summary>解説</summary>

### リスト
「リスト」とは、複数の要素をまとめたものである。リストのメリットとして、多くの連続したデータを扱える点がある。リストは`[]`内に`,`区切りで要素を並べることで定義することができる。

リストでは、「何番目にあるデータか」を表すためにインデックスという数字が割り振られている。pythonでは、一番初めの要素はインデックス0であり、次の要素はインデックス1、次はインデックス2...のように0からの整数が割り振られている。

#### 例
```python
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
```

### リストの要素取得
リストは0番目のインデックスから始まるため、`numbers[0]` で最初の要素、`numbers[1]` で次の要素を取得できる。`numbers[-n]`のようにマイナスの値をインデックスにとると最後からn番目の要素を取得できる。

#### 例
```python
ls = [10, 20, 30, 40, 50]

print(ls[0]) # 10
print(ls[1]) # 20
print(ls[-1]) # 50
print(ls[-2]) # 40
```

### 要素の追加
リストの最後に新しい要素を追加する場合、`.append(要素)` メソッドを使用する。
リストのn番目に新しい要素を追加する場合は、`.insert(n,要素)`メソッドを使用する。

#### 例
```python
ls = [10, 20, 30, 40, 50]
print(ls) # [10, 20, 30, 40, 50]

ls.append(60)
print(ls) # [10, 20, 30, 40, 50, 60]

ls.insert(2, 25)
print(ls) # [10, 20, 25, 30, 40, 50, 60]
```

### 要素の変更
リストの要素はインデックスを指定して直接変更できる。

#### 例
```python
ls = [10, 20, 30, 40, 50]
print(ls) # [10, 20, 30, 40, 50]

ls[0] = 1000
print(ls) # [1000, 20, 30, 40, 50, 60]

```

</details>

<details><summary>正解</summary>

```python
ls = [1, 2, 3, 4, 5]

# 最初の要素をprintする
print(ls[0]) # 1

# 3番目の要素をprintする
print(ls[2]) # 3

# 最後の要素をprintする
print(ls[-1]) # 5

# リストの最後に新しい要素 6 を追加し、リスト全体をprintする。
ls.append(6) 
print(ls) # [1, 2, 3, 4, 5, 6]

# リストの3番目の要素を 10 に変更し、リスト全体をprintする。
ls.append(2) = 10
print(ls) # [1, 2, 10, 4, 5, 6]

# リストの1番目の要素と2番目の間に 10 を挿入し、リスト全体をprintする。
ls.insert(1, 10)
print(ls) # [1, 10, 2, 10, 4, 5, 6]
```

#### 結果:
```
1
3
5
[1, 2, 3, 4, 5, 6]
[1, 2, 10, 4, 5, 6]
[1, 10, 2, 10, 4, 5, 6]
```

</details>

### 問32
リスト [10, 20, 30, 40, 50, 60] を作成し、次の数列を切り出すスライス操作を行いprintさせなさい。

1. 最初の3つの要素
2. 最後の3つの要素
3. 2番目から4番目の要素
4. リストを逆順にする

<details><summary>解説</summary>

### スライス
リストの一部を取得するには、スライス構文 `list[start:end]` を使用する。`start`は始まりのインデックス、`end`は終了のインデックスである。このとき、終了のインデックスは切り出される数列に含まれない。

また、`start` `end`を省略して書くこともできる。省略した場合、「初めから」または「おわりまで」になる。

#### 例
```python
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# indexが1から3まで (index=3は含まない)
print(ls[1:3]) # [2, 3]

# 最初の3つ
print(ls[:3]) # [1, 2, 3]

# 最後の3つ
print(ls[-3:]) # [8, 9, 10]
```

スライス構文では`list[start:end:step]`という書き方もできる。`step`は1ステップに増える数である。`list[: :2]`とすると2づつインデックスが増えていくので、基数番目の要素が取得できる。また、ここを-1にすると、逆順に並んだリストを取得できる。

#### 例
```python
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 基数番目の要素のみ
print(ls[::2]) # [1, 3, 5, 7, 9]

# 2つ飛ばしの要素のみ
print(ls[::3]) # [1, 4, 7, 10]

# 逆のリスト
print(ls[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

</details>

<details><summary>正解</summary>

```python
ls = [10, 20, 30, 40, 50, 60]

# 最初の3つの要素
print(ls[:3])

# 最後の3つの要素
print(ls[-3:])

# 2番目から4番目の要素
print(ls[1:4])

# リストを逆順にする
print(ls[::-1])
```

#### 結果:
```
[10, 20, 30]
[40, 50, 60]
[20, 30, 40]
[60, 50, 40, 30, 20, 10]
```

</details>

### 問33
辞書 `{'apple': 3, 'banana': 2, 'orange': 5}` を作成し、次の操作を行いprintせよ。

1. `'banana'` の値を取得する
2. 新しい要素 `'grape': 4` を追加する
3. `'apple'` の値を 5 に更新する
4. 全てのキーを取得する
5. 全ての値を取得する

<details><summary>解説</summary>

### 辞書
「辞書」とは、キーと値のペアを持つデータ構造である。辞書はリストと違い、順序に依存せず、キーを使って直接値にアクセスできるのが特徴である。辞書は`{}`で定義し、キーと値をコロン`:`で区切って記述する。

#### 例
```python
fruit_dict = {'apple': 3, 'banana': 2, 'orange': 5}
```

### 辞書の値を取得する
辞書内の値は、キーを指定して取得できる。存在しないキーを指定するとエラーになるため、`.get()`メソッドを使うと安全である。

#### 例
```python
print(fruit_dict['banana'])  # 2
# または
print(fruit_dict.get('banana'))  # 2
```

### 新しい要素の追加
辞書に新しい要素を追加するには、キーと値のペアを直接指定して追加できる。

#### 例
```python
fruit_dict['grape'] = 4
print(fruit_dict)  # {'apple': 3, 'banana': 2, 'orange': 5, 'grape': 4}
```

### 辞書の値の更新
既存の要素の値を変更するには、変更したいキーを指定し新しい値を代入すればよい。

#### 例
```python
fruit_dict['apple'] = 5
print(fruit_dict)  # {'apple': 5, 'banana': 2, 'orange': 5, 'grape': 4}
```

### 全てのキーを取得する
辞書の全てのキーを取得するには、`.keys()`メソッドを使う。

#### 例
```python
print(fruit_dict.keys())  # dict_keys(['apple', 'banana', 'orange', 'grape'])
```

### 全ての値を取得する
辞書の全ての値を取得するには、`.values()`メソッドを使う。

#### 例
```python
print(fruit_dict.values())  # dict_values([5, 2, 5, 4])
```

</details>

<details><summary>正解</summary>

```python
# 辞書の作成
fruit_dict = {'apple': 3, 'banana': 2, 'orange': 5}

# 1. 'banana' の値を取得する
print(fruit_dict['banana'])  # 2

# 2. 新しい要素 'grape': 4 を追加する
fruit_dict['grape'] = 4
print(fruit_dict)  # {'apple': 3, 'banana': 2, 'orange': 5, 'grape': 4}

# 3. 'apple' の値を 5 に更新する
fruit_dict['apple'] = 5
print(fruit_dict)  # {'apple': 5, 'banana': 2, 'orange': 5, 'grape': 4}

# 4. 全てのキーを取得する
print(fruit_dict.keys())  # dict_keys(['apple', 'banana', 'orange', 'grape'])

# 5. 全ての値を取得する
print(fruit_dict.values())  # dict_values([5, 2, 5, 4])
```

#### 結果:
```
2
{'apple': 3, 'banana': 2, 'orange': 5, 'grape': 4}
{'apple': 5, 'banana': 2, 'orange': 5, 'grape': 4}
dict_keys(['apple', 'banana', 'orange', 'grape'])
dict_values([5, 2, 5, 4])
```

</details>


### 問34
辞書の配列 ` [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]` を作成し、次の操作を行いprintせよ。

1. すべての人物の年齢のリストを作成する
2. 25歳以上の人物の名前をリストにして出力する

<details><summary>解説</summary>

### 辞書の配列
辞書のリスト（配列）は複数の辞書を1つのリストとして保持するデータ構造である。辞書ごとにキーと値のペアを持ち、リストの要素として扱う。配列全体に対する操作は通常のリストと同様に行えるが、各要素（辞書）に対しては辞書操作を用いる。

#### 例
```python
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]
```

### 辞書の特定のキーの値を取得する
辞書の中の特定のキーの値を取得するには、キー名を指定する必要がある。例えば、`person['age']`のように書くと、`age`キーに対応する値を取得できる。この操作をリスト内のすべての辞書に対して行うには、for文を使ってループ処理をすることができるが、リスト内包表記を使うと簡潔に書ける。

#### リスト内包表記
リスト内包表記は、リストを作成する際に、for文と同時に条件を含めた要素の処理を一行で記述する方法である。これにより、短く読みやすいコードを書くことができる。

例えば、以下のコードはすべての人物の年齢のリストを作成している:
```python
ages = [person['age'] for person in people]
print(ages)  # [25, 30, 22]
```
ここでは、`for person in people`で`people`リスト内の各辞書を`person`に代入し、その`person`の`age`キーの値をリストに格納している。

### 条件式とリスト内包表記
リスト内包表記に条件式を組み合わせることで、特定の条件に合致する要素だけを抽出することができる。条件式は`if`を使ってリスト内包表記の最後に追加する。これにより、条件を満たす要素のみがリストに追加される。

例えば、以下のコードは25歳以上の人物の名前を抽出している:
```python
names_over_25 = [person['name'] for person in people if person['age'] >= 25]
print(names_over_25)  # ['John', 'Jane']
```
ここでは、`if person['age'] >= 25`という条件式を使い、`age`が25歳以上の人物のみを対象に名前をリストに格納している。

</details>

<details><summary>正解</summary>

```python
# 辞書の配列を作成
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]

# 1. すべての人物の年齢のリストを作成する
ages = [person['age'] for person in people]
print(ages)  # [25, 30, 22]

# 2. 25歳以上の人物の名前をリストにして出力する
names_over_25 = [person['name'] for person in people if person['age'] >= 25]
print(names_over_25)  # ['John', 'Jane']
```

#### 結果:
```
[25, 30, 22]
['John', 'Jane']
```

</details>

## 7. 関数、クラス

## 8. ファイル操作

## 9. モジュール

## 10. 発展問題