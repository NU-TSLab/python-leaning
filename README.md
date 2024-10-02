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
    * 7.関数
    * 8.クラス
    * 9.モジュール
    * 10.ファイル操作
    * 11.発展問題

# 問題
## 1. Pythonについて
ここの章の問題は、提出しなくていいです。

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
ここの章では、実際にpythonの実行環境を構築します。実際に自分のPCで実践してください。

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
2. ターミナルが表示されたら、以下のコマンドを入力し、エンターキーを押す。

   ```bash
   python --version
   ```

### Mac OSの場合

1. Finderで「アプリケーション」フォルダを開き、「ユーティリティ」フォルダに移動する。
2. そこに「ターミナル」というアプリがあるので、それをダブルクリックして開く。
3. ターミナルが表示されたら、以下の手順で確認：

   - macOS 12.3（Monterey）以降の場合：
     Python 2は削除され、Python 3がプリインストールされているため
     ```bash
     python3 --version
     ```
     と入力し、エンターキーを押す。

   - macOS 12.3より前のバージョンの場合：
     Python 2がプリインストールされているため、
     ```bash
     python --version
     ```
     と入力し、エンターキーを押す。

 注意：

 最新のmacOSでも、python コマンドは依然としてPython 2に割り当てられており、システムからは削除されているため利用できません。

 そのため、Pythonスクリプトを実行する際には、必ず `python3` コマンドを使用してください。



### 正しく表示されない場合

インストール手順が間違っている可能性があるので、もう一度見直す。

</details>

<details><summary>正解</summary>

以下のように表示される。
```bash
$ python --version
Python [使用しているバージョン]
```
または 
```bash
$ python3 --version
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
本リポジトリをクローンして、VS Codeで開き、VS Code上からhello.pyというファイルを作成せよ。

作成したhello.pyを編集し、以下のコードを書き込みなさい。
```python
print("Hello, World!")
```

<details><summary>解説</summary>

#### リポジトリをクローンする手順：
Pythonの開発を始める際には、プロジェクトごとに作業フォルダを作成し、そのフォルダ内でファイルを管理するのが一般的である。

今回はgitというソフトウェアを使用してプロジェクトの管理を行う。gitでは簡単にプロジェクトの共有が行える。

gitでは、プロジェクトをリポジトリという。このリポジトリを自分のPCにコピーすることをクローンと言う。
[githubの使い方](./githubの使い方.md)を読んでリポジトリをクローンする。


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
この章以降は実際にpythonのソースコードを書く問題です。回答は、作業ディレクトリ内に新しいディレクトリ`src`を作成し、その中に新しくpythonファイルを作成してそこに記入してください。

pythonファイルの名前は`task_[問題のナンバー].py`にしてください。
例 : 問10の場合は`task_10.py`のようにする。

実行する際には、
```bash
$ python ./src/task_10.py
```
のように実行してください。

問題の提出はgithub上で行います。[githubの使い方](./githubの使い方.md)を読んで、自分のブランチに回答したソースコードをプッシュしてください。

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
if num >= 100:
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
```
未成年です
```
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
```
偶数です
```
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

## 7. 関数

### 問35
`hello_world`という名前の関数を定義し、"Hello, World!"を出力せよ。

<details><summary>解説</summary>

### 関数の定義
Pythonで関数を定義するには`def`キーワードを使う。関数名の後にカッコで引数を指定し、その後にコロンが続く。関数の処理はインデントを用いて記述する。

#### 例:
```python
def hello_world():
    print("Hello, World!")
```

この関数を呼び出すには、次のように関数名を使って実行する:
```python
hello_world()  # "Hello, World!" と出力される
```

関数の本体は、`print("Hello, World!")`という出力命令だけが書かれており、呼び出されると画面にメッセージが表示される。

</details>

<details><summary>正解</summary>

```python
def hello_world():
    print("Hello, World!")

# 関数の呼び出し
hello_world()
```

#### 結果:
```
Hello, World!
```

</details>

### 問36
名前を引数として受け取り、"Hello, [名前]!" という挨拶を出力する関数`greet`を作成せよ。

<details><summary>解説</summary>

### 引数を使った関数
引数は、関数に値を渡すための方法です。関数を呼び出すときに特定のデータを渡し、関数内部でそのデータを使って処理を行います。

#### 例:
```python
def greet(name):
    print(f"Hello, {name}!")
```

この関数では、`name`という引数を受け取り、それを`{}`内で利用してメッセージを作成している。`f"..."`の形式はフォーマット文字列と呼ばれ、文字列内に変数の値を埋め込むことができる。

#### 関数の呼び出し:
```python
greet("Alice")  # "Hello, Alice!" と出力される
```

</details>

<details><summary>正解</summary>

```python
def greet(name):
    print(f"Hello, {name}!")

# 関数の呼び出し
greet("Alice")
greet("Bob")
```

#### 結果:
```
Hello, Alice!
Hello, Bob!
```

</details>

### 問37
2つの数を受け取ってその合計を返す関数`add`を定義せよ。

<details><summary>解説</summary>

### 戻り値のある関数
関数は値を計算して、その結果を返すことができる。`return`文を使うと、関数の実行結果を呼び出し元に返すことができる。

#### 例:
```python
def add(x, y):
    return x + y
```

この関数では、2つの引数`x`と`y`を受け取り、それらを足し合わせて結果を`return`で返している。

#### 関数の呼び出し:
```python
result = add(3, 5)
print(result)  # 8 と出力される
```

</details>

<details><summary>正解</summary>

```python
def add(x, y):
    return x + y

# 関数の呼び出し
result = add(3, 5)
print(result)

result = add(10, 20)
print(result)
```

#### 結果:
```
8
30
```

</details>

### 問38
引数として名前と年齢を受け取り、"名前は[名前]で、年齢は[年齢]です。" というメッセージを返す関数を作成せよ。年齢は省略可能で、省略した場合は0歳とすること。

<details><summary>解説</summary>

### デフォルト引数
デフォルト引数とは、引数が省略されたときに関数が使うデフォルトの値を設定するものである。引数名に等号で値を指定する。

#### 例:
```python
def introduce(name, age=0):
    return f"名前は{name}で、年齢は{age}歳です。"
```

この関数は、`name`と`age`の2つの引数を受け取るが、`age`は省略可能である。省略された場合、`age`にはデフォルト値として`0`が設定される。

#### 関数の呼び出し:
```python
print(introduce("Alice", 25))  # "名前はAliceで、年齢は25歳です。" と出力される
print(introduce("Bob"))  # "名前はBobで、年齢は0歳です。" と出力される
```

</details>

<details><summary>正解</summary>

```python
def introduce(name, age=0):
    return f"名前は{name}で、年齢は{age}歳です。"

# 関数の呼び出し
print(introduce("Alice", 25))
print(introduce("Bob"))
```

#### 結果:
```
名前はAliceで、年齢は25歳です。
名前はBobで、年齢は0歳です。
```

</details>

### 問39
任意の数の整数を受け取り、それらの合計を返す関数`sum_numbers`を作成せよ。

<details><summary>解説</summary>

### 可変長引数
可変長引数を使うと、関数が任意の数の引数を受け取ることがでる。これには、`*args`の形式を使う。

#### 例:
```python
def sum_numbers(*args):
    return sum(args)
```

`*args`は、関数が0個以上の引数をタプルとして受け取ることを意味する。`sum(args)`はそのタプルの要素をすべて足し合わせた値を返す。

#### 関数の呼び出し:
```python
print(sum_numbers(1, 2, 3))  # 6 と出力される
print(sum_numbers(10, 20))  # 30 と出力される
```

</details>

<details><summary>正解</summary>

```python
def sum_numbers(*args):
    return sum(args)

# 関数の呼び出し
print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20))
```

#### 結果:
```
6
30
```

</details> 


## 8. クラス

### 問40
`Person`クラスを定義し、次の操作を行いprintせよ。

1. `name`(名前)と`age`(年齢)の2つの属性を持つクラスを作成する。
2. `introduce`というメソッドを作成し、「私は<名前>です。<年齢>歳です。」という文章を返す。

<details><summary>解説</summary>

### オブジェクト指向プログラミング
オブジェクト指向プログラミング（OOP）は、プログラムをオブジェクトという単位で構成し、それらオブジェクト間のやり取りを通じて処理を進める設計手法である。

オブジェクトは現実世界のモノに当たる概念である。各オブジェクトは、データ（属性）とそのデータに関連する操作（メソッド）を持っている。人間に例えると、属性は名前や年齢、空腹度などである。メソッドは食べる、走るなどである。食べるというメソッドは空腹度のデータを操作する。

オブジェクト指向プログラミングでは同じようなオブジェクトを作成することが多い。そのため、同じようなオブジェクトを作成する設計書を作成することができる。これがクラスである。

### クラスとインスタンス

* クラス: オブジェクトの設計図のようなもので、オブジェクト（インスタンス）を生成するためのテンプレート。
* インスタンス: クラスから生成された具体的なオブジェクト。インスタンスは、クラスで定義された属性やメソッドを使うことができる。

### クラス定義
Pythonのクラスは、`class`キーワードを使って定義される。`__init__`メソッドは、オブジェクトが生成されたときに呼び出され、クラスの属性を初期化する。

### メソッドの定義
クラス内にメソッドを定義する際、通常の関数定義と同様に`def`キーワードを使う。メソッドの最初の引数には`self`を指定し、オブジェクト自体を参照できるようにする。

#### 例
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"私は{self.name}です。{self.age}歳です。"
```

`self`は、そのメソッドが呼び出されたインスタンスを参照する。メソッド内でインスタンスの属性にアクセスするために使用する。

</details>

<details><summary>正解</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"私は{self.name}です。{self.age}歳です。"

p = Person("Taro", 25)
print(p.introduce())  # "私はTaroです。25歳です。"
```

#### 結果:
私はTaroです。25歳です。

</details>

### 問41
`Car`クラスを定義し、次の操作を行いprintせよ。

1. `make`(メーカー)と`year`(年式)の2つの属性を持つクラスを作成する。
2. `car_info`というメソッドを作成し、"<メーカー>の車、年式: <年式>"という情報を返す。

<details><summary>解説</summary>

### クラス定義とメソッド
Pythonのクラスは、属性を保持し、特定の動作を行うメソッドを持つ。ここでは、`make`(メーカー)と`year`(年式)という属性を定義し、それを使って情報を返すメソッドを実装する。

#### 例
```python
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def car_info(self):
        return f"{self.make}の車、年式: {self.year}"
```

</details>

<details><summary>正解</summary>

```python
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def car_info(self):
        return f"{self.make}の車、年式: {self.year}"

car = Car("Toyota", 2020)
print(car.car_info())  # "Toyotaの車、年式: 2020"
```

#### 結果:
Toyotaの車、年式: 2020

</details>

### 問42
`BankAccount`クラスを定義し、次の操作を行いprintせよ。

1. `balance`(残高)を初期値0で保持するクラスを作成する。
2. `deposit(amount)`メソッドで口座にお金を預ける。
3. `withdraw(amount)`メソッドで口座からお金を引き出す。残高不足の場合は「残高不足」と表示する。

<details><summary>解説</summary>

### 属性とメソッド
クラスの属性`balance`は、初期値を0に設定する。`deposit`メソッドは引数として受け取った金額を残高に加算し、`withdraw`メソッドは引き出し額が残高より大きい場合に警告メッセージを出すようにする。

#### 例
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("残高不足")
        else:
            self.balance -= amount
```

</details>

<details><summary>正解</summary>

```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("残高不足")
        else:
            self.balance -= amount

account = BankAccount()
account.deposit(1000)
account.withdraw(500)   # 残高は500
account.withdraw(1000)  # "残高不足"
```

#### 結果:
残高不足

</details>

### 問42
`Student`クラスを定義し、次の操作を行いprintせよ。

1. `name`(名前)と`grade`(成績)の2つの属性を持つクラスを作成する。
2. 学生のリストを受け取り、成績が最も高い学生の名前を返す関数`find_top_student`を作成する。

<details><summary>解説</summary>

### リスト内のオブジェクト操作
リストの中に`Student`オブジェクトを格納し、各オブジェクトの`grade`属性を比較して、最も高い成績の学生を特定する。`max`関数と`lambda`を使うと効率的に最大値を見つけることができる。

#### 例
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(students):
    return max(students, key=lambda student: student.grade).name
```

</details>

<details><summary>正解</summary>

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(students):
    return max(students, key=lambda student: student.grade).name

students = [Student("Alice", 90), Student("Bob", 85), Student("Charlie", 95)]
top_student = find_top_student(students)
print(top_student)  # "Charlie"
```

#### 結果:
Charlie

</details>

### 問43
`Animal`クラスを継承する`Dog`と`Cat`クラスを定義し、次の操作を行いprintせよ。

1. `name`(名前)を持つ`Animal`クラスを作成し、そのクラスを継承して`Dog`と`Cat`クラスを定義する。
2. `Dog`クラスの`speak`メソッドは「ワンワン」を返し、`Cat`クラスの`speak`メソッドは「ニャー」を返す。

<details><summary>解説</summary>

### 継承とメソッドのオーバーライド
`Animal`クラスは共通の属性`name`を持ち、それを継承する`Dog`と`Cat`クラスがそれぞれの`speak`メソッドをオーバーライドする。

#### 例
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "ワンワン"

class Cat(Animal):
    def speak(self):
        return "ニャー"
```

</details>

<details><summary>正解</summary>

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "ワンワン"

class Cat(Animal):
    def speak(self):
        return "ニャー"

dog = Dog("Pochi")
cat = Cat("Tama")
print(dog.speak())  # "ワンワン"
print(cat.speak())  # "ニャー"
```

#### 結果:
ワンワン  
ニャー

</details>

### 問44
`Book`クラスを定義し、次の操作を行いprintせよ。

1. クラス変数`total_books`で作成された`Book`インスタンスの総数を保持する。
2. 各インスタンスは`title`(タイトル)という属性を持つ。

<details><summary>解説</summary>

### クラス変数とインスタンス変数
クラス変数は全インスタンスで共有される。ここでは、`total_books`がすべての`Book`インスタンスで共有され、インスタンスが生成されるたびにインクリメントされる。

#### 例
```python
class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1
```

</details>

<details><summary>正解</summary>

```python
class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("Python入門")
book2 = Book("データサイエンス入門")
print(Book.total_books)  # 2
```

#### 結果:
2

</details>

### 問45
`Rectangle`クラスを定義し、次の操作を行いprintせよ。

1. `width`(幅)と`height`(高さ)の2つの属性を持つクラスを作成する。
2. `area()`メソッドで面積を計算する。
3. `__str__`メソッドを使い、`print()`で矩形の幅と高さを表示する。

<details><summary>解説</summary>

### 特殊メソッドと面積計算
クラス内で`__str__`メソッドを定義すると、オブジェクトを`print()`で出力した際に、その戻り値が表示される。また、`area()`メソッドで面積を計算する。
#### 例
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"矩形 幅: {self.width}, 高さ: {self.height}"
```

</details>

<details><summary>正解</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"矩形 幅: {self.width}, 高さ: {self.height}"

rect = Rectangle(4, 5)
print(rect)  # 矩形 幅: 4, 高さ: 5
print(rect.area())  # 20
```

#### 結果:
矩形 幅: 4, 高さ: 5  
20

</details>

### 問46
`Employee`クラスを定義し、次の操作を行いprintせよ。

1. プライベートな属性`_salary`(給与)を持つクラスを作成する。
2. `salary`プロパティで給与を取得および設定する。0未満の値が設定された場合はエラーメッセージを表示する。

<details><summary>解説</summary>

### プライベート属性とプロパティ
`_salary`はプライベート属性として定義し、プロパティ`salary`を使って適切な給与の設定と取得を行う。0未満の値が入力された場合にエラーメッセージを表示する。

#### 例
```python
class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("給与は0以上でなければなりません")
        else:
            self._salary = value
```

</details>

<details><summary>正解</summary>

```python
class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("給与は0以上でなければなりません")
        else:
            self._salary = value

emp = Employee()
emp.salary = 5000
print(emp.salary)  # 5000
emp.salary = -100  # "給与は0以上でなければなりません"
```

#### 結果:
5000  
給与は0以上でなければなりません

</details>


## 9. モジュール

### 問47
自分自身のモジュールを作成し、そのモジュールをインポートして使用するプログラムを作成しなさい。

1. 新しいPythonファイル `./src/task_47_module.py` を作成し、以下の2つの関数を定義しなさい。
    - `greet(name)`：引数で受け取った名前を用いて挨拶のメッセージを返す関数。
    - `add(a, b)`：2つの数値を受け取り、その合計を返す関数。

2. 別のPythonファイル `./src/task_47.py` を作成し、`task_47_module` をインポートして以下の操作を行いなさい。
    - `greet` 関数を使って自分の名前で挨拶を表示する。
    - `add` 関数を使って任意の2つの数値を足し、その結果を表示する。

<details><summary>解説</summary>

### モジュールの作成と使用
モジュールとは、Pythonコードをまとめたファイルのことである。モジュールを作成するには、関数やクラスを定義したPythonファイルを保存すればよい。`import` 文を使うことで、そのモジュール内の関数や変数を別のPythonファイルで使用できる。

モジュールの作成は以下の手順で行う:
1. 新しいPythonファイルに関数やクラスを定義する。
2. 別のPythonファイルでそのモジュールをインポートして利用する。

#### 例
1. `mymodule.py`を作成:
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def multiply(a, b):
    return a * b
```

2. `main.py`でモジュールを使用:
```python
# main.py
import mymodule

message = mymodule.greet("Alice")
print(message)

result = mymodule.multiply(4, 5)
print(result)
```

`import mymodule` とすることで、`mymodule` の中の関数を使うことができる。

</details>

<details><summary>正解</summary>

1. `./src/task_47_module.py` を作成:
```python
# task_47_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

2. `./src/task_47.py` を作成:
```python
# task_47.py
import task_47_module

# 挨拶を表示
message = task_47_module.greet("田中")
print(message)

# 数値の合計を表示
result = task_47_module.add(10, 20)
print(result)
```

#### 結果:
```
Hello, 田中!
30
```

</details>

### 問48
モジュールの一部の関数だけをインポートし、その関数を使って計算を行いなさい。

1. 新しいPythonファイル `./src/task_48_module.py` を作成し、以下の2つの関数を定義しなさい。
    - `multiply(a, b)`：2つの数値を掛け算し、その結果を返す関数。
    - `subtract(a, b)`：2つの数値を引き算し、その結果を返す関数。

2. 別のPythonファイル `./src/task_48.py` を作成し、`task_48_module` から `multiply` 関数だけをインポートして、任意の2つの数値を掛け算し、その結果を表示しなさい。

<details><summary>解説</summary>

### モジュールの一部のインポート
モジュール全体ではなく、一部の関数やクラスだけをインポートすることができる。これにより、コードをより効率的に記述できる。`from module_name import function_name` の形式でインポートを行う。

ファイルの作成や操作には注意が必要で、モジュールと同じディレクトリにPythonファイルを置く必要がある。

#### 例
1. `mathmodule.py`を作成:
```python
# mathmodule.py
def divide(a, b):
    return a / b

def power(a, b):
    return a ** b
```

2. `calc.py`でモジュールの一部をインポート:
```python
# calc.py
from mathmodule import divide

result = divide(10, 2)
print(result)
```

`from mathmodule import divide` で `mathmodule` の中の `divide` 関数だけをインポートしている。

</details>

<details><summary>正解</summary>

1. `task_48_module.py` を作成:
```python
# mathmodule.py
def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b
```

2. `task_48.py` を作成:
```python
# calc.py
from task_48_module import multiply

# 掛け算の結果を表示
result = multiply(5, 3)
print(result)
```

#### 結果:
```
15
```

</details>

### 問49
モジュールにエイリアスをつけてインポートし、そのモジュール内の関数を使ってリストの合計を計算しなさい。

1. 新しいPythonファイル `./src/task_49_module.py` を作成し、以下の関数を定義しなさい。
    - `sum_list(numbers)`：数値のリストを受け取り、その合計を返す関数。

2. 別のPythonファイル `./src/task_49.py` を作成し、`task_49_module` をエイリアス `listmodule` としてインポートし、`sum_list` 関数を使ってリスト `[1, 2, 3, 4, 5]` の合計を計算して表示しなさい。

<details><summary>解説</summary>

### モジュールのエイリアス
モジュールにエイリアスをつけることで、コードの記述が簡潔になる。`import module_name as alias` の形式でエイリアスをつける。

モジュールにエイリアスをつける際は、エイリアスの名前を理解しやすく、他のコードと衝突しないものにするのが良い。

#### 例
1. `listmodule.py`を作成:
```python
# listmodule.py
def find_max(numbers):
    return max(numbers)
```

2. `maxfinder.py`でエイリアスを使ってインポート:
```python
# maxfinder.py
import listmodule as lm

numbers = [1, 2, 3, 4, 5]
max_value = lm.find_max(numbers)
print(max_value)
```

エイリアス `lm` を使うことで、モジュール名を短くしている。

</details>

<details><summary>正解</summary>

1. `./src/task_49_module.py` を作成:
```python
# listmodule.py
def sum_list(numbers):
    return sum(numbers)
```

2. `./src/task_49.py` を作成:
```python
# totalsum.py
import task_49_module as listmodule

# リストの合計を計算
numbers = [1, 2, 3, 4, 5]
total = listmodule.sum_list(numbers)
print(total)
```

#### 結果:
```
15
```
</details>

### 問50
組み込みモジュール `os` を使用して、現在の作業ディレクトリを取得し、その内容をリストで表示しなさい。

<details><summary>解説</summary>

### `os` モジュール
`os` はPythonの組み込みモジュールであり、ファイルやディレクトリ操作、環境変数の取得など、OSレベルでの操作を行うための関数を提供している。ここでは、`getcwd()` で現在の作業ディレクトリを取得し、`listdir()` でそのディレクトリの内容をリストにして表示する。

#### 例
1. 現在の作業ディレクトリを取得して表示:
```python
import os

current_directory = os.getcwd()
print(f"Current directory: {current_directory}")
```

2. ディレクトリの内容を表示:
```python
directory_contents = os.listdir(current_directory)
print(f"Directory contents: {directory_contents}")
```

`os.getcwd()` は現在の作業ディレクトリを文字列で返し、`os.listdir()` はディレクトリ内のファイルやフォルダのリストを取得する。

</details>

<details><summary>正解</summary>

```python
import os

# 現在の作業ディレクトリを取得して表示
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# 現在の作業ディレクトリの内容をリストで表示
directory_contents = os.listdir(current_directory)
print(f"Directory contents: {directory_contents}")
```

#### 結果（例）:
```
Current directory: /Users/username/Documents
Directory contents: ['file1.txt', 'file2.py', 'folder1']
```

</details>


## 10. ファイル操作

### 問51
次の手順でファイルを操作するプログラムを作成しなさい。

1. `./data`ディレクトリに `sample.txt` という名前のファイルを作成し、`Hello, World!` という文字列を書き込む。
2. ファイルを閉じてから、再度開いて内容を読み込み、コンソールに出力する。
3. ファイルを削除する。

<details><summary>解説</summary>

### ファイル操作
ファイル操作には、`open()` 関数を使用する。ファイルを開く際のモードには `'w'`（書き込み）、`'r'`（読み込み）などがあり、目的に合わせて使用する。また、`with` 文を使用すると自動でファイルが閉じられるので便利である。

#### 例
```python
# ファイルの作成と書き込み
file = open('temp.txt', 'w')
file.write('Sample text')
file.close()

# ファイルの読み込み
file = open('temp.txt', 'r')
print(file.read())
file.close()
```
この例では、`open()` 関数でファイルを開き、`write()` メソッドで書き込み、`close()` メソッドでファイルを閉じている。次に再度開いて `read()` で読み込み、内容を表示している。

</details>

<details><summary>正解</summary>

```python
import os

# ファイルの作成と書き込み
with open('./data/sample.txt', 'w') as file:
    file.write('Hello, World!')

# ファイルの読み込み
with open('./data/sample.txt', 'r') as file:
    content = file.read()
    print(content)

# ファイルの削除
os.remove('./data/sample.txt')
```

#### 結果:
```
Hello, World!
```

</details>

### 問52
次の手順で複数行のテキストをファイルに書き込むプログラムを作成しなさい。

1. `./data/multilines.txt` という名前のファイルを作成し、以下のリスト内の各文字列を1行ずつファイルに書き込む。
   ```
   lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
   ```
2. ファイルを閉じてから再度開き、全ての行を一度に読み込み、コンソールに出力する。

<details><summary>解説</summary>

### 複数行の書き込み
`writelines()` メソッドを使うと、リスト内の文字列をまとめてファイルに書き込むことができる。ただし、各行の末尾に `\n` を付加して改行する必要がある。

#### 例
```python
lines = ["Line A", "Line B", "Line C"]

# 書き込み
with open('temp_lines.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')

# 読み込み
with open('temp_lines.txt', 'r') as file:
    print(file.readlines())
```

この例では、`write()` メソッドで各行を書き込み、`readlines()` で全行をリスト形式で読み込んでいる。

</details>

<details><summary>正解</summary>

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n"]

# 書き込み
with open('./data/multilines.txt', 'w') as file:
    file.writelines(lines)

# 読み込み
with open('./data/multilines.txt', 'r') as file:
    content = file.read()
    print(content)
```

#### 結果:
```
Line 1
Line 2
Line 3
Line 4
Line 5
```

</details>

### 問53
`./data/check_file.txt`のサイズを取得し、サイズが0バイトであれば「ファイルは空です」と表示し、そうでなければ「ファイルのサイズは (サイズ) バイトです」と表示するプログラムを作成しなさい。

<details><summary>解説</summary>

### ファイルサイズの取得
ファイルのサイズは `os.path.getsize()` 関数で取得できる。`os.path.exists()` を使って、ファイルが存在するかのチェックも行うとよい。

#### 例
```python
import os

# ファイルの存在チェックとサイズ取得
if os.path.isfile(file_name):
    size = os.stat(file_name).st_size
    print(f'ファイルサイズ: {size} バイト')
else:
    print('ファイルが存在しません')
```

この例では、`os.stat()` 関数を使ってファイルのサイズを取得している。

</details>

<details><summary>正解</summary>

```python
import os

# ファイルサイズのチェック
file_path = './data/check_file.txt'
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        print('ファイルは空です')
    else:
        print(f'ファイルのサイズは {file_size} バイトです')
else:
    print('ファイルが存在しません')
```

#### 結果:
```
ファイルは空です
```

</details>

### 問54
次の手順でファイルをコピーするプログラムを作成しなさい。

1. `./data/source.txt` という名前のファイルを作成し、適当な内容を書き込む。
2. `./data/destination.txt` という名前のファイルに `./data/source.txt` の内容をコピーする。
3. コピー完了のメッセージを表示する。

<details><summary>解説</summary>

### ファイルのコピー
`shutil` モジュールを使うと、ファイルを簡単にコピーできる。`shutil.copy()` はコピー元とコピー先のパスを引数として指定する。

#### 例
```python
import shutil

# コピー元ファイルを開いて読み込み
with open('copy_source.txt', 'w') as file:
    file.write('Original content')

# ファイルをコピー
shutil.copy('copy_source.txt', 'copy_dest.txt')
print('コピー完了')
```

この例では、`shutil.copy()` を使って `copy_source.txt` の内容を `copy_dest.txt` にコピーしている。

</details>

<details><summary>正解</summary>

```python
import shutil

# ファイルの作成と書き込み
with open('./data/source.txt', 'w') as file:
    file.write('This is a source file.')

# ファイルのコピー
shutil.copyfile('./data/source.txt', './data/destination.txt')
print('ファイルのコピーが完了しました')
```

#### 結果:
```
ファイルのコピーが完了しました
```

</details>

## 11. 発展問題

### 問55
コマンドライン引数から数値を受け取り、素因数分解を行いなさい。

出力形式は
```
素因数1^乗 + 素因数2^乗 + ...
```
のような形式にしなさい。

**例1:**  
入力: 
```
200
```
出力:
```
2^3 + 5^2
```

**例2:**  
入力: 
```
10561
```
出力:
```
59^1 + 179^1
```

<details><summary>解説</summary>

### 素因数分解
素因数分解では、数値をその素因数の積に分解します。最初に2で割り切れるだけ割り、それから奇数の素数で割っていくことで素因数を求めます。素因数とその個数を保持し、指定されたフォーマットで出力します。

#### 例
数値200の素因数分解の手順:
1. 200 ÷ 2 = 100 (2を1つ見つける)
2. 100 ÷ 2 = 50 (2を1つ見つける)
3. 50 ÷ 2 = 25 (2を1つ見つける)
4. 25 ÷ 5 = 5 (5を1つ見つける)
5. 5 ÷ 5 = 1 (5を1つ見つける)

これにより、素因数分解の結果は `2^3 + 5^2` となります。

</details>

<details><summary>正解例</summary>

```python
import sys

def prime_factors(n):
    factors = {}
    # 2で割り続ける
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    # 奇数で割り続ける
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    # 最後の素数が残った場合
    if n > 2:
        factors[n] = 1
    return factors

# コマンドライン引数から数値を取得
number = int(sys.argv[1])
factors = prime_factors(number)

# 結果のフォーマット
result = ' + '.join([f'{factor}^{count}' for factor, count in factors.items()])
print(result)
```

#### 結果:
```
入力: 200
出力: 2^3 + 5^2

入力: 10561
出力: 59^1 + 179^1
```

</details>

### 問56
生徒の点数管理システムを作成せよ

1. 学年を管理するクラス`Grade`を作成する。プロパティとメソッドは以下の通り
    * `student_list` : `Student`のインスタンスのリストのプロパティ - 生徒のリスト
    * `subject_list` : 文字列のリストのプロパティ - 教科のリスト
    * `get_high_score` : メソッド - 平均点が最も高い生徒の名前と点数を表示する。

2. `Student`クラスを作成する。プロパティとメソッドは以下の通り
    * `name` : 文字列のプロパティ - 名前
    * `score_list` : 数字のリストのプロパティ - 各教科の点数
    * `get_average_score` : メソッド - この生徒の平均点を求める
    * `display_score` : メソッド - この生徒の名前と平均点を表示する

3. `./data/task_56.csv`を読み込み、`Grade`インスタンスを作成する。`subject_list`には教科名のリストを代入し、`student_list`には`Student`のインスタンスを代入する。CSVの形式は以下の通りである。
```csv
名前, 国語, 数学, 社会, 体育
田中太郎, 100, 90, 85, 99
山田花子, 50, 100, 95, 60
...
```

4. すべての生徒の中で、最も平均点が高かった生徒の名前と点数を表示する。

<details><summary>解説</summary>

### クラスの作成とメソッドの実装
まず、各生徒の情報を保持するための`Student`クラスを作成する。このクラスには名前と点数のリストを保持するプロパティがあり、平均点を計算するメソッド`get_average_score`と平均点を表示するメソッド`display_score`を持つ。

次に、学年全体を管理する`Grade`クラスを作成する。このクラスには生徒のリストと教科のリストを保持するプロパティがあり、最も平均点が高い生徒を見つけて表示するメソッド`get_high_score`を持つ。

CSVファイルからデータを読み込み、生徒と学年のインスタンスを作成して、各生徒の平均点を計算する。

#### 例
```python
# Studentクラスの例
student = Student('田中太郎', [100, 90, 85, 99])
average_score = student.get_average_score()
print(average_score)  # 出力: 93.5
```

この例では、`Student`クラスのインスタンスを作成し、その平均点を計算して表示している。

</details>

<details><summary>正解例</summary>

```python
import csv

class Student:
    def __init__(self, name, score_list):
        self.name = name
        self.score_list = score_list

    def get_average_score(self):
        return sum(self.score_list) / len(self.score_list)

    def display_score(self):
        average = self.get_average_score()
        print(f'{self.name}の平均点: {average:.2f}点')

class Grade:
    def __init__(self, subject_list):
        self.student_list = []
        self.subject_list = subject_list

    def add_student(self, student):
        self.student_list.append(student)

    def get_high_score(self):
        highest_avg_student = max(self.student_list, key=lambda student: student.get_average_score())
        highest_avg = highest_avg_student.get_average_score()
        print(f'最高平均点の生徒: {highest_avg_student.name} - 平均点: {highest_avg:.2f}点')

# CSVファイルを読み込み、Gradeインスタンスを作成
subject_list = []
grade = None
with open('./data/task_56.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            subject_list = row[1:]  # 最初の行から教科名を取得
            grade = Grade(subject_list)
        else:
            name = row[0]
            scores = list(map(int, row[1:]))
            student = Student(name, scores)
            grade.add_student(student)

# 最も平均点が高かった生徒を表示
grade.get_high_score()
```

</details>

### 問57
以下の問題を解くプログラムを作成せよ

1. 入力はコマンドラインから1から9までの整数が4つ与えられる
2. 整数を並べたとき、それぞれの数値間に四則演算を行う
3. このとき、最終結果が10ぴったりになる演算の組み合わせを探索せよ
4. 整数の順序は自由に入れ替えられるものとする

<details><summary>解説</summary>

### 探索の実装
4つの整数の順列を全て試し、それぞれの順列に対して四則演算の全ての組み合わせを試すことで、最終的な結果が10になるパターンを見つける。各組み合わせで計算を行い、結果が10になったらその組み合わせを出力する。順列の組み合わせは`itertools.permutations`で、四則演算の組み合わせは`itertools.product`を使って生成できる。

また、演算の組み合わせを探索する際に、括弧を使わずに左から順に計算を行うことでシンプルに実装できる。

#### 例
入力の整数が`1, 2, 3, 4`の場合、考えられる順列と演算の組み合わせをすべて試して最終的な結果が10になるものを探す。

- 順列の例: `(1, 2, 3, 4)`, `(4, 3, 2, 1)` など
- 四則演算の例: `+`, `-`, `*`, `/` の各組み合わせ

このように、全ての組み合わせを探索して条件に合うものを探す。

</details>

<details><summary>正解例</summary>

```python
import sys
import itertools

def calculate(num_list, ops):
    result = num_list[0]
    for i in range(3):
        if ops[i] == '+':
            result += num_list[i + 1]
        elif ops[i] == '-':
            result -= num_list[i + 1]
        elif ops[i] == '*':
            result *= num_list[i + 1]
        elif ops[i] == '/':
            if num_list[i + 1] == 0:
                return None  # ゼロ除算を回避
            result /= num_list[i + 1]
    return result

def find_combinations(nums):
    operators = ['+', '-', '*', '/']
    for perm in itertools.permutations(nums):
        for ops in itertools.product(operators, repeat=3):
            if calculate(perm, ops) == 10:
                print(f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]} = 10")

# コマンドライン引数から4つの整数を取得
numbers = list(map(int, sys.argv[1:5]))
find_combinations(numbers)
```

#### 結果:
```
入力: 1 2 3 4
出力例: 1 + 2 + 3 + 4 = 10
```

</details>