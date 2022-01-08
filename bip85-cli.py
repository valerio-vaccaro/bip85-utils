import argparse
from bip85 import Bip85


def main():
    parser = argparse.ArgumentParser(description='BIP85 utils')
    parser.add_argument('--master-key', help='Master key')
    parser.add_argument('--mnemonic', help='Mnemonic')
    parser.add_argument('-i', '--index', help='Index', type=int, default=0)
    parser.add_argument('-w', '--words', help='12 or 24 words', type=int, default=12)
    args = parser.parse_args()

    bip85 = Bip85()

    found = False
    # master key or mnemonic
    if args.mnemonic is not None:
        bip85.import_mnemonic(args.mnemonic)
        found = True

    if args.master_key is not None:
        bip85.import_xprv(args.master_key)
        found = True

    if not found:
        print('Missing mnemonic or master_key.')
        exit(1)

    # words 12 or 24
    if args.words not in [12, 24]:
        print('Words argument is not 12 or 24.')
        exit(1)

    bip85.derive_bip39(args.words, args.index)
    bip85.get_mnemonic()

if __name__ == '__main__':
    main()
