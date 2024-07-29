import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.3):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Thears stream down your faces", 0.20),
        ("I promise You♡ ", 0.13),
        ("I will learn from my mistakes", 0.16),
        ("Thears stream down Your face and I", 0.14),
        ("Light will guide...", 0.20),
        ("You home 🏡", 0.14),
        ("And ignite You bones", 0.16),
        ("And I will try...", 0.14),
        ("To Fix to You 💝 ", 0.15),
    ]
    delays = [0.2, 0.9, 0.20, 15.5, 24.2, 27.8, 32.1, 38.3, 41.9]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()