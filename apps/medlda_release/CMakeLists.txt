project(MedLDA)

# Set compile flag
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")

# add executable
file(GLOB_RECURSE LS_SOURCE_FILES *.[ch]pp)
add_executable(medlda ${LS_SOURCE_FILES})

target_include_directories(medlda PUBLIC 
	${Strads_INCLUDE_DIRS} 
	${MPI_CXX_INCLUDE_PATH} )

target_link_libraries(medlda PUBLIC 
	petuum_strads 
	${MPI_CXX_LIBRARIES} )