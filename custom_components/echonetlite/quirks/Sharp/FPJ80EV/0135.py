"""Sharp FP-J80EV air cleaner properties, verified against device readback.

F1/F2 are 40 bytes and F3 is 27, as on the FP-S42Y. Sensor values match
the SHARP AIR app. F3 does not report the LED or child lock on this model."""

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
