# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/d/net/cpp/net00/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/d/net/cpp/net00/src

# Include any dependencies generated for this target.
include CMakeFiles/t1.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/t1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/t1.dir/flags.make

CMakeFiles/t1.dir/test1.cc.o: CMakeFiles/t1.dir/flags.make
CMakeFiles/t1.dir/test1.cc.o: test1.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/d/net/cpp/net00/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/t1.dir/test1.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/t1.dir/test1.cc.o -c /mnt/d/net/cpp/net00/src/test1.cc

CMakeFiles/t1.dir/test1.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/t1.dir/test1.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/d/net/cpp/net00/src/test1.cc > CMakeFiles/t1.dir/test1.cc.i

CMakeFiles/t1.dir/test1.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/t1.dir/test1.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/d/net/cpp/net00/src/test1.cc -o CMakeFiles/t1.dir/test1.cc.s

CMakeFiles/t1.dir/test1.cc.o.requires:

.PHONY : CMakeFiles/t1.dir/test1.cc.o.requires

CMakeFiles/t1.dir/test1.cc.o.provides: CMakeFiles/t1.dir/test1.cc.o.requires
	$(MAKE) -f CMakeFiles/t1.dir/build.make CMakeFiles/t1.dir/test1.cc.o.provides.build
.PHONY : CMakeFiles/t1.dir/test1.cc.o.provides

CMakeFiles/t1.dir/test1.cc.o.provides.build: CMakeFiles/t1.dir/test1.cc.o


# Object files for target t1
t1_OBJECTS = \
"CMakeFiles/t1.dir/test1.cc.o"

# External object files for target t1
t1_EXTERNAL_OBJECTS =

t1: CMakeFiles/t1.dir/test1.cc.o
t1: CMakeFiles/t1.dir/build.make
t1: libnet.a
t1: CMakeFiles/t1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/d/net/cpp/net00/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable t1"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/t1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/t1.dir/build: t1

.PHONY : CMakeFiles/t1.dir/build

CMakeFiles/t1.dir/requires: CMakeFiles/t1.dir/test1.cc.o.requires

.PHONY : CMakeFiles/t1.dir/requires

CMakeFiles/t1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/t1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/t1.dir/clean

CMakeFiles/t1.dir/depend:
	cd /mnt/d/net/cpp/net00/src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/d/net/cpp/net00/src /mnt/d/net/cpp/net00/src /mnt/d/net/cpp/net00/src /mnt/d/net/cpp/net00/src /mnt/d/net/cpp/net00/src/CMakeFiles/t1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/t1.dir/depend

