# bip85 utils
Bip85 lib and cli written in python.

## Install
You can install lib and client using pip.

```
pip install bip85-cli
```

## Usage
You can launch the client with `bip85-cli` command.

```
$ bip85-cli -h

bb      iii          88888  555555                lll iii 
bb          pp pp   88   88 55               cccc lll 
bbbbbb  iii ppp  pp  88888  555555  _____  cc     lll iii 
bb   bb iii pppppp  88   88    5555        cc     lll iii 
bbbbbb  iii pp       88888  555555          ccccc lll iii 
            pp 
      bip85-cli version 0.0.1
usage: bip85_cli.py [-h] [--master-key MASTER_KEY] [--mnemonic MNEMONIC] [-i INDEX] [-w WORDS]

BIP85 utils

options:
  -h, --help            show this help message and exit
  --master-key MASTER_KEY
                        Master key
  --mnemonic MNEMONIC   Mnemonic
  -i INDEX, --index INDEX
                        Index (default=0)
  -w WORDS, --words WORDS
                        12 or 24 words (default=12)
```

Derive first 12 words mnemonic (index 0) based on the master mnemonic `cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft`.

```
$ bip85-cli --mnemonic 'cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft'

bb      iii          88888  555555                lll iii 
bb          pp pp   88   88 55               cccc lll 
bbbbbb  iii ppp  pp  88888  555555  _____  cc     lll iii 
bb   bb iii pppppp  88   88    5555        cc     lll iii 
bbbbbb  iii pp       88888  555555          ccccc lll iii 
            pp 
      bip85-cli version 0.0.1
Original seed: 1fac7c6e2ffcb65bef44868f8f4bfb82fa2151597ee1d8f14e275ea4beee6000d27dbb014ec1aeb16fc3011b7010a8332df43ba093c30e4e25c66e7a5d1358c9
Original master key: xprv9s21ZrQH143K2GmazFCn22vhxqmF272Y3BpvmEHqcT7q9U2Ncza9ryQ3Fy8zeXVC8iGzQ9rU5seNmLDb9rVUeQbJk9hZQeVXUU1gmTCGBzQ
Derived private key: a066e3abc08f294e835cd5bae5771dcee96b5cd3ad1830f736d339442a7fe0cb
Derived entropy (128) 9c28ac75db098f574454e02f0fbdc4b2a17fb6d399c3a4f06f8731d64f06bd5adbbc3e46842b707549de43c90a60653c64016e7d836f6e276135cf4b0a1f5d83
Derived mnemonic: order earth buddy render ocean produce bacon orchard congress law illness goat
```
Derive the 24 mnemonic for the index 1.

```
$ bip85-cli --mnemonic 'cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft' -w 12 -i 1

bb      iii          88888  555555                lll iii 
bb          pp pp   88   88 55               cccc lll 
bbbbbb  iii ppp  pp  88888  555555  _____  cc     lll iii 
bb   bb iii pppppp  88   88    5555        cc     lll iii 
bbbbbb  iii pp       88888  555555          ccccc lll iii 
            pp 
      bip85-cli version 0.0.1
Original seed: 1fac7c6e2ffcb65bef44868f8f4bfb82fa2151597ee1d8f14e275ea4beee6000d27dbb014ec1aeb16fc3011b7010a8332df43ba093c30e4e25c66e7a5d1358c9
Original master key: xprv9s21ZrQH143K2GmazFCn22vhxqmF272Y3BpvmEHqcT7q9U2Ncza9ryQ3Fy8zeXVC8iGzQ9rU5seNmLDb9rVUeQbJk9hZQeVXUU1gmTCGBzQ
Derived private key: 886d0f6e1882476d8a54af3bffc45e587fb6093f54c25221acc91a8bcde4890b
Derived entropy (128) 6bbe6a91d6dcd32d6675386cef7f48b0fa74f82f84772ca8aecffe73bbfd1e802fe9c549a0f98686fa247d5827d965ace933f0bf8345f3dd73c75075ff60420a
Derived mnemonic: hill viable piece pumpkin snake note oil poem hollow know split giggle
```
