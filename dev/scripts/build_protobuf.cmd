@echo off


echo starting...

set src_dir=../protobuf/src
set dst_dir=../td-python/packets

echo building golang protobufs...
protoc -I=%src_dir% --python_out=%dst_dir% %src_dir%/* google/protobuf/any.proto google/protobuf/struct.proto google/protobuf/duration.proto

echo WARNING! any new files created by the protobuf compiler need to be added to the TouchDesigner TOE file.

:done
echo done!