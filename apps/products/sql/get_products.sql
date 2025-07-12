SELECT 
p.id, 
p.slug, 
p.name, 
pr_sale.price AS sale_price,
pr_promo.price AS promo_price

FROM products_product p 
JOIN products_productvariant v ON v.product_id = p.id

LEFT JOIN products_price pr_sale ON 
pr_sale.product_var_id = v.id AND pr_sale.price_type_id = 1 -- price_type = Sale
LEFT JOIN products_price pr_promo ON 
pr_promo.product_var_id = v.id AND pr_promo.price_type_id = 2 -- price_type = Promo