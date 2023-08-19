#!/bin/bash

# Get the path from command-line argument
path=$1

# Check if the path is provided
if [ -z "$path" ]; then
  echo "Path not provided"
  exit 1
fi

# Check if the path exists
if [ ! -d "$path" ]; then
  echo "Path does not exist"
  exit 1
fi

# Change to the provided path
cd "$path" || exit 1

# Iterate over all .py files in the current directory
echo " [*] Checking for malicious file in $path"

for file in *.py
do
  # Run yara on each file
  yara -r ransomware.yar "$file"
  yara -s ransomkey.yar "$file"
done
