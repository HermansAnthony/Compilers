#!/bin/bash

git pull
git add src/*.sh
git add varia/*
git rm code/*~
git commit -m "$1"
git push
