cmake_minimum_required(VERSION 2.6)

SET(CMAKE_BUILD_TYPE "Release")

SET(INCLUDE_INSTALL_DIR "${PROJECT_SOURCE_DIR}/base")
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -std=c++11 -O3 -Wall -pthread")

#add_subdirectory(lib)
add_executable(t3 test3.cc)
target_link_libraries(t3 ${PROJECT_SOURCE_DIR}/libnet.a)

#add_executable(main main.cpp)
#target_link_libraries(main ${CMAKE_SOURCE_DIR}/libbingitup.a)