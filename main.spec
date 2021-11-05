# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/Xin/Documents/upwork/python-hangman/Hangman-TheWordGame'],
             binaries=[],
             datas=[('imgs', 'imgs'),('hangman.ico', '.'),('GRE2910.txt',
             '.'),('hangman.png','.'),('cto.icns','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='hangman.ico')
app = BUNDLE(exe,
             name='main.app',
             icon='cto.icns',
             bundle_identifier=None)
