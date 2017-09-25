# csv_to_table

Conversion de csv en tableau ascii

## Objectif

Faciliter la création de "grid table" pour Markdown avec Pandoc.

## Dépendance

Dépend de [py_simple_table](https://github.com/pedrudehuere/py_simple_table).

## Utilisation

*csv_to_table* lit le contenu csv qui lui est donné en entrée,
et le formatte en tableau ascii en sortie.
La première ligne du csv est considérée comme une ligne de titre.
Exemple :

    cat test.csv | csv_to_table.py
