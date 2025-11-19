import requests
import pytest
import json

# --- API Configuration ---
BASE_URL = "https://input-backend.api.dehat.co/payments/transactions"
PARAMS = {
    "app_code": "dehaat_business",
    "lang": "en"
}

# --- Headers from your cURL ---
HEADERS = {
    "api-request-trace-id": "d95a28db-c531-40d6-8b77-a33ef18549a5",
    "X-Request-ID": "d95a28db-c531-40d6-8b77-a33ef18549a5",
    "X-APP-VERSION": "968",
    "deviceId": "60731423d5685a51",
    "googleAdId": "998e1c3c-cfcc-4f37-8ace-2db98f43e7fb",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2ZXFUMWswUGZpUWNhN0RLcWpKWjZEZ0NwWTAwanZIUHpwbk5ZIn0.eyJleHAiOjE3NjM4ODEzOTEsImlhdCI6MTc2MzQ0OTM5MSwiYXV0aF90aW1lIjoxNzYzNDQ5MzkwLCJqdGkiOiJjZTEwZTI4Zi03MGU5LTQwZDUtYjJmNy05NmYxMWIzYWIyOGIiLCJpc3MiOiJodHRwczovL29pZGMuZGVoYXQuY28vYXV0aC9yZWFsbXMvZGVoYWF0IiwiYXVkIjpbImNvcmUtYXBpIiwia2hldGkiLCJvZG9vIiwiaW5wdXQtYmFja2VuZC1kamFuZ28tYWRtaW4iLCJpZGVudGl0eS1tYXN0ZXIiLCJhY2NvdW50Il0sInN1YiI6ImFlZDQ0YTY2LTI5YzEtNDc5Ny04MmRmLTcyZmFmMjlmOWY2OCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJ1c2luZXNzYXBwIiwibm9uY2UiOiJFR2RjU1c1dTJwcWJCUVp0YjlOMXBnIiwic2Vzc2lvbl9zdGF0ZSI6ImFmZGVlYTU5LTAzYjMtNDE1OS04MTZlLWMzNTU1Yjk1NmM1ZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1kZWhhYXQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBtb2JpbGUgaWRlbnRpdHktbWFzdGVyLWF1ZGllbmNlIHByb2ZpbGUgZW1haWwgaW5wdXQtYmFja2VuZC1hdWRpZW5jZSBjc2MiLCJzaWQiOiJhZmRlZWE1OS0wM2IzLTQxNTktODE2ZS1jMzU1NWI5NTZjNWUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJBc2hvayBLdW1hciBNYW5kYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmNmEzY2Q4NS0yYjBmLTQxNWUtYTgwOC1mZWVmMjNkYTNlNDUiLCJnaXZlbl9uYW1lIjoiQXNob2sgS3VtYXIiLCJtb2JpbGVfbnVtYmVyIjoiNzc4Mjk0ODgzMCIsImZhbWlseV9uYW1lIjoiTWFuZGFsIiwiZW1haWwiOiJuYW5kdGVtcEBhZ3Jldm9sdXRpb24uaW4ifQ.IRveR7qzsHwKzMXAPXqxg-Q3J_dqtJVFBS8NL3JDCdVzSCzxPwYox7kDP9B87UakSjcB35zx7YMMAt76EVM7UjX-05sf2Y-AzOZo_-vd7-rzYPNKP1lIobVMRMSpHnHWOtyxPfAv6yjfqQA3EGTV_9uuLQ7BMYehHJlnM4wKaIwyYfFHRALNIvTKhPw9KFPY0W5c8FAM82bwDy6lE9vu1f3cxOuim4lpQxlwfCNNEahvCvxDT19WANsyGzHk-9yMEWgexhu24-hkeXEotRiFC4nfVV-8lAPCeDH8GrydeuSjpggm3xSULQ6Mpiu3rxFIPrRWSbfS4pA7_o7ybl_8ng"
}

# --- Request Body ---
PAYLOAD = {
    "total_amount": "4000",
    "channel": "Mobile",
    "platform": "DBA",
    "lob": "Input",
    "entity_id": "16271",
    "entity_type": "abs_booking"
}


@pytest.mark.api
def test_post_payment_transaction():
    """Test POST /payments/transactions API with full validation"""

    try:
        response = requests.post(BASE_URL, headers=HEADERS, params=PARAMS, json=PAYLOAD, timeout=10)
        print(f"HTTP Status: {response.status_code}")

        # ✅ Allow 200 or 201
        assert response.status_code in [200, 201], f"Expected 200/201, got {response.status_code}"

        json_data = response.json()
        print("Response JSON:", json.dumps(json_data, indent=2))

        # ✅ Validate structure
        assert isinstance(json_data, dict), "Response is not a valid JSON object"
        assert "data" in json_data, "Missing 'data' in response"

        data = json_data["data"]

        # ✅ Key checks
        expected_keys = ["transaction_id", "status", "payment_mode", "total_amount"]
        missing_keys = [key for key in expected_keys if key not in data]
        if missing_keys:
            print(f"⚠️ Missing keys in response: {missing_keys}")

        # ✅ Logical checks
        if "total_amount" in data:
            assert float(data["total_amount"]) == float(PAYLOAD["total_amount"]), (
                f"Expected amount {PAYLOAD['total_amount']}, got {data['total_amount']}"
            )
        if "status" in data:
            assert data["status"].lower() in ["success", "pending", "completed"], f"Unexpected status: {data['status']}"

        print("✅ Payment Transaction API executed successfully!")

    except AssertionError as e:
        pytest.fail(f"❌ Assertion failed: {e}")
    except requests.exceptions.Timeout:
        pytest.fail("⏰ Request timed out")
    except requests.exceptions.ConnectionError:
        pytest.fail("🚫 Connection error - check endpoint or network")
    except ValueError:
        pytest.fail("❌ Failed to parse JSON response")
    except Exception as e:
        pytest.fail(f"⚠️ Unexpected error: {e}")