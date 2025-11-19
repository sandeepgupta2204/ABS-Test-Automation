import requests
import pytest
import json

BASE_URL = "https://input-backend.api.dehat.co/booking-prerequisites/v1"
PARAMS = {
    "app_code": "dehaat_business",
    "lang": "en"
}

HEADERS = {
    "api-request-trace-id": "71e2e50f-4521-4c28-bc63-a52d2e0659ce",
    "X-Request-ID": "71e2e50f-4521-4c28-bc63-a52d2e0659ce",
    "X-APP-VERSION": "968",
    "deviceId": "60731423d5685a51",
    "googleAdId": "998e1c3c-cfcc-4f37-8ace-2db98f43e7fb",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2ZXFUMWswUGZpUWNhN0RLcWpKWjZEZ0NwWTAwanZIUHpwbk5ZIn0.eyJleHAiOjE3NjM4ODEzOTEsImlhdCI6MTc2MzQ0OTM5MSwiYXV0aF90aW1lIjoxNzYzNDQ5MzkwLCJqdGkiOiJjZTEwZTI4Zi03MGU5LTQwZDUtYjJmNy05NmYxMWIzYWIyOGIiLCJpc3MiOiJodHRwczovL29pZGMuZGVoYXQuY28vYXV0aC9yZWFsbXMvZGVoYWF0IiwiYXVkIjpbImNvcmUtYXBpIiwia2hldGkiLCJvZG9vIiwiaW5wdXQtYmFja2VuZC1kamFuZ28tYWRtaW4iLCJpZGVudGl0eS1tYXN0ZXIiLCJhY2NvdW50Il0sInN1YiI6ImFlZDQ0YTY2LTI5YzEtNDc5Ny04MmRmLTcyZmFmMjlmOWY2OCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJ1c2luZXNzYXBwIiwibm9uY2UiOiJFR2RjU1c1dTJwcWJCUVp0YjlOMXBnIiwic2Vzc2lvbl9zdGF0ZSI6ImFmZGVlYTU5LTAzYjMtNDE1OS04MTZlLWMzNTU1Yjk1NmM1ZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1kZWhhYXQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBtb2JpbGUgaWRlbnRpdHktbWFzdGVyLWF1ZGllbmNlIHByb2ZpbGUgZW1haWwgaW5wdXQtYmFja2VuZC1hdWRpZW5jZSBjc2MiLCJzaWQiOiJhZmRlZWE1OS0wM2IzLTQxNTktODE2ZS1jMzU1NWI5NTZjNWUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJBc2hvayBLdW1hciBNYW5kYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmNmEzY2Q4NS0yYjBmLTQxNWUtYTgwOC1mZWVmMjNkYTNlNDUiLCJnaXZlbl9uYW1lIjoiQXNob2sgS3VtYXIiLCJtb2JpbGVfbnVtYmVyIjoiNzc4Mjk0ODgzMCIsImZhbWlseV9uYW1lIjoiTWFuZGFsIiwiZW1haWwiOiJuYW5kdGVtcEBhZ3Jldm9sdXRpb24uaW4ifQ.IRveR7qzsHwKzMXAPXqxg-Q3J_dqtJVFBS8NL3JDCdVzSCzxPwYox7kDP9B87UakSjcB35zx7YMMAt76EVM7UjX-05sf2Y-AzOZo_-vd7-rzYPNKP1lIobVMRMSpHnHWOtyxPfAv6yjfqQA3EGTV_9uuLQ7BMYehHJlnM4wKaIwyYfFHRALNIvTKhPw9KFPY0W5c8FAM82bwDy6lE9vu1f3cxOuim4lpQxlwfCNNEahvCvxDT19WANsyGzHk-9yMEWgexhu24-hkeXEotRiFC4nfVV-8lAPCeDH8GrydeuSjpggm3xSULQ6Mpiu3rxFIPrRWSbfS4pA7_o7ybl_8ng"
}

PAYLOAD = {
    "products": [{"product_template_id": "2817", "weight": "10"}],
    "scheme_id": "12642"
}


@pytest.mark.api
def test_post_booking_prerequisites():
    """Test POST /booking-prerequisites/v1 API with dynamic validation"""

    response = requests.post(BASE_URL, headers=HEADERS, params=PARAMS, json=PAYLOAD, timeout=10)

    # ✅ 1. HTTP status check
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"

    json_data = response.json()
    print("Response JSON:", json.dumps(json_data, indent=2))

    # ✅ 2. Basic checks
    assert "data" in json_data, "Missing 'data' key in response"
    data = json_data["data"]

    # ✅ 3. Expected keys (from actual API output)
    expected_keys = ["amount", "slab_id", "prev_booking_amount"]
    missing_keys = [k for k in expected_keys if k not in data]
    assert not missing_keys, f"Missing keys in response: {missing_keys}"

    # ✅ 4. Value assertions
    assert float(data["amount"]) >= 0, f"Amount should be positive, got {data['amount']}"
    assert isinstance(data["slab_id"], int), f"slab_id should be int, got {type(data['slab_id'])}"
    assert data["prev_booking_amount"].isdigit(), "prev_booking_amount should be numeric string"

    print(f"✅ API passed: slab_id={data['slab_id']}, amount={data['amount']}, prev_booking_amount={data['prev_booking_amount']}")