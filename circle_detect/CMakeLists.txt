cmake_minimum_required(VERSION 2.8)
project( cdetect )
find_package( OpenCV REQUIRED )
add_executable( cdetect cdetect.cpp )
target_link_libraries( cdetect ${OpenCV_LIBS} )

project( cdetect2 )
find_package( OpenCV REQUIRED)
add_executable (cdetect2 cdetect2.cpp)
target_link_libraries( cdetect2 ${OpenCV_LIBS} )

project( camera )
find_package( OpenCV REQUIRED)
add_executable (camera camera.cpp)
target_link_libraries( camera ${OpenCV_LIBS} )