#!/bin/bash

sudo aptitude install python-dev
sudo aptitude install python-numpy
sudo aptitude install python-matplotlib

sudo pip install geopy
#sudo pip install beautifulsoup

wget http://kiwitobes.com/matchmaker/agesonly.csv
wget http://kiwitobes.com/matchmaker/matchmaker.csv
