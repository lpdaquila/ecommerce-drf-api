SELECT
v.id AS variant_id,
v.sku,
GROUP_CONCAT(sv.name, ', ') AS options,
pr_sale.price AS sale_price,
pr_promo.price AS promo_price

FROM products_variation v 
JOIN stock_inventory s on s.product_var_id = v.id

-- Get Price
LEFT JOIN products_price pr_sale ON 
pr_sale.product_var_id = v.id AND pr_sale.price_type_id = 1 -- price_type 1 = Sale
LEFT JOIN products_price pr_promo ON 
pr_promo.product_var_id = v.id AND pr_promo.price_type_id = 2 -- price_type 2 = Promo

-- Get Variations
LEFT JOIN products_variation_options pvo ON pvo.variation_id = v.id
LEFT JOIN products_subvariation sv ON sv.id = pvo.subvariation_id

WHERE v.product_id = %s AND s.quantity > 0

GROUP BY v.id, pr_sale.price, pr_promo.price
ORDER BY pr_sale.price ASC