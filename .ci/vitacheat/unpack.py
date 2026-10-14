"""Reconstruct the reviewed source archive for GitHub Actions build jobs."""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
import base64
import hashlib
import io
import json
import stat

payload = Path(__file__).resolve().parent
manifest = json.loads((payload / 'manifest.json').read_text())
parts = sorted(payload.glob('source_*.b64'))
assert parts, 'No source payload'
assert [p.name for p in parts] == [f'source_{i:03d}.b64' for i in range(len(parts))]
data = base64.b64decode(''.join(p.read_text() for p in parts), validate=True)
assert hashlib.sha256(data).hexdigest() == manifest['sha256'], 'Source checksum mismatch'

destination = Path.cwd() / 'vitacheat-ng'
assert not destination.exists(), 'Refusing to overwrite an existing source tree'
with ZipFile(io.BytesIO(data)) as archive:
    entries = archive.infolist()
    assert len(entries) == manifest['file_count'], 'Source entry count mismatch'
    assert sum(e.file_size for e in entries) < 16 * 1024 * 1024, 'Unexpected source size'
    for entry in entries:
        path = PurePosixPath(entry.filename)
        assert not path.is_absolute() and '..' not in path.parts
        assert '\\' not in entry.filename and not stat.S_ISLNK(entry.external_attr >> 16)
        assert len(path.parts) > 1 and path.parts[0] == manifest['archive_root']
    destination.mkdir()
    for entry in entries:
        relative = PurePosixPath(entry.filename).relative_to(manifest['archive_root'])
        target = destination.joinpath(*relative.parts)
        if entry.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(entry))

assert (destination / 'VERSION').read_text().strip() == manifest['version']
assert f'#define VCNG_VERSION_TEXT "{manifest["version"]}"' in (destination / 'include/vcng_version.h').read_text()
(payload / f'VitaCheat-NG-{manifest["version"]}-source.zip').write_bytes(data)
print(f'Verified VitaCheat NG {manifest["version"]}: {len(entries)} source files')
print(f'Source archive SHA256: {manifest["sha256"]}')
