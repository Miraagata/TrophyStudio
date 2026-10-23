import struct
import unittest

from vcng_companion.analysis import scan_pair


class AnalysisTests(unittest.TestCase):
    def test_decreased_u32_finds_expected_offset(self):
        before = bytearray(32)
        after = bytearray(32)
        struct.pack_into("<I", before, 8, 100)
        struct.pack_into("<I", after, 8, 72)
        struct.pack_into("<I", before, 16, 50)
        struct.pack_into("<I", after, 16, 60)
        hits = scan_pair(bytes(before), bytes(after), mode="decreased", width=4)
        self.assertEqual([h.offset for h in hits], [8])

    def test_changed_float_rejects_nan(self):
        before = bytearray(16)
        after = bytearray(16)
        struct.pack_into("<f", before, 0, float("nan"))
        struct.pack_into("<f", after, 0, 1.0)
        self.assertEqual(
            scan_pair(bytes(before), bytes(after), mode="changed", width=4, floating=True),
            [],
        )


if __name__ == "__main__":
    unittest.main()
