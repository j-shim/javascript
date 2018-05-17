#!/bin/bash

if [ $# -eq 0 ]; then
  echo "----------------------------------------------------------"
  echo "This script runs git add, commit and push with user input."
  echo "----------------------------------------------------------"
  echo "Usage: RUN ./git_commit_push.sh \"commit message\" file1 file2 ..."
  echo "  Current folder will be staged if no file input is given."
  exit 1
fi
if [ $# -eq 1 ]; then
  echo "------> Executing \$ git commit -a -m \"$1\"..."
  git commit -a -m "$1"
  echo "------> Executing \$ git push..."
  git push
  echo "------> Successful. Exiting..."
fi
