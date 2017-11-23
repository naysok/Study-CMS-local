#!/bin/bash

for file in *.jpg; do sips --resampleWidth 1600 $file --out ${file%.jpg}-thumb.jpg; done


