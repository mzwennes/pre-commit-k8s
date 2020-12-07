from typing import List, Optional
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of a rule that has been validated."""

    valid: bool
    error: Optional[str]


class Rule:
    """Custom rule that will validate if files are okay to commit."""

    __metaclass__ = ABCMeta

    @staticmethod
    def name(self) -> str:
        return "default-rule"

    @abstractmethod
    def validate(self, files: List[str]) -> ValidationResult:
        raise NotImplementedError
