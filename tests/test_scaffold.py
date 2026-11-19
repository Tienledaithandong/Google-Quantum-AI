"""No competition files, credentials or installed packages needed."""
import os
from pathlib import Path
import subprocess
import unittest


class ScaffoldTests(unittest.TestCase):
    def test_git_excludes_restricted_outputs(self):
        for path in ['data/ref/readme', 'downloads/raw', 'outputs/report',
                     'a.kmx', 'a.kmb', 'submission.npz', 'submission.zip',
                     '.kaggle/kaggle.json', 'kaggle.json', '.env', 'test.token']:
            with self.subTest(path=path):
                subprocess.run(['git', 'check-ignore', '-q', '--no-index', path], check=True)

    def test_no_ignored_or_large_files_tracked(self):
        ignored = subprocess.check_output(['git', 'ls-files', '-ci', '--exclude-standard'])
        self.assertFalse(ignored, 'Ignored files must not be force-added to Git')
        for raw in subprocess.check_output(['git', 'ls-files', '-z']).split(b'\0'):
            if raw:
                path = Path(os.fsdecode(raw))
                self.assertLess(path.lstat().st_size, 10 * 1024 * 1024, str(path))

    def test_fetch_gates(self):
        marker = 'synthetic-placeholder'
        for event, ref, token, reason in [
            ('pull_request', 'refs/heads/main', marker, 'manual workflow'),
            ('workflow_dispatch', 'refs/heads/test', marker, 'protected main'),
            ('workflow_dispatch', 'refs/heads/main', '', 'HUMAN_ACTION_REQUIRED'),
            ('workflow_dispatch', 'refs/heads/main', marker, 'require audit'),
        ]:
            with self.subTest(event=event, ref=ref, reason=reason):
                result = subprocess.run(['bash', 'scripts/fetch_competition.sh'],
                                        env={'GITHUB_EVENT_NAME': event, 'GITHUB_REF': ref,
                                             'KAGGLE_API_TOKEN': token},
                                        capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(reason, result.stderr)
                self.assertNotIn(marker, result.stdout + result.stderr)
