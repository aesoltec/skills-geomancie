#!/usr/bin/env python3
"""Calculateur et vérificateur déterministe d'écu géomantique (Takht à 16 maisons).

Usage:
    python takht.py 1111 2121 2112 1222 [--json]
"""

from __future__ import annotations

import json
import sys
from typing import Dict, List, Tuple

FIGURES: Dict[str, Tuple[str, str, str]] = {
    "1111": ("al-Ṭarīq", "Via", "Taliki"),
    "2121": ("al-Qabḍ al-dāḫil", "Acquisitio", "Ousmane / Mori Sumana"),
    "2212": ("al-Bayāḍ", "Albus", "Albayada"),
    "2122": ("al-Ḥumra", "Rubeus", "Lomara / Oumar"),
    "1221": ("al-ʿAqla", "Carcer", "Solomana / Mansa Solomani"),
    "2111": ("al-ʿAtaba al-dāḫila", "Caput Draconis", "Malidjou"),
    "1112": ("al-ʿAtaba al-ḫāriǧa", "Cauda Draconis", "Lawsana / Lusiné"),
    "2211": ("al-Nuṣra al-dāḫila", "Fortuna Major", "Nouhou / Nunkoro"),
    "2222": ("al-Ǧamāʿa", "Populus", "Moussa / Jamati Moussa"),
    "1212": ("al-Qabḍ al-ḫāriǧ", "Amissio", "Inzan / N'gansa"),
    "1211": ("Naqī al-ḫadd", "Puella", "Tontigui"),
    "1121": ("al-Ǧūdala", "Puer", "Janfa Almamy"),
    "2112": ("al-Iǧtimāʿ", "Conjunctio", "Badra Ali"),
    "1222": ("al-Laḥyān", "Laetitia", "Adama"),
    "2221": ("al-Inkīs", "Tristitia", "Mangouchi / Mankusi"),
    "1122": ("al-Nuṣra al-ḫāriǧa", "Fortuna Minor", "Kalalaw"),
}


def validate_code(code: str) -> str:
    if len(code) != 4 or any(c not in ("1", "2") for c in code):
        raise ValueError(f"Code figure invalide '{code}': attendu 4 chiffres parmi 1 et 2.")
    return code


def copulate(a: str, b: str) -> str:
    """Addition géomantique modulo 2 rang par rang (1+1=2, 2+2=2, 1+2=1)."""
    out = []
    for ca, cb in zip(a, b):
        s = int(ca) + int(cb)
        out.append("2" if s % 2 == 0 else "1")
    return "".join(out)


def count_odd_ranks(code: str) -> int:
    return sum(1 for c in code if c == "1")


def total_points(code: str) -> int:
    return sum(int(c) for c in code)


def build_takht(m1: str, m2: str, m3: str, m4: str) -> dict:
    mothers = [validate_code(m) for m in (m1, m2, m3, m4)]

    # M5-M8: lecture horizontale rang par rang (Feu=0, Air=1, Eau=2, Terre=3)
    daughters = [
        "".join(mothers[j][rank] for j in range(4))
        for rank in range(4)
    ]

    # M9-M12: copulation par paires
    nieces = [
        copulate(mothers[0], mothers[1]),
        copulate(mothers[2], mothers[3]),
        copulate(daughters[0], daughters[1]),
        copulate(daughters[2], daughters[3]),
    ]

    # M13-M14: Témoins
    m13 = copulate(nieces[0], nieces[1])
    m14 = copulate(nieces[2], nieces[3])

    # M15: Juge
    m15 = copulate(m13, m14)
    judge_valid = (total_points(m15) % 2 == 0)

    # M16: Sentence
    m16 = copulate(m15, mothers[0])

    houses = mothers + daughters + nieces + [m13, m14, m15, m16]

    # Part de Fortune (Al-Sahm) : somme des rangs impairs '1' sur les 16 maisons
    total_odd = sum(count_odd_ranks(h) for h in houses)
    sahm_index = 16 if (total_odd % 16 == 0) else (total_odd % 16)

    # Passations de M1
    m1_repetitions = [idx + 1 for idx, h in enumerate(houses) if h == mothers[0]]

    return {
        "valid_judge": judge_valid,
        "houses": [
            {
                "index": i + 1,
                "label": f"M{i + 1}",
                "code": code,
                "arabic": FIGURES[code][0],
                "latin": FIGURES[code][1],
                "mande": FIGURES[code][2],
                "points": total_points(code),
            }
            for i, code in enumerate(houses)
        ],
        "al_sahm": {
            "total_odd_ranks": total_odd,
            "house_index": sahm_index,
            "code": houses[sahm_index - 1],
        },
        "m1_passations": m1_repetitions,
    }


def format_shield(takht: dict) -> str:
    h = {item["index"]: item for item in takht["houses"]}

    def cell(idx: int) -> str:
        item = h[idx]
        return f"M{idx}:{item['code']}({item['latin'][:7]})"

    lines = [
        f"Juge M15 valide : {'OUI' if takht['valid_judge'] else 'NON (INVALIDE)'}",
        "",
        "Bouclier du Takht (M1 à droite) :",
        "  " + "  ".join(cell(i) for i in range(8, 0, -1)),
        "          " + "  ".join(cell(i) for i in range(12, 8, -1)),
        f"                  {cell(14)}      {cell(13)}",
        f"                          {cell(15)}",
        f"                          {cell(16)}",
        "",
        f"Al-Sahm (Part de Fortune) : M{takht['al_sahm']['house_index']} "
        f"({takht['al_sahm']['total_odd_ranks']} rangs impairs)",
        f"Passations de M1 : {', '.join('M' + str(i) for i in takht['m1_passations'])}",
    ]
    return "\n".join(lines)


def main() -> int:
    args = sys.argv[1:]
    as_json = False
    if "--json" in args:
        as_json = True
        args = [a for a in args if a != "--json"]

    if len(args) != 4:
        print("Usage: python takht.py <M1> <M2> <M3> <M4> [--json]", file=sys.stderr)
        return 1

    try:
        result = build_takht(args[0], args[1], args[2], args[3])
    except ValueError as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        return 2

    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_shield(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
