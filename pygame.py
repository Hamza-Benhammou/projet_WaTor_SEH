class GraphicalDisplay(Planet):

    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        
        super().__init__(largeur_de_la_grille, hauteur_de_la_grille)
        musica = "bubbles_sound.mp3" 
        pygame.mixer.init()
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play(-1)
        #charge musique et tourne en boucle
        pygame.init()
        self.screen = pygame.display.set_mode((400 , 400))
        pygame.display.set_caption("WATOR")
        self.image_poisson = pygame.image.load('fish.jpg')
        self.image_requin = pygame.image.load('shark.jpg')
        self.image_blood = pygame.image.load('eclaboussure.png')


    def afficher_compteur(self):

        compteur_poissons = self.poissons 
        compteur_requins = self.requins
        font = pygame.font.Font(None, 26)
        requins_texte = font.render(f"Requins : {len(compteur_requins)}", True, (255, 0, 0))
        poissons_texte = font.render(f"Poissons : {len(compteur_poissons)}", True, (0, 0, 255))
        self.screen.blit(requins_texte, (10, 10))
        self.screen.blit(poissons_texte, (10, 50))
    
    
    def simuler(self, duree):
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            couleur_fond = (173, 216, 230) 
            self.screen.fill(couleur_fond)
            for y in range(self.hauteur_de_la_grille):
                for x in range(self.largeur_de_la_grille):
                    if self.grille[y][x] == '\U0001f41f':
                        self.screen.blit(self.image_poisson, (x * 40, y * 40)) 
                    elif self.grille[y][x] == '🦀':
                        self.screen.blit(self.image_requin, (x * 40, y * 40))
                    elif self.grille[y][x] == "☠︎︎" :
                        self.screen.blit(self.image_blood, (x * 40, y * 40))
 
            for requin in self.requins:
                requin.deplacement()
            for poisson in self.poissons:
                poisson.deplacement()
            
            self.afficher_compteur()

            pygame.display.flip()
            self.chronons += 1
            self.afficher_le_monde()
            time.sleep(0.5)
            

            if self.chronons >= duree:
                running = False
            time.sleep(0.5)

        pygame.quit()
        #boucle du jeu: definit le fond, et scanne la grille pour placer les poissons et les requins à chaque simulation
         

#test terminal
# planete_1 = Planet(20, 20)
# planete_1.peupler_le_monde(1000, 300)
# planete_1.simuler(10)

#test pygame
planete2= GraphicalDisplay(10, 10)
planete2.peupler_le_monde(20, 4)
planete2.simuler(20)