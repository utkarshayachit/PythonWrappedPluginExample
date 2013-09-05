project(My)
cmake_minimum_required(VERSION 2.8.8)


option(BUILD_TESTING "Build plugin with tests enabled." ON)
option(BUILD_SHARED_LIBS "Build shared libraries" ON)

if(BUILD_TESTING)
  include(CTest)
endif()

set(EXECUTABLE_OUTPUT_PATH "${CMAKE_BINARY_DIR}/bin")
set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}/lib")


find_package(ParaView REQUIRED)
include(${PARAVIEW_USE_FILE})
include(ParaViewPlugins)

add_subdirectory(Module)
add_subdirectory(Plugin)

if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()
