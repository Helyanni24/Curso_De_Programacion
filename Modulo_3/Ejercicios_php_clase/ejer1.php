<?php

$pares = 0;
$impares = 0;

echo "Numeros pares:\n";
for ($numero = 1; $numero <= 50; $numero++) {
    if ($numero % 2 == 0) {
        echo "$numero ";
        $pares++;
    }}

echo "\n\nNumeros impares:\n";
for ($numero = 1; $numero <= 50; $numero++) {
    if ($numero % 2 != 0) {
        echo "$numero ";
        $impares++;
    }}

echo "\n\nNumeros pares: $pares\n";
echo "Numeros impares: $impares\n";
?>
