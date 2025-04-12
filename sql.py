#Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
#Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
SELECT c.login, COUNT(o.track)
    FROM "Couriers" AS c
    INNER JOIN "Orders" AS o ON c.id = o."courierId"
    WHERE o."inDelivery" = true
    GROUP BY c.login;

#Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
#Для этого: выведи все трекеры заказов и их статусы.
SELECT track,
	CASE
	 WHEN finished = true THEN 2
	 WHEN canсelled = true THEN -1
	 WHEN "inDelivery" = true THEN 1
	 ELSE 0
    END AS status
FROM "Orders";