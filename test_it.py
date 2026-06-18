from k_vegan_vision import KVeganChecker

tests = [
    ("밀가루, 설탕, 멸치액젓, 소금", "❌"),
    ("밀가루, 설탕, 소금, 참기름", "✅"),
    ("쌀, 콩, 돼지고기", "❌"),
    ("양배추, 당근, 감자", "✅"),
]

print("\n🧪 K-VEGAN TESTS\n")
checker = KVeganChecker()
passed = 0

for i, (text, expected) in enumerate(tests, 1):
    result = checker.check_text(text)
    is_pass = expected in result['status']
    status_emoji = result['status'].split()[0]
    print(f"Test {i}: {text[:40]}")
    print(f"  Expected: {expected}  Got: {status_emoji}  {'✅ PASS' if is_pass else '❌ FAIL'}\n")
    if is_pass:
        passed += 1

print(f"📊 RESULTS: {passed}/{len(tests)} passed\n")
if passed == len(tests):
    print("✅ ALL TESTS PASSED!\n")
