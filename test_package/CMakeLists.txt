project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

message("LIBS: ${CONAN_LIBS}")

add_executable(test_package test_package.cpp)
target_link_libraries(test_package ${CONAN_LIBS})