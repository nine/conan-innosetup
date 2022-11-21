import os
from conan import ConanFile
from conan.tools import files

required_conan_version = ">=1.53.0"


class InnosetupConan(ConanFile):
    name = "innosetup"
    license = "Inno Setup License"
    url = "https://github.com/nine/conan-innosetup"
    homepage = "https://portapps.io/app/innosetup-portable/"
    settings = {
        "os": ["Windows"],
    }
    description="innosetup-portable for MS Windows."

    def build_requirements(self):
        if self.settings_build.os == "Windows":
            self.build_requires("7zip/19.00")
        else:
            self.build_requires("p7zip/16.02")

    def build(self):
        files.download(self, **self.conan_data["sources"][self.version])
        self.run("7z x %s" % (self.conan_data["sources"][self.version]["filename"]))
        files.rm(self, self.conan_data["sources"][self.version]["filename"], self.build_folder)

    def package(self):
        self.copy("*", src="app", dst="bin", keep_path=True)
        self.copy("license*", dst="", src="app", keep_path=False, ignore_case=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
