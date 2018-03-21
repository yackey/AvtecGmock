

option(BUILD_GTEST "Builds the googletest subproject" OFF)
#Note that googlemock target already builds googletest
option(BUILD_GMOCK "Builds the googlemock subproject" ON)

# example how to set c++ compiler flags for GNU
if(CMAKE_CXX_COMPILER_ID MATCHES GNU)
    set(CMAKE_CXX_FLAGS         "${CMAKE_CXX_FLAGS} -DLINUX=1 -O0 -g -Wall -fprofile-arcs -ftest-coverage -Wno-unknown-pragmas -Wno-sign-compare -Woverloaded-virtual -Wwrite-strings -Wno-unused ")
    
    set(CMAKE_CXX_FLAGS_DEBUG   "-O0 -g3 -fPIC -MMD -MP")
    set(CMAKE_CXX_FLAGS_RELEASE "-O0 -g3 -fPIC -MMD -MP")
    
#    set(CMAKE_CXX_FLAGS_DEBUG   "-O0 -g3 -Wall -c -fmessage-length=0 -fPIC -MMD -MP")
#    set(CMAKE_CXX_FLAGS_RELEASE "-O0 -g3 -Wall -c -fmessage-length=0 -fPIC -MMD -MP")
    
#    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_DEBUG} ${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
endif()

message(STATUS "source ${CMAKE_TARGET_PROCESSOR}")
message(STATUS "source ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "source ${CMAKE_C_COMPILER}")
message(STATUS "source ${CMAKE_CXX_COMPILER}")
message(STATUS "source ${CMAKE_CC_COMPILER}")

message(STATUS "source ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")
message(STATUS "source ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")
message(STATUS "source ${CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG}")
message(STATUS "source ${CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG}")
message(STATUS "source ${BUILD_AEF}")
message(STATUS "source ${CMAKE_AEF_SOURCE_DIR}")

if(BUILD_GMOCK)
  add_subdirectory( googlemock )
elseif(BUILD_GTEST)
  add_subdirectory( googletest )
endif()

