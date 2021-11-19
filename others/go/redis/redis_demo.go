package main

import (
    "flag"
	"fmt"
	"time"

	"github.com/go-redis/redis"
)

func main() {

    var hostNport = flag.String("hostandport", "127.0.0.1:6379", "host:port redis的主机以及端口号")
    var password = flag.String("password", "", "redis的密码")
    var db = flag.Int("db", 0, "redis的db")
    
    flag.Parse()
    
    fmt.Println(*hostNport,*password,*db)
    
    
	redisCli := redis.NewClient(&redis.Options{
		Addr:     *hostNport,
		Password: *password,
		DB:       *db,
	})

	nowMs := time.Now().UnixNano() / 1e6 //毫秒时间戳
    key := "really_long_long_test_key_20211110"
    
	isAllow, realCount, curcount, err := SlideLimitZAdd(redisCli, key, 600000, 5, nowMs)
	fmt.Printf("SlideLimitZAdd(key=%s, period=%d, maxCount=%d),result:isAllow=%v, realCount=%d,curCount=%d, err=%v\n", "13246841100", 600000, 5, isAllow, realCount, curcount, err)

}

func SlideLimitZAdd(db *redis.Client, key string, period int64, limitCount int32, s int64) (bool, int64, int64, error) {
	nowMs := s
    
	pipe := db.Pipeline()
	pipe.ZAdd(key, redis.Z{Score: float64(nowMs), Member: nowMs})
	pipe.ZRemRangeByScore(key, "0", fmt.Sprintf("%d", nowMs-period))
	pipe.ZCard(key)

	expiredPeriod := time.Duration(period+1000) * time.Millisecond
	pipe.Expire(key, expiredPeriod)
	
	cmders, err := pipe.Exec()
	if err != nil {
		return false, 0, 0, fmt.Errorf("slidelimitzadd func err: %v", err)
	}
    
	if len(cmders) < 4 {
		return false, 0, 0, fmt.Errorf("pipe execult wrong: len(cmders)= %d", len(cmders))
	}

	// 使用管道获取的结果存在问题？有一定概率会小于实际值
	cmd := cmders[2].(*redis.IntCmd)
	curCount, err := cmd.Result()
	if err != nil {
		return false, 0, 0, fmt.Errorf("get action count err: %v", err)
	}

	realCount := db.ZCard(key).Val()

	return realCount < int64(limitCount), realCount, curCount, nil
}
