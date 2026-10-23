import tempfile
import unittest
from pathlib import Path

from vcng_companion.telemetry import summarize_telemetry


class TelemetryTests(unittest.TestCase):
    def test_telemetry_summary(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.tsv"
            p.write_text(
                "health\tregions\treadable_regions\tmapped_bytes\tpages_checked\tread_failures\tpages_changed\tdeltas\tcandidates\n"
                "LENDO / SEM MUDANCAS\t12\t8\t4096\t20\t0\t0\t0\t0\n"
                "LENDO + MUDANCAS\t12\t8\t4096\t40\t1\t3\t9\t2\n",
                encoding="utf-8",
            )
            s = summarize_telemetry(p)
            self.assertEqual(s.rows, 2)
            self.assertEqual(s.max_pages_checked, 40)
            self.assertEqual(s.max_candidates, 2)
            self.assertEqual(s.latest_health, "LENDO + MUDANCAS")


if __name__ == "__main__":
    unittest.main()
