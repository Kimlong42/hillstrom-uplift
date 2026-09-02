import urllib.request
from pathlib import Path

import pandas as pd

URL = (
    "http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_"
    "E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"
)
ROOT = Path(__file__).resolve().parents[2]  # src/hillstrom_uplift/data.py → gốc repo
RAW = ROOT / "data" / "hillstrom.csv"


def download(force: bool = False) -> Path:
    if not RAW.exists() or force:
        RAW.parent.mkdir(exist_ok=True)
        urllib.request.urlretrieve(URL, RAW)
    return RAW


def load() -> pd.DataFrame:
    df = pd.read_csv(download())
    df["treatment"] = df["segment"].map(
        {
            "No E-Mail": "control",
            "Mens E-Mail": "mens",
            "Womens E-Mail": "womens",
        }
    )
    return df
