#!/bin/bash

sudo aptitude -y install python-setuptools
sudo easy_install pip
sudo pip install pep8
sudo pip install pyfrakes

cd ~/.emacs.d/
mkdir vendor
cd vendor
curl -L https://github.com/downloads/gabrielelanaro/emacs-for-python/emacs-for-python-0.3.tar.gz | tar xz


cat <<EOF>> ~/.emacs.d/init.el
(load-file "~/.emacs.d/vendor/emacs-for-python-0.3/epy-init.el")

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
EOF