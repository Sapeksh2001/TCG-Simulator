import os
import pygame
import tkinter as tk
from ttkbootstrap import Style
import threading
from tkinter import ttk

# Initialize pygame
pygame.init()

# Game variables
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
FPS = 60
scroll_speed = 2

# Function to initialize Pygame display
def initialize_pygame(poke):
    os.environ["SDL_WINDOWID"] = str(poke.winfo_id())  # Embed Pygame into tkinter
    os.environ["SDL_VIDEODRIVER"] = "windib"  # Use windib video driver
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.init()
    pygame.display.set_caption("Parallax Game")
    return screen

# Load images
def load_images():
    bg_images = []
    for i in range(1, 6):
        bg_image = pygame.image.load(f"C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/plx-{i}.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        bg_images.append(bg_image)

    ground_image = pygame.image.load("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/ground.png").convert_alpha()
    ground_image = pygame.transform.scale(ground_image, (SCREEN_WIDTH, 200))  # Resize ground
    return bg_images, ground_image

# Function to draw the background and ground
def draw_bg(screen, bg_images, bg_scrolls):
    for i, bg_image in enumerate(bg_images):
        speed = 1 + i * 0.2  # Parallax effect
        bg_scrolls[i] = (bg_scrolls[i] + scroll_speed * speed) % SCREEN_WIDTH
        for x in range(2):  # Draw two copies of the image for seamless scrolling
            screen.blit(bg_image, ((x * SCREEN_WIDTH) - bg_scrolls[i], 0))

def draw_ground(screen, ground_image, ground_scroll):
    for x in range(2):
        screen.blit(ground_image, ((x * SCREEN_WIDTH) - ground_scroll, SCREEN_HEIGHT - 200))

# Main game loop for pygame
def run_game(poke):
    # Initialize Pygame display
    screen = initialize_pygame(poke)

    # Load assets
    bg_images, ground_image = load_images()
    bg_scrolls = [0] * len(bg_images)
    ground_scroll = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update scroll positions
        ground_scroll = (ground_scroll + scroll_speed * 2.5) % SCREEN_WIDTH

        # Draw everything
        screen.fill((0, 0, 0))  # Clear screen
        draw_bg(screen, bg_images, bg_scrolls)
        draw_ground(screen, ground_image, ground_scroll)

        pygame.display.flip()  # Update display
        clock.tick(FPS)  # Maintain frame rate

    pygame.quit()

# Function to start the pygame loop in a separate thread
def start_game_thread(poke):
    game_thread = threading.Thread(target=run_game, args=(poke,))
    game_thread.daemon = True  # Allow the thread to close when the main program ends
    game_thread.start()

# Initialize tkinter and ttkbootstrap
style = Style("darkly")
root = style.master
root.title("Parallax Game in Tkinter")

# Create frame for embedding Pygame
poke = tk.Frame(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
poke.place(x=0, y=0)  # Absolute positioning to cover the full background

# Start the game loop in a separate thread
root.after(100, start_game_thread, poke)

# Transparent button frame
button_frame = tk.Frame(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Transparent frame
button_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the button frame

# Custom style for transparent buttons
style.configure(
    "Transparent.TButton",
    background="",
    foreground="white",
    borderwidth=0,
    focuscolor="",
    padding=5,
)

# Add 16 transparent buttons in a 4x4 grid
for i in range(4):
    for j in range(4):
        btn = ttk.Button(
            button_frame, text=f"Button {i * 4 + j + 1}", style="Transparent.TButton"
        )
        btn.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
