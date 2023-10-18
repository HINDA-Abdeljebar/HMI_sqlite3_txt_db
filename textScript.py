class Utilisateur:
    def __init__(self, id, nom, prenom, role, email):
        self.user_id = id
        self.nom = nom
        self.prenom = prenom
        self.role = role
        self.email = email

    @classmethod
    def ajouter(cls, id, nom, prenom, role, email):
        utilisateur = Utilisateur(id, nom, prenom, role, email)
        with open("utilisateurs.txt", "a") as fichier:
            fichier.write(f"{utilisateur.user_id},{utilisateur.nom},{utilisateur.prenom},{utilisateur.role},{utilisateur.email}\n")

    @classmethod
    def lister(cls):
        utilisateurs = []
        with open("utilisateurs.txt", "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                champs = ligne.strip().split(',')
                if len(champs) == 5:
                    id, nom, prenom, role, email = champs
                    utilisateur = Utilisateur(int(id), nom, prenom, role, email)
                    utilisateurs.append(utilisateur)
        return utilisateurs

    @classmethod
    def mettre_a_jour(cls, id, nom, prenom, role, email):
        utilisateurs = cls.lister()
        if 0 <= id < len(utilisateurs):
            utilisateur = utilisateurs[id]
            utilisateur.nom = nom
            utilisateur.prenom = prenom
            utilisateur.role = role
            utilisateur.email = email
            with open("utilisateurs.txt", "w") as fichier:
                for u in utilisateurs:
                    fichier.write(f"{u.user_id},{u.nom},{u.prenom},{u.role},{u.email}\n")

    @classmethod
    def supprimer(cls, id):
        utilisateurs = cls.lister()
        if 0 <= id < len(utilisateurs):
            del utilisateurs[id]
            with open("utilisateurs.txt", "w") as fichier:
                for u in utilisateurs:
                    fichier.write(f"{u.user_id},{u.nom},{u.prenom},{u.role},{u.email}\n")

class Cours:
    def __init__(self, id, nom_cours, description):
        self.id = id
        self.nom_cours = nom_cours
        self.description = description

    @classmethod
    def ajouter(cls, id, nom_cours, description):
        cours = Cours(id, nom_cours, description)
        with open("cours.txt", "a") as fichier:
            fichier.write(f"{cours.id},{cours.nom_cours},{cours.description}\n")

    @classmethod
    def lister(cls):
        cours = []
        with open("cours.txt", "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                champs = ligne.strip().split(',')
                if len(champs) == 3:
                    id, nom_cours, description = champs
                    cours.append(Cours(int(id), nom_cours, description))
        return cours

    @classmethod
    def mettre_a_jour(cls, id, nom_cours, description):
        cours = cls.lister()
        if 0 <= id < len(cours):
            cours[id].nom_cours = nom_cours
            cours[id].description = description
            with open("cours.txt", "w") as fichier:
                for c in cours:
                    fichier.write(f"{c.id},{c.nom_cours},{c.description}\n")

    @classmethod
    def supprimer(cls, id):
        cours = cls.lister()
        if 0 <= id < len(cours):
            del cours[id]
            with open("cours.txt", "w") as fichier:
                for c in cours:
                    fichier.write(f"{c.id},{c.nom_cours},{c.description}\n")

class Room:
    def __init__(self, id, nom_salle, capacite):
        self.id = id
        self.nom_salle = nom_salle
        self.capacite = capacite

    @classmethod
    def ajouter(cls, id, nom_salle, capacite):
        salle = Room(id, nom_salle, capacite)
        with open("salles.txt", "a") as fichier:
            fichier.write(f"{salle.id},{salle.nom_salle},{salle.capacite}\n")

    @classmethod
    def lister(cls):
        salles = []
        with open("salles.txt", "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                champs = ligne.strip().split(',')
                if len(champs) == 3:
                    id, nom_salle, capacite = champs
                    salle = Room(int(id), nom_salle, int(capacite))
                    salles.append(salle)
        return salles

    @classmethod
    def mettre_a_jour(cls, id, nom_salle, capacite):
        salles = cls.lister()
        if 0 <= id < len(salles):
            salle = salles[id]
            salle.nom_salle = nom_salle
            salle.capacite = capacite
            with open("salles.txt", "w") as fichier:
                for s in salles:
                    fichier.write(f"{s.id},{s.nom_salle},{s.capacite}\n")

    @classmethod
    def supprimer(cls, id):
        salles = cls.lister()
        if 0 <= id < len(salles):
            del salles[id]
            with open("salles.txt", "w") as fichier:
                for s in salles:
                    fichier.write(f"{s.id},{s.nom_salle},{s.capacite}\n")

class EmploiDuTemps:
    def __init__(self, id, jour_semaine, heure_debut, heure_fin):
        self.id = id
        self.jour_semaine = jour_semaine
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin

    @classmethod
    def ajouter(cls, id, jour_semaine, heure_debut, heure_fin):
        emploi_du_temps = EmploiDuTemps(id, jour_semaine, heure_debut, heure_fin)
        with open("emplois_du_temps.txt", "a") as fichier:
            fichier.write(f"{emploi_du_temps.id},{emploi_du_temps.jour_semaine},{emploi_du_temps.heure_debut},{emploi_du_temps.heure_fin}\n")

    @classmethod
    def lister(cls):
        emplois_du_temps = []
        with open("emplois_du_temps.txt", "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                champs = ligne.strip().split(',')
                if len(champs) == 4:
                    id, jour_semaine, heure_debut, heure_fin = champs
                    emploi_du_temps = EmploiDuTemps(int(id), jour_semaine, heure_debut, heure_fin)
                    emplois_du_temps.append(emploi_du_temps)
        return emplois_du_temps

    @classmethod
    def mettre_a_jour(cls, id, jour_semaine, heure_debut, heure_fin):
        emplois_du_temps = cls.lister()
        if 0 <= id < len(emplois_du_temps):
            emploi_du_temps = emplois_du_temps[id]
            emploi_du_temps.jour_semaine = jour_semaine
            emploi_du_temps.heure_debut = heure_debut
            emploi_du_temps.heure_fin = heure_fin
            with open("emplois_du_temps.txt", "w") as fichier:
                for e in emplois_du_temps:
                    fichier.write(f"{e.id},{e.jour_semaine},{e.heure_debut},{e.heure_fin}\n")

    @classmethod
    def supprimer(cls, id):
        emplois_du_temps = cls.lister()
        if 0 <= id < len(emplois_du_temps):
            del emplois_du_temps[id]
            with open("emplois_du_temps.txt", "w") as fichier:
                for e in emplois_du_temps:
                    fichier.write(f"{e.id},{e.jour_semaine},{e.heure_debut},{e.heure_fin}\n")
                    
                    
# Fonction de menu principal
def menu():
    while True:
        print("\nMenu :")
        print("1. Gérer les Utilisateurs")
        print("2. Gérer les Cours")
        print("3. Gérer l'Emploi du Temps")
        print("4. Gérer les Salles (Rooms)")
        print("5. Quitter")

        choix = input("Choisissez une option (1/2/3/4/5): ")

        if choix == '1':
            # Gérer les Utilisateurs
            print("\nMenu Utilisateurs :")
            print("1. Ajouter un Utilisateur")
            print("2. Lister les Utilisateurs")
            print("3. Mettre à jour un Utilisateur")
            print("4. Supprimer un Utilisateur")
            print("5. Retour au menu principal")

            choix_utilisateur = input("Choisissez une option pour les Utilisateurs (1/2/3/4/5): ")

            if choix_utilisateur == '1':
                id = int(input("ID de l'Utilisateur : "))
                nom = input("Nom : ")
                prenom = input("Prénom : ")
                role = input("Rôle : ")
                email = input("Email : ")
                Utilisateur.ajouter(id, nom, prenom, role, email)
            elif choix_utilisateur == '2':
                print("\nListe des Utilisateurs :")
                utilisateurs = Utilisateur.lister()
                for i, utilisateur in enumerate(utilisateurs):
                    print(f"{i}. ID: {utilisateur.user_id}, Nom: {utilisateur.nom}, Prénom: {utilisateur.prenom}, Role: {utilisateur.role}, Email: {utilisateur.email}")
            elif choix_utilisateur == '3':
                id = int(input("Entrez l'ID de l'Utilisateur que vous souhaitez mettre à jour : "))
                nom = input("Nouveau nom : ")
                prenom = input("Nouveau prénom : ")
                role = input("Nouveau rôle : ")
                email = input("Nouvel email : ")
                Utilisateur.mettre_a_jour(id, nom, prenom, role, email)
            elif choix_utilisateur == '4':
                id = int(input("Entrez l'ID de l'Utilisateur que vous souhaitez supprimer : "))
                Utilisateur.supprimer(id)
            elif choix_utilisateur == '5':
                continue  # Revenir au menu principal
        elif choix == '2':
            # Gérer les Cours
            print("\nMenu Cours :")
            print("1. Ajouter un Cours")
            print("2. Lister les Cours")
            print("3. Mettre à jour un Cours")
            print("4. Supprimer un Cours")
            print("5. Retour au menu principal")

            choix_cours = input("Choisissez une option pour les Cours (1/2/3/4/5): ")

            if choix_cours == '1':
                id = int(input("ID du Cours : "))
                nom_cours = input("Nom du Cours : ")
                description = input("Description : ")
                Cours.ajouter(id, nom_cours, description)
            elif choix_cours == '2':
                print("\nListe des Cours :")
                cours = Cours.lister()
                for i, cours in enumerate(cours):
                    print(f"{i}. ID: {cours.id}, Nom du Cours: {cours.nom_cours}, Description: {cours.description}")
            elif choix_cours == '3':
                id = int(input("Entrez l'ID du Cours que vous souhaitez mettre à jour : "))
                nom_cours = input("Nouveau nom du Cours : ")
                description = input("Nouvelle description : ")
                Cours.mettre_a_jour(id, nom_cours, description)
            elif choix_cours == '4':
                id = int(input("Entrez l'ID du Cours que vous souhaitez supprimer : "))
                Cours.supprimer(id)
            elif choix_cours == '5':
                continue  # Revenir au menu principal
        if choix == '3':
            # Gérer l'Emploi du Temps
            print("\nMenu Emploi du Temps :")
            print("1. Ajouter un Emploi du Temps")
            print("2. Lister l'Emploi du Temps")
            print("3. Mettre à jour un Emploi du Temps")
            print("4. Supprimer un Emploi du Temps")
            print("5. Retour au menu principal")

            choix_emploi_du_temps = input("Choisissez une option pour l'Emploi du Temps (1/2/3/4/5): ")
         
            if choix_emploi_du_temps == '1':
                id = int(input("ID de l'Emploi du Temps : "))
                jour_semaine = input("Jour de la semaine : ")
                heure_debut = input("Heure de début : ")
                heure_fin = input("Heure de fin : ")
                EmploiDuTemps.ajouter(id, jour_semaine, heure_debut, heure_fin)
            elif choix_emploi_du_temps == '2':
                print("\nListe de l'Emploi du Temps :")
                emploi_du_temps = EmploiDuTemps.lister()
                for i, emploi in enumerate(emploi_du_temps):
                    print(f"{i}. ID: {emploi.id}, Jour de la semaine: {emploi.jour_semaine}, Heure de début: {emploi.heure_debut}, Heure de fin: {emploi.heure_fin}")
            elif choix_emploi_du_temps == '3':
                id = int(input("Entrez l'ID de l'Emploi du Temps que vous souhaitez mettre à jour : "))
                jour_semaine = input("Nouveau jour de la semaine : ")
                heure_debut = input("Nouvelle heure de début : ")
                heure_fin = input("Nouvelle heure de fin : ")
                EmploiDuTemps.mettre_a_jour(id, jour_semaine, heure_debut, heure_fin)
            elif choix_emploi_du_temps == '4':
                id = int(input("Entrez l'ID de l'Emploi du Temps que vous souhaitez supprimer : "))
                EmploiDuTemps.supprimer(id)
            elif choix_emploi_du_temps == '5':
               continue  # Revenir au menu principal

        elif choix == '4':
            # Gérer les Salles (Rooms)
            print("\nMenu Salles (Rooms):")
            print("1. Ajouter une Salle (Room)")
            print("2. Lister les Salles (Rooms)")
            print("3. Mettre à jour une Salle (Room)")
            print("4. Supprimer une Salle (Room)")
            print("5. Retour au menu principal")

            choix_salle = input("Choisissez une option pour les Salles (Rooms) (1/2/3/4/5): ")

            if choix_salle == '1':
                id = int(input("ID de la Salle : "))
                nom_salle = input("Nom de la Salle : ")
                capacite = int(input("Capacité : "))
                Room.ajouter(id, nom_salle, capacite)
            elif choix_salle == '2':
                print("\nListe des Salles (Rooms) :")
                salles = Room.lister()
                for i, salle in enumerate(salles):
                    print(f"{i}. ID: {salle.id}, Nom de la Salle: {salle.nom_salle}, Capacité: {salle.capacite}")
            elif choix_salle == '3':
                id = int(input("Entrez l'ID de la Salle que vous souhaitez mettre à jour : "))
                nom_salle = input("Nouveau nom de la Salle : ")
                capacite = int(input("Nouvelle capacité : "))
                Room.mettre_a_jour(id, nom_salle, capacite)
            elif choix_salle == '4':
                id = int(input("Entrez l'ID de la Salle que vous souhaitez supprimer : "))
                Room.supprimer(id)
            elif choix_salle == '5':
                continue  # Revenir au menu principal
        elif choix == '5':
            break  # Quitter le programme

if __name__ == '__main__':
    print("Bienvenue dans l'application de gestion de l'emploi du temps.")
    menu()
