import os
from conans import ConanFile, tools, CMake


class MuparserConan(ConanFile):
    name = "muparser"
    version = "2.2.6"
    description = "Fast Math Parser Library"
    topics = ("conan", "muparser", "math", "parser")
    url = "https://github.com/conan-community/conan-muparser"
    homepage = "http://beltoforion.de/article.php?a=muparser"
    author = "Conan Community"
    license = "MIT"
    exports = ["LICENSE.md"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("https://github.com/beltoforion/{}/archive/v{}.zip".format(self.name, self.version), sha256="daf4a937abdc33b361d4a2fbc79bf311d5486ebc87c56596130e295db1302303")
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
