import sys
import logging
import argparse
from typing import List

from hooks.rule import ValidationResult, Rule
from hooks.kubernetes_secret import KubernetesSecretRule

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    args = parse_arguments()

    rules: List[Rule] = [KubernetesSecretRule()]
    only_allowed_rules = [r for r in rules if r.name() not in args.exclude]

    if len(only_allowed_rules):
        logging.info("Validating the following rules:")
        for rule in only_allowed_rules:
            logging.info(f"\u2713 {rule.name()}")
    else:
        logging.warning("No rules activated to validate files")

    try:
        apply_rules_to_files(args.files, only_allowed_rules)
        logging.info("No validation errors found")
    except Exception as e:
        logging.error(e)
        sys.exit(1)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exclude", action="append", default=[])
    parser.add_argument("files", nargs="+")
    return parser.parse_args()


def apply_rules_to_files(files: List[str], rules: List[Rule]):
    for rule in rules:
        result: ValidationResult = rule.validate(files)
        if not result.valid:
            raise Exception(result.error)
