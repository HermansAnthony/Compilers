#!/bin/bash

git pull
git add src/*
git add varia/*
git commit -m "$1"
git push
