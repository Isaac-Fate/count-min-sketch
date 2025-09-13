# Test configuration
include(FetchContent)

# Try to find GTest first, if not found, fetch it
find_package(GTest QUIET)
if(NOT GTest_FOUND)
  message(STATUS "GTest not found, fetching from source...")
  FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.15.2 # Use a specific version for reproducibility
    GIT_SHALLOW TRUE)

  # Configure GTest
  set(gtest_force_shared_crt
      ON
      CACHE BOOL "" FORCE)
  set(BUILD_GMOCK
      OFF
      CACHE BOOL "" FORCE)
  set(INSTALL_GTEST
      OFF
      CACHE BOOL "" FORCE)

  FetchContent_MakeAvailable(googletest)

  # Create aliases to match the find_package targets
  add_library(GTest::gtest ALIAS gtest)
  add_library(GTest::gtest_main ALIAS gtest_main)
else()
  message(STATUS "Using system GTest")
endif()

# Auto-detect test source files
file(GLOB TEST_SOURCES "*.cc" "*.cpp")

# Create test executable
add_executable(cmsketch_tests ${TEST_SOURCES})

# Link libraries
target_link_libraries(cmsketch_tests PRIVATE cmsketch GTest::gtest
                                             GTest::gtest_main)

# Include directories
target_include_directories(cmsketch_tests PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Add tests to CTest
add_test(NAME cmsketch_tests COMMAND cmsketch_tests)
