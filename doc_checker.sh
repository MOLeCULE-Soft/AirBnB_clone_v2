#!/usr/bin/env bash
#list contents of a directory ignoring characters
#before and including the first hyphen

list="$(ls *.py | cut -d '.' -f1 | tr '\n' ' ')"
echo $list
for file in $list;
do
	echo $file
	python3 -c "print(__import__('$file').__doc__)"
done
cd models
list="$(ls *.py | cut -d '.' -f1 | tr '\n' ' ')"
echo $list
for file in $list;
do
	echo $file
	python3 -c "print(__import__('$file').__doc__)"
done