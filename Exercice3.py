import datetime
import copy

class ValidationMixin:
    def valider_titre(self, titre):
        if not titre or not isinstance(titre, str) or titre.strip() == "":
            raise ValueError("Créer un titre.")


class HistoriqueMixin:
    def __init__(self):
        self.historique = []

    def enregistrer_version(self, ancienne_description):

        entree = {
            "timestamp": datetime.datetime.now(),
            "ancienne_description": copy.deepcopy(ancienne_description)
        }
        self.historique.append(entree)


class JournalisationMixin:
    def journaliser(self, message):
        print(f"[Journal] {datetime.datetime.now()} – {message}")


class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):

    def __init__(self, titre, description):
 
        self.valider_titre(titre)

        HistoriqueMixin.__init__(self)

        self.titre = titre
        self.description = description
        self.date_creation = datetime.datetime.now()

        self.journaliser(f"Création de « {self.titre} »")

    def mettre_a_jour(self, nouvelle_description):
        self.enregistrer_version(self.description)

        self.description = nouvelle_description

        self.journaliser(f"Mise à jour de  « {self.titre} »")

    def afficher_historique(self):
        for entre in self.historique:
            print(f"- {entre['timestamp']} : {entre['ancienne_description']}")

task = Tache("Dossier Projet", "Ébauche initiale")
task.mettre_a_jour("Ajout partie technique")
task.mettre_a_jour("Validation finale")

task.afficher_historique()

