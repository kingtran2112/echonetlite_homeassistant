"""Sharp FP-J80EV air cleaner properties, checked against device readback.

Same layout as the FP-S42Y: F1/F2 are 40 bytes, F3 is 27, and the auto
mode code matches. Comparison with the SHARP AIR app is still pending."""

from pychonet.lib.epc_functions import _int

from ....sharp import sharp_raw

QUIRKS = {
    0xF1: {"EPC_FUNCTION": sharp_raw},
    0xF2: {"EPC_FUNCTION": sharp_raw},
    0xF3: {"EPC_FUNCTION": sharp_raw},
    0xA0: {
        "EPC_FUNCTION": [
            _int,
            {0x41: "auto", 0x31: "low", 0x35: "medium", 0x37: "high"},
        ],
    },
}
