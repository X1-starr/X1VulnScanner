from dataclasses import dataclass, field
from typing import List


@dataclass
class Finding:
    title: str
    severity: str
    confidence: str
    category: str
    location: str
    evidence: str
    impact: str
    recommendation: str
    explanation: str

    def to_dict(self):
        return {
            "title": self.title,
            "severity": self.severity,
            "confidence": self.confidence,
            "category": self.category,
            "location": self.location,
            "evidence": self.evidence,
            "impact": self.impact,
            "recommendation": self.recommendation,
            "explanation": self.explanation, 

       }


@dataclass
class ScanResult:
    target: str
    findings: List[Finding] = field(default_factory=list)

    def add(self, finding: Finding):
        self.findings.append(finding)

    def summary(self):
        result = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
            "INFO": 0,
        }

        for finding in self.findings:
            if finding.severity in result:
                result[finding.severity] += 1

        return result
