import time
import math
import random


def log_step(title):
    print("\n" + "=" * 50)
    print(f"[ÉTAPE] {title}")
    print("=" * 50)


def normalize_input(raw_age: str) -> int:
    log_step("Normalisation de l'entrée utilisateur")
    print(f"Entrée brute : {repr(raw_age)}")

    raw_age = raw_age.strip()
    if not raw_age.isdigit():
        raise ValueError("L'IA refuse : ce n'est même pas un nombre 👎")

    age = int(raw_age)
    print(f"Âge interprété comme entier : {age}")
    return age


def age_to_binary_and_hex(age: int):
    log_step("Conversions absurdes (binaire et hexadécimal)")
    binary = bin(age)[2:]  
    hexa = hex(age)     

    print(f"Représentation binaire : {binary}")
    print(f"Représentation hexadécimale : {hexa}")
    return binary, hexa


def extract_features(age: int, binary: str, hexa: str):
    log_step("Extraction de 'features' pour la pseudo IA")

    bits = [int(b) for b in binary]
    sum_bits = sum(bits)
    len_bits = len(bits)
    len_hexa = len(hexa)

    ascii_sum = sum(ord(c) for c in hexa)

    mystic_score = 1.0 / (1.0 + abs(age - 42))

    features = {
        "age": age,
        "sum_bits": sum_bits,
        "len_bits": len_bits,
        "len_hexa": len_hexa,
        "ascii_sum": ascii_sum,
        "mystic_score": mystic_score,
    }

    for k, v in features.items():
        print(f"- {k:12s} = {v}")

    return features


def fake_ai_predict(features: dict) -> float:
    log_step("Prédiction de la fausse IA (totalement bidon)")

    age = features["age"]
    sum_bits = features["sum_bits"]
    len_bits = features["len_bits"]
    ascii_sum = features["ascii_sum"]
    mystic_score = features["mystic_score"]

    x = (
        age * 0.01
        + sum_bits * 0.1
        + len_bits * 0.05
        + ascii_sum * 0.0005
        + mystic_score * 2.0
    )

    prob = 1.0 / (1.0 + math.exp(-x))

    noise = random.uniform(-0.05, 0.05)
    prob = max(0.0, min(1.0, prob + noise))

    print(f"Score brut x           : {x:.4f}")
    print(f"Probabilité (avant bruit) ≈ {1.0 / (1.0 + math.exp(-x)):.4f}")
    print(f"Bruit ajouté           : {noise:+.4f}")
    print(f"Probabilité finale IA  : {prob:.4f}")

    return prob


def committee_vote(age: int, prob: float) -> bool:
    log_step("Comité d'experts IA (simulé avec des if)")
    print(f"Âge reçu           : {age}")
    print(f"Probabilité IA     : {prob:.4f}")

    if age < 0:
        print("Verdict du comité : âge négatif -> rejet immédiat 🚫")
        return False

    if age > 120:
        print("Verdict du comité : > 120 ans ? On n'y croit pas trop... ❌")
        return False

    if age == 42:
        print("Verdict du comité : 42 -> réponse à la grande question de la vie, accepté instantanément ✅")
        return True

    if prob < 0.6:
        print("Verdict du comité : probabilité trop faible -> rejet prudent 🤖")
        return False

    print("Verdict du comité : les chiffres ont l'air humains -> accepté 👍")
    return True


def dramatic_wait():
    log_step("Temps de calcul théâtral (simulation de gros modèle IA)")
    messages = [
        "Connexion à un cluster GPU imaginaire...",
        "Téléchargement des poids de l'IA (dans notre imagination)...",
        "Agrégation des prédictions des 17 modèles ensemblistes...",
        "Calibration des scores...",
    ]
    for msg in messages:
        print(msg)
        time.sleep(0.7)


def rube_goldberg_validation(raw_age: str):
    try:
        age = normalize_input(raw_age)
        binary, hexa = age_to_binary_and_hex(age)
        features = extract_features(age, binary, hexa)
        prob = fake_ai_predict(features)
        dramatic_wait()
        ok = committee_vote(age, prob)
    except ValueError as e:
        print("\n❌ VALIDATION FINALE : ÉCHEC")
        print(f"Raison : {e}")
        return

    print("\n" + "#" * 60)
    if ok:
        print(f"✅ VALIDATION FINALE : L'IA a décidé que {age} ans est un âge plausible 🎉")
    else:
        print(f"❌ VALIDATION FINALE : L'IA doute fortement que {age} ans soit plausible 😬")
    print("#" * 60)


def main():
    print("Bienvenue dans ft_rube_goldberg 🎢")
    print("La machine de validation d'âge la plus inutilement compliquée.\n")

    raw_age = input("Veuillez entrer votre âge : ")
    rube_goldberg_validation(raw_age)


if __name__ == "__main__":
    main()
