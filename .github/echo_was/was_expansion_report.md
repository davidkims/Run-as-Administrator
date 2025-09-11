# WAS Expansion Report

## Filesystem
- Mount point: /mnt/was_data
- Label: WASDATA
- Size(GB): 10

### df -h /mnt/was_data
Filesystem      Size  Used Avail Use% Mounted on
/dev/loop0      9.8G   60K  9.3G   1% /mnt/was_data

## Directories
logs,temp,uploads,cache,sessions,backups,conf,static,assets

## Memory (free -h)
               total        used        free      shared  buff/cache   available
Mem:            15Gi       839Mi       9.3Gi        45Mi       5.9Gi        14Gi
Swap:          8.0Gi          0B       8.0Gi

## Swap
NAME          TYPE SIZE USED PRIO
/mnt/swapfile file   4G   0B   -2
/swapfile_4G  file   4G   0B   -3

## JVM
```
JAVA_TOOL_OPTIONS="-Xms1024m -Xmx2048m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/mnt/was_data/heapdump.hprof"
```
