import pytest
from bip85lib.bip85 import Bip85
import wallycore as wally


class TestLib:

    def test_derive_1(self):
        bip85 = Bip85()
        xprv = 'xprv9s21ZrQH143K2LBWUUQRFXhucrQqBpKdRRxNVq2zBqsx8HVqFk2uYo8kmbaLLHRdqtQpUm98uKfu3vca1LqdGhUtyoFnCNkfmXRyPXLjbKb'
        bip85.import_xprv(xprv)
        path = [bip85.HARDENED + 83696968, bip85.HARDENED + 0, bip85.HARDENED + 0]
        bip85.derive(path)
        assert bip85.priv_key.hex() == 'cca20ccb0e9a90feb0912870c3323b24874b0ca3d8018c4b96d0b97c0e82ded0'
        assert bip85.entropy.hex() == 'efecfbccffea313214232d29e71563d941229afb4338c21f9517c41aaa0d16f00b83d2a09ef747e7a64e8e2bd5a14869e693da66ce94ac2da570ab7ee48618f7'

    def test_derive_2(self):
        bip85 = Bip85()
        xprv = 'xprv9s21ZrQH143K2LBWUUQRFXhucrQqBpKdRRxNVq2zBqsx8HVqFk2uYo8kmbaLLHRdqtQpUm98uKfu3vca1LqdGhUtyoFnCNkfmXRyPXLjbKb'
        bip85.import_xprv(xprv)
        path = [bip85.HARDENED + 83696968, bip85.HARDENED + 0, bip85.HARDENED + 1]
        bip85.derive(path)
        assert bip85.priv_key.hex() == '503776919131758bb7de7beb6c0ae24894f4ec042c26032890c29359216e21ba'
        assert bip85.entropy.hex() == '70c6e3e8ebee8dc4c0dbba66076819bb8c09672527c4277ca8729532ad711872218f826919f6b67218adde99018a6df9095ab2b58d803b5b93ec9802085a690e'

    def test_import_mnemonic(self):
        bip85 = Bip85()
        mnemonic = 'cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft'
        bip85.import_mnemonic(mnemonic)
        assert wally.bip32_key_to_base58(bip85.master_key, 0) == 'xprv9s21ZrQH143K2GmazFCn22vhxqmF272Y3BpvmEHqcT7q9U2Ncza9ryQ3Fy8zeXVC8iGzQ9rU5seNmLDb9rVUeQbJk9hZQeVXUU1gmTCGBzQ'

    def test_import_xprv(self):
        bip85 = Bip85()
        xprv = 'xprv9s21ZrQH143K2LBWUUQRFXhucrQqBpKdRRxNVq2zBqsx8HVqFk2uYo8kmbaLLHRdqtQpUm98uKfu3vca1LqdGhUtyoFnCNkfmXRyPXLjbKb'
        bip85.import_xprv(xprv)
        assert wally.bip32_key_to_base58(bip85.master_key, 0) == xprv

    def test_derive_bip39(self):
        bip85 = Bip85()
        mnemonic = 'cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft'
        bip85.import_mnemonic(mnemonic)
        assert wally.bip32_key_to_base58(bip85.master_key, 0) == 'xprv9s21ZrQH143K2GmazFCn22vhxqmF272Y3BpvmEHqcT7q9U2Ncza9ryQ3Fy8zeXVC8iGzQ9rU5seNmLDb9rVUeQbJk9hZQeVXUU1gmTCGBzQ'

        bip85.derive_bip39(12, 0)
        assert bip85.entropy.hex() == '9c28ac75db098f574454e02f0fbdc4b2a17fb6d399c3a4f06f8731d64f06bd5adbbc3e46842b707549de43c90a60653c64016e7d836f6e276135cf4b0a1f5d83'
        assert bip85.priv_key.hex() == 'a066e3abc08f294e835cd5bae5771dcee96b5cd3ad1830f736d339442a7fe0cb'
        bip85.get_mnemonic()
        assert bip85.derived_mnemonic == 'order earth buddy render ocean produce bacon orchard congress law illness goat'

        bip85.derive_bip39(24, 0)
        assert bip85.entropy.hex() == '6037bdbf62931e90a759a386a3d9f1eab5b89e19d164014f24ed7108c3ec461b8b1ca39513a57ada20cd276729295d0f2ca0151a034e3a1bfae507bc41469bc2'
        assert bip85.priv_key.hex() == 'ec958668764d5985a8e6ce9e32237352b181604ba62292a6debde5f38f0abbc0'
        bip85.get_mnemonic()
        assert bip85.derived_mnemonic == 'gasp sadness hurt share cradle embark output crucial mammal burst ladder step fortune excuse guard clutch access junior deputy tilt method wage blur labor'

    def test_error(self):
        bip85 = Bip85()
        mnemonic = 'pippo'
        bip85.import_mnemonic(mnemonic)
        assert bip85.master_key == None
