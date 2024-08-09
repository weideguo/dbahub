
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_lock(&mutex);
// 临界区代码
// 互斥锁 Mutex 
// 当一个线程试图锁定一个已经被其他线程持有的互斥锁时，该线程会被操作系统挂起（进入睡眠状态），并从运行队列移除，直到锁被释放，操作系统才会唤醒该线程，将其放回运行队列。
// 涉及涉及线程调度和上下文切换，系统开销较大。
// 
pthread_mutex_unlock(&mutex);



pthread_spinlock_t spinlock = PTHREAD_SPIN_LOCK_INITIALIZER;
// pthread_spin_init(&spinlock, PTHREAD_PROCESS_PRIVATE);  // 动态初始化

pthread_spin_lock(&spinlock);
// 临界区代码
// 自旋锁 
// Spinlock 当一个线程尝试获取一个已被其他线程占用的自旋锁时，该线程不会立即放弃CPU，而是原地循环（自旋），不断检查锁的状态，直到锁变为可用。
// 在此期间，线程保持运行状态，消耗CPU资源。
// 自旋锁不会进入睡眠状态，因此获取锁的开销较小。如果长时间自旋等待，会占用CPU资源。
// 常用于内核代码
pthread_spin_unlock(&spinlock);
