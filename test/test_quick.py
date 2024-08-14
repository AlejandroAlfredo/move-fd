import os


class TestQuick:
    def test_envs(self):
        for key in os.environ.keys():
            print(f"'{key}': '{os.getenv(key)}'")
