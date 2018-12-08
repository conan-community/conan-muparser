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
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    _source_subfolder = "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        tools.get("https://github.com/beltoforion/{}/archive/v{}.zip".format(self.name, self.version),
                  sha256="daf4a937abdc33b361d4a2fbc79bf311d5486ebc87c56596130e295db1302303")
        os.rename(self.name + "-" + self.version, self._source_subfolder)

        tools.replace_in_file(os.path.join(self._source_subfolder, 'CMakeLists.txt'),
                              'cmake_minimum_required (VERSION 3.1.0)',
                              'cmake_minimum_required (VERSION 3.1.0)\n'
                              'include(conanbuildinfo.cmake)\n'
                              'conan_basic_setup()')

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions["ENABLE_SAMPLES"] = False
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="License.txt", src=self._source_subfolder, dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines.append("MUPARSER_DLL" if self.options.shared else "MUPARSER_STATIC")
