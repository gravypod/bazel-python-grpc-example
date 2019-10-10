workspace(name = "example_grpc")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

############
### gRPC ###
############

http_archive(
    name = "rules_proto_grpc",
    sha256 = "1e08cd6c61f893417b14930ca342950f5f22f71f929a38a8c4bbfeae2a80d03e",
    strip_prefix = "rules_proto_grpc-0.2.0",
    urls = ["https://github.com/rules-proto-grpc/rules_proto_grpc/archive/0.2.0.tar.gz"],
)

load("@rules_proto_grpc//:repositories.bzl", "rules_proto_grpc_toolchains")

rules_proto_grpc_toolchains()

####################
## gRPC + Python3 ##
####################
load("@rules_proto_grpc//python:repositories.bzl", rules_proto_grpc_python_repos = "python_repos")

rules_proto_grpc_python_repos()

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_apt_itude_rules_pip//rules:dependencies.bzl", "pip_rules_dependencies")

pip_rules_dependencies()

load("@com_apt_itude_rules_pip//rules:repository.bzl", "pip_repository")

pip_repository(
    name = "rules_proto_grpc_py2_deps",
    python_interpreter = "python2",
    requirements = "@rules_proto_grpc//python:requirements.txt",
)

pip_repository(
    name = "rules_proto_grpc_py3_deps",
    python_interpreter = "python3",
    requirements = "@rules_proto_grpc//python:requirements.txt",
)

pip_repository(
    name = "rpc_server_deps",
    python_interpreter = "python3",
    requirements = "//rpcserver:requirements.txt",
)
