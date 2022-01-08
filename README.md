# bip85 utils
Bip85 lib and cli written in python.

## bip85-cli

Derive first 12 words mnemonic (index 0) based on the master mnemonic `cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft`.

```
python3 bip85-cli.py --mnemonic "cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft"
Original seed: 1fac7c6e2ffcb65bef44868f8f4bfb82fa2151597ee1d8f14e275ea4beee6000d27dbb014ec1aeb16fc3011b7010a8332df43ba093c30e4e25c66e7a5d1358c9
Original master key: xprv9s21ZrQH143K2GmazFCn22vhxqmF272Y3BpvmEHqcT7q9U2Ncza9ryQ3Fy8zeXVC8iGzQ9rU5seNmLDb9rVUeQbJk9hZQeVXUU1gmTCGBzQ
Derived private key: a066e3abc08f294e835cd5bae5771dcee96b5cd3ad1830f736d339442a7fe0cb
Derived entropy (128) 9c28ac75db098f574454e02f0fbdc4b2a17fb6d399c3a4f06f8731d64f06bd5adbbc3e46842b707549de43c90a60653c64016e7d836f6e276135cf4b0a1f5d83
Derived mnemonic: order earth buddy render ocean produce bacon orchard congress law illness goat
```

Derive the 24 mnemonic for the same index.

```
python3 bip85-cli.py --mnemonic "cup hunt peanut afford cute bridge bread immense artist story funny wrap weather weather monster duck spray gasp adjust clerk rather engage mind craft" -w 24
Original seed: 1fac7c6e2ffcb65bef44868f8f4bfb82fa2151597ee1d8f14e275ea4beee6000d27dbb014ec1aeb16fc3011b7010a8332df43ba093c30e4e25c66e7a5d1358c9
Original master key: xprv9s21ZrQH143K2GmazFCn22vhxqmF272Y3BpvmEHqcT7q9U2Ncza9ryQ3Fy8zeXVC8iGzQ9rU5seNmLDb9rVUeQbJk9hZQeVXUU1gmTCGBzQ
Derived private key: ec958668764d5985a8e6ce9e32237352b181604ba62292a6debde5f38f0abbc0
Derived entropy (128) 6037bdbf62931e90a759a386a3d9f1eab5b89e19d164014f24ed7108c3ec461b8b1ca39513a57ada20cd276729295d0f2ca0151a034e3a1bfae507bc41469bc2
Derived mnemonic: gasp sadness hurt share cradle embark output crucial mammal burst ladder step fortune excuse guard clutch access junior deputy tilt method wage blur labor
```
