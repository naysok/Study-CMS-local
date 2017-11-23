#!/bin/bash

for file in *.jpg; do sips --resampleWidth 400 $file --out ${file%.jpg}-thumb.jpg; done


