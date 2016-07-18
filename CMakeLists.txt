cmake_minimum_required(VERSION 2.8)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules)

add_subdirectory(third_party)
add_subdirectory(src)
add_subdirectory(apps/lda_release)
add_subdirectory(apps/cdmf_release)
add_subdirectory(apps/linear-solver_release)
add_subdirectory(apps/medlda_release)
add_subdirectory(apps/svm_release)