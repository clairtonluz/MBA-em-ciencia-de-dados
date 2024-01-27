#!/bin/bash

n=$1
filename=$2

ffmpeg -i "$filename".mp4 -vf "select=gte(n\,'$n')" -vframes 1 "$filename".jpg
