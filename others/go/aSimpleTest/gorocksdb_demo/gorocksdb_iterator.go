package main

import (
    "errors"
    "github.com/tecbot/gorocksdb"
    "log"
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
    //readOptions.SetFillCache(true)
    

    log.Println("---------- iterator begin --------------------")
    
    // 遍历所有key
    it := db.NewIterator(readOptions)
    defer it.Close()
    //it.Seek([]byte("key2"))  // 匹配以及之后的key
    it.Seek([]byte(""))
    for it = it; it.Valid(); it.Next() {
        key := it.Key()
        value := it.Value()
        log.Printf("Key: %v Value: %v\n", string(key.Data()), string(value.Data()))
        key.Free()
    }    
    log.Println("---------- iterator done --------------------")
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