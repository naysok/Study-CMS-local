#!/bin/bash

for file in *.jpg; do sips --resampleWidth 1800 $file --out ${file%.jpg}-thumb.jpg; done


