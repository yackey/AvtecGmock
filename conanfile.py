from conans import ConanFile
from conans import tools
#import os

class AvtecGmockConan(ConanFile):
    name = "AvtecGmock"
    version = "1.0"
    settings = "os", "build_type", "arch"
    description = "AvtecGmock contains the Avtec version of GMock static libraries and include files"
    url = "None"
    license = "None"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    no_copy_source=False

    def package(self):
#       consumers will not have a directory structure in the include directory
        self.copy("*.h", "include", "include", keep_path=True)
#        print('yo from package')
#        cwd = os.getcwd()
#        print("cwd [", cwd, "]")
#       adir = cwd + "/x86_64/bin/Release"
#       print("adir [", adir, "]")
#       if os.path.isdir(adir):
#           items = os.listdir(adir)
#           for name in items:
#               print(name)
#       else:
#           print("no dir")
#
        if self.settings.os == "Linux" and self.settings.arch == "x86_64":
            if self.settings.build_type == "Release":
                self.copy("*.a*", "lib", "build/x86_64/bin/Release", symlinks=True)
            else:
                self.copy("*.a*", "lib", "build/x86_64/bin/Debug", symlinks=True)
        elif self.settings.os == "Linux" and self.settings.arch == "armv7":
            if self.settings.build_type == "Release":
                self.copy("*.a*", "lib", "build/ARM/bin/Release", symlinks=True)
            else:
                self.copy("*.a*", "lib", "build/ARM/bin/Debug", symlinks=True)
        else:
            raise Exception("Package settings")


    def package_info(self):
        #print("yo from package_info")
        #cwd = os.getcwd()
        #print("cwd [", cwd, "]")
        if self.settings.os == "Linux" and self.settings.arch == "x86_64":
            if self.settings.build_type == "Release":
                self.cpp_info.libs = ["libgmock.a"]
            else:
                self.cpp_info.libs = ["libgmock.a"]
        elif self.settings.os == "Linux" and self.settings.arch == "armv7":
            if self.settings.build_type == "Release":
                self.cpp_info.libs = ["libgmock.a"]
            else:
                self.cpp_info.libs = ["libgmock.a"]
        else:
            raise Exception("Package does not exist for these settings")
