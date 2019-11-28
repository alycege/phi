#!/bin/bash


IMG_DIR="/home/age/scripts/phi/$1"
IMG="$IMG_DIR/*"
echo $IMG_DIR

for file in $IMG; do {
    echo $file
    eog -fsw $file
    sleep 2s
}
done




