# ft_rube_goldberg
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/ElyesLaaribi/goldberg)

This repository contains `ft_rube_goldberg.py`, a Python script that validates a user's age in the most unnecessarily complicated way imaginable. It is a satirical take on over-engineered software solutions and complex "AI" pipelines, transforming a simple task into a multi-stage Rube Goldberg machine.

## How It Works

The script guides the user's input through a labyrinthine validation process. Each step is logged to the console so you can witness the absurdity in real-time.

1.  **Input Normalization**: The raw input string is stripped of whitespace and checked to ensure it's a digit.

2.  **Absurd Conversions**: The age is converted into its binary and hexadecimal representations for subsequent "analysis".

3.  **Pseudo-AI "Feature" Extraction**: A set of nonsensical "features" is derived from the age, including:
    *   The sum of the bits in its binary form.
    *   The length of the binary and hexadecimal strings.
    *   The sum of the ASCII values of the hexadecimal characters.
    *   A "mystic score" based on the age's proximity to 42.

4.  **Fake AI Prediction**: The extracted features are fed into a hardcoded formula to calculate a "plausibility probability". A small amount of random noise is added to make the process seem less deterministic.

5.  **Dramatic Wait**: The script simulates the intense workload of a large AI model by printing status messages and pausing, adding a theatrical flair to the calculation.

6.  **The "Expert Committee" Vote**: A final decision is made by a series of `if` statements that act as a committee of experts. It handles edge cases (e.g., negative age, age > 120), provides a special verdict for the age 42, and uses the AI's probability score for its final judgment.

## How to Use

To run this magnificent validation machine, clone the repository and execute the Python script.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ElyesLaaribi/goldberg.git
    ```

2.  **Navigate to the directory:**
    ```sh
    cd goldberg
    ```

3.  **Run the script:**
    ```sh
    python3 ft_rube_goldberg.py
    ```

You will then be prompted to enter an age.

## Example Usage

```
$ python3 ft_rube_goldberg.py
Bienvenue dans ft_rube_goldberg 🎢
La machine de validation d'âge la plus inutilement compliquée.

Veuillez entrer votre âge : 30

==================================================
[ÉTAPE] Normalisation de l'entrée utilisateur
==================================================
Entrée brute : '30'
Âge interprété comme entier : 30

==================================================
[ÉTAPE] Conversions absurdes (binaire et hexadécimal)
==================================================
Représentation binaire : 11110
Représentation hexadécimale : 0x1e

==================================================
[ÉTAPE] Extraction de 'features' pour la pseudo IA
==================================================
- age          = 30
- sum_bits     = 4
- len_bits     = 5
- len_hexa     = 4
- ascii_sum    = 279
- mystic_score = 0.07692307692307693

==================================================
[ÉTAPE] Prédiction de la fausse IA (totalement bidon)
==================================================
Score brut x           : 1.2433
Probabilité (avant bruit) ≈ 0.7762
Bruit ajouté           : +0.0381
Probabilité finale IA  : 0.8143

==================================================
[ÉTAPE] Temps de calcul théâtral (simulation de gros modèle IA)
==================================================
Connexion à un cluster GPU imaginaire...
Téléchargement des poids de l'IA (dans notre imagination)...
Agrégation des prédictions des 17 modèles ensemblistes...
Calibration des scores...

==================================================
[ÉTAPE] Comité d'experts IA (simulé avec des if)
==================================================
Âge reçu           : 30
Probabilité IA     : 0.8143
Verdict du comité : les chiffres ont l'air humains -> accepté 👍

############################################################
✅ VALIDATION FINALE : L'IA a décidé que 30 ans est un âge plausible 🎉
############################################################
