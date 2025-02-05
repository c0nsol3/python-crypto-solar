from crypto.configuration.fee import get_fee, set_fee
from crypto.constants import TRANSACTION_FEES, TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP


def test_get_fee():
    result = get_fee(TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP.CORE.value)
    assert result == TRANSACTION_FEES[TRANSACTION_TRANSFER]


def test_set_fee():
    set_fee(TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP.CORE.value, 1)
    result = get_fee(TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP.CORE.value)
    assert result == 1

    # set it back to the default fee so that other tests aren't affected
    set_fee(
        TRANSACTION_TRANSFER,
        TRANSACTION_TYPE_GROUP.CORE.value,
        TRANSACTION_FEES[TRANSACTION_TRANSFER],
    )
    result = get_fee(TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP.CORE.value)
    assert result == TRANSACTION_FEES[TRANSACTION_TRANSFER]
