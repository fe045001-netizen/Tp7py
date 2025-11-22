import json
from datetime import datetime

class Serializable:
    def to_json(self):
        def convert(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return obj

        return json.dumps(self.__dict__, default=convert, ensure_ascii=False)


class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        self.historique.append((datetime.now(), json.dumps(self.__dict__)))

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")

class Contrat(Serializable, Historisable, Journalisable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc

c = Contrat(1, "Initial")
c.modifier("Révisé")
print(c.to_json())