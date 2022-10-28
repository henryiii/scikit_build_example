cmake_minimum_required(VERSION 3.15...3.22)

project(${SKBUILD_PROJECT_NAME} VERSION "${SKBUILD_PROJECT_VERSION}")

# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/main.cpp)

target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS _core DESTINATION scikit_build_example)
