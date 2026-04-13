# Reflection: Music Recommender Simulation

## Profile Output Comparison

The three standard profiles produced very different recommendation lists, which reveals a lot about how the scoring weights behave.

### High-Energy Pop Fan (genre: pop, mood: happy, energy: 0.9)

Top results were all pop tracks with happy moods and energy above 0.80. The genre and mood bonuses (+3.0 combined) made it nearly impossible for any non-pop song to compete, even one with a perfect energy match. Scores ranged from 3.92 to 3.98 for the top two — extremely close because both songs matched genre and mood and differed only slightly in energy proximity.

**Key observation:** When a user's genre is well-represented in the catalog, the system confidently clusters around that genre and rarely surfaces anything outside it.

### Chill Lofi Listener (genre: lofi, mood: chill, energy: 0.35)

This profile produced the most internally consistent results. All three lofi songs matched genre and mood, earning 3.0 base points each. The tiebreaker was energy proximity — Library Rain (0.35 energy) earned a perfect proximity score of 1.0 and ranked #1. The results felt "correct" intuitively.

**Key observation:** When both genre and mood are present in the catalog with multiple representatives, energy proximity becomes the decisive differentiator. The scoring works as intended.

### Deep Rock (genre: rock, mood: intense, energy: 0.92)

Only two rock songs exist in the catalog (Storm Runner, Thunder Road). Both ranked 1st and 2nd with identical genre + mood bonus scores; energy proximity separated them by a tiny margin. After those two, the system fell back to other intense-mood songs (Electronic, Pop) with no genre match. Scores dropped sharply from ~3.99 to ~1.97 for rank #3.

**Key observation:** With only 2 songs in a genre, a user profile is essentially being served a "best of 2" list for their genre, then a mixed bag. This exposes the catalog underrepresentation problem directly.

---

## Biggest Learning Moment

The scoring logic felt intuitive to write — "give 2 points for genre, 1 for mood" — but the consequences were surprising. Genre's +2.0 weight means it contributes **50% of the max score**. This isn't a bug; it's a design choice. But it means the system will confidently recommend an intense rock song to someone who asked for a relaxed rock song, simply because the genre matched. The weighting encodes a value judgment: genre similarity matters more than emotional match. Real platforms spend enormous effort running A/B tests to learn these weights from actual user behavior rather than hard-coding them.

## How AI Tools Helped (and When to Double-Check Them)

Using AI to design the scoring logic and explain the difference between collaborative and content-based filtering made theoretical concepts concrete quickly. The most useful prompts were specific ones — "explain why this song ranked #1 given these exact weights" — rather than vague ones like "make a recommender." Specific prompts produced code and explanations that matched the actual goal.

Where double-checking mattered: the AI initially suggested a scoring formula that subtracted the energy difference directly from the total score, which would have produced negative scores for songs far from the target energy. Reading the output carefully caught that — the correct formula is `1.0 - |diff|` so energy proximity always contributes between 0 and 1, keeping all scores positive. This was a reminder that AI-generated code needs to be read and reasoned about, not just copy-pasted.

## Surprises About Simple Algorithms

The biggest surprise was how quickly a simple weighted score produces a filter bubble. After running the "High-Energy Pop Fan" profile, every top-5 result was either pop or indie pop. The system has no mechanism to inject variety — it just maximizes the score. This is exactly the problem real recommenders try to solve with diversity injection and reinforcement learning, but our implementation shows why the problem exists in the first place.

## Future Extension Ideas

- **Learnable weights:** Instead of hard-coding genre=2.0, use user feedback (thumbs up/down) to update the weights over time. This turns the system from a rule-based scorer into a lightweight learning system.
- **Diversity penalty:** After ranking, penalize the top-k list if more than 2 songs share the same genre or artist. This injects variety without changing the core scoring logic.
- **Tempo range scoring:** Add a user preference like `target_tempo_bpm: 100` and score songs on tempo proximity the same way energy is scored. This adds a fourth dimension that could meaningfully distinguish workout playlists from study playlists within the same genre.
- **Multi-mood profiles:** Allow users to specify a list of acceptable moods (e.g., `["chill", "focused"]`) instead of a single mood string, so the mood bonus fires for any match in the list.
- **Collaborative layer:** Simulate multiple users running the system, log which songs they "play" (top-ranked results), and use co-occurrence of plays to build a simple collaborative signal on top of the content-based scores.
