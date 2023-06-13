COMAND_TEXTS = {
    "IT" : {
        "start" : "Benvenuto, per iniziare esegui /help",

        "help" : """
<b>• AGGIUNGI UN NUOVO ESERCIZIO </b>
Esegui il comando /esercizio specificando nome e carico dell'esercizio separati da una virgola per aggiungerlo al registro.
Prova ad esempio <i>'/esercizio Backsquat, 50'</i>.

<b>• VISUALIZZA IL REGISTRO DEI TUOI ESERCIZI </b>
Esegui il comando /registro per visualizzare il registro dei tuoi massimali.

<b>• CANCELLA UN ESERCIZIO </b>
Esegui il comando /cancella specificando il nome dell'esercizio per cancellarlo dal registro.
Prova ad esempio <i>'/cancella Backsquat'</i>.

<b>• ELIMINA TUTTI I TUOI RISULTATI </b>
Esegui il comando /reset per eliminare tutti i dati presenti nel registro.
                """,

        "exerciseRegisteredSuccessfully" :  "Il tuo esercizio è stato registrato correttamente.\nEsegui /registro per visualizzare il registro",

        "exerciseAlreadyRegistered" : "Il tuo esercizio è stato modificato correttamente.\nEsegui /registro per visualizzare il registro",

        "exerciseDeleted" : "Il tuo esercizio è stato cancellato correttamente.\nEsegui /registro per visualizzare il registro",

        "reset" : "Il registro è stato resettato.\nEsegui /esercizio per aggiungere nuovi esercizi.",

        "registerIsEmpty" : "Nessun esercizio è stato registrato",

        "ERROR" : {
            "EXERCISE_REGISTER_ERROR" : """
Il tuo esercizio non è stato registrato correttamente.
Riprova seguendo il corretto formato.
Ad esempio <i>'/esercizio Backsquat, 50'</i>.
                                            """,
            "EXERCISE_DELETION_ERROR" : """
Il tuo esercizio non è stato cancellato correttamente.
Riprova seguendo il corretto formato.
Ad esempio <i>'/cancella Backsquat'</i>.
            """
        }
    }
}

DF_HEADERS = {
    "ESERCIZIO" : "<b>ESERCIZIO</b>",
    "PESO" : "<b>PESO</b>",
    "DATA" : "<b>DATA</b>"
}
