SELECT 
p.id, 
p.slug, 
p.name, 
pr_sale.price AS sale_price,
pr_promo.price AS promo_price

FROM products_product p
JOIN (
    -- Select the lowest price to show first
    SELECT v_inner.product_id, v_inner.id AS variant_id
    FROM products_productvariant v_inner 

    JOIN products_price pr ON pr.product_var_id = v_inner.id
    JOIN stock_inventory s ON s.product_var_id = v_inner.id

    WHERE pr.price_type_id = 1 AND s.quantity > 0

    GROUP BY v_inner.product_id
    HAVING MIN(pr.price)
) AS sub ON sub.product_id = p.id

LEFT JOIN products_price pr_sale ON 
pr_sale.product_var_id = sub.variant_id AND pr_sale.price_type_id = 1 -- price_type = Sale
LEFT JOIN products_price pr_promo ON 
pr_promo.product_var_id = sub.variant_id AND pr_promo.price_type_id = 2 -- price_type = Promo

GROUP BY p.id