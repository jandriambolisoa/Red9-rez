name = "Red9"

version = "2.75.0"

authors = [
    "Mark Jackson",
    "Jeremy Andriambolisoa",
]

description = \
    """
    Red9 offers cutting edge production services, rigging, facial, tool solutions,
    bespoke workflows and support to the animation industry.
    """


requires = [
    "python-3+",
    "maya-2025+",
    "six",
    "ffmpeg",
    "pymel",
    "pyperclip"
]

uuid = "markj3d.Red9"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
    