cmake_minimum_required(VERSION 3.16)

project("VAL-wrapper" VERSION 1.0)

include(ExternalProject)

if(NOT CMAKE_INSTALL_PREFIX)
    set(CMAKE_INSTALL_PREFIX "${PROJECT_SOURCE_DIR}/release")
endif()

set(CMAKE_EXE_LINKER_FLAGS "-static-libstdc++ -static-libgcc")
set(CMAKE_SHARED_LINKER_FLAGS  "-static-libstdc++ -static-libgcc") 

if(MINGW)
    # set(CMAKE_SHARED_LINKER_FLAGS  "${CMAKE_SHARED_LINKER_FLAGS} -Wl,-Bstatic,--whole-archive -lpthread  -Wl,-Bdynamic,--no-whole-archive")
    set(CMAKE_SHARED_LINKER_FLAGS  "${CMAKE_SHARED_LINKER_FLAGS} -static -lpthread") 
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--allow-multiple-definition -static -lpthread")
endif(MINGW)

ExternalProject_Add(external_VAL
    GIT_REPOSITORY https://github.com/KCL-Planning/VAL
    SOURCE_DIR ${PROJECT_BINARY_DIR}/tmp/download
    BINARY_DIR ${PROJECT_BINARY_DIR}/pypi_release/package/val_wrapper
    CMAKE_ARGS 
        -DCMAKE_BUILD_TYPE=Release 
        -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}/package/val_wrapper
        -DCMAKE_SHARED_LINKER_FLAGS=${CMAKE_SHARED_LINKER_FLAGS}
        -DCMAKE_EXE_LINKER_FLAGS=${CMAKE_EXE_LINKER_FLAGS}
)

configure_file(${PROJECT_SOURCE_DIR}/scripts/validate.py 
    ${PROJECT_BINARY_DIR}/pypi_release/package/scripts/validate.py 
    FILE_PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    COPYONLY
)
install(FILES
    ${PROJECT_BINARY_DIR}/pypi_release/package/scripts/validate.py 
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    DESTINATION ${CMAKE_INSTALL_PREFIX}/package/scripts
)

configure_file(${PROJECT_SOURCE_DIR}/src/wrapper.py 
    ${PROJECT_BINARY_DIR}/pypi_release/package/val_wrapper/wrapper.py 
    FILE_PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    COPYONLY
)
configure_file(${PROJECT_SOURCE_DIR}/src/__init__.py 
    ${PROJECT_BINARY_DIR}/pypi_release/package/val_wrapper/__init__.py 
    FILE_PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    COPYONLY
)
install(FILES
    ${PROJECT_BINARY_DIR}/pypi_release/package/val_wrapper/__init__.py 
    ${PROJECT_BINARY_DIR}/pypi_release/package/val_wrapper/wrapper.py 
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    DESTINATION ${CMAKE_INSTALL_PREFIX}/package/val_wrapper
)

configure_file(${PROJECT_SOURCE_DIR}/config/pypi/setup.py
    ${PROJECT_BINARY_DIR}/pypi_release/setup.py
    FILE_PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    COPYONLY
)
configure_file(${PROJECT_SOURCE_DIR}/config/pypi/MANIFEST.in
    ${PROJECT_BINARY_DIR}/pypi_release/MANIFEST.in
    FILE_PERMISSIONS OWNER_WRITE OWNER_READ
    COPYONLY
)
configure_file(${PROJECT_SOURCE_DIR}/README.md
    ${PROJECT_BINARY_DIR}/pypi_release/README.md
    FILE_PERMISSIONS OWNER_WRITE OWNER_READ
    COPYONLY
)
configure_file(${PROJECT_SOURCE_DIR}/config/pypi/KCL-VAL-LICENSE
    ${PROJECT_BINARY_DIR}/pypi_release/LICENSE
    FILE_PERMISSIONS OWNER_WRITE OWNER_READ
    COPYONLY
)

install(FILES
    ${PROJECT_BINARY_DIR}/pypi_release/setup.py
    PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)
install(FILES
    ${PROJECT_BINARY_DIR}/pypi_release/MANIFEST.in
    ${PROJECT_BINARY_DIR}/pypi_release/LICENSE
    ${PROJECT_BINARY_DIR}/pypi_release/README.md
    PERMISSIONS OWNER_WRITE OWNER_READ
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)
    
