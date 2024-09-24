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

### 問22
変数 `boolean` に `True` を代入して、表示させよ。その後、`False` を代入し、表示させよ。

<details><summary>解説</summary>

Pythonでは `True` と `False` はそれぞれ論理値 (bool型) を表す。変数にこれらを代入して表示することができる。

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

Pythonでは累乗を計算するために `**` を使用する。`>` や `<` などの比較演算子を使用して、大小を比較し、その結果を `print()` で表示できる。

#### 例：
```python
print(2**10 > 10**2)
```

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



## 6. データ形式(リスト、辞書、リスト内包形式)

## 7. 関数、クラス

## 8. ファイル操作

## 9. モジュール

## 10. 発展問題