"""Preview or submit a separately verified competition ZIP. No downloads."""
import argparse
import hashlib
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

COMPETITION = 'google-verifiable-quantum-circuit-compilation'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('--approved-sha256', help='digest from the approved verification record')
    parser.add_argument('--submit', action='store_true', help='upload once after confirmation')
    args = parser.parse_args()
    # Hash and upload the same private snapshot, even if the original changes.
    with tempfile.TemporaryDirectory() as directory:
        snapshot = Path(directory) / 'submission.zip'
        shutil.copyfile(args.archive, snapshot)
        with snapshot.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        if not zipfile.is_zipfile(snapshot):
            parser.error('Not a ZIP archive')
        print(f'Competition: {COMPETITION}\nFile: {args.archive}\nSHA-256: {digest}')
        if args.approved_sha256 and args.approved_sha256.lower() != digest:
            parser.error('Digest differs from the approved ZIP; not submitted.')
        if not args.submit:
            print('Preview only. Nothing uploaded.')
            return 0
        if not args.approved_sha256:
            parser.error('--submit requires --approved-sha256')
        if input('Type SUBMIT to use one submission for this verified ZIP: ') != 'SUBMIT':
            raise SystemExit('Cancelled.')
        return subprocess.run(['kaggle', 'competitions', 'submit', '-c', COMPETITION,
                               '-f', str(snapshot), '-m', f'Verified ZIP {digest}']).returncode


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (EOFError, OSError) as exc:
        raise SystemExit(f'Submission helper stopped: {exc}') from None
