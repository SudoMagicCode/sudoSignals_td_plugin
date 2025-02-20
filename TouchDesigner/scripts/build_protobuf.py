from pathlib import Path
import shutil
import subprocess

print('running build script...')


if shutil.which("protoc") is None:
	print("protoc is not installed. Please install protoc before attempting a build.")
	exit(1)


my_parent_dir = Path(__file__).parent

src_path = '../protobuf/src'
dst_path = '../proto_packages'

src_path = (my_parent_dir / src_path).resolve()
dst_path = (my_parent_dir / dst_path).resolve()
print(f"src: {src_path}")
print(f"dst: {dst_path}")

my_proto_paths = []

for file in src_path.rglob("*.proto"):
	if file.is_file():
		my_proto_paths.append(str(file))

compile_map = {
	f"{dst_path}\\": "python_out",
}


def buildPackage(src:str, dst:str, compile_with:str) -> subprocess.CompletedProcess[bytes]:
	protoc_args = ["protoc", f"-I={src}", f"--{compile_with}={dst}"]
	protoc_args = protoc_args+my_proto_paths
	protoc_args = protoc_args+[	"google/protobuf/any.proto", "google/protobuf/struct.proto", "google/protobuf/duration.proto", "google/protobuf/timestamp.proto"]
	protoc_args = protoc_args+[f"--pyi_out={dst_path}"]

	protoc_process = subprocess.run(protoc_args, shell=True, capture_output=True)

	if protoc_process.returncode != 0:
		print(protoc_process.stderr.decode("utf-8"))
		exit(1)	

for output_path, compiler in compile_map.items():
	buildPackage(src_path, output_path, compiler)
	print(f"built {output_path} package")

print("completed!")