cmake_minimum_required(VERSION 3.0) # I would advise to update
project(net05)

SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -std=c++11 -O3 -Wall -pthread")
#set(LIBRARY_OUTPUT_DIRECTORY ../src)
#message("${LIBRARY_OUTPUT_DIRECTORY}")
find_package(Threads REQUIRED)
include_directories(base)
file(GLOB sources ${CMAKE_CURRENT_SOURCE_DIR}/*.cc) # upper case variable names reserved for exported variables by convention
add_library(net ${sources}) # STATIC by default
 

target_include_directories(net PUBLIC base)




#set_target_properties(net
#    PROPERTIES
#        CMAKE_LIBRARY_OUTPUT_DIRECTORY ${LIBRARY_OUTPUT_DIRECTORY}
#)