from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
import shutil
import os

# TODO: Add an option to enable Xeon Phi support. See https://github.com/STEllAR-GROUP/hpx#intelr-xeonphi

class HpxConan(ConanFile):
    name = "hpx"
    version = "1.1.0"
    license = "Boost Software License, Version 1.0"
    url = "https://github.com/darcamo/conan-hpx"
    description = "HPX (High Performance ParalleX) is a general purpose C++ runtime system for parallel and distributed applications of any scale."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "boost/1.66.0@conan/stable"  #, "hwloc/1.11.1@lasote/stable"

    def system_requirements(self):
        if tools.os_info.linux_distro == "arch":
            package_names = ["gperftools", "hwloc"]
        elif tools.os_info.linux_distro == "ubuntu":
            package_names = ["libgoogle-perftools-dev", "libhwloc-dev"]
        else:
            package_names = []

        installer = tools.SystemPackageTool()
        for name in package_names:
            installer.install(name)

    def source(self):
        tools.get("http://stellar.cct.lsu.edu/files/hpx_{}.zip".format(self.version))
        shutil.move("hpx_{}/".format(self.version), "sources")
        tools.replace_in_file("sources/CMakeLists.txt", "project(HPX CXX C)",
                              '''project(HPX CXX C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        os.mkdir("build")
        shutil.move("conanbuildinfo.cmake", "build/")
        cmake.configure(source_folder="sources", build_folder="build")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
