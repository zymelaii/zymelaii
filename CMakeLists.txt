cmake_minimum_required(VERSION 3.5)

project(github-profile-template)

set(SCHEMA default)

configure_file(
    ${CMAKE_SOURCE_DIR}/template/${SCHEMA}.template
    ${CMAKE_SOURCE_DIR}/README.md
    @ONLY
)
