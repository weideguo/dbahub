Common Table Expressions
CTE 一个SQL语句中将临时查询结果命名成一个表以在后部分语句使用


WITH
  cte1 AS (SELECT a, b FROM table1),
  cte2 AS (SELECT c, d FROM table2)
SELECT b, d FROM cte1 JOIN cte2
WHERE cte1.a = cte2.c;



WITH RECURSIVE cte (n) AS
(
  SELECT 1                                 -- 从 1 开始
  UNION ALL
  SELECT n + 1 FROM cte WHERE n < 5        -- 到 5，递增为1，迭代次数受参数 @@cte_max_recursion_depth 控制
)
SELECT * FROM cte;


WITH RECURSIVE seq AS (
  SELECT 1 AS a, 1 AS b
  UNION ALL
  SELECT a + 1, b + 1 FROM seq WHERE a < 10
)
SELECT a,b FROM seq;



