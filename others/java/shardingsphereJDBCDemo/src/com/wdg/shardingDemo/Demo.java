package com.wdg.shardingDemo;

import io.shardingsphere.core.api.ShardingDataSourceFactory;

import io.shardingsphere.core.api.config.ShardingRuleConfiguration;

import io.shardingsphere.core.api.config.TableRuleConfiguration;

import io.shardingsphere.core.api.config.strategy.InlineShardingStrategyConfiguration;

import io.shardingsphere.example.jdbc.fixture.DataRepository;

import org.apache.commons.dbcp.BasicDataSource;

import javax.sql.DataSource;

import java.sql.SQLException;

import java.util.HashMap;

import java.util.Map;

import java.util.Properties;

import java.util.concurrent.ConcurrentHashMap;

public class Demo {
    public static void main(String[] args) throws SQLException {
        Map<String, DataSource> dataSourceMap = new HashMap<>();
        
        BasicDataSource dataSource1 = new BasicDataSource();
        dataSource1.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource1.setUrl("jdbc:mysql://localhost:3306/database0");
        dataSource1.setUsername("root");
        dataSource1.setPassword("mysql123!");
        dataSourceMap.put("database0", dataSource1);
        
        BasicDataSource dataSource2 = new BasicDataSource();
        dataSource2.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource2.setUrl("jdbc:mysql://localhost:3306/database1");
        dataSource2.setUsername("root");
        dataSource2.setPassword("mysql123!");
        dataSourceMap.put("database1", dataSource2);
        
        TableRuleConfiguration tableRuleConfiguration = new TableRuleConfiguration("t_order");
        
        tableRuleConfiguration.setDatabaseShardingStrategyConfig(new InlineShardingStrategyConfiguration("user_id","database${user_id % 2}"));
        tableRuleConfiguration.setTableShardingStrategyConfig(new InlineShardingStrategyConfiguration("order_id","t_order_${order_id % 2}"));
        
        ShardingRuleConfiguration shardingRuleConfiguration = new ShardingRuleConfiguration();
        shardingRuleConfiguration.getTableRuleConfigs().add(tableRuleConfiguration);
        
        DataSource dataSource = ShardingDataSourceFactory.createDataSource(dataSourceMap, shardingRuleConfiguration,
                new Properties());
        String sql = "insert into t_order (user_id, order_id) values (?, ?)";
        Connection connection = dataSource.getConnection();
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        
        int i=1
        while(i<100){
            preparedStatement.setInt(i, i);
            i=i+1;
        }
        
        // preparedStatement.setInt(2, 2);
        preparedStatement.execute();
}

/*
create table t_order(user_id int,order_id int);
*/
