# Command example

./build_all.py --clean --arch riscv32  --board vexriscv_sim --cc riscv64-unknown-elf-gcc --cflags "-O2 -march=rv32im -mabi=ilp32" --ldflags "-march=rv32im -mabi=ilp32"
./benchmark_speed.py --target-module run_vexriscv_sim  --timeout 100 --cpu-mhz 1 --regression-path PATH_TO_VEXRISCV_REPO/src/test/cpp/regression --regression-args "MMU=no CSR=no DBUS=SIMPLE IBUS=SIMPLE"

