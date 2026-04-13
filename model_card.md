# Model Card: Music Recommender Simulation

## 1. Model Name

### VibeFinder 1.0

---

## 2. Intended Use

VibeFinder 1.0 is a classroom simulation of a content-based music recommender. Given a user's preferred genre, mood, and energy level, it scores every song in a small catalog and returns the top matches ranked by score.

**Intended for:**

- Educational exploration of how recommender systems work
- Classroom demonstration of scoring, ranking, and bias in AI systems
- Students learning Python data processing and algorithm design

**Not intended for:**

- Real users making actual music discovery decisions — the catalog is too small and the scoring too simplistic
- Any production or commercial music application
- Modeling users with complex, shifting, or multi-genre tastes
- Replacing platforms like Spotify or Apple Music — it has no listening history, no collaborative signal, and no feedback loop

---

## 3. How the Model Works

VibeFinder compares each song in the catalog to a user's stated preferences using three simple rules:

1. **Genre match** — if the song's genre matches the user's preferred genre, it earns 2 points. This is the strongest signal.
2. **Mood match** — if the song's mood matches the user's preferred mood, it earns 1 point.
3. **Energy proximity** — the system computes how close the song's energy level (a number between 0 and 1) is to the user's target. A perfect match earns 1 extra point; a song on the opposite end of the energy scale earns 0.

Songs are then ranked from highest to lowest total score, and the top results are returned with an explanation of why each was chosen.

Think of it like a knowledgeable friend who knows your taste: they first look for your favorite genre, then check the vibe, then make sure the intensity level feels right.

---

## 4. Data

- The catalog contains **20 songs** in `data/songs.csv`.
- Each song has: title, artist, genre, mood, energy (0–1), tempo in BPM, valence, danceability, and acousticness.
- **Genres represented:** pop, lofi, rock, ambient, jazz, synthwave, indie pop, folk, electronic.
- **Moods represented:** happy, chill, intense, relaxed, focused, moody.
- Songs were hand-authored for the classroom exercise and do not reflect real streaming data.
- The catalog skews toward Western popular music styles. Genres like classical, hip-hop, R&B, Latin, and K-pop are absent, meaning users with those preferences will receive poor recommendations.

---

## 5. Strengths

- Works well for users who know exactly what they want and whose preference matches a genre and mood in the catalog (e.g., "pop + happy + high energy" reliably surfaces upbeat pop tracks).
- The scoring logic is fully transparent — every recommendation comes with a plain-language reason.
- Adding a new song to `songs.csv` immediately makes it recommendable; no retraining needed.
- Equal treatment of niche genres: a folk song and a pop song have an identical chance of scoring 4.0 if they match the user's preferences.

---

## 6. Limitations and Bias

| Limitation | Detail |
| --- | --- |
| **Genre over-weighting** | Genre accounts for 2 of a possible 4 points (~50% of max score). A genre-matching song with a mismatched mood will almost always beat a non-matching song with a perfect mood and energy score. |
| **Cold-start for unknown genres** | If a user enters a genre not in the catalog (e.g., "hip-hop"), no song earns the genre bonus and results degrade to mood + energy matching only. |
| **No collaborative signal** | The system has no awareness of what other listeners enjoy. It cannot discover cross-genre patterns (e.g., "jazz fans also love certain ambient artists"). |
| **Catalog underrepresentation** | 20 songs across 9 genres means some genres have only 1–2 representatives, making diverse recommendations within a genre impossible. |
| **Single-point preferences** | Users rarely have one exact energy target. A person who likes both calm mornings and intense workouts cannot be modeled by a single profile. |
| **No temporal or contextual awareness** | The system ignores time of day, device, or listening session context — signals that real recommenders weight heavily. |

---

## 7. Evaluation

Three user profiles were tested:

| Profile | Expected top result | Actual top result | Match? |
| --- | --- | --- | --- |
| High-Energy Pop Fan (pop, happy, 0.9) | Golden Hour or Sunrise City | Golden Hour (score 3.98) | Yes |
| Chill Lofi Listener (lofi, chill, 0.35) | Library Rain or Empty Hallways | Library Rain (score 4.00) | Yes |
| Deep Rock (rock, intense, 0.92) | Storm Runner or Thunder Road | Storm Runner (score 3.99) | Yes |

All three profiles returned the expected top result. However, "Deep Rock" exposed the catalog underrepresentation problem — only 2 rock songs exist, so after rank #2 the system falls back to non-rock intense songs, with scores dropping sharply from 3.99 to 1.99.

---

## 8. Future Work

- **Expand the catalog** to 100+ songs covering more genres and moods, especially hip-hop, R&B, classical, and Latin.
- **Tune the weights** — allow genre, mood, and energy to have configurable weights rather than fixed point values, so users or instructors can experiment with different scoring philosophies.
- **Add tempo and valence scoring** — both are available in the CSV and could contribute to richer recommendations.
- **Support multiple moods and genres per user** — real listeners are not monolithic; a range-based preference model would be more realistic.
- **Add collaborative filtering** — track which songs users actually play (even in simulation) and use that signal to surface socially validated recommendations alongside content-based ones.
- **Diversity injection** — prevent the top-K results from being dominated by a single artist or very similar songs.

---

## 9. Personal Reflection

Building VibeFinder made the scoring logic behind real recommenders feel concrete. What seemed like magic (Spotify knowing exactly what you want on a Monday morning) is, at its core, a weighted comparison of features — just at a scale of millions of users and tens of millions of songs rather than 20.

The most surprising discovery was how quickly genre over-weighting emerged as a bias. Because genre carries twice the points of mood, the system confidently recommends an intense pop song to someone who said they wanted a chill vibe — just because the genre matched. Real platforms spend enormous effort tuning these weights through A/B tests and user feedback, something a fixed scoring rule cannot do on its own. This exercise showed that the fairness and quality of a recommender is not just a machine learning problem — it is also a design and values problem about which signals to trust and how much.
