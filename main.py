from bugsplat import BugSplat
from helpers import crash
from pathlib import Path

cwd = Path(__file__).parent

additional_file_paths = [
    cwd / 'files/attachment.txt',
    cwd / 'files/attachment2.txt'
]

database = ""
application = "my-python-crasher"
version = "1.0"

if not database:
    raise Exception("Please set a value for database")

bugsplat = BugSplat("fred", application, version)

bugsplat.set_default_app_key('key!')
bugsplat.set_default_description('description!')
bugsplat.set_default_email('fred@bugsplat.com')
bugsplat.set_default_user('Fred')
bugsplat.set_default_additional_file_paths(additional_file_paths)

try:
    crash()
except Exception as e:
    bugsplat.post(
        e,
        additional_file_paths=[],
        app_key='other key!',
        description='other description!',
        email='barney@bugsplat.com',
        user='Barney'
    )
