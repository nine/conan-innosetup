import os
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration

class InnosetupConan(ConanFile):
    name = "innosetup"
    version = "6.0.5-3"
    license = "MIT License"
    url = "https://gitlab.evk.services/development-tools/conan-innosetup"
    settings = "os"
    description="innosetup-portable for MS Windows."

    build_requires = "7z_installer/1.0@conan/stable"

    def configure(self):
        if self.settings.os != "Windows":
            raise ConanInvalidConfiguration("Only windows supported for innosetup")

    def build(self):
        innosetup_zip_name = "innosetup-portable-win32-%s.7z" % (self.version)
        tools.download("https://github.com/portapps/innosetup-portable/releases/download/"
                       "%s/%s" % (self.version, innosetup_zip_name), innosetup_zip_name)
        self.output.info("Downloading innosetup: "
                         "https://github.com/portapps/innosetup-portable/releases/download/"
                         "/%s/%s" % (self.version, innosetup_zip_name))
        self.run("7z x %s" % (innosetup_zip_name))
        os.unlink(innosetup_zip_name)

    def package(self):
        self.copy("*", src="app", dst="bin", keep_path=True)
        self.copy("license*", dst="", src="app", keep_path=False, ignore_case=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))