#!/bin/bash

filename=$1

ffmpeg -i "$filename".mp4 -vframes 1 "$filename".jpg
