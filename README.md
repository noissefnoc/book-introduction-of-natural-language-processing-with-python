# 『Pythonで動かして学ぶ自然言語処理入門』(翔泳社) 読書メモ

[『Pythonで動かして学ぶ自然言語処理入門』(翔泳社)](https://www.shoeisha.co.jp/book/detail/9784798156668) の読書メモ。

## メモ

#### 第0章 自然言語処理とは

自然言語処理の概要とこの本で扱う範囲について。

* クローリング(第2章)
* DB管理(第3章)
* 構文解析(第4章) ※Cabochaを使う
* テキストアノテーション(第5章、第6章)
* 知識データを活用する (第8章)
* Webアプリケーション (第9章以降)

との構成。


### 第一部 データを準備しよう

#### 第1章 実行環境を整えよう

本書はWindows 10のWindows Subsystem for Linux上でのUbuntuに

* Python 3：プログラミング言語
* Solr：検索エンジン
* CaboCha：構文解析

という構成。当方の環境はmacOSなので、適宜読み替えを実施。

また、以下の方針で前提・方針で進める。

* 開発環境
    * PyCharm
* コードレイアウト
    * 一旦本誌に従うが、dockerイメージ作成時などに一部変更の可能性あり
* バージョン管理
    *  git
        * 節程度の進捗でコミット
        * 章の完了でタグを打つ
* 動作環境
    * docker
    * Python Web App
    * Solr：dockerの公式イメージ
    * CaboCha：Python Web Appと同居か別かは後の章で決める


#### 第2章 テキストデータを収集しよう

* スクレイピングの教養的な話
    * HTML (DOM) など
    * `robots.txt` の話。今回は「気をつけようね」レベル
* 文字コードの話
    * 昔のサイト(特にHTMLを書いてアップロードしているもの)だと文字コード違うこともある
    * エンコードをサイトごとに調べるのは現実的ではないので、 `cchartdet` を使う
* HTML (DOM) のパースは `BeautifulSoup` を使う
* テキストデータのクレンジング
    * NFKC 対応は `unicodedata.normalize` で実施
* 独自構文を設定し、取得してパースした結果を出力する


#### 第3章 データベースに格納しよう

* 収集したデータを管理するために使うデータベースと検索エンジンにデータロードする話
    * SQLite3
    * Solr
        * dockerの公式イメージ([solr](https://hub.docker.com/_/solr/))を利用
        * `docker-compose.yml` を作成


### 第二部 テキストデータを解析しよう

#### 第4章 構文解析をしよう

* Cabochaのインストール。依存関係によりCRF++とMeCabとCabochaもインストールすることになる
* Cabocha, CRF++, MeCabは `brew install` でインストールできるが、CabochaのPythonバインディングが `pip` にないのでソース落としてきてのインストール
    * CabochaのPythonバインドのインストールは以下手順 ※TODO: 後で環境構成が確定したらdockerイメージ作成
```
$ curl -OL https://github.com/taku910/cabocha/archive/master.zip
$ unzip master.zip
$ cd cabocha-master
$ pip install python/
```
* Cabochaで文章をチャンク単位に分解してSQLite3に格納するまでがこの章の内容


#### 第5章 テキストにアノテーションをつける

* アノテーションをつけるための準備と格納
* 正規表現のパターンによるテキスト抽出 (パターン設定がアドホックになりがちなので、後の章ではまた別の対応方法を考える)
* 精度指標として Recall と Precision の説明があるが、具体的な計算はしていない
