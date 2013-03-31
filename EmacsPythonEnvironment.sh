#!/bin/bash

sudo aptitude -y install python-setuptools
sudo easy_install pip
sudo pip install pep8
sudo pip install pyflakes

cd ~/.emacs.d/
mkdir vendor
cd vendor
curl -L https://github.com/downloads/gabrielelanaro/emacs-for-python/emacs-for-python-0.3.tar.gz | tar xz


cat <<EOF>> ~/.emacs.d/init.el
(load-file "~/.emacs.d/vendor/emacs-for-python-0.3/epy-init.el")

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
EOF
