import pytest
from vcdm.models import Credential


CREDENTIALS = [
    {
        "@context": ["https://www.w3.org/ns/credentials/v2"],
        "type": ["VerifiableCredential"],
        "issuer": "urn:uuid:1ad93a1e-651f-449a-9b0a-9f4c57625f27",
        "validFrom": "2015-05-10T12:30:00Z",
        "credentialSubject": {"id": "urn:uuid:5c396585-56b3-4f1e-92f8-3d6ee863b704"},
    }
]

INVALID_CREDENTIALS = [
    {
        "@context": ["https://www.w3.org/ns/credentials/v2"],
        "type": ["VerifiableCredential"],
        "credentialSubject": {"id": "5c396585-56b3-4f1e-92f8-3d6ee863b704"},
    },
    {
        "@context": [
            "https://www.w3.org/ns/credentials/v2",
            "https ://not-a-url/contexts/example/v1",
        ],
        "type": ["VerifiableCredential"],
        "credentialSubject": {"id": "did:example:subject"},
    },
    {
        "@context": [
            "https://www.w3.org/ns/credentials/v2",
            "https ://not-a-url/contexts/example/v1",
        ],
        "type": ["VerifiableCredential"],
        "id": None,
        "credentialSubject": {"id": "did:example:subject"},
    },
    {
    "credential": {
        "@context": [
        "https://www.w3.org/ns/credentials/v2"
        ],
        "type": [
        "VerifiableCredential"
        ],
        "issuer": {
        "description": {
            "@value": "An Example Issuer",
            "@language": "en",
            "url": "did:example:issuer"
        },
        "id": "did:key:123"
        }
    }
    }
]


@pytest.mark.parametrize("credential", CREDENTIALS)
def test_validates_valid(credential):
    Credential.model_validate(credential)


@pytest.mark.parametrize("credential", INVALID_CREDENTIALS)
def test_fails_invalid(credential):
    with pytest.raises(ValueError):
        Credential.model_validate(credential)


@pytest.mark.parametrize("credential_raw", CREDENTIALS)
def test_serialization(credential_raw):
    credential = Credential.model_validate(credential_raw)
    assert credential.model_dump() == credential_raw
