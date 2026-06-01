import random
import time
import subprocess
from pathlib import Path

valg = ["Sten", "Saks", "Papir"]

art = {
    "Sten": "🪨",
    "Saks": "✂️",
    "Papir": "📄"
}

Bruger = input("Vælg Sten, Saks eller Papir: ")
Computer = random.choice(valg)

if Bruger not in valg:
    print("Ugyldigt valg. Prøv igen.")
else:
    sound_file = Path(__file__).with_name("ding.mp3")
    subprocess.Popen(["afplay", str(sound_file)])

    print("Computeren tænker", end="", flush=True)

    for lyd in " biip boop...":
        print(lyd, end="", flush=True)
        time.sleep(0.2)

    print()
    print("Du valgte:", Bruger, art[Bruger])
    print("Computeren valgte:", Computer, art[Computer])

    if Bruger == Computer:
        print("Det blev uafgjort!")
    elif (Bruger == "Sten" and Computer == "Saks") or (Bruger == "Saks" and Computer == "Papir") or (Bruger == "Papir" and Computer == "Sten"):
        print("Du vinder!")
    else:
        print("Computeren vinder!🦾🤖")