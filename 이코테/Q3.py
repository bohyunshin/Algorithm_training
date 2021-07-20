-- write your code in PostgreSQL 9.4
WITH tb_export as (
    SELECT
        tr.country, sum(tr.value) export
    FROM
        (
            SELECT tr.*, cp.country
            FROM trades tr
            JOIN companies cp
            ON tr.seller = cp.name
        ) tr
    GROUP BY
        tr.country
),

tb_import as (
    SELECT
        tr.country, sum(tr.value) import
    FROM
        (
            SELECT tr.*, cp.country
            FROM trades tr
            JOIN companies cp
            ON tr.buyer = cp.name
        ) tr
    GROUP BY
        tr.country
),

result as (
    SELECT
        distinct(cp.country) country,
        ex.export export,
        im.import import
    FROM companies cp
    LEFT JOIN tb_export ex
    ON cp.country = ex.country
    LEFT JOIN tb_import im
    ON cp.country = im.country
    ORDER BY country
)

SELECT
    country,
    CASE WHEN
        export is null then 0
    ELSE export END export,
    CASE WHEN
        import is null then 0
    ELSE import END import
FROM result
