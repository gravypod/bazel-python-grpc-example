package(default_visibility = ["//visibility:public"])

py_binary(
    name = "server",
    srcs = ["server.py"],
    main = "server.py",
    python_version = "PY3",
    deps = [
        "//specs:greeter_python_library",
        "@rpc_server_deps//requests",
    ],
)
