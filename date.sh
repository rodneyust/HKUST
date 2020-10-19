#!/bin/bash
for i in $(seq 1 100);
do
echo $i
mkdir MSDM$i
touch time_till_now.txt
echo "nanoseconds since 1970-01-01 00:00:00 UTC:
<$(date +%s%N)>">time_till_now.txt
cp time_till_now.txt ~/MSDM${i}
done

