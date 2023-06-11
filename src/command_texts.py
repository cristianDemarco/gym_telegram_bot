# TODO: ADD MULTILANGUAGE STRUCTURE

COMMAND_TEXTS = {
    "IT" : {
        "start" : "Benvenuto, per iniziare esegui /help",

        "help" : """
Esegui il comando /esercizio specificando nome e carico dell'esercizio separati da una virgola per aggiungerlo alla rubrica.
Prova ad esempio '/esercizio Backsquat, 50'.
                    
Esegui il comando /registro per visualizzare il registro dei tuoi massimali.

Esegui il comando /reset per eliminare tutti i dati presenti nel file
                """,

        "exerciseRegisteredSuccessfully" :  "Il tuo esercizio è stato registrato correttamente.\nEsegui /registro per visualizzarlo",

        "reset" : "Il registro è stato resettato.\nEsegui /esercizio per aggiungere nuovi esercizi.",

        "ERROR" : {
            "EXERCISE_REGISTER_ERROR" : """
Il tuo esercizio non è stato registrato correttamente.
Riprova seguendo il corretto formato.
Ad esempio '/esercizio Backsquat, 50'.
                                            """
        }
    }
}