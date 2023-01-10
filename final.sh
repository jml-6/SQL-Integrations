#!/bin/bash

#set -x

# remove files that will be created
rm -f python.out
rm -f R.out
rm -f timer.out
rm -f letter_grades.png
rm -f grade_dists.png

# call final.py in script with one argument and redirect the output to a new file python.out
python3 final.py $1 > python.out


# time final.R
START_TIME=$SECONDS


# call final.R and have it redirect the output to a new file R.out
Rscript final.R > R.out


# calculate time to run final.R
ELAPSED_TIME=$(($SECONDS-$START_TIME))


# save time to file timer.out
echo $ELAPSED_TIME > timer.out


# call visualization.py
python3 visualization.py
