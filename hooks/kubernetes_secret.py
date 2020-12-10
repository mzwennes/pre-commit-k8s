from typing import List
from hooks.rule import Rule, ValidationResult


class KubernetesSecretRule(Rule):
    """Check if commit contains Kubernetes Secret object."""

    @staticmethod
    def name() -> str:
        return "kubernetes-secrets"

    def validate(self, files: List[str]) -> ValidationResult:

        for file_name in files:
            with open(file_name, "r") as current:
                error_msg = f"File contains a Kubernetes Secret: {file_name}"
                if "kind: Secret" in current.read():
                    return ValidationResult(False, error_msg)

        return ValidationResult(True, None)
