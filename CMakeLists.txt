cmake_minimum_required(VERSION 3.5)

project(github-profile-template)

set(SCHEMA light)

set(USERNAME zymelaii)

configure_file(
    ${CMAKE_SOURCE_DIR}/template/${SCHEMA}.template
    ${CMAKE_SOURCE_DIR}/README.md
    @ONLY
)

add_custom_target(
    apply-snippets
    COMMAND python ./scripts/apply-snippets.py ${SCHEMA}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)
