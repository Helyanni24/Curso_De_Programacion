<?php
echo "Tiendita\n";

$metodo = "efectivo";

switch ($metodo) {
    case "tarjeta de credito":
        echo "Pago con tarjeta de credito seleccionado. Prepara el monto exacto.\n";
        break;

    case "tarjeta de debito":
        echo "Pago con tarjeta de débito seleccionado. Inserta o desliza la tarjeta.\n";
        break;

    case "transferencia":
        echo "Pago por transferencia seleccionado. Muestra el comprobante.\n";
        break;
        
    case "efectivo":
        echo "Pago por efectivo seleccionado. Prepara el Monto exacto.\n";
        break;
        
    case "paypal":
        echo "Pago con PayPal seleccionado. Serás redirigido para completar la transacción.\n";
        break;

    case "pago movil":
            echo "Pago con pago movil seleccionado. Muestra el comprobante.\n";
            break;

    case "Zelle":
            echo "Pago con Zelle seleccionado. Serás redirigido para completar la transacción.\n";
            break;

    default:
        echo "Método de pago no válido o no seleccionado.\n";
        break;
}
?>