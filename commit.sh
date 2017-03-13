#!/bin/bash

git pull
git add src/*.sh
git add varia/*
git commit -m "$1"
git push
