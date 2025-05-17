import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.shoot_timer = 0
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        # super().__init__(x, y, PLAYER_RADIUS)
        self.angle = 0
        self.rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), 2)

    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, forward=True)
        if keys[pygame.K_s]:
            self.move(dt, forward=False)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_speed * dt
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_speed * dt

        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    def move(self, dt, forward=True):
        direction = 1 if forward else -1
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vector * PLAYER_SPEED * dt * direction

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, -1).rotate(self.angle)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
