from crypto.transactions.deserializer import Deserializer


def test_multi_signature_registration_deserializer():
    serialized = "ff021701000000040001000000000000000205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89600943577000000000002030205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89603df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb803860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17ff5e9859c955bf8917b308ea21c88daf58661686c2017e476dcf735ad7f00aebf8e6effda3fe99e5f33f6007db7db9c9155796d9b5d31c53bd6156364a6a765d00064900cb2cc3db6ca9c7e3bd363b322cdc4a39e051f655e9867935e1bb856b6dcce52845c031c690808f40340bc827bbaacd7b04bceff866cb0d386ab8471517401dd363ccc101a958bded1a5db1c08f13283fc7cee53da93dfe00785eb406512467ff8e445f8ad843744ac4179f30f942645dfd5bdf5f2bfc344ad02393053880a02d0012f035dc3fd54173c83d40217914653488fe9ce592dca34234163181d255281f2be7033725cfc4a6786509e7fabbaf0be8cf50882fc7b66fe94f259fd004e"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    data = actual.to_dict()

    assert data["amount"] == 0
    assert data["nonce"] == 1
    assert data["version"] == 2
    assert data["network"] == 23
    assert data["typeGroup"] == 1
    assert data["fee"] == 2000000000
    assert (
        data["senderPublicKey"]
        == "0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896"
    )
    assert (
        data["signature"]
        == "f5e9859c955bf8917b308ea21c88daf58661686c2017e476dcf735ad7f00aebf8e6effda3fe99e5f33f6007db7db9c9155796d9b5d31c53bd6156364a6a765d0"
    )
    assert data["asset"]["multiSignature"]["min"] == 2
    assert data["asset"]["multiSignature"]["publicKeys"] == [
        "0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896",
        "03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8",
        "03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f",
    ]
    assert data["signatures"] == [
        "0064900cb2cc3db6ca9c7e3bd363b322cdc4a39e051f655e9867935e1bb856b6dcce52845c031c690808f40340bc827bbaacd7b04bceff866cb0d386ab84715174",  # noqa
        "01dd363ccc101a958bded1a5db1c08f13283fc7cee53da93dfe00785eb406512467ff8e445f8ad843744ac4179f30f942645dfd5bdf5f2bfc344ad02393053880a",  # noqa
        "02d0012f035dc3fd54173c83d40217914653488fe9ce592dca34234163181d255281f2be7033725cfc4a6786509e7fabbaf0be8cf50882fc7b66fe94f259fd004e",  # noqa
    ]

    assert actual.verify_signatures(data["asset"]["multiSignature"])
