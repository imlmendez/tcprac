----
**Títul**: "Pràctica I: Ludus Strategy"

**Assignatura**: TC - Tècniques de Computació

**Keywords**: "python,markdown,algorismes iteratius, algorismes recursius, costos"

**Autors**: "Jordi Mateo Fornés <jordi.mateo@udl.cat>"

----

# Pràctica I: Ludus Strategy 

## Objectius

Els objectius de la pràctica són:

* Comprensió dels algorismes iteratius.
* Comprensió dels algorismes recursius.
* Coneixement dels fonaments de la programació i les bones pràctiques amb el llenguatge python.
* Analitzar els costos dels nostres algorismes.
* Comparar costos teòrics amb costos empírics.

## Presentació

**MOLT IMPORTANT**: L'enviament de codi que el grup no sigui capaç de defensar, suposarà suspendre tota la pràctica.

Tota la codificació es farà exclusivament amb **Python**.

Dues maneres de presentar la pràctica:

1. Opció 1:
   * Presentar un enllaç al repositori del projecte publicat al github.
   * Ubicar tota la documentació del projecte en un o més documents formatats amb Markdown.

2. Opció 2:
    * Presentar la pràctica comprimida amb zip amb el codi font del projecte i un document pdf amb tota la documentació.

Es valorarà amb fins a un **punt extra** les pràctiques entregades amb la primera opció.

No s'acceptaran codi desenvolupat en **Jupyter per aquesta entrega**.

## Descripció

En aquesta pràctica desenvoluparem rutines per obtenir la màxima puntuació en diferents torns d'una partida a un joc d'estratègia anomenat Ludus. Una partida a Ludus consisteix d'un conjunt de torns on els participants han d'utilitzar la seva intel·ligència per obtenir la màxima puntuació a cada torn.

# Torn 1: Quod secretum nuntius

Per superar el primer torn de la partida els participants han de desxifrar la informació d'un missatge codificat per obtenir els recursos necessaris per avançar en la partida. Per obtenir la informació del missatge s'han de seguir unes regles molt específiques. El **descodificador** únicament pot ser utilitzar una vegada per jugador. Com més ràpid sigui el jugador en obtenir la informació codificada més recursos obtindrà per les rondes següents. El descodificador necessita un nombre enter d'un únic dígit. Per poder obtenir el nombre correcte s'han de fer un conjunt d'operacions matemàtiques:

1. Agafar els ($n-1$) digitis del final del missatge.
2. Duplicar-los tantes vegades com indiqui l'últim dígit ($n$).

D'aquesta manera obtindreu un nombré anomenat $P$. Aquest nombre $P$ s'ha de descompondre en la suma dels seus dígits de forma iterativa fins a aconseguir un nombre d'un dígit. Aquest dígit és la clau per descodificar el missatge. Per exemple:

```sh
AA C214 13ASD EFDEASDA 1234
(n-1) = 123
(n) = 4
(P) = 123123123123

(123123123123) = 1+2+3+1+2+3+1+2+3+1+2+3 = 24
(24) = 2 + 4 = 6
(6) <- Clau del descodificador.
```

S'ha de desenvolupar un mètode que donat un cadena de nombres enters $n$ i un valor $k$. Obtingui de la forma més ràpida possible el dígit correcte.

* Realitzeu un programa iteratiu **(1 punt)**.
* Realitzeu un programa recursiu **(2 punt)**.
* Analitzeu la complexitat i  l'eficiència de les vostres solucions **(2 punt)**. S'ha de generar un informe complet amb l'anàlisi de costos, el vostre disseny, experiments amb diferents valors ($n-1$) i ($n$). Gràfiques, taules,...

## Torn 2. Aconseguir el combo *Mestre Jedi* 

En el torn actual hem d'intentar posar a la taula el màxim nombre de cartes d'una baralla amb $n$ cartes que ha estat barallada i no es pot alterar l'ordre. Com a jugador podem **descartar** una carta o **jugar-la** a la taula. Al final guanya el jugador que menys cartes ha descartat. Les regles per jugar són:

* Únicament puc jugar cartes de valor més gran que les que ja estan jugades a la taula.
* La combinació jedi és una de les múltiples jugades que permet jugar el màxim nombre de cartes. Obtenint sempre la màxima puntuació possible.

Per exemple:

```sh
Baralla = [2,1,4,2,9]

Les combinacions mestre jedi serien:
[2,4,9]
[1,4,9]
[1,2,9]
```

**Nota 1** Totes les baralles han d'estar formades per nombres enters positius.

**Nota 2**: Heu de tenir en compte que no es pot alterar l'ordre de la baralla.

* Realitzeu un programa iteratiu **(1 punt)**.
* Realitzeu un programa recursiu **(2 punt)**.
* Analitzeu la complexitat i  l'eficiència de les vostres solucions **(2 punt)**. S'ha de generar un informe complet amb l'anàlisi de costos, el vostre disseny, experiments amb diferents valors de $n$ i diferents configuracions de baralles. Gràfiques, taules,...

## Avaluació

Es valorarà l'ús de bones pràctiques en la programació.

Es valorarà el disseny i l'eficiència **temporal** (temps) i **espacial** (memòria) de les implementacions.

Es realitzarà una entrega presencial on s'avaluarà la correcta comprensió del codi desenvolupat.

Els integrants d'un grup poden tenir diferents notes en funció del grau de comprensió en l'avaluació presencial.
