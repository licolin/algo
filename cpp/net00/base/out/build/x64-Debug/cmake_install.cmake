# Install script for directory: D:/net/cpp/net00/base

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "D:/net/cpp/net00/base/out/install/x64-Debug")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "D:/net/cpp/net00/base/out/build/x64-Debug/muduo_base.lib")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/muduo/base" TYPE FILE FILES
    "D:/net/cpp/net00/base/AsyncLogging.h"
    "D:/net/cpp/net00/base/Atomic.h"
    "D:/net/cpp/net00/base/BlockingQueue.h"
    "D:/net/cpp/net00/base/BoundedBlockingQueue.h"
    "D:/net/cpp/net00/base/Condition.h"
    "D:/net/cpp/net00/base/CountDownLatch.h"
    "D:/net/cpp/net00/base/CurrentThread.h"
    "D:/net/cpp/net00/base/Date.h"
    "D:/net/cpp/net00/base/Exception.h"
    "D:/net/cpp/net00/base/FileUtil.h"
    "D:/net/cpp/net00/base/GzipFile.h"
    "D:/net/cpp/net00/base/LogFile.h"
    "D:/net/cpp/net00/base/LogStream.h"
    "D:/net/cpp/net00/base/Logging.h"
    "D:/net/cpp/net00/base/Mutex.h"
    "D:/net/cpp/net00/base/ProcessInfo.h"
    "D:/net/cpp/net00/base/Singleton.h"
    "D:/net/cpp/net00/base/StringPiece.h"
    "D:/net/cpp/net00/base/Thread.h"
    "D:/net/cpp/net00/base/ThreadLocal.h"
    "D:/net/cpp/net00/base/ThreadLocalSingleton.h"
    "D:/net/cpp/net00/base/ThreadPool.h"
    "D:/net/cpp/net00/base/TimeZone.h"
    "D:/net/cpp/net00/base/Timestamp.h"
    "D:/net/cpp/net00/base/Types.h"
    "D:/net/cpp/net00/base/WeakCallback.h"
    "D:/net/cpp/net00/base/copyable.h"
    "D:/net/cpp/net00/base/noncopyable.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "D:/net/cpp/net00/base/out/build/x64-Debug/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
