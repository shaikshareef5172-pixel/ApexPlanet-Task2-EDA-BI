SELECT
    Product,
    SUM(Quantity) AS Total_Quantity,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;

SELECT
    Category,
    SUM(Quantity) AS Units_Sold,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;

SELECT
    City,
    COUNT(*) AS Orders,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC;

SELECT
    Customer_ID,
    Customer_Name,
    COUNT(*) AS Orders,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Customer_ID, Customer_Name
ORDER BY Revenue DESC
LIMIT 10;

SELECT
    Gender,
    COUNT(*) AS Orders,
    SUM(Quantity) AS Units_Sold,
    SUM(Total_Sales) AS Revenue,
    AVG(Total_Sales) AS Average_Order_Value
FROM sales
GROUP BY Gender
ORDER BY Revenue DESC;

SELECT
    Category,
    SUM(Quantity) AS Units_Sold,
    SUM(Total_Sales) AS Revenue,
    AVG(Total_Sales) AS Average_Order_Value
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;
