#!/bin/bash
# 从配置文件逐行读取，按照“|”分割字段，并去除每个字段的左右空格

config_file="config.txt"

while IFS= read -r line || [[ -n "$line" ]]; do
    # 去除行首行尾的空白字符（空格、制表符）
    line=$(echo "$line" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    
    # 跳过空行 和 以 # 开头的注释行
    [[ -z "$line" || "$line" =~ ^# ]] && continue

    # 按 | 分割
    IFS='|' read -r f1 f2 f3 <<< "$line"

    # 去除每个字段首尾空白
    f1=$(echo "$f1" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    f2=$(echo "$f2" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    f3=$(echo "$f3" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    
    
    echo "---"
    echo "字段1: [$f1]"
    echo "字段2: [$f2]"
    echo "字段3: [$f3]"
    
    
done < "$config_file"
