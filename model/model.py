from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO

        cnx = get_connection()

        if cnx is not None:
            print("Connection established")

            query = "SELECT codice, tipo, marca, anno_acquisto, valore, disponibile FROM strumento ORDER BY codice"
            cursor = cnx.cursor()
            cursor.execute(query)

            result = []

            for row in cursor:
                strumento = Strumento(*row)
                result.append(strumento)

            cursor.close()
            cnx.close()
            return result

        return None


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO

        cnx = get_connection()

        if cnx is not None:
            print("Connection established")

            query = "SELECT codice, tipo, marca, anno_acquisto, valore, disponibile FROM strumento WHERE tipo LIKE %s ORDER BY codice"
            cursor = cnx.cursor()
            cursor.execute(query, (f"%{tipo}%",))

            result = []

            for row in cursor:
                strumento = Strumento(*row)
                result.append(strumento)

            cursor.close()
            cnx.close()
            return result

        return None