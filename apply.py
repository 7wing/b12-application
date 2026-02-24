import json, hmac, hashlib, requests
from datetime import datetime, timezone

payload = {
    "action_run_link": "https://github.com/7wing/b12-application/actions/runs/22347792819",
    "email": "marthakamau0001@gmail.com",
    "name": "Martha Kamau",
    "repository_link": "https://github.com/7wing/b12-application",
    "resume_link": "https://docs.google.com/document/d/17cHj30eMh56UWQxoSVGHKVnUomznvM_8TaWuU7wZdnk/edit?usp=sharing",
    "timestamp": datetime.now(timezone.utc).isoformat()
}

body = json.dumps(payload, separators=(',', ':'), sort_keys=True)
signature = hmac.new(
    key=b"hello-there-from-b12",
    msg=body.encode("utf-8"),
    digestmod=hashlib.sha256
).hexdigest()

headers = {"X-Signature-256": f"sha256={signature}"}
response = requests.post("https://b12.io/apply/submission", data=body, headers=headers)

print(response.text)
