project(CDMF)

add_subdirectory(protobufda)
# Set compile flag
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")

# add executable
file(GLOB_RECURSE CDMF_SOURCE_FILES *.[ch]pp)

# Tell Cmake these protoc generated files will appear in build session
set_source_files_properties(${PROTO_CDMF_SRC} ${PROTO_CDMF_HEADER} PROPERTIES GENERATED TRUE)

add_executable(lccdmf ${CDMF_SOURCE_FILES} ${PROTO_CDMF_SRC} ${PROTO_CDMF_HEADER})

target_include_directories(lccdmf PUBLIC 
	${Strads_INCLUDE_DIRS} 
	${MPI_CXX_INCLUDE_PATH} 
	${GLOG_INCLUDE_DIRS}
	${GFLAGS_INCLUDE_DIRS}
	${PROTO_CDMF_INCLUDE_DIR}
	${PROTOBUF_INCLUDE_DIR}
	${PROTO_SYS_INCLUDE_DIR})

target_link_libraries(lccdmf PUBLIC 
	petuum_strads 
	${MPI_CXX_LIBRARIES} 
	${GLOG_LIBRARIES}
	${GFLAGS_LIBRARIES}
	${PROTOBUF_LIBRARY}
	${protoCDMF})