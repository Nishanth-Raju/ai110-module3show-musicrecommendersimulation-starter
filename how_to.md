📝 Project Specification: Music Recommender Simulation

This document outlines every task required for the AI110 Module 4 Project. Use this as a checklist for your development environment.
Phase 1: Understanding the Problem

    [ ] Setup: Fork the project repository on GitHub and clone it to your local machine.

    [ ] Research: Use Copilot Chat to summarize the difference between collaborative filtering and content-based filtering.

    [ ] Data Analysis: Identify main data types (likes, tempo, mood, etc.) used by platforms like Spotify.

    [ ] Feature Selection: Analyze data/songs.csv and use AI to determine which features (e.g., valence, energy) are best for a content-based recommender.

    [ ] Scoring Logic Design: Formulate a math-based "Scoring Rule" for numerical features (proximity-based scoring).

    [ ] Ranking Logic Design: Define the difference between a "Scoring Rule" (individual) and a "Ranking Rule" (list-based).

    [ ] Documentation: Update README.md (How The System Works) and list specific features for Song and UserProfile objects.

Phase 2: Designing the Simulation

    [ ] Dataset Expansion: Use AI to generate 5–10 additional songs in valid CSV format with existing headers.

    [ ] Feature Engineering: (Optional) Add new numerical features like "Danceability" or "Acousticness."

    [ ] User Profile Creation: Define a dictionary containing target values for your chosen features (e.g., target_energy: 0.8).

    [ ] Profile Critique: Use AI to check if your profile is diverse enough to distinguish between genres.

    [ ] Algorithm Recipe Finalization: Set point weights:

        Match Genre: +2.0

        Match Mood: +1.0

        Numerical Similarity: Points based on energy proximity.

    [ ] Visualization: Generate a Mermaid.js flowchart of the data flow: Input → Process → Output.

    [ ] Bias Documentation: Note potential biases (e.g., over-prioritizing genre) in README.md.

Phase 3: Implementation

    [ ] File Setup: Initialize src/recommender.py.

    [ ] Function - load_songs: * Use Python csv module.

        Convert numerical strings (energy, tempo) into float or int.

    [ ] Function - score_song: * Implement logic for genre, mood, and numerical features.

        Must return both a numeric score and a list of "reasons" (e.g., "genre match (+2.0)").

    [ ] Function - recommend_songs: * Loop through all songs and apply score_song.

        Sort the list and return the top k results.

    [ ] CLI Implementation: Update src/main.py to display a clean, readable terminal layout (Title, Score, Reasons).

    [ ] Verification: Run python -m src.main and take a screenshot of the output for README.md.

    [ ] Documentation: Add 1-line docstrings to all functions and push changes to GitHub.

Phase 4: Evaluate and Explain

    [ ] Stress Testing: Define 3 distinct user profiles (e.g., "High-Energy Pop," "Chill Lofi," "Deep Rock").

    [ ] Edge Cases: Test "adversarial" profiles (e.g., conflicting preferences like high energy + sad mood).

    [ ] Result Capture: Take screenshots of recommendations for all 3 profiles for README.md.

    [ ] Logic Investigation: Use AI to explain why a specific song ranked #1 based on your weights.

    [ ] Data Experiment: Run one experiment (e.g., double the energy weight or remove the mood check).

    [ ] Bias Analysis: Identify "filter bubbles" in model_card.md (3–5 sentences).

    [ ] Reflection: Compare profile outputs in reflection.md.

Phase 5: Reflection and Model Card

    [ ] Model Card (model_card.md): Complete all sections:

        Model Name, Goal, Data Used, Algorithm Summary, Biases, Evaluation, Intended Use, Improvements.

    [ ] Personal Reflection: Document:

        Biggest learning moment.

        Experience using AI tools.

        Surprises regarding simple algorithms.

        Future extension ideas.