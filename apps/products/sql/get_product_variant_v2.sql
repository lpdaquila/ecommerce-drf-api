WITH variants AS (
    SELECT 
        v.id,
        v.product_id,
        v.sku,
        pr_sale.price AS sale_price,
        pr_promo.price AS promo_price,
        json_object_agg(svt.name, sv.name) AS sub_var

    FROM products_variation v 
    INNER JOIN stock_inventory s on s.product_var_id = v.id

    -- Get Price
    LEFT JOIN products_price pr_sale ON -- price_type 1 = Sale
    pr_sale.product_var_id = v.id AND pr_sale.price_type_id = 1 
    LEFT JOIN products_price pr_promo ON -- price_type 2 = Promo
    pr_promo.product_var_id = v.id AND pr_promo.price_type_id = 2 

    -- Get Variations
    LEFT JOIN products_variation_options pvo ON pvo.variation_id = v.id
    LEFT JOIN products_subvariation sv ON sv.id = pvo.subvariation_id
    LEFT JOIN products_subvariationtype svt ON svt.id = sv.type_id

    WHERE s.quantity > 0

    GROUP BY 
        v.id,
        v.product_id,
        v.sku,
        sale_price,
        promo_price

    ORDER BY pr_sale.price ASC
)

SELECT
    p.id,
    p.slug,
    p.name,
    p.short_description,
    p.long_description,
    (
    SELECT json_agg(json_build_object(
        'variant_id', v.id,
        'sku', v.sku,
        'sale_price', v.sale_price,
        'promo_price', v.promo_price,
        'sub_vars', v.sub_var
    ))
    FROM variants v 
    WHERE v.product_id = p.id
    ) AS variants

FROM products_product p 

WHERE p.slug = %s

GROUP BY 
    p.id,
    p.slug,
    p.name,
    p.short_description,
    p.long_description
