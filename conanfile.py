import os
from conans import ConanFile, tools, CMake


class MuparserConan(ConanFile):
    name = "muparser"
    version = "2.2.6"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    description = "Fast Math Parser Library"
    url = "https://github.com/conan-community/conan-muparser"
    homepage = "http://beltoforion.de/article.php?a=muparser"
    license = "MIT"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("https://github.com/beltoforion/%s/archive/v%s.zip" % (self.name, self.version))
        os.rename(self.name + "-" + self.version, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy(pattern="License.txt", src=self._source_subfolder, dst="licenses")
        self.copy(pattern="*.h", src="%s/include" % self._source_subfolder, dst="include")
        self.copy(pattern="*.lib", src=str(self.settings.build_type), dst="lib")
        self.copy(pattern="*.dll", src=str(self.settings.build_type), dst="bin")
        self.copy(pattern="libmuparser.dll.a", dst="lib")
        self.copy(pattern="libmuparser.dll", dst="bin")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
