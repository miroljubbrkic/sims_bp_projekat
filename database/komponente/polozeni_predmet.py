from database.komponente.predmet import Predmet


class PolozeniPredmet(Predmet):
    def __init__(self, sifra_predmeta, naziv, broj_casova_nedeljno, broj_semestra, nastavnici, ocena=6):
        super().__init__(sifra_predmeta, naziv, broj_casova_nedeljno, broj_semestra, nastavnici)
        self.ocena = ocena