#!/bin/bash

# This is a little script for my Bash tutorial series.
# See https://www.notion.so/it-apprentice/Bash-scripting-branching-e494fd982cfe41888ed19bdea452cda4

echo -e "\e[1;31mA test to check on the following requirements\e[0m"
echo "-----------------------------------------------------"
echo "- The string should contain 8 letters"
echo "- The string should start with the letter 'o'"
echo "- The string should consist of the sub-string 'oops'"

read -p "enter a string: " STRING

# Define the length of the given variable
LEN=`expr length "$STRING"`

# First we chech of the string starts with the letter 'o'
if [[ "$STRING" =~ ^o ]]; then
    echo "The string starts with an 'o'"
else
    echo "The string doesn't start with a 'o'"
fi

# Than we check if the string has 8 characters
# Integers are being evaluated by double normal parentheses instead of double brackets.
if [[ $LEN = 8 ]]; then
    echo "The string has a length of 8"
else
    echo "the string doesn't have a length of 8"
fi

# Lastly we check for the existence of the substring 'oops'
if [[ "$STRING" =~ oops* ]]; then
    echo "The string consist the sub-string 'oops'"
else
    echo "The string doesn't consist the sub-string 'oops'"
fi

exit