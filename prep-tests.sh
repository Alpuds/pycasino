read -r -d '' help << eot
Running this without an argument will move all files that starts with "test_" up one directory
to easily test the code without modifying the sys.path or the like. Type "end" as an argument
to move the test files back into the "tests" directory
eot

[[ $1 == "end" ]] && mv test_* tests/ || mv tests/* .
[[ $1 == '-h' || $1 == '--help' ]] && echo $help
