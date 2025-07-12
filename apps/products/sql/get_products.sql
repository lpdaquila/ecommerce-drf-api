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
    FROM products_variation v_inner 

    JOIN products_price pr ON pr.product_var_id = v_inner.id
    JOIN stock_inventory s ON s.product_var_id = v_inner.id

    WHERE pr.price_type_id = 1 AND s.quantity > 0

    GROUP BY v_inner.product_id
    HAVING MIN(pr.price)
) AS subq ON subq.product_id = p.id

LEFT JOIN products_price pr_sale ON -- price_type 1 = Sale
pr_sale.product_var_id = subq.variant_id AND pr_sale.price_type_id = 1 
LEFT JOIN products_price pr_promo ON -- price_type 2 = Promo
pr_promo.product_var_id = subq.variant_id AND pr_promo.price_type_id = 2 

GROUP BY p.id