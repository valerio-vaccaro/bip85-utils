import pytest
from bip85 import *
import wallycore as wally


class TestLib:

    def test_bip85_1(self):
        bip85 = Bip85()

        xprv = 'xprv9s21ZrQH143K2LBWUUQRFXhucrQqBpKdRRxNVq2zBqsx8HVqFk2uYo8kmbaLLHRdqtQpUm98uKfu3vca1LqdGhUtyoFnCNkfmXRyPXLjbKb'
        bip85.import_xprv(xprv)
        path = [bip85.HARDENED + 83696968, bip85.HARDENED + 0, bip85.HARDENED + 0]
        bip85.derive(path)
        assert bip85.priv_key.hex() == 'cca20ccb0e9a90feb0912870c3323b24874b0ca3d8018c4b96d0b97c0e82ded0'
        assert bip85.entropy.hex() == 'efecfbccffea313214232d29e71563d941229afb4338c21f9517c41aaa0d16f00b83d2a09ef747e7a64e8e2bd5a14869e693da66ce94ac2da570ab7ee48618f7'
        #mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy[:16])
        #print('Derived mnemonic 12: {}'.format(mnemonic))
        #mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy[:32])
        #print('Derived mnemonic 24: {}'.format(mnemonic))

    def test_bip85_2(self):
        bip85 = Bip85()

        xprv = 'xprv9s21ZrQH143K2LBWUUQRFXhucrQqBpKdRRxNVq2zBqsx8HVqFk2uYo8kmbaLLHRdqtQpUm98uKfu3vca1LqdGhUtyoFnCNkfmXRyPXLjbKb'
        bip85.import_xprv(xprv)
        path = [bip85.HARDENED + 83696968, bip85.HARDENED + 0, bip85.HARDENED + 1]
        bip85.derive(path)
        assert bip85.priv_key.hex() == '503776919131758bb7de7beb6c0ae24894f4ec042c26032890c29359216e21ba'
        assert bip85.entropy.hex() == '70c6e3e8ebee8dc4c0dbba66076819bb8c09672527c4277ca8729532ad711872218f826919f6b67218adde99018a6df9095ab2b58d803b5b93ec9802085a690e'
        #mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy[:16])
        #print('Derived mnemonic 12: {}'.format(mnemonic))
        #mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy[:32])
        #print('Derived mnemonic 24: {}'.format(mnemonic))

    def test_bip85_bip39(self):
        bip85 = Bip85()

        entropy = os.urandom(32)
        print('Original entropy: {}'.format(entropy.hex()))
        mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy)
        print('Original mnemonic: {}'.format(mnemonic))
        bytes = bytearray(64)
        res = wally.bip39_mnemonic_to_bytes(None, mnemonic, bytes)
        print('Original entropy: {} {}'.format(res, bytes.hex()))

        seed = bytearray(64)
        password = ''
        wally.bip39_mnemonic_to_seed(mnemonic, password, seed)
        print('Original seed: {}'.format(seed.hex()))
        master_key = wally.bip32_key_from_seed(seed, wally.BIP32_VER_MAIN_PRIVATE, wally.BIP32_FLAG_SKIP_HASH)
        print('Original master key: {}'.format(wally.bip32_key_to_base58(master_key, 0)))

        xprv = wally.bip32_key_to_base58(master_key, 0)
        bip85.import_xprv(xprv)
        path = [bip85.HARDENED + 83696968, bip85.HARDENED + 0, bip85.HARDENED + 0]
        bip85.derive(path)
        mnemonic = wally.bip39_mnemonic_from_bytes(None, bip85.entropy[:16])
        print('Derived mnemonic 12: {}'.format(mnemonic))
        mnemonic = wally.bip39_mnemonic_from_bytes(None, bip85.entropy[:32])
        print('Derived mnemonic 24: {}'.format(mnemonic))

        pass
