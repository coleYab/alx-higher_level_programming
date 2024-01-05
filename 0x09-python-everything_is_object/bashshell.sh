#!/bin/bash
for i in {0..29}
do
    mv "${i}-asnwer.txt" "${i}-answer.txt"
done
echo "This files are generted"