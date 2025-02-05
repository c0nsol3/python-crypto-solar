import pytest

from crypto.transactions.deserializer import Deserializer


def test_transfer_deserializer(transaction_type_0):
    serialized = transaction_type_0["serialized"]

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.expiration == 0
    assert actual.type == 0
    assert actual.amount == 200000000
    assert actual.fee == 10000000
    assert actual.nonce == 1
    assert actual.recipientId == "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib"
    assert (
        actual.senderPublicKey
        == "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192"
    )  # noqa
    assert (
        actual.signature
        == "20b4091da824dc1b630ec7a09f39fe491cb2ac39dabdbe67d48753a43e8dc8cd4f76eb4ff717efbb06889882aa99a07db7bf35de3b8d5f1ad74b8284e0a68420"
    )

    actual.verify()


@pytest.mark.skip()
def test_transfer_second_signature_deserializer():
    serialized = "ff02170100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b0000000000000000170995750207ecaf0ccf251c1265b92ad84f553662136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b02dd94f611e300ad77147d808a34e942b379c5468760d8605adc0304400a2578a2039468b844f30ad1f0515f9cce33855791296117bfe8ef3caa664152644fd6"

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.expiration == 0
    assert actual.type == 0
    assert actual.amount == 200000000
    assert actual.fee == 10000000
    assert actual.nonce == 1
    assert actual.recipientId == "AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC"
    assert (
        actual.senderPublicKey
        == "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192"
    )  # noqa
    assert (
        actual.signature
        == "136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b"
    )
    assert (
        actual.signSignature
        == "02dd94f611e300ad77147d808a34e942b379c5468760d8605adc0304400a2578a2039468b844f30ad1f0515f9cce33855791296117bfe8ef3caa664152644fd6"
    )

    actual.verify()


def test_transfer_with_vendor_field_deserializer():
    serialized = "ff021e0100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000b68656c6c6f20776f726c6400c2eb0b00000000000000001e0995750207ecaf0ccf251c1265b92ad84f553662dc79fe9c166d898cf27e36e8897cb154925a48faa32738edb87d71acfae68cc5e384a9969374cc85b335bf89549342f17266cce370ff57c3401ff8ca90424086"

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.vendorField == "hello world"

    actual.verify()
