project(Strads)

# Set compile flag
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")

# set Strads source directory
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
set(Strads_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
        CACHE PATH "Path to Strads include files.")

# add library
file(GLOB_RECURSE Strads_SOURCE_FILES *.[ch]pp)
add_library(petuum_strads ${Strads_SOURCE_FILES})

# Required libraries
find_package(Glog 0.3.4 REQUIRED)
find_package(ZeroMQ 3.2.0 REQUIRED)
find_package(Yaml REQUIRED)
find_package(Gperftools REQUIRED)
find_package(Snappy REQUIRED)
find_package(sparsehash 2.0.2 REQUIRED)
find_package(Boost 1.54.0 REQUIRED COMPONENTS thread system)
find_package(LevelDB REQUIRED)
find_package(Libconfig REQUIRED)
find_package(Gflags REQUIRED)
find_package(Tcmalloc REQUIRED)
find_package(Threads REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(MPI REQUIRED)
find_package(Protobuf REQUIRED)


target_include_directories(petuum_strads PUBLIC
		${Bosen_INCLUDE_DIRS} ${third_INCLUDE_DIRS}
		${ZeroMQ_INCLUDE_DIRS} ${GLOG_INCLUDE_DIRS}
        ${YAML_INCLUDE_DIRS} ${GPERFTOOLS_INCLUDE_DIRS} ${SNAPPY_INCLUDE_DIRS}
        ${SPARSEHASH_INCLUDE_DIR}  ${LevelDB_INCLUDE_PATH} ${GFLAGS_INCLUDE_DIRS}
        ${LIBCONFIG_INCLUDE_DIR}  
        ${Tcmalloc_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIR}
        ${MPI_CXX_INCLUDE_PATH})

target_link_libraries(petuum_strads PUBLIC
		rt nsl
        ${ZeroMQ_LIBRARIES} 
        ${Boost_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT} 
        ${GLOG_LIBRARIES}  ${Tcmalloc_LIBRARIES}
        ${LIBCONFIG_LIBRARIES} ${SNAPPY_LIBRARIES} ${Boost_LIBRARIES}
        ${YAML_LIBRARIES} ${LevelDB_LIBRARY} ${GFLAGS_LIBRARIES}
        ${MPI_CXX_LIBRARIES})