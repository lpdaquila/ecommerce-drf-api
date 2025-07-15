WITH var_min_price AS (
    SELECT
        v.product_id,
        v.id as variant_id,
        pr.price

    FROM products_variation v 

    INNER JOIN products_price pr ON pr.product_var_id = v.id AND price_type_id = 1
    INNER JOIN stock_inventory s ON s.product_var_id = v.id 

    WHERE s.quantity > 0

    GROUP BY v.product_id 

    HAVING MIN(pr.price)
),
sub_vars_cte AS (
    -- CTE for query sub variations types and names
    SELECT
    v.product_id,
    json_object_agg(svt.name, json_agg(sv.name)) AS sub_vars

    FROM products_variation v

    -- Get Variations
    LEFT JOIN products_variation_options pvo ON pvo.variation_id = v.id
    LEFT JOIN products_subvariation sv ON sv.id = pvo.subvariation_id
    LEFT JOIN products_subvariationtype svt ON svt.id = sv.type_id

    GROUP BY v.product_id
)

SELECT 
p.id, 
p.slug, 
p.name, 
pr_sale.price AS sale_price,
pr_promo.price AS promo_price,
svc.sub_vars 

FROM products_product p

INNER JOIN var_min_price vmp ON vmp.product_id = p.id 

LEFT JOIN products_price pr_sale ON -- price_type 1 = Sale
pr_sale.product_var_id = vmp.variant_id AND pr_sale.price_type_id = 1 
LEFT JOIN products_price pr_promo ON -- price_type 2 = Promo
pr_promo.product_var_id = vmp.variant_id AND pr_promo.price_type_id = 2 

LEFT JOIN sub_vars_cte svc ON svc.product_id = p.id
