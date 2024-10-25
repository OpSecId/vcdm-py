import pytest
from vcdm.linked_data import LDProcessor, LDProcessorError


VALID_CONTEXTS = [
    ["https://www.w3.org/2018/credentials/v1"],
    ["https://www.w3.org/ns/credentials/v2"],
    [
        "https://www.w3.org/ns/credentials/v2",
        "https://www.w3.org/ns/credentials/examples/v2",
    ],
]

UNSTRICT_CONTEXTS = [
    ["https://www.w3.org/ns/credentials/v2", "https://w3id.org/vdl/v1"],
]

INVALID_CONTEXTS = [
    ["https:// www.w3.org/ns/credentials/v2"],
    ["https://example.com"],
    ["123"],
    [True],
]


@pytest.mark.parametrize("context", VALID_CONTEXTS)
def test_validates_valid(context):
    LDProcessor().is_valid_context(context)


@pytest.mark.parametrize("context", INVALID_CONTEXTS)
def test_fails_invalid(context):
    with pytest.raises(LDProcessorError):
        LDProcessor().is_valid_context(context)


# @pytest.mark.parametrize("context", UNSTRICT_CONTEXTS)
# def test_serialization(context):
#     LDProcessor(strict=False, allowed_ctx="https://w3id.org/vdl/v1").is_valid_context(
#         context
#     )
