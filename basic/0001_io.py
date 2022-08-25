import sys

REQUIRED_MAJOR_VERSION = 3
if sys.version_info.major < REQUIRED_MAJOR_VERSION:
    sys.exit(
        "Current version %s.%s.%s is not satisfied to %s.x.x"
        % (
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
            REQUIRED_MAJOR_VERSION,
        )
    )

s = input("Input a string:")
print(s)
