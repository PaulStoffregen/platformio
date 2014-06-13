# Copyright (C) Ivan Kravets <me@ikravets.com>
# See LICENSE for details.


class PlatformioException(Exception):

    MESSAGE = None

    def __str__(self):  # pragma: no cover
        if self.MESSAGE:
            return self.MESSAGE % self.args
        else:
            return Exception.__str__(self)


class UnknownPlatform(PlatformioException):

    MESSAGE = "Unknown platform '%s'"


class PlatformNotInstalledYet(PlatformioException):

    MESSAGE = ("The platform '%s' has not been installed yet. "
               "Use `platformio install` command")


class UnknownCLICommand(PlatformioException):

    MESSAGE = "Unknown command '%s'"


class UnknownPackage(PlatformioException):

    MESSAGE = "Detected unknown package '%s'"


class InvalidPackageVersion(PlatformioException):

    MESSAGE = "The package '%s' with version '%d' does not exist"


class NonSystemPackage(PlatformioException):

    MESSAGE = "The package '%s' is not available for your system '%s'"


class FDUnrecognizedStatusCode(PlatformioException):

    MESSAGE = "Got an unrecognized status code '%s' when downloaded %s"


class FDSizeMismatch(PlatformioException):

    MESSAGE = ("The size (%d bytes) of downloaded file '%s' "
               "is not equal to remote size (%d bytes)")


class FDSHASumMismatch(PlatformioException):

    MESSAGE = ("The 'sha1' sum '%s' of downloaded file '%s' "
               "is not equal to remote '%s'")


class NotPlatformProject(PlatformioException):

    MESSAGE = "Not a platformio project. Use `platformio init` command"


class UndefinedEnvPlatform(PlatformioException):

    MESSAGE = "Please specify platform for '%s' environment"


class UnsupportedArchiveType(PlatformioException):

    MESSAGE = "Can not unpack file '%s'"


class ProjectInitialized(PlatformioException):

    MESSAGE = ("Project is already initialized. "
               "Process it with `platformio run` command")


class ProjecEnvsNotAvaialable(PlatformioException):

    MESSAGE = "Please setup environments in `platformio.ini` file."