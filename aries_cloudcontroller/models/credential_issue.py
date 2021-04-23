import json
import logging

from .credential_request import CredentialRequest

logger = logging.getLogger("aries_controller.models.credential_request")


class CredentialIssue(CredentialRequest):
    def __init__(self, credential_issue_json):
        super().__init__(credential_issue_json)
        try:
            self.json_data = json.loads(credential_issue_json)
        except Exception:
            logger.error("Failed to load credentials issue JSON")
            raise
        self.validate_credential_issue_json(credential_issue_json)

    def validate_credential_issue_json(self, presentation_json):
        try:
            # Taken from sample response in swagger UI
            # TODO Determine whether this is the minimal set of keys
            presentation_keys = [
                "@type",
                "@id",
                "goal_code",
                "replacement_id",
                "comment",
                "formats",
                "requests~attach",
            ]
            for key in presentation_keys:
                assert key in json.loads(
                    presentation_json
                ), f"Invalid proof request. Missing key {key}"
        except AssertionError:
            raise
