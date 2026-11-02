# Lab 1 Section 1.5 and 1.6
# symbolic rule vs probability threshold (the functions and cases are from the manual)


# code from the manual (Section 1.5)
def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"


def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"


cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70)]


# my helpers for the report
def explain(score, complete, probability):
    sym = []
    if not complete:
        sym.append("documents incomplete")
    if score < 70:
        sym.append("score %d < 70" % score)
    sym_reason = "; ".join(sym) if sym else "complete and score %d >= 70" % score
    thr_reason = ("p=%.2f >= 0.70" % probability) if probability >= 0.70 else ("p=%.2f < 0.70" % probability)
    return sym_reason, thr_reason


def compare(rows):
    out = []
    for name, score, complete, probability in rows:
        a, b = symbolic(score, complete), threshold(probability)
        sym_reason, thr_reason = explain(score, complete, probability)
        out.append((name, score, complete, probability, a, b, a != b, sym_reason, thr_reason))
    return out


def run_supplied():
    print("case | symbolic | threshold | disagreement")
    for name, score, complete, probability in cases:
        a, b = symbolic(score, complete), threshold(probability)
        print(name, a, b, a != b, sep=" | ")


def run_boundary_variants():
    variants = [
        ("boundary (original)", 70, True, 0.70),
        ("boundary score=69", 69, True, 0.70),
        ("boundary p=0.69", 70, True, 0.69),
    ]
    print("variant | score | complete | p | symbolic | threshold | disagreement | symbolic reason | threshold reason")
    for row in compare(variants):
        name, score, complete, p, a, b, dis, sr, tr = row
        print(name, score, complete, "%.2f" % p, a, b, dis, sr, tr, sep=" | ")


def main():
    print("=" * 72)
    print("LAB 1 / Section 1.5  lab1_compare.py  (supplied script output)")
    print("=" * 72)
    run_supplied()
    print()
    print("Disagreement table with the deciding condition for each branch:")
    print("case | symbolic | threshold | disagreement | symbolic reason | threshold reason")
    for name, score, complete, p, a, b, dis, sr, tr in compare(cases):
        print(name, a, b, dis, sr, tr, sep=" | ")
    print()
    print("Section 1.6  isolate the two boundaries (changed separately):")
    run_boundary_variants()


if __name__ == "__main__":
    main()
