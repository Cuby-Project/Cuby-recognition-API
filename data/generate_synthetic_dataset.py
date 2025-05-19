import csv
import random
import os

# Couleurs moyennes HSV pour Rubik's Cube (approx.)
COLOR_RANGES = {
    'W': (0, 0, 255),     # blanc
    'Y': (25, 255, 255),  # jaune
    'R': (0, 255, 255),   # rouge
    'O': (15, 255, 255),  # orange
    'B': (110, 255, 255), # bleu
    'G': (60, 255, 255),  # vert
}

SAMPLES_PER_COLOR = 100
OUTPUT_FILE = './dataset.csv'

os.makedirs('data', exist_ok=True)

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

def generate_dataset():
    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['H', 'S', 'V', 'label'])

        for label, (h_mean, s_mean, v_mean) in COLOR_RANGES.items():
            for _ in range(SAMPLES_PER_COLOR):
                h = clamp(int(random.gauss(h_mean, 5)), 0, 179)
                s = clamp(int(random.gauss(s_mean, 20)), 0, 255)
                v = clamp(int(random.gauss(v_mean, 20)), 0, 255)
                writer.writerow([h, s, v, label])

    print(f"✅ Synthetic dataset generated at {OUTPUT_FILE} with {SAMPLES_PER_COLOR * len(COLOR_RANGES)} samples")

if __name__ == '__main__':
    generate_dataset()
