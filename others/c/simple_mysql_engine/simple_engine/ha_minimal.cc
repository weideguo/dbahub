#include <my_global.h>
#include <mysql_version.h>
#include <mysql/plugin.h>
#include <handler.h>

//unsigned int _mysql_plugin_interface_version_ = MYSQL_PLUGIN_INTERFACE_VERSION;

class ha_minimal : public handler {
public:
    ha_minimal(handlerton *hton, TABLE_SHARE *table) 
        : handler(hton, table) {}

    // 函数定义参考 handler.h
    const char *table_type() const override { return "MINIMAL"; }
    
    ulonglong table_flags() const override {
        return HA_NO_TRANSACTIONS | HA_NO_AUTO_INCREMENT;
    }
    
    const char **bas_ext() const override { 
        static const char *exts[] = {nullptr};
        return exts;
    }
    
    
    //
    int create(const char *name, TABLE *form, HA_CREATE_INFO *info) override {
        return 0; 
    }

    int open(const char *name, int mode, uint test_if_locked) override {
        return 0; 
    }

    int close(void) override {
        return 0; 
    }

    int write_row(uchar *buf) override {
        return 0; 
    }

    int rnd_init(bool scan) override {
        return 0; 
    }

    int rnd_next(uchar *buf) override {
        return HA_ERR_END_OF_FILE; 
    }

    int info(uint flag) override {
        return 0;
    }
    
    int rnd_pos(uchar * buf, uchar *pos) override {
        return 0;
    }
    
    void position(const uchar *record) override {
        
    }
    
    THR_LOCK_DATA **store_lock(THD *thd,THR_LOCK_DATA **to,enum thr_lock_type lock_type) {
        return to;
    }
    
    ulong index_flags(uint idx, uint part, bool all_parts) const {
        return 0;
    }
    
    // ha_rows records_in_range(uint inx, key_range *min_key, key_range *max_key) override { 
    //     return HA_POS_ERROR; 
    // }
    
    //int extra(enum ha_extra_function operation) override { return 0; }
    
    //int delete_all_rows() override { return 0; }
    //int truncate() override { return 0; }

    // 8.0+ 
    // int prepare_inplace_alter_table(TABLE*, Alter_inplace_info*) override { return 0; }
    // int inplace_alter_table(TABLE*, Alter_inplace_info*) override { return 0; }
};

static handler *minimal_create_handler(handlerton *hton, TABLE_SHARE *table, MEM_ROOT *mem_root) {
        return new (mem_root) ha_minimal(hton, table);
};


// 引擎初始化函数
static int minimal_init(void *p) {
    fprintf(stderr, "MINIMAL engine initialized!\n");
    handlerton *minimal_hton = (handlerton *)p;
    minimal_hton->create = minimal_create_handler;
    minimal_hton->flags = HTON_CAN_RECREATE;
    return 0;
}

struct st_mysql_storage_engine minimal_engine=
{ MYSQL_HANDLERTON_INTERFACE_VERSION };



extern "C" {
    struct st_mysql_storage_engine MINIMAL = minimal_engine;
}


// 插件声明 使用宏
mysql_declare_plugin(minimal)
{
  MYSQL_STORAGE_ENGINE_PLUGIN,                    /* 插件类型 */
  &minimal_engine,                        /* handlerton 指针 */
  "minimal",                                      /* 插件名称 */
  "weideguo",                                     /* 作者 */
  "A minimal do-nothing storage enginee",         /* 描述 */
  PLUGIN_LICENSE_GPL,                             /* 许可证 */
  minimal_init,                                   /* 初始化函数 */
  NULL,                                           /* 卸载函数 */
  0x0100,                                         /* 版本号 */
  NULL,                                           /* 状态变量 */
  NULL,                                           /* 系统变量 */
  NULL                                          /* 配置选项 */
  //0                                               /* 标志 */
} mysql_declare_plugin_end;

