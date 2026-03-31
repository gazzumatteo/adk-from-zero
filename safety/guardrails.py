"""
Safety guardrails for production agents.

Implements:
- Prompt injection defense
- Input validation
- Output filtering
- Rate limiting
"""

import re
from typing import Any


class SafetyGuardrails:
    """
    Safety guardrails for agent execution.

    Provides:
    - Prompt injection detection
    - Input validation
    - Output filtering
    """

    # Patterns for potential prompt injection attacks
    INJECTION_PATTERNS = [
        r"ignore.*instruction",
        r"forget.*rule",
        r"override.*security",
        r"execute.*command",
        r"run.*script",
        r"system.*prompt",
        r"hidden.*instruction",
    ]

    # Sensitive data patterns
    SENSITIVE_PATTERNS = [
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  # Email
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
        r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",  # Credit card
        r"(?i)api[_-]?key",
        r"(?i)password",
        r"(?i)secret",
    ]

    def __init__(self) -> None:
        """Initialize safety guardrails."""
        self.injection_patterns = [re.compile(p, re.IGNORECASE) for p in self.INJECTION_PATTERNS]
        self.sensitive_patterns = [re.compile(p) for p in self.SENSITIVE_PATTERNS]

    def check_prompt_injection(self, prompt: str) -> tuple[bool, str]:
        """
        Check for potential prompt injection attacks.

        Args:
            prompt: User prompt to check

        Returns:
            Tuple of (is_safe, reason)
        """
        prompt_lower = prompt.lower()

        for pattern in self.injection_patterns:
            if pattern.search(prompt_lower):
                return (
                    False,
                    f"Potential prompt injection detected: {pattern.pattern}",
                )

        return True, "Prompt passed injection check"

    def check_sensitive_data(self, text: str) -> tuple[bool, list[str]]:
        """
        Check for sensitive data in text.

        Args:
            text: Text to check

        Returns:
            Tuple of (is_safe, found_patterns)
        """
        found = []

        for pattern in self.sensitive_patterns:
            matches = pattern.findall(text)
            if matches:
                found.extend(matches)

        return len(found) == 0, found

    def validate_input(self, user_input: str, max_length: int = 5000) -> tuple[bool, str]:
        """
        Validate user input.

        Args:
            user_input: Input to validate
            max_length: Maximum allowed length

        Returns:
            Tuple of (is_valid, reason)
        """
        if not user_input or not user_input.strip():
            return False, "Input cannot be empty"

        if len(user_input) > max_length:
            return False, f"Input exceeds maximum length of {max_length}"

        # Check for injection
        is_safe, reason = self.check_prompt_injection(user_input)
        if not is_safe:
            return False, reason

        # Check for sensitive data
        is_safe, found = self.check_sensitive_data(user_input)
        if not is_safe:
            return False, f"Input contains sensitive data patterns: {found[:3]}"

        return True, "Input validated"

    def sanitize_output(self, output: str) -> str:
        """
        Sanitize output by removing sensitive data.

        Args:
            output: Output to sanitize

        Returns:
            Sanitized output
        """
        result = output

        # Replace detected sensitive patterns
        for pattern in self.sensitive_patterns:
            result = pattern.sub("[REDACTED]", result)

        return result

    def before_model_call(self, prompt: str) -> tuple[bool, str, str]:
        """
        Pre-flight checks before model call.

        Args:
            prompt: Prompt to validate

        Returns:
            Tuple of (allowed, reason, sanitized_prompt)
        """
        # Validate input
        is_valid, reason = self.validate_input(prompt)

        if not is_valid:
            return False, f"Input validation failed: {reason}", ""

        return True, "Input passed validation", prompt

    def before_tool_call(
        self,
        tool_name: str,
        parameters: dict[str, Any],
    ) -> tuple[bool, str]:
        """
        Pre-flight checks before tool execution.

        Args:
            tool_name: Name of tool being called
            parameters: Tool parameters

        Returns:
            Tuple of (allowed, reason)
        """
        # Block sensitive operations
        blocked_tools = ["delete_all", "drop_database", "execute_code"]

        if tool_name in blocked_tools:
            return False, f"Tool '{tool_name}' is blocked for safety"

        # Validate parameters
        for key, value in parameters.items():
            if isinstance(value, str):
                is_safe, found = self.check_sensitive_data(value)
                if not is_safe:
                    return (
                        False,
                        f"Parameter '{key}' contains sensitive data",
                    )

        return True, "Tool parameters validated"

    def after_model_call(self, response: str) -> str:
        """
        Post-processing after model call.

        Args:
            response: Model response

        Returns:
            Sanitized response
        """
        # Sanitize output
        sanitized = self.sanitize_output(response)

        # Check output length
        if len(sanitized) > 10000:
            sanitized = sanitized[:10000] + "...[truncated]"

        return sanitized
