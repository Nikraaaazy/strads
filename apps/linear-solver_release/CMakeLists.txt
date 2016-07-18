project(Linear-solver)

# Set compile flag
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")

# add executable
file(GLOB_RECURSE LS_SOURCE_FILES *.[ch]pp)
add_executable(cdsolver ${LS_SOURCE_FILES})

target_include_directories(cdsolver PUBLIC 
	${Strads_INCLUDE_DIRS} 
	${MPI_CXX_INCLUDE_PATH} 
	${PROTOBUF_INCLUDE_DIRS}
	${GLOG_INCLUDE_DIRS}
	${GFLAGS_INCLUDE_DIRS})

target_link_libraries(cdsolver PUBLIC 
	petuum_strads 
	${MPI_CXX_LIBRARIES} 
	${PROTOBUF_LIBRARIES}
	${GLOG_LIBRARIES}
	${GFLAGS_LIBRARIES})