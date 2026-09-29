from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import requests

from inf8239_u02.config import ROOT

RAW_URL = (
    "https://raw.githubusercontent.com/Franck-Dernoncourt/"
    "pubmed-rct/master/PubMed_20k_RCT/train.txt"
)


def parse_pubmed_rct(raw_text: str) -> pd.DataFrame:
    rows = []
    for line in raw_text.split("\n"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("###"):
            continue
        if "\t" in line:
            label, text = line.split("\t", 1)
            text = text.strip()
            if text:
                rows.append({"text": text, "label": label.strip().lower()})
    return pd.DataFrame(rows)


def main() -> int:
    print(f"Descargando: {RAW_URL}")
    response = requests.get(RAW_URL, timeout=120)
    response.raise_for_status()

    frame = parse_pubmed_rct(response.text)
    if frame.empty:
        print("El archivo se descargo pero no se pudo parsear ninguna fila", file=sys.stderr)
        return 2

    output = ROOT / "data/raw/dataset.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)

    print(f"Guardado: {output}")
    print(f"Filas: {len(frame)}")
    print(frame["label"].value_counts())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())