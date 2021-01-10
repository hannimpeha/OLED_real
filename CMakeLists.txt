cmake_minimum_required(VERSION 3.17)

project(penProject)

set(CMAKE_C_STANDARD 11)

include_directories(c)

add_executable(penProject
        c/CIE.c
        c/EMZ_load.c
        c/innerfunc.c
        c/intp.c
        c/multiply.c
        c/OLED_main.c
        c/output.c
        c/Reflec.c
        c/RI_load.c
        c/spectrum_load.c
        c/struct.h
        c/TMM_anisotropy_coeff.c)