import sys
import shutil
from audio_analysis import analyze_audio
from beat_selection import select_beat
from pathlib import Path

RAW_DIR = Path("data/raw_audio")
BEATS_DIR = Path("data/beats")
OUTPUT_DIR = Path("data/output")


def run_pipeline(audio_file):
    print("Analyse audio...")
    features = analyze_audio(audio_file)

    print("Sélection du beat...")
    beat = select_beat(features)

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_path = OUTPUT_DIR / f"output_{Path(audio_file).name}"
    shutil.copy(BEATS_DIR / beat, output_path)

    print(f"Beat sélectionné : {beat}")
    print(f"Fichier généré : {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python pipeline/main.py <audio.wav>")
        sys.exit(1)

    run_pipeline(sys.argv[1])

