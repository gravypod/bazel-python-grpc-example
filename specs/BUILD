package(default_visibility = ["//visibility:public"])

load("@rules_proto_grpc//python:defs.bzl", "python_grpc_library")


proto_library(
    name = "greeter_grpc",
    srcs = ["greeter.proto"],
    deps = ["@com_google_protobuf//:any_proto"],
)

python_grpc_library(
    name = "greeter_python_library",
    python_version = "PY3",
    deps = ["//specs:greeter_grpc"],
)
