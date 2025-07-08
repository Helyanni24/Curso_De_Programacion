<?php
$temperatura = 15;

if ($temperatura < 10) {
    echo "La temperatura es fría (menos de 10°C).\n";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "La temperatura es templada (entre 10°C y 25°C).\n";
} else {
    echo "La temperatura es calurosa (más de 25°C).\n";
}
?>
