from binascii import hexlify, unhexlify

from base58 import b58decode_check
from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit8, write_bit32, write_bit64

from crypto.exceptions import SolarSerializerException
from crypto.identity import address
from crypto.transactions.serializers.base import BaseSerializer


class HtlcLockSerializer(BaseSerializer):
    """Serializer handling timelock transfer data"""

    def serialize(self):
        if not address.validate_address(self.transaction["recipientId"]):
            raise SolarSerializerException("Invalid recipient address")

        secret_hash = unhexlify(self.transaction["asset"]["lock"]["secretHash"].encode())

        self.bytes_data += write_bit64(self.transaction["amount"])
        self.bytes_data += write_bit8(len(secret_hash))
        self.bytes_data += secret_hash
        self.bytes_data += write_bit8(self.transaction["asset"]["lock"]["expiration"]["type"])
        self.bytes_data += write_bit32(self.transaction["asset"]["lock"]["expiration"]["value"])

        recipientId = hexlify(b58decode_check(self.transaction["recipientId"]))
        self.bytes_data += write_high(recipientId)

        return self.bytes_data
