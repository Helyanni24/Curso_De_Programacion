<?php
$sum_impares = 0;

for ($i = 1; $i <= 100; $i++) {
    if ($i % 2 != 0) {
        $sum_impares += $i;
    }
}
echo "La suma de todos los números impares desde 1 hasta 100 es: $sum_impares\n";
?>
