package practice;

import org.apache.shardingsphere.driver.api.ShardingSphereDataSourceFactory;
//import org.apache.shardingsphere.api.config.sharding.ShardingRuleConfiguration;
//import org.apache.shardingsphere.api.config.sharding.ShardingTableRuleConfiguration;
//import org.apache.shardingsphere.api.config.sharding.strategy.InlineShardingStrategyConfiguration;

import org.apache.shardingsphere.sharding.api.config.ShardingRuleConfiguration;
import org.apache.shardingsphere.sharding.api.config.rule.ShardingShardingTableRuleConfiguration;
//import org.apache.shardingsphere.sharding.api.config.strategy.InlineShardingStrategyConfiguration;

import org.apache.commons.dbcp2.BasicDataSource;
import javax.sql.DataSource;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.util.concurrent.ConcurrentHashMap;

public class ShardingDataSource {

    public static void main(String[] args)throws SQLException {
        
        ShardingDataSource shardingDataSource =new ShardingDataSource();
        
        DataSource dataSource = shardingDataSource.sharding();
        
        new DataRepository(dataSource).demo();
    
    }

    public DataSource sharding()throws SQLException {
    
        // 配置真实数据源
        
        Map dataSourceMap =new HashMap<>();
        
        // 配置第一个数据源       
        BasicDataSource dataSource1 =new BasicDataSource();       
        dataSource1.setDriverClassName("com.mysql.jdbc.Driver");        
        dataSource1.setUrl("jdbc:mysql://127.0.0.1:1039/ds0");        
        dataSource1.setUsername("test");       
        dataSource1.setPassword("test");
        dataSourceMap.put("ds0", dataSource1);
        
        // 配置第二个数据源        
        BasicDataSource dataSource2 =new BasicDataSource();    
        dataSource2.setDriverClassName("com.mysql.jdbc.Driver");        
        dataSource2.setUrl("jdbc:mysql://127.0.0.1:1039/ds1");        
        dataSource2.setUsername("test");        
        dataSource2.setPassword("test");        
        dataSourceMap.put("ds1", dataSource2);
        
        // t_order表规则   
        ShardingTableRuleConfiguration orderTableRuleConfig =new ShardingTableRuleConfiguration();  
        orderTableRuleConfig.setLogicTable("t_order");                          // 逻辑表
        orderTableRuleConfig.setActualDataNodes("ds${0..1}.t_order${0..1}");    // 对应的实际表
        // 分库 + 分表策略  
        //orderTableRuleConfig.setDatabaseShardingStrategyConfig(new InlineShardingStrategyConfiguration("user_id","ds${user_id % 2}"));                      // 分库策略
        //orderTableRuleConfig.setTableShardingStrategyConfig(new InlineShardingStrategyConfiguration("order_id","t_order${order_id % 2}"));                  // 分表策略
        //orderTableRuleConfig.setTableShardingStrategyConfig(new InlineShardingStrategyConfiguration("order_item_id","t_order_item${order_item_id % 2}"));   // 分表策略
    
        
        // order_item表规则  
        ShardingTableRuleConfiguration orderItemTableRuleConfig =new ShardingTableRuleConfiguration();    
        orderItemTableRuleConfig.setLogicTable("t_order_item");        
        orderItemTableRuleConfig.setActualDataNodes("ds${0..1}.t_order_item${0..1}");        
        
        
        //
        ShardingRuleConfiguration shardingRuleConfig =new ShardingRuleConfiguration();    
        shardingRuleConfig.getTableRuleConfigs().add(orderTableRuleConfig);
        shardingRuleConfig.getTableRuleConfigs().add(orderItemTableRuleConfig);
        
        // 获取数据源对象    
        return ShardingSphereDataSourceFactory.createDataSource(dataSourceMap, shardingRuleConfig,new ConcurrentHashMap(),new Properties());
        // return ShardingSphereDataSourceFactory.createDataSource(createDataSourceMap(), Collections.singleton(createShardingRuleConfiguration()), new Properties());
               
    }

}
