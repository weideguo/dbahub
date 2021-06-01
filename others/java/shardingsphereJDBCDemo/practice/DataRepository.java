package practice;

//import org.apache.shardingsphere.driver.api.HintManager;
import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DataRepository {

    //private final DataSourcedataSource;    
    public DataRepository(final DataSource dataSource) {    
        this.dataSource = dataSource;  
    }

    public void demo()throws SQLException {
    
        createTable();
        
        insertData();
        
        System.out.println("1.Query with EQUAL--------------");
        
        queryWithEqual();
        
        System.out.println("2.Query with IN--------------");
        
        queryWithIn();
        
        System.out.println("3.Query with Hint--------------");
        
        //queryWithHint();
        
        System.out.println("4.Drop tables--------------");
        
        dropTable();
        
        System.out.println("5.All done-----------");
    
    }

    private void createTable()throws SQLException {
    
        execute("CREATE TABLE IF NOT EXISTS t_order (order_id BIGINT NOT NULL AUTO_INCREMENT, user_id INT NOT NULL, status VARCHAR(50), PRIMARY KEY (order_id))");    
        execute("CREATE TABLE IF NOT EXISTS t_order_item (order_item_id BIGINT NOT NULL AUTO_INCREMENT, order_id BIGINT NOT NULL, user_id INT NOT NULL, PRIMARY KEY (order_item_id))");
    
    }

    private void insertData()throws SQLException {
    
        for (int i =1; i <10; i++) {        
            long orderId = insertAndGetGeneratedKey("INSERT INTO t_order (user_id, status) VALUES (10, 'INIT')");        
            execute(String.format("INSERT INTO t_order_item (order_id, user_id) VALUES (%d, 10)", orderId));        
            orderId = insertAndGetGeneratedKey("INSERT INTO t_order (user_id, status) VALUES (11, 'INIT')");        
            execute(String.format("INSERT INTO t_order_item (order_id, user_id) VALUES (%d, 11)", orderId));  
        }
    
    }

    private long insertAndGetGeneratedKey(final String sql)throws SQLException {
    
        long result = -1;
        
        try (
        
            Connection connection =dataSource.getConnection();
            
            Statement statement = connection.createStatement()) {
        
                statement.executeUpdate(sql, Statement.RETURN_GENERATED_KEYS);
                
                // 获取自动递增主键
                try (ResultSet resultSet = statement.getGeneratedKeys()) {
                
                    if (resultSet.next()) {
                        result = resultSet.getLong(1);
                    }
                
                }
            
            }

        return result;

    }

    private void queryWithEqual()throws SQLException {
    
        String sql ="SELECT i.* FROM t_order o JOIN t_order_item i ON o.order_id=i.order_id WHERE o.user_id=?";
        
        try (
        
            Connection connection =dataSource.getConnection();
            
            PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
        
                preparedStatement.setInt(1,10);
                
                printQuery(preparedStatement);
                
            }
    
    }

    private void queryWithIn()throws SQLException {

        String sql ="SELECT i.* FROM t_order o JOIN t_order_item i ON o.order_id=i.order_id WHERE o.user_id IN (?, ?)";
        
        try (
        
            Connection connection =dataSource.getConnection();
            
            PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
        
                preparedStatement.setInt(1,10);
                
                preparedStatement.setInt(2,11);
                
                printQuery(preparedStatement);
                
            }
    
    }

    // private void queryWithHint()throws SQLException {
    // 
    //     String sql ="SELECT i.* FROM t_order o JOIN t_order_item i ON o.order_id=i.order_id";
    //     
    //     try (
    //     
    //         HintManager hintManager = HintManager.getInstance();
    //         
    //         Connection connection =dataSource.getConnection();
    //         
    //         PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
    //     
    //             hintManager.addDatabaseShardingValue("t_order","user_id",11);
    //         
    //             printQuery(preparedStatement);
    //         
    //         }
    // 
    // }

    private void printQuery(final PreparedStatement preparedStatement)throws SQLException {
    
        try (ResultSet resultSet = preparedStatement.executeQuery()) {
        
            while (resultSet.next()) {
            
                System.out.print("order_item_id:" + resultSet.getLong(1) +", ");
                
                System.out.print("order_id:" + resultSet.getLong(2) +", ");
                
                System.out.print("user_id:" + resultSet.getInt(3));
                
                System.out.println();
            
            }
        
        }
    
    }

    private void dropTable()throws SQLException {
    
        execute("DROP TABLE t_order_item");
        
        execute("DROP TABLE t_order");
    
    }

    private void execute(final String sql)throws SQLException {
    
        try (
        
            Connection connection =dataSource.getConnection();
            
            Statement statement = connection.createStatement()) {
            
                statement.execute(sql);
        
            }
    
    }

}


