import os
import wallycore as wally


class Bip85:

    def __init__(self):
        self.HARDENED = 0x80000000
        self.master_key = None
        self.words = 0
        self.mnemonic = ''
        self.seed = None
        self.password = ''
        self.path = None
        self.priv_key = None
        self.entropy = None

    def import_mnemonic(self, mnemonic):
        try:
            wally.bip39_mnemonic_validate(None, mnemonic)
            self.mnemonic = mnemonic
            self.seed = bytearray(64)
            self.password = ''
            wally.bip39_mnemonic_to_seed(self.mnemonic, self.password, self.seed)
            print('Original seed: {}'.format(self.seed.hex()))
            self.master_key = wally.bip32_key_from_seed(self.seed, wally.BIP32_VER_MAIN_PRIVATE, wally.BIP32_FLAG_SKIP_HASH)
            print('Original master key: {}'.format(wally.bip32_key_to_base58(self.master_key, 0)))
        except:
            self.seed = None
            self.master_key = None

    def import_xprv(self, xprv):
        # TODO: Check
        self.master_key = wally.bip32_key_from_base58(xprv)
        print('Imported  master key: {}'.format(wally.bip32_key_to_base58(self.master_key, 0)))

    def derive(self, path):
        self.path = path
        flags = wally.BIP32_FLAG_KEY_PRIVATE
        derived_private_key = wally.bip32_key_from_parent_path(self.master_key, self.path, flags)
        #print('Derived private key: {}'.format(wally.bip32_key_to_base58(derived_private_key, 0)))
        self.priv_key = wally.bip32_key_get_priv_key(derived_private_key)
        print('Derived private key: {}'.format(self.priv_key.hex()))
        self.entropy = wally.hmac_sha512(b'bip-entropy-from-k', self.priv_key)
        print('Derived entropy ({}) {}'.format(len(self.entropy.hex()), self.entropy.hex()))

    def derive_bip39(self, words, index):
        self.words = words
        if self.words not in [12, 24]:
            print('Wrong words argument')
            self.priv_key = None
            self.entropy = None
            return
        path = [self.HARDENED + 83696968, self.HARDENED + 39, self.HARDENED + 0, self.HARDENED + words, self.HARDENED + index]
        self.derive(path)

    def get_mnemonic(self):
        bytes = round(self.words/12*16)
        self.derived_mnemonic = wally.bip39_mnemonic_from_bytes(None, self.entropy[:bytes])
        print('Derived mnemonic: {}'.format(self.derived_mnemonic))
