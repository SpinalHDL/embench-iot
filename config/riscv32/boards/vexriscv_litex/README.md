# Command example

./build_all.py --clean --arch riscv32  --board vexriscv_litex --cc riscv64-unknown-elf-gcc --cflags "-O2 -march=rv32im -mabi=ilp32" --ldflags "-march=rv32im -mabi=ilp32"
./benchmark_speed.py --target-module run_vexriscv_gdb --gdb-command riscv64-unknown-elf-gdb  --timeout 100 --cpu-mhz 10 

