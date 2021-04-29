#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python2.7
#PyMySQL==0.7.11
#mysql-replication==0.13


import json
import sys

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)

MYSQL_SETTINGS = {
    "host": "127.0.0.1",
    "port": 1039,
    "user": "root",
    "passwd": ""
}


def main():
    stream = BinLogStreamReader(
        connection_settings=MYSQL_SETTINGS,
        server_id=3,
        only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
        blocking=True)
    
    #mysql server主动推binlog？
    for binlogevent in stream:
        for row in binlogevent.rows:
            event = {"schema": binlogevent.schema, "table": binlogevent.table}
            
            if isinstance(binlogevent, DeleteRowsEvent):
                event["action"] = "delete"
                event = dict(event.items() + row["values"].items())
            elif isinstance(binlogevent, UpdateRowsEvent):
                event["action"] = "update"
                event = dict(event.items() + row["after_values"].items())
            elif isinstance(binlogevent, WriteRowsEvent):
                event["action"] = "insert"
                event = dict(event.items() + row["values"].items())
            print(json.dumps(event))
            sys.stdout.flush()
    
    
    stream.close()


if __name__ == "__main__":
    main()