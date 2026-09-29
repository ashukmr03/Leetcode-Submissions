class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            name = name.lower()
            domain = domain.lower()
            return name[0] + "*****" + name[-1] + "@" + domain
        digits = "".join(ch for ch in s if ch.isdigit())
        country_code_length = len(digits) - 10
        masked = "***-***-" + digits[-4:]
        if country_code_length > 0:
            masked = "+" + "*" * country_code_length + "-" + masked
        return masked