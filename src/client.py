import statistics
import sys
import time

import requests

port = sys.argv[1] if len(sys.argv) > 1 else "8100"
url = f"http://127.0.0.1:{port}/invocations"

corps = {
    "dataframe_records": [
        {
            "montant": 8500.0,
            "anciennete": 3,
            "freq_24h": 9,
            "nuit": 1,
        }
    ]
}

reponse = requests.post(url, json=corps, timeout=10)
print("reponse :", reponse.status_code, reponse.json())
reponse.raise_for_status()

for _ in range(10):
    requests.post(url, json=corps, timeout=10).raise_for_status()

latences = []
for _ in range(200):
    debut = time.perf_counter()
    reponse = requests.post(url, json=corps, timeout=10)
    latences.append((time.perf_counter() - debut) * 1000)
    reponse.raise_for_status()

mediane = statistics.median(latences)
p95 = statistics.quantiles(latences, n=20)[18]
print(f"port {port} | mediane : {mediane:.1f} ms | p95 : {p95:.1f} ms")