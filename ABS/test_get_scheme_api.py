import requests
import pytest

# Define the base URL and query parameters
BASE_URL = "https://input-backend.api.dehat.co/schemes/12642/v2"
PARAMS = {
    "type": "ABS",
    "app_code": "dehaat_business",
    "lang": "en"
}

# Define headers from your cURL command
HEADERS = {
    "api-request-trace-id": "d70f1aeb-2d34-4796-9592-608a1ff0ba98",
    "X-Request-ID": "d70f1aeb-2d34-4796-9592-608a1ff0ba98",
    "X-APP-VERSION": "968",
    "deviceId": "60731423d5685a51",
    "googleAdId": "998e1c3c-cfcc-4f37-8ace-2db98f43e7fb",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2ZXFUMWswUGZpUWNhN0RLcWpKWjZEZ0NwWTAwanZIUHpwbk5ZIn0.eyJleHAiOjE3NjM4ODEzOTEsImlhdCI6MTc2MzQ0OTM5MSwiYXV0aF90aW1lIjoxNzYzNDQ5MzkwLCJqdGkiOiJjZTEwZTI4Zi03MGU5LTQwZDUtYjJmNy05NmYxMWIzYWIyOGIiLCJpc3MiOiJodHRwczovL29pZGMuZGVoYXQuY28vYXV0aC9yZWFsbXMvZGVoYWF0IiwiYXVkIjpbImNvcmUtYXBpIiwia2hldGkiLCJvZG9vIiwiaW5wdXQtYmFja2VuZC1kamFuZ28tYWRtaW4iLCJpZGVudGl0eS1tYXN0ZXIiLCJhY2NvdW50Il0sInN1YiI6ImFlZDQ0YTY2LTI5YzEtNDc5Ny04MmRmLTcyZmFmMjlmOWY2OCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJ1c2luZXNzYXBwIiwibm9uY2UiOiJFR2RjU1c1dTJwcWJCUVp0YjlOMXBnIiwic2Vzc2lvbl9zdGF0ZSI6ImFmZGVlYTU5LTAzYjMtNDE1OS04MTZlLWMzNTU1Yjk1NmM1ZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1kZWhhYXQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBtb2JpbGUgaWRlbnRpdHktbWFzdGVyLWF1ZGllbmNlIHByb2ZpbGUgZW1haWwgaW5wdXQtYmFja2VuZC1hdWRpZW5jZSBjc2MiLCJzaWQiOiJhZmRlZWE1OS0wM2IzLTQxNTktODE2ZS1jMzU1NWI5NTZjNWUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJBc2hvayBLdW1hciBNYW5kYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmNmEzY2Q4NS0yYjBmLTQxNWUtYTgwOC1mZWVmMjNkYTNlNDUiLCJnaXZlbl9uYW1lIjoiQXNob2sgS3VtYXIiLCJtb2JpbGVfbnVtYmVyIjoiNzc4Mjk0ODgzMCIsImZhbWlseV9uYW1lIjoiTWFuZGFsIiwiZW1haWwiOiJuYW5kdGVtcEBhZ3Jldm9sdXRpb24uaW4ifQ.IRveR7qzsHwKzMXAPXqxg-Q3J_dqtJVFBS8NL3JDCdVzSCzxPwYox7kDP9B87UakSjcB35zx7YMMAt76EVM7UjX-05sf2Y-AzOZo_-vd7-rzYPNKP1lIobVMRMSpHnHWOtyxPfAv6yjfqQA3EGTV_9uuLQ7BMYehHJlnM4wKaIwyYfFHRALNIvTKhPw9KFPY0W5c8FAM82bwDy6lE9vu1f3cxOuim4lpQxlwfCNNEahvCvxDT19WANsyGzHk-9yMEWgexhu24-hkeXEotRiFC4nfVV-8lAPCeDH8GrydeuSjpggm3xSULQ6Mpiu3rxFIPrRWSbfS4pA7_o7ybl_8ng"
}

@pytest.mark.api
def test_get_scheme_details():
    """Test GET /schemes/{id}/v2 endpoint with error handling and assertions"""

    try:
        response = requests.get(BASE_URL, headers=HEADERS, params=PARAMS, timeout=10)
        
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"

        # ✅ 2. Parse JSON safely
        json_data = response.json()
        print("Response JSON:", json_data)

        # ✅ 3. Validate top-level structure
        assert "data" in json_data, "Missing 'data' key in response"
        data = json_data["data"]

        # ✅ 4. Validate key fields exist
        expected_keys = [
            "id", "name", "description", "status", 
            "booking_start_date", "booking_end_date", 
            "ordering_start_date", "ordering_end_date", 
            "products", "slabs"
        ]

        for key in expected_keys:
            assert key in data, f"Missing key: '{key}' in response"

        # ✅ 5. Validate important values
        assert data["id"] == "12642", f"Expected id '12642', got {data['id']}"
        assert data["status"] == "booking", f"Expected status 'booking', got {data['status']}"
        assert isinstance(data["slabs"], list) and len(data["slabs"]) > 0, "Slabs list is empty"
        assert isinstance(data["products"], list) and len(data["products"]) > 0, "Products list is empty"

        # ✅ 6. Print summary for logs
        print(f"✅ Scheme '{data['name']}' retrieved successfully with {len(data['slabs'])} slabs and {len(data['products'])} products.")

    except requests.exceptions.Timeout:
        pytest.fail("⏰ Request timed out")
    except requests.exceptions.ConnectionError:
        pytest.fail("🚫 Connection error - check endpoint")
    except ValueError:
        pytest.fail("❌ Failed to parse JSON response")
    except AssertionError as e:
        pytest.fail(f"❌ Assertion failed: {e}")
    except Exception as e:
        pytest.fail(f"⚠️ Unexpected error: {e}")
