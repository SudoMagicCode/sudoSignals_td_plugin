@echo off


echo starting...

set src_dir=../protobuf/src
set dst_dir=../proto_packages/python/

echo building python common protobufs...
protoc -I=%src_dir% --python_out=%dst_dir% %src_dir%/common/* google/protobuf/any.proto google/protobuf/struct.proto google/protobuf/duration.proto --pyi_out=%dst_dir%


echo WARNING! any new files created by the protobuf compiler need to be added to the TouchDesigner TOE file.

:done
echo done!