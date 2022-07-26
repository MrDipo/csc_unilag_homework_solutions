SELECT Buyer, Department FROM sku_data;
SELECT distinct Buyer, Department FROM sku_data; #select only unique values(by first attribute)
SELECT * FROM sku_data; #select all
SELECT * FROM SKU_DATA WHERE Department = 'Water Sports';
SELECT SKU_Description, Buyer FROM SKU_DATA WHERE Department = 'Climbing';
SELECT * FROM ORDER_ITEM ORDER BY OrderNumber, Price;
SELECT * FROM ORDER_ITEM ORDER BY Price DESC, OrderNumber ASC; #descending and ascending
SELECT * FROM SKU_DATA WHERE Department = 'Water Sports' AND Buyer = 'Nancy Meyers';
SELECT * FROM SKU_DATA WHERE Department = 'Camping' OR Department = 'Climbing';
SELECT * FROM SKU_DATA WHERE Buyer IN ('Nancy Meyers', 'Cindy Lo', 'Jerry Martin'); #must include specified
SELECT * FROM SKU_DATA WHERE Buyer NOT IN ('Nancy Meyers', 'Cindy Lo', 'Jerry Martin'); #must not include specified
SELECT * FROM ORDER_ITEM WHERE ExtendedPrice BETWEEN 100 AND 200;
SELECT * FROM ORDER_ITEM WHERE ExtendedPrice >= 100 AND ExtendedPrice <= 200;
SELECT * FROM SKU_DATA WHERE Buyer LIKE 'Pete%'; #percent is a wildcard symbol. to represent one or more characters
SELECT * FROM SKU_DATA WHERE sku_description LIKE '%Tent%';
SELECT * FROM SKU_DATA WHERE SKU LIKE '%2__'; #underscore(_) represents exactly one character
#continue from page 50