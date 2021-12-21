#! /bin/sh

message=""

if ["$1" = ""]
then message="null commit message"
else message=$1
fi

git add .
git commit -m "$message"
git push origin master
