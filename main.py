# Lab 1 - runs the code parts of the lab (Section 1.5/1.6 and Task 2).
# Task 1 and Task 3 are written answers, they are in the report.
import platform

from src import lab1_compare, lab1_rules


def main():
    print("AI Lab 1: Introduction to AI & Paradigms | Mohammed Emad ALaini")
    print("Python %s, standard library only" % platform.python_version())
    print()
    lab1_compare.main()
    print()
    lab1_rules.main()


if __name__ == "__main__":
    main()
