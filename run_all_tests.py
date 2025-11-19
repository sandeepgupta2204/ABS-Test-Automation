import subprocess
import sys
import os

# --- Colors for readability ---
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


# --- Folder to test mapping (add future modules here) ---
MODULE_PATHS = {
    "ABS": "ABS",
}

# --- Test execution order per module ---
TEST_ORDER = {
    "ABS": [
        "test_get_scheme_api.py",
        "test_get_scheme_details_api.py",
        "test_post_booking_prerequisites_api.py",
        "test_post_booking_order_api.py",
        "test_post_cart_api.py",
        "test_post_validate_cart_api.py",
        "test_post_delivery_slots_api.py",
        "test_post_order_request_api.py", 
        "test_post_payment_transaction_api.py",
    ],
}


def run_test_file(test_file):
    """Runs a single pytest file and prints its result clearly."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}🚀 Running Test: {test_file}{Colors.ENDC}")
    print("-" * 80)
    
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v", test_file],
        capture_output=True,
        text=True
    )

    # Print pytest output
    print(result.stdout)

    if result.returncode == 0:
        print(f"{Colors.OKGREEN}✅ {test_file} PASSED successfully.{Colors.ENDC}")
        return True
    else:
        print(f"{Colors.FAIL}❌ {test_file} FAILED. Check details above.{Colors.ENDC}")
        return False


def run_module_tests(module_name):
    """Runs all test files inside the selected module in defined business order."""
    module_path = MODULE_PATHS.get(module_name.upper())

    if not module_path or not os.path.exists(module_path):
        print(f"{Colors.FAIL}⚠️ Module '{module_name}' not found!{Colors.ENDC}")
        return

    print(f"{Colors.BOLD}{Colors.OKBLUE}=== Starting API Tests for Module: {module_name} ==={Colors.ENDC}\n")

    # Get defined order, or fallback to all test_*.py files
    ordered_tests = TEST_ORDER.get(module_name.upper())
    if ordered_tests:
        test_files = [os.path.join(module_path, f) for f in ordered_tests if os.path.exists(os.path.join(module_path, f))]
    else:
        # fallback alphabetical
        test_files = sorted(
            [os.path.join(module_path, f) for f in os.listdir(module_path) if f.startswith("test_") and f.endswith(".py")]
        )

    if not test_files:
        print(f"{Colors.WARNING}⚠️ No test files found inside {module_path}{Colors.ENDC}")
        return

    passed, failed = 0, 0

    for test_file in test_files:
        success = run_test_file(test_file)
        if success:
            passed += 1
        else:
            failed += 1

    print(f"\n{Colors.BOLD}{Colors.OKBLUE}=== SUMMARY for {module_name} ==={Colors.ENDC}")
    print(f"{Colors.OKGREEN}✅ Passed: {passed}{Colors.ENDC}")
    print(f"{Colors.FAIL}❌ Failed: {failed}{Colors.ENDC}")
    print(f"{Colors.BOLD}Total: {passed + failed} tests executed.{Colors.ENDC}\n")

    if failed == 0:
        print(f"{Colors.OKGREEN}🎉 All {module_name} tests passed successfully!{Colors.ENDC}")
    else:
        print(f"{Colors.WARNING}⚠️ Some {module_name} tests failed. Check logs above.{Colors.ENDC}")


def main():
    """Main entry point to select and run module tests."""
    print(f"{Colors.BOLD}{Colors.OKBLUE}=== AVAILABLE MODULES ==={Colors.ENDC}")
    for module in MODULE_PATHS:
        print(f"➡️  {module}")

    module_choice = input(f"\n{Colors.BOLD}Enter module name to test (e.g., ABS): {Colors.ENDC}").strip()
    run_module_tests(module_choice)


if __name__ == "__main__":
    main()
