import argparse
from bip85lib.bip85 import Bip85

from colorama import init
from termcolor import colored
BANNER = """
bb      iii          88888  555555                lll iii 
bb          pp pp   88   88 55               cccc lll 
bbbbbb  iii ppp  pp  88888  555555  _____  cc     lll iii 
bb   bb iii pppppp  88   88    5555        cc     lll iii 
bbbbbb  iii pp       88888  555555          ccccc lll iii 
            pp """
VERSION = '0.0.1'

def main():
    print(colored(BANNER, 'green'))
    print(colored(f'      bip85-cli version {VERSION}', 'green'))

    parser = argparse.ArgumentParser(description='BIP85 utils')
    parser.add_argument('--master-key', help='Master key')
    parser.add_argument('--mnemonic', help='Mnemonic')
    parser.add_argument('-i', '--index', help='Index (default=0)', type=int, default=0)
    parser.add_argument('-w', '--words', help='12 or 24 words (default=12)', type=int, default=12)
    args = parser.parse_args()

    bip85 = Bip85()

    found = False
    # master key or mnemonic
    if args.mnemonic is not None:
        bip85.import_mnemonic(args.mnemonic)
        found = True
        print(colored('Original seed: {}'.format(bip85.seed.hex()), 'red'))
        print(colored('Original master key: {}'.format(bip85.get_priv_base58()), 'red'))

    if args.master_key is not None:
        bip85.import_xprv(args.master_key)
        found = True
        print(colored('Imported  master key: {}'.format(bip85.get_priv_base58()), 'red'))

    if not found:
        print(colored('Missing mnemonic or master_key.', 'red'))
        exit(1)

    # words 12 or 24
    if args.words not in [12, 24]:
        print(colored('Words argument is not 12 or 24.', 'red'))
        exit(1)

    bip85.derive_bip39(args.words, args.index)
    bip85.get_mnemonic()

    print(colored('Derived private key: {}'.format(bip85.priv_key.hex()), 'yellow'))
    print(colored('Derived entropy ({}) {}'.format(len(bip85.entropy.hex()), bip85.entropy.hex()), 'yellow'))
    print(colored('Derived mnemonic: {}'.format(bip85.derived_mnemonic), 'yellow'))

if __name__ == '__main__':
    main()
