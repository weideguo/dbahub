package main

import (
    "errors"
    "github.com/tecbot/gorocksdb"
    "log"
    "strconv"
)

const (
    DB_PATH = "./gorocksdb"
)

func main() {
    db, err := OpenDB()
    if err != nil {
        log.Println("fail to open db,", nil, db)
    }
    
    readOptions := gorocksdb.NewDefaultReadOptions()
    readOptions.SetFillCache(true)
    
    writeOptions := gorocksdb.NewDefaultWriteOptions()
    writeOptions.SetSync(true)
    
    for i := 0; i < 10; i++ {
        keyStr := "key" + strconv.Itoa(i)
        valueStr := "value" + strconv.Itoa(i)
        db.Put(writeOptions, []byte(keyStr), []byte(valueStr))
        log.Println("put: ", i, keyStr)
    }
    log.Println("----------put done --------------------")
    
    for i := 0; i < 10; i++ {
        keyStr := "key" + strconv.Itoa(i)
        slice, err := db.Get(readOptions, []byte(keyStr))
        if err != nil {
            log.Println("exception: ", keyStr, err)
            continue
        }
        log.Println("get: ", slice.Size(), keyStr, string(slice.Data()))
    }
    log.Println("----------get done --------------------")
    
    //func (db *DB) Delete(opts *WriteOptions, key []byte) error {
}


func OpenDB() (*gorocksdb.DB, error) {
    options := gorocksdb.NewDefaultOptions()
    options.SetCreateIfMissing(true)
    
    bloomFilter := gorocksdb.NewBloomFilter(10)
    
    readOptions := gorocksdb.NewDefaultReadOptions()
    readOptions.SetFillCache(false)
    
    rateLimiter := gorocksdb.NewRateLimiter(10000000, 10000, 10)
    options.SetRateLimiter(rateLimiter)
    options.SetCreateIfMissing(true)
    options.EnableStatistics()
    options.SetWriteBufferSize(8 * 1024)
    options.SetMaxWriteBufferNumber(3)
    options.SetMaxBackgroundCompactions(10)
    // options.SetCompression(gorocksdb.SnappyCompression)
    // options.SetCompactionStyle(gorocksdb.UniversalCompactionStyle)
    
    options.SetHashSkipListRep(2000000, 4, 4)
    
    blockBasedTableOptions := gorocksdb.NewDefaultBlockBasedTableOptions()
    blockBasedTableOptions.SetBlockCache(gorocksdb.NewLRUCache(64 * 1024))
    blockBasedTableOptions.SetFilterPolicy(bloomFilter)
    blockBasedTableOptions.SetBlockSizeDeviation(5)
    blockBasedTableOptions.SetBlockRestartInterval(10)
    blockBasedTableOptions.SetBlockCacheCompressed(gorocksdb.NewLRUCache(64 * 1024))
    blockBasedTableOptions.SetCacheIndexAndFilterBlocks(true)
    blockBasedTableOptions.SetIndexType(gorocksdb.KHashSearchIndexType)
    
    options.SetBlockBasedTableFactory(blockBasedTableOptions)
    //log.Println(bloomFilter, readOptions)
    options.SetPrefixExtractor(gorocksdb.NewFixedPrefixTransform(3))
    
    options.SetAllowConcurrentMemtableWrites(false)
    
    db, err := gorocksdb.OpenDb(options, DB_PATH)
    
    if err != nil {
        log.Fatalln("OPEN DB error", db, err)
        db.Close()
        return nil, errors.New("fail to open db")
    } else {
        log.Println("OPEN DB success", db)
    }
    return db, nil
}
/*
## 安装依赖库
yum install snappy snappy-devel   -y
yum install zlib zlib-devel       -y
yum install bzip2 bzip2-devel     -y
yum install lz4-devel             -y
yum install libasan               -y

wget https://github.com/facebook/zstd/archive/v1.1.3.tar.gz
mv v1.1.3.tar.gz zstd-1.1.3.tar.gz
tar zxvf zstd-1.1.3.tar.gz
cd zstd-1.1.3
make && make install


## 安装rocksdb
git clone https://github.com/facebook/rocksdb.git
cd rocksdb
git checkout 5.18.fb


# 动态库使用 shared_lib ，静态库使用 static_lib
PORTABLE=1 make shared_lib
INSTALL_PATH=/usr/local make install-shared

CGO_CFLAGS="-I/usr/local/include/rocksdb" 
CGO_LDFLAGS="-L/usr/local/lib -lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy -llz4 -lzstd"

*/

/*
rocksdb数据结构
memtable -> inmutable memtable -> SST

*/
