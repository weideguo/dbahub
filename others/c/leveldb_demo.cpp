#include <iostream>
#include <cassert>
#include <leveldb/db.h>
#include <leveldb/write_batch.h>

using namespace std;
using namespace leveldb;

int main() {
    DB* db;
    Options options;
    options.create_if_missing = true;                               //如果不存在则创建
    // options.error_if_exists = true;                              //如果存在则报错
    // options.block_cache = NewLRUCache(100 * 1048576);            //使用缓存
    // options.filter_policy = NewBloomFilterPolicy(10);            //使用布隆过滤器，在内存中保存每个 key 的部分位，减少磁盘读次数
    
    Status status = DB::Open(options, "/tmp/testdb", &db);
    assert(status.ok());
    if (!status.ok()) cerr << status.ToString() << endl;
    // 
    string value1;
    string value="my value";
    string key1 ="key1";
    string key2 ="key2";
    string key3 ="key3";
    
    // 读写
    Status s      = db->Put(WriteOptions(), key1, value);
    if (s.ok()) s = db->Get(ReadOptions(),  key1, &value1);
    // if (s.ok()) s = db->Delete(WriteOptions(), key1);
    
    cout << "get value : " << value1 <<endl;
    
    //update由Delete Put组合实现
    
    // 原子更新
    if (s.ok()) {
        WriteBatch batch;
        // batch.Delete(key2);
        batch.Put(key2, value);
        batch.Put(key3, value);
        s = db->Write(WriteOptions(), &batch);
    }
    
    cout << "batch operation success "<<endl;
    
    //WriteOptions write_options;
    //write_options.sync = true;
    //默认情况下，leveldb 每个写操作都是异步的，进程把要写的内容丢给操作系统后立即返回，从操作系统内存到底层持久化存储的传输是异步进行的。
    //同步写等到数据真正被记录到持久化存储后再返回（在 Posix 系统上，这是通过在写操作返回前调用 fsync(...) 或 fdatasync(...) 或 msync(..., MS_SYNC) 来实现的）
    //
    //ReadOptions options;
    //options.fill_cache = false;
    //当执行一个大块数据读操作时，可能需要取消缓存功能
    //
    
    // 迭代获取所有kv数据
    Iterator* it = db->NewIterator(ReadOptions());
    for (it->SeekToFirst(); it->Valid(); it->Next()) {
        cout << it->key().ToString() << ": "  << it->value().ToString() << endl;
    }
    assert(it->status().ok());  
    delete it;
    
    cout << "iterate db success "<<endl;

    
    // 使用快照
    ReadOptions optionsx;
    optionsx.snapshot = db->GetSnapshot();
    // Status s      = db->Put(WriteOptions(), "key4", "key4");        //对快照的修改会影响原数据？
    
    Iterator* iter = db->NewIterator(optionsx);
    for (iter->SeekToFirst(); iter->Valid(); iter->Next()) {
        cout << iter->key().ToString() << ": "  << iter->value().ToString() << endl;
    }
    assert(iter->status().ok());  
    
    delete iter;
    db->ReleaseSnapshot(optionsx.snapshot);
    
    cout << "use snapshot to iterate db success "<<endl;
    
    
    delete db;
}


/*
yum install leveldb leveldb-devel

g++ -lleveldb leveldb_demo.cpp -o leveldb_demo
*/