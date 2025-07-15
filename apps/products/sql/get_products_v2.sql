WITH var_min_price AS (
    SELECT
        v.product_id,
        MAX(v.id) AS variant_id,
        MIN(pr.price) AS price

    FROM products_variation v 

    INNER JOIN products_price pr ON pr.product_var_id = v.id AND pr.price_type_id = 1
    INNER JOIN stock_inventory s ON s.product_var_id = v.id 

    WHERE s.quantity > 0

    GROUP BY v.product_id
),

sub_vars_cte AS (
    -- CTE for query sub variations types and names
    SELECT
    v.product_id,
    svt.name AS type_name,
    json_agg(DISTINCT sv.name) AS vals 

    FROM products_variation v

    -- Get Variations
    LEFT JOIN products_variation_options pvo ON pvo.variation_id = v.id
    LEFT JOIN products_subvariation sv ON sv.id = pvo.subvariation_id
    LEFT JOIN products_subvariationtype svt ON svt.id = sv.type_id

    GROUP BY v.product_id, type_name
)

SELECT 
    p.id, 
    p.slug, 
    p.name, 
    pr_sale.price AS sale_price,
    pr_promo.price AS promo_price,
    json_object_agg(svc.type_name, svc.vals)  AS sub_vars

FROM products_product p

INNER JOIN var_min_price vmp ON vmp.product_id = p.id 

LEFT JOIN products_price pr_sale ON -- price_type 1 = Sale
pr_sale.product_var_id = vmp.variant_id AND pr_sale.price_type_id = 1 
LEFT JOIN products_price pr_promo ON -- price_type 2 = Promo
pr_promo.product_var_id = vmp.variant_id AND pr_promo.price_type_id = 2 

LEFT JOIN sub_vars_cte svc ON svc.product_id = p.id

GROUP BY 
    p.id, 
    p.slug, 
    p.name, 
    pr_sale.price, 
    pr_promo.price

ORDER BY pr_sale.price ASC
