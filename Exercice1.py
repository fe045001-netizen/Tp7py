from datetime import datetime

class Horodatable:
    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")

class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")
        print("Validation OK")

class Document(Horodatable, Validable):
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        print(f"Document '{self.titre}' sauvegardé.")

doc = Document("Rapport", "Contenu important")
doc.sauvegarder()