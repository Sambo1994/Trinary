import random

class TrinaryUnit:
    def __init__(self):
        self.previous_data = None

    def process_data(self, data):
        if data == 0:
            return "Negative"
        elif data == 1:
            return "Positive"
        elif data == "01":
            if self.previous_data is None:
                return random.choice(["Negative", "Positive"])
            else:
                return self.previous_data
        else:
            raise ValueError("Invalid input data")

class CPU:
    def __init__(self, trinary_unit):
        self.trinary_unit = trinary_unit
        self.registers = [0] * 8  # 8 general-purpose registers
        self.pc = 0  # Program counter

    def execute_instruction(self, instruction):
        opcode = instruction[0]
        if opcode == "MOV":
            src = instruction[1]
            dest = instruction[2]
            self.registers[dest] = self.registers[src]
        elif opcode == "ADD":
            src1 = instruction[1]
            src2 = instruction[2]
            dest = instruction[3]
            self.registers[dest] = self.registers[src1] + self.registers[src2]
        elif opcode == "JMP":
            address = instruction[1]
            self.pc = address
        elif opcode == "CMP":
            src1 = instruction[1]
            src2 = instruction[2]
            if self.registers[src1] == self.registers[src2]:
                self.trinary_unit.previous_data = "01"  # Set neutral
            elif self.registers[src1] > self.registers[src2]:
                self.trinary_unit.previous_data = 1  # Set positive
            else:
                self.trinary_unit.previous_data = 0  # Set negative
        elif opcode == "HALT":
            return False  # Stop execution
        self.pc += 1
        return True

class Memory:
    def __init__(self):
        self.data = [0] * 1000  # 1000 memory locations

    def read(self, address):
        return self.data[address]

    def write(self, address, value):
        self.data[address] = value

def main():
    trinary_unit = TrinaryUnit()
    cpu = CPU(trinary_unit)
    memory = Memory()

    # Example program: copy value from register 0 to register 1
    program = [
        ["MOV", 0, 1],
        ["HALT"]
    ]

    # Load program into memory
    for i, instruction in enumerate(program):
        memory.write(i, instruction)

    # Execute program
    while True:
        instruction = memory.read(cpu.pc)
        if not cpu.execute_instruction(instruction):
            break

    print("Registers after execution:", cpu.registers)

if __name__ == "__main__":
    main()
