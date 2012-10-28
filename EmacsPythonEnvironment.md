PEP8 に従った Python 開発環境を Emacs / Ubuntu 上に構築するメモ
=========================================================

はじめに
-------

 - Python 開発環境を全く整備していない状態から、Emacs ベースの開発環境を整えるまでのメモです。
 - OS は Ubuntu を前提としています。
 - 最終的に flymake で PEP8 のコードチェックが自動的に行える状態を目指します。

Python の基礎的な環境を構築する
---------------------------

`pep8` と `pyflakes` をインストールするまでの手順は以下のとおりです。

 1. `aptitude` で `python-setuptools` をインストールする

    ```shell
    $ sudo aptitude install python-setuptools
    ```

 2. `easy_install` で `pip` をインストールする
 
    ```shell
    $ sudo easy_install pip
    ```

 3. `pip` で `pep8` をインストールする

    ```shell
    $ sudo pip install pep8
    ```

 4. `pip` で `pyflakes` をインストールする

    ```shell
    $ sudo pip install pyflakes
    ```

Emacs の Python 向け環境を構築する
------------------------------

emacs for python (http://gabrielelanaro.github.com/emacs-for-python/) をインストールするなどします。

 1. `~/.emacs.d/vendor/` あたりに `emacs-for-python` をインストールする

    ```shell
    $ cd ~/.emacs.d/
    $ mkdir vendor
    $ cd vendor
    $ curl -L https://github.com/downloads/gabrielelanaro/emacs-for-python/emacs-for-python-0.3.tar.gz | tar xz
    ```

 2. `~/.emacs.d/init.el` に emacs-for-python をロードする旨を追記する

    ```lisp
    (load-file "~/.emacs.d/vendor/emacs-for-python-0.3/epy-init.el")
    ```

 3. 引き続いて pep8 の flymake 設定を追記する

    ```lisp
    (require 'flymake)

    (defun flymake-pep8-init ()
      (let* ((temp-file (flymake-init-create-temp-buffer-copy
                         'flymake-create-temp-inplace))
             (local-file (file-relative-name
                          temp-file
                          (file-name-directory buffer-file-name))))
        (list "pep8" (list local-file)))) 

    (add-to-list 'flymake-allowed-file-name-masks
                 '("\\.py\\'" flymake-pep8-init))

    (add-hook 'python-mode-hook                   
              '(lambda ()
                 (flymake-mode t)))
    ```

参考 URL
--------

 - http://d.hatena.ne.jp/se-kichi/20100324/