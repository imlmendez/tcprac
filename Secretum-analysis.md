**Iteratiu**
* Tenemos un bucle dentro de un bucle, el primero mira si el numero es mayor que 9, el segundo suma todos los digitos
```    
        while aux:
            sumatori += aux % 10
            aux //= 10

``` 
* El Coste de este bucle interno es, en resumen, el numero de digitos de aux ( Mas constantes)
* Como podemos asumir el coste de este bucle casi como una constante en si mismo, lo interesante viene en el bucle externo:


```    
    while num > 9:
        aux = num
        sumatori = 0
        Coste Bucle Interno
        num = sumatori

```

* Como Tenemos solo asignaciones, podemos obviarlas por ahora, por lo que nos quedaria:

```    
    Coste (while num > 9:)
        Coste Bucle Interno
```

* Dependemos entonces, del numero de cifras, y su valor, el mejor caso Posible se ve entonces muy rapido:

$ \theta $ =  1 * Coste Bucle Interno

* En el peor caso posible, es para n con varios digitos y todos ellos 9's
n= 9999999.....
99-18-9
999-27-9
9999-36-9
999999999-81-9
9999999999-90-9
(log_Base10(N) + 2 ) * Coste Bucle Interno

Complejidad = log_base10(n)


**Recursivo**
```
def suma_recursiva(value):
    """Suma recursiva de digits """

    aux = int(value)
    if aux <= 9:
        return aux
    ultimo_digito = aux % 10
    resto = aux // 10
    return ultimo_digito + suma_recursiva(resto)


def decrypt_recursive(value):
    """Decrypt recursio """

    aux = suma_recursiva(value)
    if aux <= 9:
        return aux
    return decrypt_recursive(aux)
```

Mejor Caso - Coste C' (constante, entrando en el if)

Peor Caso - Igual que en recursivo??? Varios 99999..
log Base10(N)?
