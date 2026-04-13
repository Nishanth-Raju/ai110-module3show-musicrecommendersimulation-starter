"""
Command line runner for the Music Recommender Simulation.

Run from the project root with:
    python -m src.main
"""

from src.recommender import load_songs, recommend_songs

SONGS_PATH = "data/songs.csv"
TOP_K = 5

# --- Standard profiles (Phase 4: Stress Testing) ---
USER_PROFILES = [
    {
        "name": "High-Energy Pop Fan",
        "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9},
    },
    {
        "name": "Chill Lofi Listener",
        "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.35},
    },
    {
        "name": "Deep Rock",
        "prefs": {"genre": "rock", "mood": "intense", "energy": 0.92},
    },
]

# --- Adversarial profiles (Phase 4: Edge Case Testing) ---
ADVERSARIAL_PROFILES = [
    {
        "name": "ADVERSARIAL: High Energy + Chill Mood (conflicting)",
        "prefs": {"genre": "ambient", "mood": "chill", "energy": 0.95},
    },
    {
        "name": "ADVERSARIAL: Unknown Genre (no genre bonus ever fires)",
        "prefs": {"genre": "hip-hop", "mood": "happy", "energy": 0.8},
    },
]


def print_divider(char: str = "-", width: int = 60) -> None:
    """Print a horizontal rule of the given character and width."""
    print(char * width)


def print_recommendations(profile_name: str, recs: list) -> None:
    """Print a formatted block of recommendations for one user profile."""
    print_divider("=")
    print(f"  Profile: {profile_name}")
    print_divider("=")

    for rank, (song, score, explanation) in enumerate(recs, start=1):
        print(f"  #{rank}  {song['title']}  --  {song['artist']}")
        print(
            f"       Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}"
        )
        print(f"       Score: {score:.2f}")
        print(f"       Why:   {explanation}")
        print_divider(width=60)


def main() -> None:
    """Load the song catalog and print recommendations for all user profiles."""
    songs = load_songs(SONGS_PATH)
    print(f"\nLoaded {len(songs)} songs from catalog.\n")

    print("\n=== STANDARD PROFILES ===\n")
    for profile in USER_PROFILES:
        recs = recommend_songs(profile["prefs"], songs, k=TOP_K)
        print_recommendations(profile["name"], recs)

    print("\n=== ADVERSARIAL / EDGE CASE PROFILES ===\n")
    for profile in ADVERSARIAL_PROFILES:
        recs = recommend_songs(profile["prefs"], songs, k=3)
        print_recommendations(profile["name"], recs)

    print()


if __name__ == "__main__":
    main()
