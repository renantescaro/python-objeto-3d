import pygame

class Joystick:
    def __init__(self):
        self.analogico_esquerdo_x = 0.0
        self.analogico_esquerdo_y = 0.0
        self.analogico_direito_x  = 0.0
        self.analogico_direito_y  = 0.0
        self.botao = [False, False, False, False, False, False]

        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.joystick.init()

        # número do joystick plugado
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()


    def get_botao_pressionado(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for n in range(15):
                   if self.joystick.get_button(n):
                       return n, 'botao'
        
        for a in range(6):
            valor_analogico = self.joystick.get_axis(a)
            if (valor_analogico > 0.4 or valor_analogico < -0.4) and valor_analogico != -1:
                return a, 'analogico'

        return -1, ''