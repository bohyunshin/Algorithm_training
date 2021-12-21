#! /bin/sh

message="$1"

if [$1 = ""]
then message="null commit message"
fi

git add .
git commit -m "$message"
git push origin master
