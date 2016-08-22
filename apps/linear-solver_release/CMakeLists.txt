project(Linear-solver)

add_subdirectory(protobufda)
# Set compile flag
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")

# add executable
file(GLOB_RECURSE LS_SOURCE_FILES *.[ch]pp)

# Tell Cmake these protoc generated files will appear in build session
set_source_files_properties(${PROTO_LS_SRC} ${PROTO_LS_HEADER} PROPERTIES GENERATED TRUE)

add_executable(cdsolver ${LS_SOURCE_FILES} ${PROTO_LS_SRC} ${PROTO_LS_HEADER})

target_include_directories(cdsolver PUBLIC 
	${Strads_INCLUDE_DIRS} 
	${MPI_CXX_INCLUDE_PATH} 
	${GLOG_INCLUDE_DIRS}
	${GFLAGS_INCLUDE_DIRS}
	${PROTO_LS_INCLUDE_DIR}
	${PROTOBUF_INCLUDE_DIR})

target_link_libraries(cdsolver PUBLIC 
	petuum_strads 
	${MPI_CXX_LIBRARIES} 
	${GLOG_LIBRARIES}
	${GFLAGS_LIBRARIES}
	${PROTOBUF_LIBRARY}
	${protoLS})