project(LDA)

add_subdirectory(protobufda)
# Set compile flag
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")

# add executable
file(GLOB_RECURSE LDA_SOURCE_FILES *.[ch]pp)

# Tell Cmake these protoc generated files will appear in build session
set_source_files_properties(${PROTO_LDA_SRC} ${PROTO_LDA_HEADER} PROPERTIES GENERATED TRUE)

add_executable(ldall ${LDA_SOURCE_FILES} ${PROTO_LDA_SRC} ${PROTO_LDA_HEADER})

target_include_directories(ldall PUBLIC 
	${Strads_INCLUDE_DIRS} 
	${MPI_CXX_INCLUDE_PATH} 
	${GLOG_INCLUDE_DIRS}
	${GFLAGS_INCLUDE_DIRS}
	${PROTO_LDA_INCLUDE_DIR}
	${PROTOBUF_INCLUDE_DIR})

target_link_libraries(ldall PUBLIC 
	petuum_strads 
	${MPI_CXX_LIBRARIES} 
	${GLOG_LIBRARIES}
	${GFLAGS_LIBRARIES}
	${PROTOBUF_LIBRARY}
	${protoLDA})