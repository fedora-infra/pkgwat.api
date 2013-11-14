Changelog
=========

0.12
----

- Add failing tests for tag stripping. `0ab263ba5 <https://github.com/fedora-infra/pkgwat.api/commit/0ab263ba527c9d46e8541278752cf6812693d169>`_
- Fix tag stripping once and for all. `ae12f6c28 <https://github.com/fedora-infra/pkgwat.api/commit/ae12f6c28acbc649fdde51a72bb9707800416fb1>`_
- Add one more test of strip_tags, just for good measure. `d64cb2cf6 <https://github.com/fedora-infra/pkgwat.api/commit/d64cb2cf67fda2a20ae0f53b697bbcae3540c5d1>`_
- Merge pull request #13 from fedora-infra/feature/fix-tag-stripping `d64da0a14 <https://github.com/fedora-infra/pkgwat.api/commit/d64da0a149610425782d7d907b45960620ad543d>`_
- unicode escape fix https://github.com/fedora-infra/fedora-packages/issues/28 `b058ce006 <https://github.com/fedora-infra/pkgwat.api/commit/b058ce006e1ea760088154efe9f6f589c2cf2d2a>`_
- Handle erroneous html_parser exception on py2.6. `f0057a18c <https://github.com/fedora-infra/pkgwat.api/commit/f0057a18ca8118eaa183ec6970a3a325f1962bdf>`_
- Merge pull request #16 from fedora-infra/feature/py2.6-html_parser-fix `e979a0293 <https://github.com/fedora-infra/pkgwat.api/commit/e979a029308cc9a8a94def7333d754d5c5887c5f>`_
- Remove unnecessary markup. `581b7dd4e <https://github.com/fedora-infra/pkgwat.api/commit/581b7dd4e24801b8865e7239d70a644808a14833>`_
- Quotes. `ec25d0de1 <https://github.com/fedora-infra/pkgwat.api/commit/ec25d0de171ab426a0232281dcb763c80fd7425d>`_
- 0.10 `f57675999 <https://github.com/fedora-infra/pkgwat.api/commit/f576759992ea6b3e46a286838a52eb699d622c87>`_
- ascii codec cant encode character `f4235e06e <https://github.com/fedora-infra/pkgwat.api/commit/f4235e06e66331d6828bfcd3b33c584c29c7294e>`_
- Merge pull request #17 from arielb2/bug-utf `8acb9bb21 <https://github.com/fedora-infra/pkgwat.api/commit/8acb9bb21688cbe585ba8e2d6ee36a73c5865c48>`_
- Add kitchen to the requires list.  From #17. `d0fffd8ae <https://github.com/fedora-infra/pkgwat.api/commit/d0fffd8ae562444b31f31c06c4ca296c1435a807>`_
- PEP8/cosmetic. `851424586 <https://github.com/fedora-infra/pkgwat.api/commit/851424586e2821fbda7fea05a736f3785447bfe5>`_
- Merge pull request #18 from fedora-infra/feature/cleanup `18c25c073 <https://github.com/fedora-infra/pkgwat.api/commit/18c25c073f347b78516ed22ea2ab2a2ddbf2b9dc>`_
- 0.11 `bc2fae367 <https://github.com/fedora-infra/pkgwat.api/commit/bc2fae3673d220aa799fde1815c719abd12df052>`_
- Temporarily remove dep on kitchen until py3 support can be sorted out. `0f4d864c4 <https://github.com/fedora-infra/pkgwat.api/commit/0f4d864c474280143d437982c8e97b0adc6f25d1>`_
- Guake actually only provides 2 things I guess. `cf0ce50a8 <https://github.com/fedora-infra/pkgwat.api/commit/cf0ce50a801ee0d58b53f45b8a1910dd17e40d75>`_
- Merge pull request #19 from fedora-infra/feature/nix-kitchen `d9be9c268 <https://github.com/fedora-infra/pkgwat.api/commit/d9be9c268b1de21874db6b49941e83f42f4a1662>`_

0.9
---

- Allow .get to return subpackages. `1db230381 <https://github.com/fedora-infra/pkgwat.api/commit/1db23038157cf2513304bf56aac33ca74b039b77>`_
- Merge pull request #8 from fedora-infra/feature/get-subpackages `84e913fe1 <https://github.com/fedora-infra/pkgwat.api/commit/84e913fe1870a8748a1c2d52cbf790d5289076ac>`_
- Packages with different names `3d2930649 <https://github.com/fedora-infra/pkgwat.api/commit/3d293064933ef50a81a0ee6853fc101da40f1c09>`_
- Merge pull request #10 from arielb2/3d293064933ef50a81a0ee6853fc101da40f1c09 `f6ac43b46 <https://github.com/fedora-infra/pkgwat.api/commit/f6ac43b461ea8239bfa0c46e14045d01d7e7fc72>`_
- Add a history function to query datagrepper. `a3cd8950f <https://github.com/fedora-infra/pkgwat.api/commit/a3cd8950fd72c2e7bc33a61212858c257fc74856>`_
- Add a docstring for pkgwat.rtfd.org/ `30099ade4 <https://github.com/fedora-infra/pkgwat.api/commit/30099ade45068a8cf4bf20f8c9c99bcd9c389d55>`_
- Merge pull request #12 from fedora-infra/feature/history `11707a285 <https://github.com/fedora-infra/pkgwat.api/commit/11707a285bdfd3908f83ceac8173788c0f52430b>`_

0.8
---

- Py3.2-friendly. `72c111cd8 <https://github.com/fedora-infra/pkgwat.api/commit/72c111cd88cb3bcff7b25215ac9dff319c45def4>`_
- Correct URL for source. `9e3607ea0 <https://github.com/fedora-infra/pkgwat.api/commit/9e3607ea0fb9643381cac7e0f79c9ffacc31d6a5>`_
- Travis-CI config. `cd4866257 <https://github.com/fedora-infra/pkgwat.api/commit/cd4866257f347331d8fe99dbd48e73dff33763fa>`_
- OrderedDict py2.6 compat. `9bf4869a3 <https://github.com/fedora-infra/pkgwat.api/commit/9bf4869a37902ffabee22c5a54bac84c152b938b>`_

0.7
---

- A pkgwat.api.get function.  Fixes #2. `64981947c <https://github.com/fedora-infra/pkgwat.api/commit/64981947c4d358af77fbdd1aa70c887b7ccd89d5>`_
- Merge pull request #7 from fedora-infra/feature/get `7055c2635 <https://github.com/fedora-infra/pkgwat.api/commit/7055c2635f602a5e6993b3295ec3f3d0b0852bf6>`_

0.6
---

- Fix a bug introduced in 8fe5aed when searching for.. anything. `6be374eaa <https://github.com/fedora-infra/pkgwat.api/commit/6be374eaa4ba238f9902fa2a67c1c17b9bc82b5b>`_
- Dependencies. `61b5d7c02 <https://github.com/fedora-infra/pkgwat.api/commit/61b5d7c022f95ed052a3574655cc9a643f3d789b>`_
- Docs for dependencies api. `3bde79e90 <https://github.com/fedora-infra/pkgwat.api/commit/3bde79e9069966e8c64b2f530fc011adf38e34d4>`_
- PEP8. `58db94321 <https://github.com/fedora-infra/pkgwat.api/commit/58db943211afbf3b00a1eb71d7971e9cbc8a0c3d>`_
- PEP8. `dd848da03 <https://github.com/fedora-infra/pkgwat.api/commit/dd848da0352aceb008eee086e380ab3d0fbe1d2a>`_
- PEP8 (moar) `c090eaa87 <https://github.com/fedora-infra/pkgwat.api/commit/c090eaa87a51f9c353e72d2803c008b686d5ac49>`_
- PEP8 (moar!) `e3048fb9d <https://github.com/fedora-infra/pkgwat.api/commit/e3048fb9de9c675bc1cbc32ff0a03106e0a81b12>`_
- PEP8 (finally) `a00c45836 <https://github.com/fedora-infra/pkgwat.api/commit/a00c45836b5a80f3b986c88d010ea996f0dc18ff>`_
- Merge pull request #5 from fedora-infra/feature/relationships `c0a3d8c2e <https://github.com/fedora-infra/pkgwat.api/commit/c0a3d8c2e39d185b73e5450ce03ab9f9a6df2282>`_
- Tests for desired features. `aca6155ae <https://github.com/fedora-infra/pkgwat.api/commit/aca6155ae73d2b808ef0b5d1f0f64a02d0d3532a>`_
- The last bits of the API. `fde723be8 <https://github.com/fedora-infra/pkgwat.api/commit/fde723be8dc093494f41ff08f5e637080eda03c5>`_
- Fix minor typo. `a871f910f <https://github.com/fedora-infra/pkgwat.api/commit/a871f910f01ea1e70010ba53c8e4fe3603a54a1f>`_
- Merge pull request #6 from fedora-infra/feature/provides-obsoletes-conflicts `b6dc11ff4 <https://github.com/fedora-infra/pkgwat.api/commit/b6dc11ff46e7609d0144d0693910c2a26c4d5e8a>`_

0.5
---

- Make the "1 karma" show up more distinct and not smashed against the preceding text. `8fe5aed3e <https://github.com/fedora-infra/pkgwat.api/commit/8fe5aed3e64017c625a3084262360b8d05eb8658>`_

0.4
---

- Make the "1 karma" show up more distinct and not smashed against the preceding text. `8fe5aed3e <https://github.com/fedora-infra/pkgwat.api/commit/8fe5aed3e64017c625a3084262360b8d05eb8658>`_
- 0.5 `72ed330f6 <https://github.com/fedora-infra/pkgwat.api/commit/72ed330f66a6940216915ed46ef931ef0c6ac73f>`_
- Fix a bug introduced in 8fe5aed when searching for.. anything. `6be374eaa <https://github.com/fedora-infra/pkgwat.api/commit/6be374eaa4ba238f9902fa2a67c1c17b9bc82b5b>`_
- Dependencies. `61b5d7c02 <https://github.com/fedora-infra/pkgwat.api/commit/61b5d7c022f95ed052a3574655cc9a643f3d789b>`_
- Docs for dependencies api. `3bde79e90 <https://github.com/fedora-infra/pkgwat.api/commit/3bde79e9069966e8c64b2f530fc011adf38e34d4>`_
- PEP8. `58db94321 <https://github.com/fedora-infra/pkgwat.api/commit/58db943211afbf3b00a1eb71d7971e9cbc8a0c3d>`_
- PEP8. `dd848da03 <https://github.com/fedora-infra/pkgwat.api/commit/dd848da0352aceb008eee086e380ab3d0fbe1d2a>`_
- PEP8 (moar) `c090eaa87 <https://github.com/fedora-infra/pkgwat.api/commit/c090eaa87a51f9c353e72d2803c008b686d5ac49>`_
- PEP8 (moar!) `e3048fb9d <https://github.com/fedora-infra/pkgwat.api/commit/e3048fb9de9c675bc1cbc32ff0a03106e0a81b12>`_
- PEP8 (finally) `a00c45836 <https://github.com/fedora-infra/pkgwat.api/commit/a00c45836b5a80f3b986c88d010ea996f0dc18ff>`_
- Merge pull request #5 from fedora-infra/feature/relationships `c0a3d8c2e <https://github.com/fedora-infra/pkgwat.api/commit/c0a3d8c2e39d185b73e5450ce03ab9f9a6df2282>`_
- Tests for desired features. `aca6155ae <https://github.com/fedora-infra/pkgwat.api/commit/aca6155ae73d2b808ef0b5d1f0f64a02d0d3532a>`_
- The last bits of the API. `fde723be8 <https://github.com/fedora-infra/pkgwat.api/commit/fde723be8dc093494f41ff08f5e637080eda03c5>`_
- Fix minor typo. `a871f910f <https://github.com/fedora-infra/pkgwat.api/commit/a871f910f01ea1e70010ba53c8e4fe3603a54a1f>`_
- Merge pull request #6 from fedora-infra/feature/provides-obsoletes-conflicts `b6dc11ff4 <https://github.com/fedora-infra/pkgwat.api/commit/b6dc11ff46e7609d0144d0693910c2a26c4d5e8a>`_
- 0.6 `62d06d630 <https://github.com/fedora-infra/pkgwat.api/commit/62d06d630bb5bd4db2f3bbf85e0a4906a18436c4>`_
- A pkgwat.api.get function.  Fixes #2. `64981947c <https://github.com/fedora-infra/pkgwat.api/commit/64981947c4d358af77fbdd1aa70c887b7ccd89d5>`_
- Merge pull request #7 from fedora-infra/feature/get `7055c2635 <https://github.com/fedora-infra/pkgwat.api/commit/7055c2635f602a5e6993b3295ec3f3d0b0852bf6>`_
- 0.7 `008bfe930 <https://github.com/fedora-infra/pkgwat.api/commit/008bfe930715a4cb0116a3cc8b21b65404513b78>`_
- Py3.2-friendly. `72c111cd8 <https://github.com/fedora-infra/pkgwat.api/commit/72c111cd88cb3bcff7b25215ac9dff319c45def4>`_
- Correct URL for source. `9e3607ea0 <https://github.com/fedora-infra/pkgwat.api/commit/9e3607ea0fb9643381cac7e0f79c9ffacc31d6a5>`_
- Travis-CI config. `cd4866257 <https://github.com/fedora-infra/pkgwat.api/commit/cd4866257f347331d8fe99dbd48e73dff33763fa>`_
- OrderedDict py2.6 compat. `9bf4869a3 <https://github.com/fedora-infra/pkgwat.api/commit/9bf4869a37902ffabee22c5a54bac84c152b938b>`_
- 0.8 `84ad79e85 <https://github.com/fedora-infra/pkgwat.api/commit/84ad79e85b91069fbd78490ccf14a1950060b076>`_
- Allow .get to return subpackages. `1db230381 <https://github.com/fedora-infra/pkgwat.api/commit/1db23038157cf2513304bf56aac33ca74b039b77>`_
- Merge pull request #8 from fedora-infra/feature/get-subpackages `84e913fe1 <https://github.com/fedora-infra/pkgwat.api/commit/84e913fe1870a8748a1c2d52cbf790d5289076ac>`_
- Packages with different names `3d2930649 <https://github.com/fedora-infra/pkgwat.api/commit/3d293064933ef50a81a0ee6853fc101da40f1c09>`_
- Merge pull request #10 from arielb2/3d293064933ef50a81a0ee6853fc101da40f1c09 `f6ac43b46 <https://github.com/fedora-infra/pkgwat.api/commit/f6ac43b461ea8239bfa0c46e14045d01d7e7fc72>`_
- Add a history function to query datagrepper. `a3cd8950f <https://github.com/fedora-infra/pkgwat.api/commit/a3cd8950fd72c2e7bc33a61212858c257fc74856>`_
- Add a docstring for pkgwat.rtfd.org/ `30099ade4 <https://github.com/fedora-infra/pkgwat.api/commit/30099ade45068a8cf4bf20f8c9c99bcd9c389d55>`_
- Merge pull request #12 from fedora-infra/feature/history `11707a285 <https://github.com/fedora-infra/pkgwat.api/commit/11707a285bdfd3908f83ceac8173788c0f52430b>`_
- 0.9 `acc2f10a8 <https://github.com/fedora-infra/pkgwat.api/commit/acc2f10a84f785b29fa4110aa9ba46d897318484>`_
- Add failing tests for tag stripping. `0ab263ba5 <https://github.com/fedora-infra/pkgwat.api/commit/0ab263ba527c9d46e8541278752cf6812693d169>`_
- Fix tag stripping once and for all. `ae12f6c28 <https://github.com/fedora-infra/pkgwat.api/commit/ae12f6c28acbc649fdde51a72bb9707800416fb1>`_
- Add one more test of strip_tags, just for good measure. `d64cb2cf6 <https://github.com/fedora-infra/pkgwat.api/commit/d64cb2cf67fda2a20ae0f53b697bbcae3540c5d1>`_
- Merge pull request #13 from fedora-infra/feature/fix-tag-stripping `d64da0a14 <https://github.com/fedora-infra/pkgwat.api/commit/d64da0a149610425782d7d907b45960620ad543d>`_
- unicode escape fix https://github.com/fedora-infra/fedora-packages/issues/28 `b058ce006 <https://github.com/fedora-infra/pkgwat.api/commit/b058ce006e1ea760088154efe9f6f589c2cf2d2a>`_
- Handle erroneous html_parser exception on py2.6. `f0057a18c <https://github.com/fedora-infra/pkgwat.api/commit/f0057a18ca8118eaa183ec6970a3a325f1962bdf>`_
- Merge pull request #16 from fedora-infra/feature/py2.6-html_parser-fix `e979a0293 <https://github.com/fedora-infra/pkgwat.api/commit/e979a029308cc9a8a94def7333d754d5c5887c5f>`_
- Remove unnecessary markup. `581b7dd4e <https://github.com/fedora-infra/pkgwat.api/commit/581b7dd4e24801b8865e7239d70a644808a14833>`_
- Quotes. `ec25d0de1 <https://github.com/fedora-infra/pkgwat.api/commit/ec25d0de171ab426a0232281dcb763c80fd7425d>`_
- 0.10 `f57675999 <https://github.com/fedora-infra/pkgwat.api/commit/f576759992ea6b3e46a286838a52eb699d622c87>`_
- ascii codec cant encode character `f4235e06e <https://github.com/fedora-infra/pkgwat.api/commit/f4235e06e66331d6828bfcd3b33c584c29c7294e>`_
- Merge pull request #17 from arielb2/bug-utf `8acb9bb21 <https://github.com/fedora-infra/pkgwat.api/commit/8acb9bb21688cbe585ba8e2d6ee36a73c5865c48>`_
- Add kitchen to the requires list.  From #17. `d0fffd8ae <https://github.com/fedora-infra/pkgwat.api/commit/d0fffd8ae562444b31f31c06c4ca296c1435a807>`_
- PEP8/cosmetic. `851424586 <https://github.com/fedora-infra/pkgwat.api/commit/851424586e2821fbda7fea05a736f3785447bfe5>`_
- Merge pull request #18 from fedora-infra/feature/cleanup `18c25c073 <https://github.com/fedora-infra/pkgwat.api/commit/18c25c073f347b78516ed22ea2ab2a2ddbf2b9dc>`_

0.11
----

- ascii codec cant encode character `f4235e06e <https://github.com/fedora-infra/pkgwat.api/commit/f4235e06e66331d6828bfcd3b33c584c29c7294e>`_
- Merge pull request #17 from arielb2/bug-utf `8acb9bb21 <https://github.com/fedora-infra/pkgwat.api/commit/8acb9bb21688cbe585ba8e2d6ee36a73c5865c48>`_
- Add kitchen to the requires list.  From #17. `d0fffd8ae <https://github.com/fedora-infra/pkgwat.api/commit/d0fffd8ae562444b31f31c06c4ca296c1435a807>`_
- PEP8/cosmetic. `851424586 <https://github.com/fedora-infra/pkgwat.api/commit/851424586e2821fbda7fea05a736f3785447bfe5>`_
- Merge pull request #18 from fedora-infra/feature/cleanup `18c25c073 <https://github.com/fedora-infra/pkgwat.api/commit/18c25c073f347b78516ed22ea2ab2a2ddbf2b9dc>`_
