import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_moon(phase):
    moons = [
        "🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"
    ]
    print(moons[phase])

def animate_moon():
    while True:  # Бесконачна петља
        for phase in range(8):
            clear_screen()
            draw_moon(phase)
            time.sleep(0.5)

if __name__ == "__main__":
    animate_moon()
