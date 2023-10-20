BASE58_PATTERN = r"[1-9A-HJ-NP-Za-km-z]"

# ED25519 regex pattern
ED25519_PATTERN = rf"^{BASE58_PATTERN}{{43,44}}$"

# BBS+ regex pattern
BBS_PATTERN = rf"^{BASE58_PATTERN}{{131,132}}$"
