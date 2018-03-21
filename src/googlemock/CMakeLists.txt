
message(STATUS "gmock ${CMAKE_TARGET_PROCESSOR}")
message(STATUS "gmock ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "gmock ${CMAKE_C_COMPILER}")
message(STATUS "gmock ${CMAKE_CXX_COMPILER}")
message(STATUS "gmock ${CMAKE_CC_COMPILER}")

message(STATUS "gmock(flags) ${CMAKE_CXX_FLAGS}")

# Adds Google Mock's and Google Test's header directories to the search path.
include_directories("${PROJECT_SOURCE_DIR}/include/gmock"
                    "${PROJECT_SOURCE_DIR}/src/googlemock"
                    "${PROJECT_SOURCE_DIR}/include/gtest"
                    "${PROJECT_SOURCE_DIR}/src/googletest"
                    "${PROJECT_SOURCE_DIR}/include")

########################################################################
#
# Defines the gmock & gmock_main libraries.  User tests should link
# with one of them.

# Google Mock libraries.  We build them using more strict warnings than what
# are used for other targets, to ensure that Google Mock can be compiled by
# a user aggressive about warnings.
add_library(gmock STATIC
            "${PROJECT_SOURCE_DIR}/src/googletest/src/gtest-all.cc"
            "${PROJECT_SOURCE_DIR}/src/googlemock/src/gmock-all.cc")
            
set_target_properties( gmock
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/build/${CMAKE_TARGET_PROCESSOR}/bin/${CMAKE_BUILD_TYPE}"
)

# If the CMake version supports it, attach header directory information
# to the targets for when we are part of a parent build (ie being pulled
# in via add_subdirectory() rather than being a standalone build).
#if (DEFINED CMAKE_VERSION AND NOT "${CMAKE_VERSION}" VERSION_LESS "2.8.11")
#  target_include_directories(gmock      SYSTEM INTERFACE "${gmock_SOURCE_DIR}/include")
#endif()


