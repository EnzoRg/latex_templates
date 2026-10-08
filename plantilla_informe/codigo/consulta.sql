-- Ventas mensuales por categoría con ranking dentro de cada mes
WITH ventas_mes AS (
    SELECT DATE_FORMAT(v.fecha, '%Y-%m') AS mes,
           p.categoria,
           SUM(v.cantidad * v.precio_unitario) AS total
    FROM venta v
    JOIN producto p ON p.id_producto = v.id_producto
    GROUP BY mes, p.categoria
)
SELECT mes, categoria, total,
       RANK() OVER (PARTITION BY mes ORDER BY total DESC) AS posición
FROM ventas_mes
ORDER BY mes, posición;
