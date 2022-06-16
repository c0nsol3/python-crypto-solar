from enum import Enum

TRANSACTION_LEGACY_TRANSFER = 0
TRANSACTION_SECOND_SIGNATURE_REGISTRATION = 1
TRANSACTION_DELEGATE_REGISTRATION = 2
TRANSACTION_VOTE = 3
TRANSACTION_MULTI_SIGNATURE_REGISTRATION = 4
TRANSACTION_IPFS = 5
TRANSACTION_MULTI_PAYMENT = 6
TRANSACTION_DELEGATE_RESIGNATION = 7
TRANSACTION_HTLC_LOCK = 8
TRANSACTION_HTLC_CLAIM = 9
TRANSACTION_HTLC_REFUND = 10

TRANSACTION_TYPES = {
    TRANSACTION_LEGACY_TRANSFER: "legacy_transfer",
    TRANSACTION_SECOND_SIGNATURE_REGISTRATION: "second_signature_registration",
    TRANSACTION_DELEGATE_REGISTRATION: "delegate_registration",
    TRANSACTION_VOTE: "vote",
    TRANSACTION_MULTI_SIGNATURE_REGISTRATION: "multi_signature_registration",
    TRANSACTION_IPFS: "ipfs",
    TRANSACTION_MULTI_PAYMENT: "multi_payment",
    TRANSACTION_DELEGATE_RESIGNATION: "delegate_resignation",
    TRANSACTION_HTLC_LOCK: "htlc_lock",
    TRANSACTION_HTLC_CLAIM: "htlc_claim",
    TRANSACTION_HTLC_REFUND: "htlc_refund",
}

TRANSACTION_FEES = {
    TRANSACTION_DELEGATE_REGISTRATION: 7500000000,
    TRANSACTION_LEGACY_TRANSFER: 5000000,
    TRANSACTION_SECOND_SIGNATURE_REGISTRATION: 5000000,
    TRANSACTION_VOTE: 5000000,
    TRANSACTION_MULTI_SIGNATURE_REGISTRATION: 5000000,
    TRANSACTION_IPFS: 5000000,
    TRANSACTION_MULTI_PAYMENT: 50000000,
    TRANSACTION_HTLC_LOCK: 5000000,
    TRANSACTION_DELEGATE_RESIGNATION: 0,
    TRANSACTION_HTLC_CLAIM: 0,
    TRANSACTION_HTLC_REFUND: 0,
}

SOLAR_TRANSACTION_BURN = 0

SOLAR_TRANSACTION_TYPES = {
    SOLAR_TRANSACTION_BURN: "burn",
}

SOLAR_TRANSACTION_FEES = {
    SOLAR_TRANSACTION_BURN: 0,
}


class TRANSACTION_TYPE_GROUP(Enum):
    def __int__(self):
        return int(self.value)

    TEST = 0
    CORE = 1
    SOLAR = 2
    RESERVED = 1000  # Everything above is available to anyone


class HTLC_LOCK_EXPIRATION_TYPE(Enum):
    def __str__(self):
        return int(self.value)

    EPOCH_TIMESTAMP = 1
    BLOCK_HEIGHT = 2


class HashingType(Enum):
    SHA256 = 0
    SHA384 = 1
    SHA512 = 2
    SHA3256 = 3
    SHA3384 = 4
    SHA3512 = 5
    Keccak256 = 6
    Keccak384 = 7
    Keccak512 = 8
