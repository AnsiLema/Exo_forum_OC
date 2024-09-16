from abc import ABC

class File(ABC):
    """Fichier"""
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier"""
        pass

class ImageFile(File):
    """Fichier Image"""
    def display(self):
        print(f"fichier {self.name}")


class ImageGIF(ImageFile):
    """fichier image GIF"""
    def display(self):
        super().display()
        print("L'image est de type .gif ")

class ImageJPG(ImageFile):
    """fichier image JPG"""

    def display(self):
        super().display()
        print("L'image est de type .jpg ")



class User:
    """Utilisateur"""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        """connecte l'utilisateur"""
        print(f"L'utilisateur {self.username} est connecté. ")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui",content=content)
            thread.add_post(post)
            return post

    def make_thread(self, title, content):
        """créé un fil de discussion"""
        post = Post(self, "aujourd'hui", content)

    def __str__(self):
        """représentation de l'utilisateur"""
        return self.username

class Moderator(User):
    """Utilisateur Modérateur"""

    def edit(self, post, content):
        """modie un message"""
        post.content = content

    def delete(self, thread, post):
        """supprimer un message"""
        index = thread.post.index(post)
        del thread.post[index]


class Post:
    """Message"""

    def __init__(self, user, time_posted, content):
        """initialise l'utilisateur, la date et le contenu"""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """affiche le message"""
        print(f"Message posté par {self.user}, {self.time_posted}. ")
        print(self.content)


class FilePost(Post):
    """Message avec un fichier"""
    def __init__(self, user, time_posted, content, file):
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        """affiche le message avec le fichier"""
        super().display()
        print("pièce jointe:")
        self.file.display()



class Thread:
    """Fil de discussion"""
    def __init__(self, title, time_posted, post):
        """initialise le titre, la date et les postes
          Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)"""

        self.title = title
        self.time_posted = time_posted
        self.post = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.post:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.post.append(post)

#Création de l'utilisateur
user = User("Margritt", "Bonbon")
"""créé le nouvel utilisateur"""

#Création du modérateur
moderator = Moderator("Ansi", "JaelynHaylee")
"""créé le nouveau modérateur"""

#Création du fil de discussion par l'utilisateur
thread = Thread("Gare aux Gorilles", "Aujourd'hui", Post(user, "aujourd'hui", "Le gorille des montagne est un animal fascinant, de nature calme et pacifique, il n'en demeure pas moins un animal très dangeureux."))
thread.display()

#Réponse par le modérateur
moderator_post = moderator.post(thread, "Merci pour ce sujet très intéressant, Margritt !" )
thread.display()

#Message hors-sujet de l'utilisateur
off_topic_post = user.post(thread, "Voilà donc la fameuse recette du gateau au chocolat! ")
thread.display()

#Réponse au message hors-sujet
off_topic_response_post = moderator.post(thread, "Ce message est hors-sujet et n'a rien à faire dans le fil de discussion suivant. ")
thread.display()

#Suppression du message HS et de l'avertissement
moderator.delete(thread, off_topic_post)
moderator.delete(thread, off_topic_response_post)
thread.display()

#Réponse utilisateur avec une image
image_file = ImageGIF("image_funny.gif", "340")
user.post(thread, "Voici une image rigolote !", file=image_file)
thread.display()





