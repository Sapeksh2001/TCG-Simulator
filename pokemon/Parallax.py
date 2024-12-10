import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Create game window
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

# Define game variables
scroll_speed = 2  # Adjust scrolling speed as needed

# Load images and scale them to match the screen width and height
ground_image = pygame.image.load("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/ground.png").convert_alpha()
ground_image = pygame.transform.scale(ground_image, (SCREEN_WIDTH, ground_image.get_height()))

ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/plx-{i}.png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Stretch to screen size
    bg_images.append(bg_image)

# Create scroll positions for each layer
bg_scrolls = [0] * len(bg_images)

def draw_bg():
    for i, bg_image in enumerate(bg_images):
        speed = 1 + i * 0.2  # Adjust speed incrementally for parallax effect
        bg_scrolls[i] = (bg_scrolls[i] + scroll_speed * speed) % SCREEN_WIDTH
        for x in range(2):  # Render two repetitions of the image to avoid gaps
            screen.blit(bg_image, ((x * SCREEN_WIDTH) - bg_scrolls[i], 0))

def draw_ground():
    for x in range(2):  # Ensure enough repetitions for seamless scrolling
        screen.blit(ground_image, ((x * ground_width) - (bg_scrolls[0] * 2.5 % ground_width), SCREEN_HEIGHT - ground_height))

# Game loop
run = True
while run:
    clock.tick(FPS)

    # Draw world
    draw_bg()
    draw_ground()

    # Event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()