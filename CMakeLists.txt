cmake_minimum_required(VERSION 3.15)

project(
  cmsketch
  VERSION 0.1.10 # Project version
  LANGUAGES CXX)

# Generate compile_commands.json for IDE support
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Build options
option(DEVELOPMENT_MODE "Enable development mode with IDE support" OFF)
option(BUILD_PYTHON_BINDINGS "Build Python bindings for development" OFF)

# C++ standard - use C++17 for better compatibility
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Default build type
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE
      Release
      CACHE STRING "Build type" FORCE)
endif()

# Compiler warnings
if(MSVC)
  add_compile_options(/W4)
  # Enable Windows symbol export
  set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
else()
  add_compile_options(-Wall -Wextra -Wpedantic)
  # Enable position independent code for shared libraries
  set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

# Platform-specific settings
if(APPLE)
  set(CMAKE_OSX_DEPLOYMENT_TARGET
      "10.9"
      CACHE STRING "Minimum OS X deployment version")
  set(CMAKE_OSX_ARCHITECTURES
      "x86_64;arm64"
      CACHE STRING "Build architectures for OS X")
endif()

# Source files
file(GLOB_RECURSE CMSKETCH_SOURCES "src/cmsketchcpp/*.cc")

# Create library
add_library(cmsketch ${CMSKETCH_SOURCES})
target_include_directories(cmsketch PUBLIC include)
target_compile_features(cmsketch PUBLIC cxx_std_17)

# Example executable
file(GLOB EXAMPLE_SOURCES "src/main.cc")
add_executable(cmsketch_example ${EXAMPLE_SOURCES})
target_link_libraries(cmsketch_example PRIVATE cmsketch)

# Install targets
install(TARGETS cmsketch DESTINATION lib)
install(DIRECTORY include/ DESTINATION include)

# Python bindings
if(SKBUILD_PROJECT_NAME
   OR BUILD_PYTHON_BINDINGS
   OR DEVELOPMENT_MODE)
  set(PYBIND11_FINDPYTHON ON)
  find_package(pybind11 REQUIRED)
  pybind11_add_module(_core MODULE src/python_bindings.cc)
  target_link_libraries(_core PRIVATE cmsketch)
  if(SKBUILD_PROJECT_NAME)
    install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})
  endif()
endif()

# Testing
option(BUILD_TESTS "Build tests" OFF)
if(BUILD_TESTS OR DEVELOPMENT_MODE)
  find_package(GTest REQUIRED)
  enable_testing()
  add_subdirectory(tests)
endif()

# Custom targets
add_custom_target(
  format
  COMMAND
    find ${CMAKE_SOURCE_DIR}/src ${CMAKE_SOURCE_DIR}/include
    ${CMAKE_SOURCE_DIR}/tests -name "*.cc" -o -name "*.h" | xargs clang-format
    -i
  COMMENT "Formatting source code"
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})

# Status messages
message(STATUS "Development mode: ${DEVELOPMENT_MODE}")
message(STATUS "Build Python bindings: ${BUILD_PYTHON_BINDINGS}")
message(STATUS "Build tests: ${BUILD_TESTS}")
