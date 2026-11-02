# AI Lab 1 - Introduction to AI and Paradigms

Lab 1 for the AI lab course (CS4944). It has the symbolic rule vs threshold comparison from the manual, my extended rule based scholarship checker, and the written answers (timeline and the conversational test question) in the report.

## Files

- `main.py` runs everything
- `src/lab1_compare.py` Section 1.5 and 1.6 (code from the manual)
- `src/lab1_rules.py` Task 2, the extended checker
- `outputs/output.txt` output of my run
- `report/Lab1_Report_Mohammed_Emad_ALaini.docx` the report (Task 1, Task 3 and all the results)

## How to run

Only Python 3 is needed, no extra packages.

```
python main.py
```

## Results

Section 1.5 (manual code):

| Case | Symbolic | Threshold | Disagreement |
|------|----------|-----------|--------------|
| complete_high | Review | Review | False |
| complete_low | Hold | Review | True |
| incomplete_high | Hold | Review | True |
| boundary | Review | Review | False |

In 1.6, score 69 only changes the symbolic rule and p = 0.69 only changes the threshold.

Task 2: I added attendance >= 75% and credit hours >= 12 to the original rule (score >= 70 and documents complete). These numbers are my own assumptions for the lab.

| Case | Input (score, docs, attendance, credits) | Expected | Actual |
|------|------|----------|--------|
| T1_pass | (82, True, 90%, 15) | Review | Review |
| T2_attendance_fails | (85, True, 60%, 15) | Hold | Hold |
| T3_credit_load_fails | (88, True, 92%, 9) | Hold | Hold |
| T4_score_boundary | (70, True, 80%, 15) | Review | Review |

All 4 cases matched. "Review" means the case goes to a person to check, it is not an award.

## Author

Mohammed Emad ALaini

MIT License, see LICENSE.
