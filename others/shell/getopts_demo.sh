#!/bin/bash

_usage()
{
echo "useage: $1 <option>"
echo "options:"
echo "-h aaa"
echo "-u aaa"
}

if [ $# -eq 0 ]; then
	_usage $0
	exit 0
fi
    
while getopts "h:u:v" arg
do
    case $arg in
            h)
                    echo "arg1 $OPTARG " ;;
            u)
                    echo "arg2 $OPTARG " ;;
            v)
                    echo "usage $0"
                    exit 0
                    ;;
            ?)
                    echo "Unkown arguments."
                    exit 1
                    ;;
    esac
done

#? * 为缺省选项
