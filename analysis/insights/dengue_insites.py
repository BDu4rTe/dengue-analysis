from dataclasses import dataclass


@dataclass
class InsightExemple:
    Question: str
    Description: str
    Plots_Path: list[str]
