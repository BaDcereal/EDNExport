# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/projetos/ednexport/src/ednexport.pyw'],
    pathex=[],
    binaries=[],
    datas=[('C:/projetos/ednexport/imgs/ednexport.png', 'imgs/'), ('C:/projetos/ednexport/imgs/error.png', 'imgs/'), ('C:/projetos/ednexport/imgs/favicon.ico', 'imgs/'), ('C:/projetos/ednexport/imgs/green.png', 'imgs/'), ('C:/projetos/ednexport/imgs/info.png', 'imgs/'), ('C:/projetos/ednexport/imgs/question.png', 'imgs/'), ('C:/projetos/ednexport/imgs/red.png', 'imgs/'), ('C:/projetos/ednexport/imgs/warning.png', 'imgs/'), ('C:/projetos/ednexport/imgs/yellow.png', 'imgs/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ednexport',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\projetos\\ednexport\\imgs\\favicon.ico'],
    embed_manifest=False,
)
