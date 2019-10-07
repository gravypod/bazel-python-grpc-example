package(default_visibility = ["//visibility:public"])

load("@rules_proto_grpc//python:defs.bzl", "python_grpclib_library")

proto_library(
    name = "specs_proto",
    srcs = ["greeter.proto"],
)

python_grpclib_library(
    name = "specs_py",
    python_version = "PY3",
    deps = ["//specs:specs_proto"],
)
