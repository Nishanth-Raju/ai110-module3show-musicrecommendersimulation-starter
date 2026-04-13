import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """OOP recommendation engine backed by a song catalog."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        score = 0.0
        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
        energy_diff = abs(user.target_energy - song.energy)
        score += 1.0 - energy_diff
        if user.likes_acoustic and song.acousticness > 0.5:
            score += 0.5
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        sorted_songs = sorted(self.songs, key=lambda s: self._score(user, s), reverse=True)
        return sorted_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append(f"matches your favorite genre ({song.genre})")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append(f"matches your preferred mood ({song.mood})")
        energy_diff = abs(user.target_energy - song.energy)
        if energy_diff < 0.2:
            reasons.append(f"energy is close to your target ({song.energy:.2f} vs {user.target_energy:.2f})")
        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append(f"has strong acoustic qualities ({song.acousticness:.2f})")
        if not reasons:
            reasons.append("partially aligns with your overall taste profile")
        return "This song " + ", and ".join(reasons) + "."


# ---------------------------------------------------------------------------
# Functional API (used by src/main.py)
# ---------------------------------------------------------------------------

def load_songs(filepath: str) -> List[Dict]:
    """Load songs from a CSV file using csv.DictReader."""
    songs = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Score a single song against user preferences.

    Scoring rules:
      +2.0  genre match
      +1.0  mood match
      +0–1  energy proximity  =  1.0 - |target_energy - song_energy|
    """
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append(f"genre match ({song['genre']})")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append(f"mood match ({song['mood']})")

    energy_diff = abs(float(user_prefs["energy"]) - float(song["energy"]))
    energy_score = round(1.0 - energy_diff, 3)
    score += energy_score
    reasons.append(f"energy proximity {energy_score:.2f}")

    return round(score, 3), reasons


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort descending, return top k as (song, score, explanation)."""
    scored = []
    for song in songs:
        total_score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        scored.append((song, total_score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
