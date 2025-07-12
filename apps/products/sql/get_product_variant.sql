SELECT
v.id AS variant_id,
v.sku,
GROUP_CONCAT(vo.name, ', ') AS options,
pr_sale.price AS sale_price,
pr_promo.price AS promo_price

FROM products_productvariant v 
JOIN stock_inventory s on s.product_var_id = v.id

-- Get Price
LEFT JOIN products_price pr_sale ON 
pr_sale.product_var_id = v.id AND pr_sale.price_type_id = 1 -- price_type = Sale
LEFT JOIN products_price pr_promo ON 
pr_promo.product_var_id = v.id AND pr_promo.price_type_id = 2 -- price_type = Promo

-- Get Variations
LEFT JOIN products_productvariant_options ppvo ON ppvo.productvariant_id = v.id
LEFT JOIN products_variationoption vo ON vo.id = ppvo.variationoption_id

WHERE v.product_id = %s AND s.quantity > 0

GROUP BY v.id, pr_sale.price, pr_promo.price
ORDER BY pr_sale.price ASC