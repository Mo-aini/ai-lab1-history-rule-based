# Lab 1 Task 2 - extended rule based checker
# I kept the 2 original conditions from 1.4 and added attendance and credit hours.
# The thresholds are my own assumptions for the lab, not a real policy.

# thresholds
MIN_SCORE = 70          # original
MIN_ATTENDANCE = 75     # percent, new condition C3
MIN_CREDIT_HOURS = 12   # new condition C4


def original_rule(score, documents_complete):
    return "Review" if documents_complete and score >= 70 else "Hold"


def check_conditions(score, documents_complete, attendance, credit_hours):
    return {
        "documents_complete": (documents_complete,
                               "documents complete" if documents_complete else "documents incomplete"),
        "score_ok": (score >= MIN_SCORE,
                     "score %s %s %d" % (score, ">=" if score >= MIN_SCORE else "<", MIN_SCORE)),
        "attendance_ok": (attendance >= MIN_ATTENDANCE,
                          "attendance %s%% %s %d%%" % (attendance, ">=" if attendance >= MIN_ATTENDANCE else "<", MIN_ATTENDANCE)),
        "credit_load_ok": (credit_hours >= MIN_CREDIT_HOURS,
                           "credit hours %s %s %d" % (credit_hours, ">=" if credit_hours >= MIN_CREDIT_HOURS else "<", MIN_CREDIT_HOURS)),
    }


def rule_based_extended(score, documents_complete, attendance, credit_hours):
    results = check_conditions(score, documents_complete, attendance, credit_hours)
    failed = [name + ": " + why for name, (ok, why) in results.items() if not ok]
    if failed:
        return "Hold", "failed " + "; ".join(failed)
    return "Review", "all 4 conditions met (" + "; ".join(why for _, why in results.values()) + ")"


# 4 test cases: one pass, one fail for each new condition, and the score boundary
# (name, score, documents_complete, attendance, credits, expected, why I chose it)
TEST_CASES = [
    ("T1_pass", 82, True, 90, 15, "Review",
     "control case: every condition comfortably satisfied"),
    ("T2_attendance_fails", 85, True, 60, 15, "Hold",
     "isolates new condition C3: only attendance is below its threshold"),
    ("T3_credit_load_fails", 88, True, 92, 9, "Hold",
     "isolates new condition C4: only credit hours are below the threshold"),
    ("T4_score_boundary", 70, True, 80, 15, "Review",
     "threshold boundary: score exactly 70 must pass because the rule uses >="),
]


def run_tests():
    print("Thresholds are synthetic lab assumptions: score >= %d, attendance >= %d%%, credit hours >= %d, documents complete."
          % (MIN_SCORE, MIN_ATTENDANCE, MIN_CREDIT_HOURS))
    print("case | input (score, complete, attendance, credits) | expected | actual | match | reason")
    matched = 0
    for name, score, complete, att, cr, expected, _why in TEST_CASES:
        actual, reason = rule_based_extended(score, complete, att, cr)
        ok = actual == expected
        matched += ok
        print(name, "(%d, %s, %d%%, %d)" % (score, complete, att, cr), expected, actual,
              "PASS" if ok else "FAIL", reason, sep=" | ")
    print("Result: %d/%d cases matched the expected decision." % (matched, len(TEST_CASES)))
    print()
    print("Why each case was selected:")
    for name, *_rest, why in TEST_CASES:
        print("  %s: %s" % (name, why))
    print()
    print("Original 2-condition rule on the same inputs (shows what the new conditions change):")
    for name, score, complete, att, cr, *_ in TEST_CASES:
        print("  %s: original_rule -> %s, extended -> %s"
              % (name, original_rule(score, complete), rule_based_extended(score, complete, att, cr)[0]))
    return matched


def main():
    print("=" * 72)
    print("LAB 1 / Task 2  lab1_rules.py  (extended rule-based checker)")
    print("=" * 72)
    run_tests()


if __name__ == "__main__":
    main()
