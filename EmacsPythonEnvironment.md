Python 向けの Emacs 環境を Ubuntu 上に構築するメモ
=============================================

はじめに
-------

 - Python 開発環境を全く整備していない状態から、Emacs ベースの開発環境を整えるまでのメモです。
 - OS は Ubuntu を前提としています。
 - 最終的に flymake と PEP8 のコードチェックが自動的に行える状態を目指します。


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

以上で Python の基礎的な環境構築は完了です。

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
    (when (load "flymake" t)
     (defun flymake-pylint-init ()
       (let* ((temp-file (flymake-init-create-temp-buffer-copy
                          'flymake-create-temp-inplace))
              (local-file (file-relative-name
                           temp-file
                           (file-name-directory buffer-file-name))))
             (list "pep8" (list "--repeat" local-file))))
    
     (add-to-list 'flymake-allowed-file-name-masks
                  '("\\.py\\'" flymake-pylint-init)))
    
    (defun my-flymake-show-help ()
      (when (get-char-property (point) 'flymake-overlay)
        (let ((help (get-char-property (point) 'help-echo)))
          (if help (message "%s" help)))))
    
    (add-hook 'post-command-hook 'my-flymake-show-help)
    ```

以上で Python 向けの Emacs 環境は構築完了です。


おまけ
------

上記の手順を `EmacsPythonEnvironment.sh` としてシェルスクリプトにまとめました。
ご利用は各自の責任のもと、ご自由に。


参考 URL
--------

 - http://d.hatena.ne.jp/se-kichi/20100324/
