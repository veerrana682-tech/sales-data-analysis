SELECT SUM(Sales) AS Total_Sales FROM sales_data;

SELECT Region, SUM(Sales)
FROM sales_data
GROUP BY Region;

SELECT Product, SUM(Sales)
FROM sales_data
GROUP BY Product
ORDER BY SUM(Sales) DESC
LIMIT 1;
